# Overseas AI Rules for Surge / 海外 AI 分流规则（Surge）

- English: see [English](#english)
- 中文：见 [中文说明](#中文说明)

## English

### Overview

This repository builds a single overseas AI rule-set for Surge and other rule-based clients. It combines selected upstream rules from `blackmatrix7/ios_rule_script` with a curated custom domain list for overseas AI products, coding tools, media tools, and AI infrastructure.

### Scope

- Focus on overseas AI services and supporting platforms
- Include model vendors, AI apps, AI IDEs, media tools, agent/search/data infrastructure, and AI-related verification or payment services
- Exclude mainland-first AI services that are usually directly reachable from mainland China
- Keep domains as narrow as possible; avoid overly broad catch-all domains when they would capture large amounts of non-AI traffic

### Coverage Snapshot

- Model vendors: OpenAI, Anthropic, Gemini, xAI, Cohere, Mistral, Groq, Cerebras, AI21, NVIDIA, Writer, SambaNova, Aleph Alpha, Ai2, Liquid AI, Nous Research
- Platforms and infra: OpenRouter, Hugging Face, Firecrawl, Tavily, Together, Fireworks, Replicate, Fal, LangChain, LlamaIndex, Pinecone, Weaviate, Qdrant, Milvus, Modal, Baseten, Anyscale, CoreWeave, Nebius, Crusoe, Vast.ai, Hyperbolic, Voyage AI, Nomic, turbopuffer
- LLM ops and data/agent infra: Langfuse, Helicone, Braintrust, Arize, Portkey, LiteLLM, Weights & Biases, Apify, Bright Data, Browserbase, Browserless, ScrapingBee, ZenRows, Diffbot, Serper, SerpApi, Glean, Hebbia, Dust, Sierra, Lindy, Relay, Bardeen
- Apps and coding tools: Perplexity, Poe, Cursor, Windsurf, v0, Lovable, Bolt, OpenClaw, Replit, AmpCode, Context7, Grep.app, Devin/Cognition, Cline, Roo Code, Qodo, Warp, Factory, CodeRabbit, Greptile, Sourcery, Sweep, Cosine, Pieces, Tabby, Refact, Mintlify, Gamma, Read AI, Granola
- Media and voice: Midjourney, Sora, Runway, Leonardo, Ideogram, ElevenLabs, Suno, Udio, Deepgram, AssemblyAI, HeyGen, Synthesia, D-ID, Black Forest Labs (FLUX), Recraft, Magnific, Photoroom, Topaz, Captions, Hedra, Higgsfield, Viggle, Genmo, Hume, Cartesia, Resemble, WellSaid, Speechify, LMNT, Fliki, Pictory, InVideo, Colossyan

### Files

- `rule/Surge/OverseasAI/OverseasAI.list`: main Surge rule-set
- `rule/Surge/OverseasAI/OverseasAI_Resolve.list`: same rules with IP rules normalized
- `rule/Surge/OverseasAI/OverseasAI_Custom.list`: custom-only domains merged into the main list
- `rule/<Client>/OverseasAI/OverseasAI.list`: generated outputs for Clash, Loon, Shadowrocket, QuantumultX, and Quantumult
- `rule/Singbox/OverseasAI/OverseasAI.json`: sing-box rule-set source format (version 3)
- `rule/Singbox/OverseasAI/OverseasAI.srs`: sing-box rule-set binary format (compiled)

### Usage

Surge:

```ini
[Rule]
RULE-SET,OverseasAI,PROXY

[Rule Set]
OverseasAI = https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Surge/OverseasAI/OverseasAI.list
```

Other clients:

- Clash: `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Clash/OverseasAI/OverseasAI.list`
- Loon: `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Loon/OverseasAI/OverseasAI.list`
- Shadowrocket: `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Shadowrocket/OverseasAI/OverseasAI.list`
- QuantumultX: `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/QuantumultX/OverseasAI/OverseasAI.list`
- Quantumult: `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Quantumult/OverseasAI/OverseasAI.list`
- sing-box (.json): `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Singbox/OverseasAI/OverseasAI.json`
- sing-box (.srs): `https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Singbox/OverseasAI/OverseasAI.srs`

sing-box config snippet:

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
      {
        "rule_set": "overseas-ai",
        "action": "route",
        "outbound": "proxy"
      }
    ]
  }
}
```

### Automation and Local Workflow

GitHub Actions runs daily sync, rebuild, and NXDOMAIN checks. Deletions are not automatic; review reports manually.

Local commands:

```bash
python scripts/sync_rules.py --upstream /path/to/ios_rule_script
python scripts/build_clients.py
python scripts/check_domains.py
```

Artifacts:

- `reports/nxdomain_report.md`
- `reports/nxdomain_candidates.txt`
- `reports/upstream_missing.txt`
- `data/nxdomain_state.json`

### Adding Domains

1. Edit `rule/Surge/OverseasAI/OverseasAI_Custom.list`
2. Rebuild the merged rule-set and client outputs
3. Review the generated diff before commit

## 中文说明

### 项目简介

这个仓库维护一份面向 Surge 及其他规则客户端的“海外 AI 分流规则集”。规则由两部分组成：上游 `blackmatrix7/ios_rule_script` 的精选规则，以及仓库维护的自定义海外 AI 域名清单。

### 收录范围

- 以海外 AI 服务和相关平台为主
- 收录大模型厂商、AI 应用、AI 编程工具、生成式媒体、Agent / 搜索 / 数据基础设施，以及 AI 相关认证或支付服务
- 默认不收录中国大陆通常可直接访问的大陆系 AI 服务
- 尽量使用边界清晰的域名，避免把大量非 AI 流量一并纳入

### 覆盖概览

- 模型厂商：OpenAI、Anthropic、Gemini、xAI、Cohere、Mistral、Groq、Cerebras、AI21、NVIDIA、Writer、SambaNova、Aleph Alpha、Ai2、Liquid AI、Nous Research
- 平台与基础设施：OpenRouter、Hugging Face、Firecrawl、Tavily、Together、Fireworks、Replicate、Fal、LangChain、LlamaIndex、Pinecone、Weaviate、Qdrant、Milvus、Modal、Baseten、Anyscale、CoreWeave、Nebius、Crusoe、Vast.ai、Hyperbolic、Voyage AI、Nomic、turbopuffer
- 大模型运维与数据 / Agent 基础设施：Langfuse、Helicone、Braintrust、Arize、Portkey、LiteLLM、Weights & Biases、Apify、Bright Data、Browserbase、Browserless、ScrapingBee、ZenRows、Diffbot、Serper、SerpApi、Glean、Hebbia、Dust、Sierra、Lindy、Relay、Bardeen
- 应用与编程工具：Perplexity、Poe、Cursor、Windsurf、v0、Lovable、Bolt、OpenClaw、Replit、AmpCode、Context7、Grep.app、Devin/Cognition、Cline、Roo Code、Qodo、Warp、Factory、CodeRabbit、Greptile、Sourcery、Sweep、Cosine、Pieces、Tabby、Refact、Mintlify、Gamma、Read AI、Granola
- 媒体与语音：Midjourney、Sora、Runway、Leonardo、Ideogram、ElevenLabs、Suno、Udio、Deepgram、AssemblyAI、HeyGen、Synthesia、D-ID、Black Forest Labs（FLUX）、Recraft、Magnific、Photoroom、Topaz、Captions、Hedra、Higgsfield、Viggle、Genmo、Hume、Cartesia、Resemble、WellSaid、Speechify、LMNT、Fliki、Pictory、InVideo、Colossyan

### 文件说明

- `rule/Surge/OverseasAI/OverseasAI.list`：Surge 主规则
- `rule/Surge/OverseasAI/OverseasAI_Resolve.list`：去掉 `no-resolve` 的 Surge 变体
- `rule/Surge/OverseasAI/OverseasAI_Custom.list`：仅自定义补充域名，已合并进主规则
- `rule/<Client>/OverseasAI/OverseasAI.list`：各客户端生成结果
- `rule/Singbox/OverseasAI/OverseasAI.json`：sing-box rule-set 源格式（version 3）
- `rule/Singbox/OverseasAI/OverseasAI.srs`：sing-box rule-set 二进制格式（编译后）

### 使用方法

Surge 示例：

```ini
[Rule]
RULE-SET,OverseasAI,PROXY

[Rule Set]
OverseasAI = https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Surge/OverseasAI/OverseasAI.list
```

其他客户端订阅地址：

- Clash：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Clash/OverseasAI/OverseasAI.list`
- Loon：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Loon/OverseasAI/OverseasAI.list`
- Shadowrocket：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Shadowrocket/OverseasAI/OverseasAI.list`
- QuantumultX：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/QuantumultX/OverseasAI/OverseasAI.list`
- Quantumult：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Quantumult/OverseasAI/OverseasAI.list`
- sing-box (.json)：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Singbox/OverseasAI/OverseasAI.json`
- sing-box (.srs)：`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Singbox/OverseasAI/OverseasAI.srs`

### 自动化与本地更新

GitHub Actions 会按日同步上游、重建规则并检查 NXDOMAIN。候选域名不会自动删除，需要人工复核报告。

本地常用命令：

```bash
python scripts/sync_rules.py --upstream /path/to/ios_rule_script
python scripts/build_clients.py
python scripts/check_domains.py
```

相关产物：

- `reports/nxdomain_report.md`
- `reports/nxdomain_candidates.txt`
- `reports/upstream_missing.txt`
- `data/nxdomain_state.json`

### 如何补充新域名

1. 编辑 `rule/Surge/OverseasAI/OverseasAI_Custom.list`
2. 重新生成主规则和各客户端规则
3. 检查 diff，确认没有误收录或过宽域名后再提交

## License / 许可

Derived from `blackmatrix7/ios_rule_script` (GPL-2.0). See `LICENSE`.
