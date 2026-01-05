# Overseas AI Rules for Surge / 海外 AI 分流规则（Surge）

This repo aggregates overseas AI/LLM services into a single Surge rule-set,
based on the upstream `blackmatrix7/ios_rule_script` Surge rules and a curated
set of AI-related custom domains.

本仓库将海外 AI/大模型相关服务整合为一个 Surge 规则集，基础规则来源于
`blackmatrix7/ios_rule_script`，并补充了常用 AI 应用的自定义域名。

## Sources (Upstream) / 上游规则来源
- OpenAI
- Claude
- Anthropic
- Gemini
- BardAI
- Copilot
- Civitai
- Stripe
- PayPal

## Coverage / 覆盖范围
Model vendors, AI platforms, and apps are grouped below; the exact domains
are in `OverseasAI.list`, and custom-only entries are in `OverseasAI_Custom.list`.

以下按类别概览覆盖范围，具体域名请以 `OverseasAI.list` 为准，
自定义补充项见 `OverseasAI_Custom.list`。

### AI Model Vendors / 大模型厂商
OpenAI, Anthropic, Google Gemini, xAI, Meta, Cohere, Mistral, Groq, Cerebras,
AI21, Inflection (Pi), Reka, NVIDIA (NIM/API), and more.

### AI Platforms & Infra / 平台与基础设施
OpenRouter, Hugging Face, Together, Fireworks, Replicate, Fal, LangChain,
LlamaIndex, Pinecone, Weaviate, Qdrant, Milvus, Chroma, OpenCode (opencode.ai /
opncd.ai / models.dev), and more.

### AI Apps / AI 应用
Perplexity, Poe, Character.AI, You.com, Phind, Exa, Jasper, Copy.ai,
Writesonic, Rytr, Sudowrite, Wordtune, Grammarly, QuillBot, Diabrowser, and
more.

### AI Media (Image/Video/Audio) / 生成式媒体
Midjourney, Runway, Leonardo, Ideogram, Krea, Luma, Pika, Stability,
DreamStudio, PlaygroundAI, Kaiber, ElevenLabs, Suno, Udio, and more.

### AI IDEs & Coding Tools / AI 编程工具
GitHub Copilot, Cursor, Windsurf, Codeium, Augment, Tabnine, Supermaven,
Continue, Sourcegraph/Cody, Replit, Context7, Grep.app (MCP endpoints), and
more.

### AI Verification & Payments / 认证与支付
SheerID, Stripe, PayPal, ID.me, Paddle, LemonSqueezy, Chargebee,
FastSpring, Checkout.com, and more.

## Custom AI Domains / 自定义 AI 域名（上游未包含）
Custom domains are merged into the main list and recorded in:
`rule/Surge/OverseasAI/OverseasAI_Custom.list`.

自定义域名已合并进主规则，并记录在：
`rule/Surge/OverseasAI/OverseasAI_Custom.list`。

If you want more custom domains added, send the list and I will extend
`OverseasAI_Custom.list` and re-merge.

如果需要新增更多自定义域名，请提供清单，我会扩展
`OverseasAI_Custom.list` 并重新合并。

## Files / 文件
- `rule/Surge/OverseasAI/OverseasAI.list`
- `rule/Surge/OverseasAI/OverseasAI_Resolve.list` (same rules, IP rules without `no-resolve`)
- `rule/Surge/OverseasAI/OverseasAI_Custom.list` (custom-only, already merged)
- `rule/Clash/OverseasAI/OverseasAI.list`
- `rule/Loon/OverseasAI/OverseasAI.list`
- `rule/Shadowrocket/OverseasAI/OverseasAI.list`
- `rule/QuantumultX/OverseasAI/OverseasAI.list`
- `rule/Quantumult/OverseasAI/OverseasAI.list` (alias of QuantumultX format)

## Surge Usage / Surge 使用方式
Add one RULE-SET pointing at the list you prefer and map it to a single
proxy policy.

添加一个 RULE-SET 指向你选择的列表，并映射到单一代理策略即可。

Example / 示例:

```
[Rule]
RULE-SET,OverseasAI,PROXY

[Rule Set]
OverseasAI = https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Surge/OverseasAI/OverseasAI.list
```

## Other Clients / 其他客户端订阅

### Clash
Rule provider URL:
`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Clash/OverseasAI/OverseasAI.list`

### Loon
RULE-SET URL:
`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Loon/OverseasAI/OverseasAI.list`

### Shadowrocket
RULE-SET URL:
`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Shadowrocket/OverseasAI/OverseasAI.list`

### Quantumult / QuantumultX
Filter URL (policy name is embedded as `OverseasAI`):
`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/QuantumultX/OverseasAI/OverseasAI.list`

Quantumult alias:
`https://raw.githubusercontent.com/viewer12/OverseasAI.list/main/rule/Quantumult/OverseasAI/OverseasAI.list`

## Automation / 自动化

Daily GitHub Actions syncs from upstream, rebuilds all client formats, and
checks domains for NXDOMAIN. Deletion is **not** automatic; the report is for
manual confirmation.

每日自动同步上游、重建规则、检测域名 NXDOMAIN，但**不会自动删除**，仅输出报告供人工确认。

Artifacts and state:
- `reports/nxdomain_report.md`
- `reports/nxdomain_candidates.txt`
- `data/nxdomain_state.json`

Scripts (local usage):

```
python scripts/sync_rules.py --upstream /path/to/ios_rule_script
python scripts/build_clients.py
python scripts/check_domains.py
```

## License / 许可
Derived from `blackmatrix7/ios_rule_script` (GPL-2.0). See `LICENSE`.
