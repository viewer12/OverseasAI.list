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

## Upstream AI Services / 上游通用列表里的 AI 服务
- GitHub Copilot (`githubcopilot.com`, `api.githubcopilot.com`)
- Sourcegraph/Cody (`sourcegraph.com`)
- xAI (`x.ai`, `grok.com`)
- Perplexity (`perplexity.ai`, `perplexity.com`, `pplx.ai`)
- Poe (`poe.com`, `qpoe.com`)
- Cursor (`cursor.com`, `cursor.sh`)
- OpenRouter (`openrouter.ai`)
- Cohere (`cohere.ai`, `cohere.com`)
- Mistral (`mistral.ai`)
- Groq (`groq.com`)
- Cerebras (`cerebras.ai`)
- Hugging Face (`huggingface.co`, `hf.co`)
- Character.AI (`character.ai`)
- Suno (`suno.ai`)
- ElevenLabs (`elevenlabs.com`, `elevenlabs.io`)
- Clipdrop (`clipdrop.co`)

## Custom AI Domains / 自定义 AI 域名（上游未包含）
These are merged into the main list and also recorded in:
`rule/Surge/OverseasAI/OverseasAI_Custom.list`

以下域名已合并进主规则，并同时记录在：
`rule/Surge/OverseasAI/OverseasAI_Custom.list`

- SheerID (`sheerid.com`)
- Windsurf/Codeium (`windsurf.ai`, `codeium.com`, `windsurf-telemetry.codeium.com`)
- Augment (`augment.dev`, `augmentcode.com`)
- Tabnine (`tabnine.com`)
- Supermaven (`supermaven.com`)
- Continue (`continue.dev`)
- AI21 (`ai21.com`, `ai21labs.com`)
- Stability (`stability.ai`)
- Midjourney (`midjourney.com`)
- Runway (`runwayml.com`)
- Replicate (`replicate.com`)
- Together (`together.ai`)
- Fireworks (`fireworks.ai`)
- Leonardo (`leonardo.ai`)
- Luma (`luma.ai`)
- Pika (`pika.art`)
- Ideogram (`ideogram.ai`)
- Krea (`krea.ai`)
- Fal (`fal.ai`)
- Udio (`udio.com`)

If you want more custom domains added, send the list and I will extend
`OverseasAI_Custom.list` and re-merge.

如果需要新增更多自定义域名，请提供清单，我会扩展
`OverseasAI_Custom.list` 并重新合并。

## Files / 文件
- `rule/Surge/OverseasAI/OverseasAI.list`
- `rule/Surge/OverseasAI/OverseasAI_Resolve.list` (same rules, IP rules without `no-resolve`)
- `rule/Surge/OverseasAI/OverseasAI_Custom.list` (custom-only, already merged)

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

## License / 许可
Derived from `blackmatrix7/ios_rule_script` (GPL-2.0). See `LICENSE`.
