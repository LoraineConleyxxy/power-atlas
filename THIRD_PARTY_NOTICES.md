# Token counter references

The public page contains precomputed counts, not the tokenizer vocabulary files.
The build caches downloaded vocabularies in the ignored `.tokenizer-cache/` directory.

- **Claude:** legacy Anthropic tokenizer, using the Hugging Face conversion bundled with [SillyTavern](https://github.com/SillyTavern/SillyTavern/tree/release/src/tokenizers). [Anthropic's original tokenizer](https://github.com/anthropics/anthropic-tokenizer-typescript) describes it as a rough approximation for Claude 3 and later models.
- **Gemini:** the plain-text ASCII/non-ASCII heuristic documented in [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/utils/tokenCalculation.ts), copyright Google LLC, Apache-2.0. This project implements the character-count formula; it does not call the Gemini API.
- **Kimi K2:** the vocabulary and splitting pattern from [Moonshot AI's Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct). The splitting pattern in `token_counter.py` follows that model's published tokenizer. Its license is reproduced below.
- **DeepSeek V3:** the official [DeepSeek-V3 tokenizer](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/tokenizer.json), used at build time with special-token insertion disabled. Vocabulary files remain in the local build cache.
- **GLM 4.5:** the official [GLM-4.5 tokenizer](https://huggingface.co/zai-org/GLM-4.5/blob/main/tokenizer.json), used at build time with special-token insertion disabled. Vocabulary files remain in the local build cache.

All counters operate on the displayed worldbook text, section by section, including the separating newlines. The total is the sum of section estimates. Message wrappers, character cards, conversation history, tools, images, and generation output are outside this counter. Display-only colour labels are not counted or copied.

## Kimi K2 Modified MIT License

Copyright (c) 2025 Moonshot AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Our only modification part is that, if the Software (or any derivative works
thereof) is used for any of your commercial products or services that have
more than 100 million monthly active users, or more than 20 million US dollars
(or equivalent in other currencies) in monthly revenue, you shall prominently
display "Kimi K2" on the user interface of such product or service.
