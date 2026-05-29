<div align="center">

# 🌐 OverseasAI · 海外 AI 分流规则集

**一份持续维护、覆盖全面的海外 AI 服务分流规则，适用于 Surge / Clash / sing-box 等主流规则客户端。**

[![License](https://img.shields.io/github/license/viewer12/OverseasAI.list?color=blue)](./LICENSE)
[![Rules](https://img.shields.io/badge/rules-592-success)](./rule/Surge/OverseasAI/OverseasAI.list)
[![Daily Sync](https://img.shields.io/github/actions/workflow/status/viewer12/OverseasAI.list/rules-sync.yml?label=daily%20sync)](./.github/workflows/rules-sync.yml)
[![Last Commit](https://img.shields.io/github/last-commit/viewer12/OverseasAI.list)](https://github.com/viewer12/OverseasAI.list/commits/main)
[![Stars](https://img.shields.io/github/stars/viewer12/OverseasAI.list?style=flat)](https://github.com/viewer12/OverseasAI.list/stargazers)

**简体中文** · [English](#-english)

</div>

---

## 📖 简介

`OverseasAI` 把上游 [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) 的精选核心规则，与本仓库人工维护的 **海外 AI 域名清单** 合并为 **一份规则集**，并自动生成各主流客户端格式。

它的目标只有一个：**让你把海外 AI 相关的流量（大模型、AI 应用、AI 编程、生成式媒体、Agent / 向量 / 数据基础设施、AI 相关认证与支付）干净地分流到代理出口**，同时尽量不误伤普通流量。

- ✅ **覆盖全面** —— 100+ 海外 AI 服务商，含模型厂商、推理云、编程 Agent、生成式媒体、Agent / 数据基础设施
- 🤖 **每日自动同步** —— GitHub Actions 每天拉取上游、重建规则、并做 NXDOMAIN 失效检测
- 🧩 **多客户端开箱即用** —— Surge / Clash / Loon / Shadowrocket / Quantumult X / Quantumult / sing-box
- 🎯 **边界清晰** —— 优先精确域名，避免过宽的 catch-all 把大量非 AI 流量一并纳入
- 🌏 **聚焦海外** —— 默认排除大陆可直连的大陆系 AI 服务，并标注归属存疑/已停服的服务

> ⚠️ 本规则集只负责「**匹配哪些域名**」，至于把它们导向代理还是直连，由你在客户端的策略里决定。

## 📑 目录

- [收录范围](#-收录范围)
- [快速开始](#-快速开始)
- [订阅地址一览](#-订阅地址一览)
- [规则统计](#-规则统计)
- [文件结构](#-文件结构)
- [工作原理与自动化](#-工作原理与自动化)
- [如何贡献](#-如何贡献)
- [收录原则](#-收录原则)
- [常见问题](#-常见问题)
- [致谢与许可](#-致谢与许可)

## 🗂 收录范围

| 类别 | 代表服务 |
| --- | --- |
| **模型厂商 / 研究实验室** | OpenAI、Anthropic（Claude）、Google Gemini / DeepMind、xAI（Grok）、Cohere、Mistral、Groq、Cerebras、AI21、NVIDIA、Meta AI、Character.AI、Inflection、Reka、Writer、SambaNova、Aleph Alpha、Ai2、Liquid AI、Nous Research |
| **推理 / GPU 云** | OpenRouter、Together、Fireworks、Replicate、Fal、DeepInfra、Runpod、Lambda、Modal、Baseten、Anyscale、CoreWeave、Nebius、Crusoe、Vast.ai、Hyperbolic |
| **向量库 / Embedding** | Pinecone、Weaviate、Qdrant、Milvus、Chroma、turbopuffer、Voyage AI、Nomic |
| **LLM 运维 / 网关 / 评测** | LangChain / LangSmith、LlamaIndex、Langfuse、Helicone、Braintrust、Arize、Portkey、LiteLLM、Weights & Biases |
| **AI 应用 / 搜索 / 浏览器** | Perplexity、Poe、You.com、Phind、Pi、Dia、Gamma、Read AI、Granola、Sierra、Glean、Hebbia、Dust |
| **AI 编程 / IDE / Agent** | GitHub Copilot、Cursor、Windsurf、Zed、Continue、Tabnine、Supermaven、Sourcegraph、Augment、Replit、v0、Lovable、Bolt、Devin / Cognition、Cline、Roo Code、Qodo、Warp、Factory、CodeRabbit、Greptile、Sourcery、Sweep、Cosine、Pieces、Tabby、Refact、Mintlify |
| **生成式媒体 / 语音 / 视频** | Midjourney、Sora、Runway、Leonardo、Ideogram、Stability、HeyGen、Synthesia、D-ID、Black Forest Labs（FLUX）、Recraft、Magnific、Photoroom、Topaz、Captions、Hedra、Higgsfield、Viggle、Genmo、Pika、Luma |
| **语音 / TTS / STT** | ElevenLabs、Deepgram、AssemblyAI、Hume、Cartesia、Resemble、WellSaid、Speechify、LMNT、Murf、Play.ht |
| **Agent / 抓取 / 数据 API** | Firecrawl、Tavily、Exa、Apify、Bright Data、Browserbase、Browserless、ScrapingBee、ZenRows、Diffbot、Serper、SerpApi、Lindy、Relay、Bardeen |
| **认证 / 支付（AI 相关）** | Stripe、PayPal、Paddle、Chargebee、FastSpring、Lemon Squeezy、Checkout.com、SheerID、ID.me |

> 完整清单见 [`rule/Surge/OverseasAI/OverseasAI.list`](./rule/Surge/OverseasAI/OverseasAI.list)。

## 🚀 快速开始

所有规则集都托管在 `main` 分支，原始地址前缀为：

```
https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/
```

### Surge

```ini
[Rule]
RULE-SET,OverseasAI,PROXY

[Rule Set]
OverseasAI = https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Surge/OverseasAI/OverseasAI.list
```

### Clash / Mihomo

```yaml
rule-providers:
  OverseasAI:
    type: http
    behavior: classical
    format: text
    interval: 86400
    url: https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Clash/OverseasAI/OverseasAI.list
    path: ./rule-providers/OverseasAI.list

rules:
  - RULE-SET,OverseasAI,🚀 代理
```

### sing-box

```json
{
  "route": {
    "rule_set": [
      {
        "type": "remote",
        "tag": "overseas-ai",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Singbox/OverseasAI/OverseasAI.srs",
        "download_detour": "proxy"
      }
    ],
    "rules": [
      { "rule_set": "overseas-ai", "action": "route", "outbound": "proxy" }
    ]
  }
}
```

## 🔗 订阅地址一览

| 客户端 | 订阅地址 |
| --- | --- |
| **Surge** | `…/main/rule/Surge/OverseasAI/OverseasAI.list` |
| **Surge**（IP 规则去 `no-resolve`） | `…/main/rule/Surge/OverseasAI/OverseasAI_Resolve.list` |
| **Clash / Mihomo** | `…/main/rule/Clash/OverseasAI/OverseasAI.list` |
| **Loon** | `…/main/rule/Loon/OverseasAI/OverseasAI.list` |
| **Shadowrocket** | `…/main/rule/Shadowrocket/OverseasAI/OverseasAI.list` |
| **Quantumult X** | `…/main/rule/QuantumultX/OverseasAI/OverseasAI.list` |
| **Quantumult** | `…/main/rule/Quantumult/OverseasAI/OverseasAI.list` |
| **sing-box**（源格式 `.json`） | `…/main/rule/Singbox/OverseasAI/OverseasAI.json` |
| **sing-box**（编译 `.srs`） | `…/main/rule/Singbox/OverseasAI/OverseasAI.srs` |

> `…` 代表前缀 `https://raw.githubusercontent.com/viewer12/OverseasAI.list`。国内访问 GitHub 较慢时，可自行替换为 jsDelivr 等加速镜像。

## 📊 规则统计

| 类型 | 数量 |
| --- | ---: |
| `DOMAIN` | 48 |
| `DOMAIN-SUFFIX` | 528 |
| `DOMAIN-KEYWORD` | 11 |
| `IP-CIDR` | 2 |
| `IP-ASN` | 2 |
| `USER-AGENT` | 1 |
| **合计** | **592** |

> 数量随每日同步变化，以规则文件头部的 `# TOTAL` 为准。

## 📁 文件结构

```
OverseasAI.list
├── rule/
│   ├── Surge/OverseasAI/
│   │   ├── OverseasAI.list          # Surge 主规则（核心 + 上游补充 + 自定义 合并）
│   │   ├── OverseasAI_Resolve.list  # 去掉 no-resolve 的变体
│   │   └── OverseasAI_Custom.list   # 仅自定义补充域名（贡献入口）
│   ├── Clash|Loon|Shadowrocket|QuantumultX|Quantumult/OverseasAI/OverseasAI.list
│   └── Singbox/OverseasAI/
│       ├── OverseasAI.json          # sing-box 源格式（version 3）
│       └── OverseasAI.srs           # sing-box 编译后的二进制
├── scripts/
│   ├── sync_rules.py                # 合并上游核心 + 上游补充 + 自定义 → Surge 主规则
│   ├── build_clients.py             # 由 Surge 主规则生成其余客户端格式
│   └── check_domains.py             # NXDOMAIN 失效域名检测
├── data/
│   ├── upstream_extra_rules.txt     # 必须存在于上游的「补充」规则清单
│   └── nxdomain_state.json          # 失效检测状态
└── reports/                         # 自动生成的报告（失效候选、上游缺失等）
```

## ⚙️ 工作原理与自动化

规则由三部分合并而成：

1. **核心规则（CORE）** —— 取自上游 `blackmatrix7/ios_rule_script` 的 `OpenAI / Claude / Anthropic / Gemini / BardAI / Copilot / Civitai / Stripe / PayPal` 列表；
2. **上游补充（UPSTREAM-EXTRA）** —— 在 `data/upstream_extra_rules.txt` 中声明、且必须在上游存在的额外规则（如 Perplexity、Cursor、OpenRouter 等）；
3. **自定义（CUSTOM）** —— 本仓库人工维护的海外 AI 域名，见 `OverseasAI_Custom.list`。

GitHub Actions 每天定时执行：拉取上游 → `sync_rules.py` 合并 → `build_clients.py` 生成各客户端 → `check_domains.py` 做 NXDOMAIN 检测并产出报告。**失效域名不会自动删除**，需人工复核 `reports/` 后处理。

本地复现：

```bash
pip install -r requirements.txt
python scripts/sync_rules.py --upstream /path/to/ios_rule_script
python scripts/build_clients.py     # 需要 sing-box 在 PATH 中才会编译 .srs
python scripts/check_domains.py
```

## 🤝 如何贡献

欢迎补充新的海外 AI 服务！流程很简单：

1. 编辑 [`rule/Surge/OverseasAI/OverseasAI_Custom.list`](./rule/Surge/OverseasAI/OverseasAI_Custom.list)，按字母序新增 `DOMAIN-SUFFIX,example.com`；
2. 运行 `python scripts/build_clients.py` 重新生成各客户端规则（主规则会在下次同步时自动合并）；
3. 检查 `git diff`，确认没有误收录或过宽域名；
4. 提交 PR，并在描述中说明服务名称、官方域名归属与是否为海外服务。

> 不确定怎么改？直接开 [Issue](https://github.com/viewer12/OverseasAI.list/issues) 提名服务，我们来核实收录。

## 🧭 收录原则

- **聚焦海外 AI**：以海外 AI 服务及配套平台为主。
- **排除大陆直连**：默认不收录大陆通常可直接访问的大陆系 AI 服务（如 DeepSeek、Kimi、智谱、MiniMax 等）。
- **边界清晰**：尽量使用精确域名 / 后缀，避免 `notion.so`、`brave.com`、`freepik.com` 这类大量承载非 AI 流量的过宽域名。
- **归属可核实**：新增前核实域名确实归属该公司，并验证可解析；归属存疑、已停服或被收购整合的服务会被标注或排除。

## ❓ 常见问题

<details>
<summary><b>规则匹配后是走代理还是直连？</b></summary>

由你自己决定。本规则集只提供「`OverseasAI`」这一组匹配规则，你需要在客户端里把它指向某个策略（如 `PROXY` / 代理组）。
</details>

<details>
<summary><b>为什么我常用的某个 AI 服务没收录？</b></summary>

可能是：① 它是大陆可直连的大陆系服务（按原则不收录）；② 域名过宽会误伤普通流量；③ 我们还没发现它。欢迎开 Issue / PR 提名。
</details>

<details>
<summary><b>失效（NXDOMAIN）的域名会被自动删除吗？</b></summary>

不会。自动化只产出候选报告，删除需人工复核，以免误删临时解析异常的域名。
</details>

<details>
<summary><b>国内拉取规则很慢怎么办？</b></summary>

把 `raw.githubusercontent.com/viewer12/OverseasAI.list/main/` 换成 jsDelivr 等 CDN 镜像即可，规则内容一致。
</details>

## 🙏 致谢与许可

- 规则核心衍生自 [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script)（GPL-2.0）。
- 部分收录范围参考了社区精选的 [`v2fly/domain-list-community`](https://github.com/v2fly/domain-list-community)。

本项目以 **GPL-2.0** 许可发布，详见 [`LICENSE`](./LICENSE)。

---

<div align="center">

## 🌐 English

**A continuously maintained, broad-coverage rule-set for overseas AI services — for Surge / Clash / sing-box and other rule-based clients.**

[简体中文](#-overseasai--海外-ai-分流规则集) · **English**

</div>

### Overview

`OverseasAI` merges curated core rules from [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) with a hand-maintained list of **overseas AI domains** into a single rule-set, then auto-generates every major client format.

Its single goal: **cleanly route your overseas-AI traffic** (model vendors, AI apps, AI coding, generative media, agent / vector / data infra, AI-related auth & payments) to your proxy, while avoiding collateral damage to ordinary traffic.

- ✅ **Broad coverage** — 100+ overseas AI services across vendors, inference clouds, coding agents, generative media, and agent/data infra
- 🤖 **Daily auto-sync** — GitHub Actions pulls upstream, rebuilds rules, and runs NXDOMAIN checks every day
- 🧩 **Multi-client** — Surge / Clash / Loon / Shadowrocket / Quantumult X / Quantumult / sing-box
- 🎯 **Narrow by design** — prefers precise domains; avoids broad catch-alls that capture lots of non-AI traffic
- 🌏 **Overseas-focused** — excludes mainland-first AI services reachable directly from mainland China

> ⚠️ This rule-set only decides **which domains match**. Whether they go to proxy or direct is up to your client policy.

### Quick start

All rule-sets live on `main`; raw prefix:

```
https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/
```

**Surge**

```ini
[Rule]
RULE-SET,OverseasAI,PROXY

[Rule Set]
OverseasAI = https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Surge/OverseasAI/OverseasAI.list
```

**sing-box**

```json
{
  "route": {
    "rule_set": [
      {
        "type": "remote",
        "tag": "overseas-ai",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Singbox/OverseasAI/OverseasAI.srs",
        "download_detour": "proxy"
      }
    ],
    "rules": [
      { "rule_set": "overseas-ai", "action": "route", "outbound": "proxy" }
    ]
  }
}
```

### Subscription URLs

| Client | URL |
| --- | --- |
| Surge | `…/main/rule/Surge/OverseasAI/OverseasAI.list` |
| Surge (IP rules without `no-resolve`) | `…/main/rule/Surge/OverseasAI/OverseasAI_Resolve.list` |
| Clash / Mihomo | `…/main/rule/Clash/OverseasAI/OverseasAI.list` |
| Loon | `…/main/rule/Loon/OverseasAI/OverseasAI.list` |
| Shadowrocket | `…/main/rule/Shadowrocket/OverseasAI/OverseasAI.list` |
| Quantumult X | `…/main/rule/QuantumultX/OverseasAI/OverseasAI.list` |
| Quantumult | `…/main/rule/Quantumult/OverseasAI/OverseasAI.list` |
| sing-box (`.json`) | `…/main/rule/Singbox/OverseasAI/OverseasAI.json` |
| sing-box (`.srs`) | `…/main/rule/Singbox/OverseasAI/OverseasAI.srs` |

> `…` = `https://raw.githubusercontent.com/viewer12/OverseasAI.list`.

### How it works

Rules are merged from three sources: **CORE** (upstream `blackmatrix7` lists for OpenAI / Claude / Anthropic / Gemini / BardAI / Copilot / Civitai / Stripe / PayPal), **UPSTREAM-EXTRA** (declared in `data/upstream_extra_rules.txt`, must exist upstream), and **CUSTOM** (`OverseasAI_Custom.list`). A daily GitHub Action syncs upstream, runs `sync_rules.py` → `build_clients.py` → `check_domains.py`. NXDOMAIN candidates are reported, never auto-deleted.

Local rebuild:

```bash
pip install -r requirements.txt
python scripts/sync_rules.py --upstream /path/to/ios_rule_script
python scripts/build_clients.py
python scripts/check_domains.py
```

### Contributing

1. Edit [`OverseasAI_Custom.list`](./rule/Surge/OverseasAI/OverseasAI_Custom.list) — add `DOMAIN-SUFFIX,example.com` in order.
2. Run `python scripts/build_clients.py` to regenerate client outputs.
3. Review the `git diff` for over-broad or mistaken entries.
4. Open a PR noting the service name, domain ownership, and that it's an overseas service.

### Credits & License

Core rules derive from [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) (GPL-2.0); coverage also references [`v2fly/domain-list-community`](https://github.com/v2fly/domain-list-community). Released under **GPL-2.0** — see [`LICENSE`](./LICENSE).
