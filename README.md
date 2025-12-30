# Overseas AI Rules for Surge

This repo aggregates AI and LLM related overseas services from the
blackmatrix7/ios_rule_script Surge rules into a single rule-set.

## Included sources (upstream rule sets)
- OpenAI
- Claude
- Anthropic
- Gemini
- BardAI
- Copilot
- Civitai
- Stripe
- PayPal

## AI services found in upstream general lists
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

## Custom AI-related domains (not in upstream)
These are merged into the main list and also recorded in:
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

## Files
- `rule/Surge/OverseasAI/OverseasAI.list`
- `rule/Surge/OverseasAI/OverseasAI_Resolve.list` (same rules, IP rules without `no-resolve`)
- `rule/Surge/OverseasAI/OverseasAI_Custom.list` (custom-only, already merged)

## Surge usage
Add one RULE-SET pointing at the list you prefer and map it to a single
proxy policy.

Example:

```
[Rule]
RULE-SET,OverseasAI,PROXY

[Rule Set]
OverseasAI = https://raw.githubusercontent.com/<your-org>/<your-repo>/master/rule/Surge/OverseasAI/OverseasAI.list
```

## License
Derived from `blackmatrix7/ios_rule_script` (GPL-2.0). See `LICENSE`.
