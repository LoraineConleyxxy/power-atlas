# Tokenizer comparison — 2026-09-15

This comparison covers the public tokenizer files used to count the catalogue's plain-text worldbook content. It does not compare model capabilities or chat-template overhead.

| Provider | Previously used | Updated source | Observed difference |
| --- | --- | --- | --- |
| Kimi | K2 | K3, revision `f831ab66814297da540d832a5235f8e904f29d06` | `tiktoken.model` bytes and ordinary-text splitting regex are identical. K3 separately changes conversation/control-token handling. |
| DeepSeek | V3 | V4.1-Flash, revision `dba1be0a40aa45a94ad051997016db3960a90277` | The full BPE model, normalizer, pre-tokenizer and post-processor match. Both ordinary vocabularies have 128,000 entries. Added tokens differ. |
| GLM | 4.5 | 5.3, revision `aca966e4e02791568aa6a4ced368624b3d897f42` | Vocabulary, merge rules, added tokens and post-processor differ. Ordinary vocabulary changes from 151,329 to 154,820 entries. Normalizer and pre-tokenizer match. |

For the concatenated `密教·蛾·通晓者` prompt in catalogue v1.17, with special-token insertion disabled, DeepSeek V3 and V4.1-Flash both produce 1,526 tokens; GLM 4.5 and 5.3 both produce 1,598. Equal counts for this example do not establish identical tokenization for every text. The website retains per-section estimates, so joining all sections before encoding can produce a slightly different total.

Public sources:

- [Kimi K3 tokenizer implementation](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/tokenization_kimi.py)
- [DeepSeek V4.1-Flash tokenizer](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/dba1be0a40aa45a94ad051997016db3960a90277/tokenizer.json)
- [GLM 5.3 tokenizer](https://huggingface.co/zai-org/GLM-5.3/blob/aca966e4e02791568aa6a4ced368624b3d897f42/tokenizer.json)

Downloaded-file SHA-256:

- Kimi K3 `tiktoken.model`: `b6c497a7469b33ced9c38afb1ad6e47f03f5e5dc05f15930799210ec050c5103`
- DeepSeek V4.1 `tokenizer.json`: `c90dfa01249db1be4245780a052ede752e1361c612ac6d08e2bdada7d599476b`
- GLM 5.3 `tokenizer.json`: `19e773648cb4e65de8660ea6365e10acca112d42a854923df93db4a6f333a82d`
