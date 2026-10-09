#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
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

CORE_SOURCES = [
    "OpenAI",
    "Claude",
    "Anthropic",
    "Gemini",
    "BardAI",
    "Copilot",
    "Civitai",
    "Stripe",
]


def parse_rules(path: Path) -> list[str]:
    rules: list[str] = []
    for raw in path.read_text(errors="ignore").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        rules.append(line)
    return rules


def sort_key(rule: str) -> tuple[int, str, str]:
    rule_type, _, rest = rule.partition(",")
    return (RULE_ORDER.get(rule_type, 99), rule_type, rest)


def build_header(name: str, updated: str, counts: Counter) -> list[str]:
    header = [
        f"# NAME: {name}",
        "# AUTHOR: aggregated by request",
        "# REPO: git@github.com:viewer12/OverseasAI.list.git",
        "# SOURCE: https://github.com/blackmatrix7/ios_rule_script (rule/Surge)",
        "# INCLUDED-CORE: OpenAI, Claude, Anthropic, Gemini, BardAI, Copilot, Civitai, Stripe",
        "# INCLUDED-UPSTREAM-EXTRA: see README",
        "# INCLUDED-CUSTOM: see README",
        f"# UPDATED: {updated}",
    ]
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream", required=True, help="Path to ios_rule_script repo")
    parser.add_argument("--refresh-custom", action="store_true", help="Regenerate custom list from merged rules")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    upstream_root = Path(args.upstream)

    rules_dir = repo_root / "rule" / "Surge" / "OverseasAI"
    rules_dir.mkdir(parents=True, exist_ok=True)

    custom_path = rules_dir / "OverseasAI_Custom.list"
    upstream_extra_path = repo_root / "data" / "upstream_extra_rules.txt"
    upstream_missing_path = repo_root / "reports" / "upstream_missing.txt"

    # Load upstream lines (for extra lookup)
    upstream_lines: set[str] = set()
    for path in (upstream_root / "rule" / "Surge").rglob("*.list"):
        for line in parse_rules(path):
            upstream_lines.add(line)

    # Core rules
    core_rules: set[str] = set()
    for name in CORE_SOURCES:
        path = upstream_root / "rule" / "Surge" / name / f"{name}.list"
        if not path.exists():
            raise SystemExit(f"Missing upstream list: {path}")
        core_rules.update(parse_rules(path))

    # Extra rules that must exist upstream
    upstream_extra_rules: set[str] = set()
    missing_extra: list[str] = []
    if upstream_extra_path.exists():
        for raw in upstream_extra_path.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line in upstream_lines:
                upstream_extra_rules.add(line)
            else:
                missing_extra.append(line)

    # Custom rules (manual)
    custom_rules: set[str] = set()
    if custom_path.exists():
        for line in parse_rules(custom_path):
            custom_rules.add(line)

    merged_rules = set()
    merged_rules.update(core_rules)
    merged_rules.update(upstream_extra_rules)
    merged_rules.update(custom_rules)

    rules_sorted = sorted(merged_rules, key=sort_key)
    counts = Counter(rule.split(",", 1)[0] for rule in rules_sorted)
    updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header = build_header("OverseasAI", updated, counts)
    main_path = rules_dir / "OverseasAI.list"
    main_path.write_text("\n".join(header) + "\n" + "\n".join(rules_sorted) + "\n")

    resolve_rules = sorted({r.replace(",no-resolve", "") for r in rules_sorted}, key=sort_key)
    resolve_counts = Counter(rule.split(",", 1)[0] for rule in resolve_rules)
    resolve_header = build_header("OverseasAI_Resolve", updated, resolve_counts)
    resolve_path = rules_dir / "OverseasAI_Resolve.list"
    resolve_path.write_text("\n".join(resolve_header) + "\n" + "\n".join(resolve_rules) + "\n")

    if args.refresh_custom:
        custom_rules_new = sorted(
            {r for r in merged_rules if r not in core_rules and r not in upstream_extra_rules},
            key=sort_key,
        )
        custom_path.write_text("\n".join(custom_rules_new) + "\n")

    if missing_extra:
        upstream_missing_path.write_text("\n".join(sorted(missing_extra, key=sort_key)) + "\n")
    else:
        upstream_missing_path.write_text("")


if __name__ == "__main__":
    main()
