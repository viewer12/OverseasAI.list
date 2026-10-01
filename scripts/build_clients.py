#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path

RULE_ORDER = {
    "DOMAIN": 0,
    "DOMAIN-SUFFIX": 1,
    "DOMAIN-KEYWORD": 2,
    "DOMAIN-WILDCARD": 3,
    "DOMAIN-REGEX": 4,
    "IP-CIDR": 5,
    "IP-CIDR6": 6,
    "IP-ASN": 7,
    "USER-AGENT": 8,
}

# mihomo 规则类型白名单（不支持 USER-AGENT）。
# 参考：https://wiki.metacubex.one/config/rules/
CLASH_SUPPORTED_TYPES = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "DOMAIN-WILDCARD",
    "DOMAIN-REGEX",
    "IP-CIDR",
    "IP-CIDR6",
    "IP-ASN",
}


def parse_rules(path: Path) -> tuple[list[str], list[str]]:
    header: list[str] = []
    rules: list[str] = []
    for raw in path.read_text(errors="ignore").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            header.append(line)
            continue
        rules.append(line)
    return header, rules


def sort_key(rule: str) -> tuple[int, str, str]:
    rule_type, _, rest = rule.partition(",")
    return (RULE_ORDER.get(rule_type, 99), rule_type, rest)


def build_header(name: str, base_meta: list[str], counts: Counter) -> list[str]:
    header = [f"# NAME: {name}"]
    header.extend(base_meta)
    for key in [
        "DOMAIN",
        "DOMAIN-SUFFIX",
        "DOMAIN-KEYWORD",
        "DOMAIN-WILDCARD",
        "DOMAIN-REGEX",
        "IP-CIDR",
        "IP-CIDR6",
        "IP-ASN",
        "USER-AGENT",
    ]:
        if counts.get(key):
            header.append(f"# {key}: {counts[key]}")
    header.append(f"# TOTAL: {sum(counts.values())}")
    return header


def build_qx_header(name: str, base_meta: list[str], counts: Counter) -> list[str]:
    header = [f"# NAME: {name}"]
    header.extend(base_meta)
    for key in [
        "HOST",
        "HOST-SUFFIX",
        "HOST-KEYWORD",
        "HOST-WILDCARD",
        "HOST-REGEX",
        "IP-CIDR",
        "IP-CIDR6",
        "IP-ASN",
        "USER-AGENT",
    ]:
        if counts.get(key):
            header.append(f"# {key}: {counts[key]}")
    header.append(f"# TOTAL: {sum(counts.values())}")
    return header


def wildcard_to_regex(pattern: str) -> str:
    """将 DOMAIN-WILDCARD 模式转换为 Go 正则表达式（sing-box domain_regex 字段）。
    例：*.foo.com → ^[^.]+\\.foo\\.com$
    """
    if pattern.startswith("*."):
        suffix = re.escape(pattern[2:])
        return f"^[^.]+\\.{suffix}$"
    escaped = re.escape(pattern).replace(r"\*", "[^.]+")
    return f"^{escaped}$"


def build_singbox(rules: list[str], output_dir: Path) -> None:
    rules_map: dict[str, list] = {
        "domain": [],
        "domain_suffix": [],
        "domain_keyword": [],
        "domain_regex": [],
        "ip_cidr": [],
    }
    skipped: Counter = Counter()

    for rule in rules:
        # 去掉 ,no-resolve 修饰符（Surge 专用）
        clean = rule.replace(",no-resolve", "")
        parts = clean.split(",", 1)
        if len(parts) != 2:
            continue
        rule_type, value = parts[0].strip(), parts[1].strip()

        if rule_type == "DOMAIN":
            rules_map["domain"].append(value)
        elif rule_type == "DOMAIN-SUFFIX":
            rules_map["domain_suffix"].append(value)
        elif rule_type == "DOMAIN-KEYWORD":
            rules_map["domain_keyword"].append(value)
        elif rule_type == "DOMAIN-WILDCARD":
            rules_map["domain_regex"].append(wildcard_to_regex(value))
        elif rule_type == "DOMAIN-REGEX":
            rules_map["domain_regex"].append(value)
        elif rule_type in ("IP-CIDR", "IP-CIDR6"):
            rules_map["ip_cidr"].append(value)
        elif rule_type in ("IP-ASN", "USER-AGENT"):
            skipped[rule_type] += 1

    for rule_type, count in skipped.items():
        print(
            f"  [Singbox] Skipped {count} {rule_type} rule(s) (not supported in rule-set)"
        )

    rule_entry = {k: v for k, v in rules_map.items() if v}
    ruleset = {"version": 3, "rules": [rule_entry]}

    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "OverseasAI.json"
    srs_path = output_dir / "OverseasAI.srs"

    json_path.write_text(json.dumps(ruleset, indent=2, ensure_ascii=False) + "\n")

    counts_str = ", ".join(f"{len(v)} {k}" for k, v in rule_entry.items())
    print(f"  [Singbox] .json written: {json_path} ({counts_str})")

    singbox_bin = shutil.which("sing-box")
    if singbox_bin:
        result = subprocess.run(
            [singbox_bin, "rule-set", "compile", str(json_path), "-o", str(srs_path)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"  [Singbox] .srs compiled:  {srs_path}")
        else:
            print(f"  [Singbox] WARNING: compile failed:\n{result.stderr.strip()}")
    else:
        print("  [Singbox] sing-box not found in PATH; .srs compilation skipped")


# 可安全作为 YAML 裸标量的值：域名、CIDR、ASN 号等。
# 通配符(*)、正则等含特殊字符的值需加双引号。
_SAFE_SCALAR = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/\-]*$")


def yaml_scalar(value: str) -> str:
    """为 egern YAML 列表项做最小化安全引用。
    普通域名/CIDR/ASN 保持裸值；含通配符或正则等特殊字符时用双引号包裹。
    """
    if _SAFE_SCALAR.match(value):
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_egern(rules: list[str], meta: list[str], output_dir: Path) -> None:
    """生成 egern 的 YAML 规则集（rule-set）。

    egern 规则集使用 *_set 顶层键，IP 类规则的 no-resolve 修饰符
    通过顶层 `no_resolve: true` 表达。IP-ASN 值形如 "AS20473"。
    参考：https://egernapp.com/docs/configuration/rules/
    """
    buckets: dict[str, list[str]] = {
        "domain_set": [],
        "domain_suffix_set": [],
        "domain_keyword_set": [],
        "domain_wildcard_set": [],
        "domain_regex_set": [],
        "ip_cidr_set": [],
        "ip_cidr6_set": [],
        "asn_set": [],
        "user_agent_set": [],
    }
    type_to_bucket = {
        "DOMAIN": "domain_set",
        "DOMAIN-SUFFIX": "domain_suffix_set",
        "DOMAIN-KEYWORD": "domain_keyword_set",
        "DOMAIN-WILDCARD": "domain_wildcard_set",
        "DOMAIN-REGEX": "domain_regex_set",
        "IP-CIDR": "ip_cidr_set",
        "IP-CIDR6": "ip_cidr6_set",
        "IP-ASN": "asn_set",
        "USER-AGENT": "user_agent_set",
    }

    has_no_resolve = False
    skipped: Counter = Counter()

    for rule in rules:
        parts = rule.split(",")
        rule_type = parts[0].strip()
        value = parts[1].strip() if len(parts) > 1 else ""
        modifiers = [p.strip() for p in parts[2:]]

        bucket = type_to_bucket.get(rule_type)
        if bucket is None:
            skipped[rule_type] += 1
            continue

        if "no-resolve" in modifiers:
            has_no_resolve = True

        if rule_type == "IP-ASN":
            value = f"AS{value}"

        buckets[bucket].append(value)

    for rule_type, count in skipped.items():
        print(f"  [Egern] Skipped {count} {rule_type} rule(s) (unsupported)")

    lines: list[str] = ["# NAME: OverseasAI"]
    lines.extend(meta)
    for key, items in buckets.items():
        if items:
            lines.append(f"# {key}: {len(items)}")
    lines.append(f"# TOTAL: {sum(len(v) for v in buckets.values())}")

    if has_no_resolve:
        lines.append("no_resolve: true")

    for key, items in buckets.items():
        if not items:
            continue
        lines.append(f"{key}:")
        for item in items:
            lines.append(f"- {yaml_scalar(item)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "OverseasAI.yaml"
    out_path.write_text("\n".join(lines) + "\n")

    counts_str = ", ".join(f"{len(v)} {k}" for k, v in buckets.items() if v)
    print(f"  [Egern] .yaml written: {out_path} ({counts_str})")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    surge_path = repo_root / "rule" / "Surge" / "OverseasAI" / "OverseasAI.list"

    header, rules = parse_rules(surge_path)

    # Extract meta lines except counts and name
    meta = []
    count_prefixes = (
        "# DOMAIN",
        "# IP-",
        "# USER-AGENT",
        "# TOTAL",
    )
    for line in header:
        if line.startswith("# NAME:"):
            continue
        if line.startswith(count_prefixes):
            continue
        meta.append(line)

    rules_sorted = sorted(rules, key=sort_key)
    counts = Counter(rule.split(",", 1)[0] for rule in rules_sorted)
    surge_header = build_header("OverseasAI", meta, counts)

    # Write Surge-like lists
    for platform in ["Loon", "Shadowrocket"]:
        out_dir = repo_root / "rule" / platform / "OverseasAI"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "OverseasAI.list"
        out_path.write_text(
            "\n".join(surge_header) + "\n" + "\n".join(rules_sorted) + "\n"
        )

    clash_rules = [
        r for r in rules_sorted if r.split(",", 1)[0] in CLASH_SUPPORTED_TYPES
    ]
    clash_skipped = Counter(
        r.split(",", 1)[0]
        for r in rules_sorted
        if r.split(",", 1)[0] not in CLASH_SUPPORTED_TYPES
    )
    for rule_type, count in clash_skipped.items():
        print(f"  [Clash] Skipped {count} {rule_type} rule(s) (unsupported by mihomo)")
    clash_counts = Counter(rule.split(",", 1)[0] for rule in clash_rules)
    clash_header = build_header("OverseasAI", meta, clash_counts)
    clash_dir = repo_root / "rule" / "Clash" / "OverseasAI"
    clash_dir.mkdir(parents=True, exist_ok=True)
    (clash_dir / "OverseasAI.list").write_text(
        "\n".join(clash_header) + "\n" + "\n".join(clash_rules) + "\n"
    )

    # QuantumultX transform
    qx_rules = []
    qx_counts = Counter()

    for rule in rules_sorted:
        parts = rule.split(",")
        rule_type = parts[0]
        value = parts[1] if len(parts) > 1 else ""
        extra = parts[2:]
        extra = [x for x in extra if x != "no-resolve"]

        if rule_type == "DOMAIN":
            qx_type = "HOST"
        elif rule_type == "DOMAIN-SUFFIX":
            qx_type = "HOST-SUFFIX"
        elif rule_type == "DOMAIN-KEYWORD":
            qx_type = "HOST-KEYWORD"
        elif rule_type == "DOMAIN-WILDCARD":
            qx_type = "HOST-WILDCARD"
        elif rule_type == "DOMAIN-REGEX":
            qx_type = "HOST-REGEX"
        else:
            qx_type = rule_type

        qx_line = f"{qx_type},{value},OverseasAI"
        qx_rules.append(qx_line)
        qx_counts[qx_type] += 1

    qx_header = build_qx_header("OverseasAI", meta, qx_counts)

    qx_dir = repo_root / "rule" / "QuantumultX" / "OverseasAI"
    qx_dir.mkdir(parents=True, exist_ok=True)
    qx_path = qx_dir / "OverseasAI.list"
    qx_path.write_text("\n".join(qx_header) + "\n" + "\n".join(qx_rules) + "\n")

    q_dir = repo_root / "rule" / "Quantumult" / "OverseasAI"
    q_dir.mkdir(parents=True, exist_ok=True)
    q_path = q_dir / "OverseasAI.list"
    q_path.write_text("\n".join(qx_header) + "\n" + "\n".join(qx_rules) + "\n")

    singbox_dir = repo_root / "rule" / "Singbox" / "OverseasAI"
    build_singbox(rules_sorted, singbox_dir)

    egern_dir = repo_root / "rule" / "Egern" / "OverseasAI"
    build_egern(rules_sorted, meta, egern_dir)


if __name__ == "__main__":
    main()
