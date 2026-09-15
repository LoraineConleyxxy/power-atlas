"""Build offline, per-section token estimates for the text displayed by the catalogue.

Claude: the legacy Anthropic tokenizer converted to Hugging Face format by
SillyTavern (https://github.com/SillyTavern/SillyTavern/tree/release/src/tokenizers).
Anthropic describes this tokenizer as a rough approximation for Claude 3+:
https://github.com/anthropics/anthropic-tokenizer-typescript

Gemini: ASCII / non-ASCII character heuristic used by Google's Gemini CLI,
https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/utils/tokenCalculation.ts
Copyright Google LLC, Apache-2.0. The implementation below counts plain text only.

Kimi: Kimi-K2-Instruct vocabulary and splitting pattern published by Moonshot AI:
https://huggingface.co/moonshotai/Kimi-K2-Instruct/blob/main/tokenization_kimi.py
Copyright Moonshot AI, Modified MIT license (see that model's LICENSE).

Sections are counted independently, including separators. Results are estimates
of the displayed worldbook text; chat-message wrappers are not added.
"""
from pathlib import Path
import base64
import math
from functools import lru_cache
import urllib.request

import tiktoken
from tokenizers import Tokenizer

PROFILES = [
    dict(id='claude', name='Claude', method='旧版 Claude 分词器近似；Claude 3 及以后版本以官方计数为准。',
         source='https://github.com/anthropics/anthropic-tokenizer-typescript'),
    dict(id='gemini', name='Gemini', method='采用 Gemini CLI 的字符估算法，中文等非 ASCII 字符按较宽裕的系数估算。',
         source='https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/utils/tokenCalculation.ts'),
    dict(id='kimi', name='Kimi K2', method='采用公开 Kimi K2 分词器，按正文分段计数。',
         source='https://huggingface.co/moonshotai/Kimi-K2-Instruct/blob/main/tokenization_kimi.py'),
    dict(id='deepseek', name='DeepSeek V3', method='采用官方公开的 DeepSeek V3 分词器，按正文分段计数。',
         source='https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/tokenizer.json'),
    dict(id='glm', name='GLM 4.5', method='采用官方公开的 GLM 4.5 分词器，按正文分段计数。',
         source='https://huggingface.co/zai-org/GLM-4.5/blob/main/tokenizer.json'),
]

KIMI_PATTERN = '|'.join([
    r'[\p{Han}]+',
    r"[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+(?i:'s|'t|'re|'ve|'m|'ll|'d)?",
    r"[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*(?i:'s|'t|'re|'ve|'m|'ll|'d)?",
    r'\p{N}{1,3}', r' ?[^\s\p{L}\p{N}]+[\r\n]*', r'\s*[\r\n]+', r'\s+(?!\S)', r'\s+',
])

class Counter:
    def __init__(self):
        cache = Path(__file__).parent / '.tokenizer-cache'
        cache.mkdir(exist_ok=True)
        def asset(name, url):
            path = cache / name
            if not path.exists():
                with urllib.request.urlopen(url, timeout=60) as response:
                    data = response.read()
                path.write_bytes(data)
            return path
        claude_path = asset('claude-legacy-hf.json', 'https://raw.githubusercontent.com/SillyTavern/SillyTavern/release/src/tokenizers/claude.json')
        kimi_path = asset('kimi-k2.model', 'https://huggingface.co/moonshotai/Kimi-K2-Instruct/resolve/main/tiktoken.model')
        self.claude = Tokenizer.from_file(str(claude_path))
        self.deepseek = Tokenizer.from_file(str(asset('deepseek-v3.json',
            'https://huggingface.co/deepseek-ai/DeepSeek-V3/resolve/main/tokenizer.json')))
        self.glm = Tokenizer.from_file(str(asset('glm-4.5.json',
            'https://huggingface.co/zai-org/GLM-4.5/resolve/main/tokenizer.json')))
        ranks = {}
        for line in kimi_path.read_bytes().splitlines():
            token, rank = line.split()
            ranks[base64.b64decode(token)] = int(rank)
        self.kimi = tiktoken.Encoding(name='kimi-k2-text', pat_str=KIMI_PATTERN,
            mergeable_ranks=ranks, special_tokens={})

    @lru_cache(maxsize=None)
    def count(self, text):
        # Gemini CLI measures JS UTF-16 code units, including surrogate pairs.
        units = len(text.encode('utf-16-le')) // 2
        ascii_units = sum(ord(c) <= 127 for c in text)
        return dict(claude=len(self.claude.encode(text, add_special_tokens=False).ids),
            gemini=math.floor(ascii_units / 4 + (units - ascii_units) * 1.5),
            kimi=len(self.kimi.encode_ordinary(text)),
            deepseek=len(self.deepseek.encode(text, add_special_tokens=False).ids),
            glm=len(self.glm.encode(text, add_special_tokens=False).ids))

def attach_counts(catalog, grades):
    counter = Counter()
    for system in catalog:
        for row in system['records']:
            variants = {}
            for grade in (list(dict.fromkeys([row['grade'], *grades])) if row['kind'] == 'level' else [row['grade']]):
                totals = {p['id']:dict(general=0, system=0, keyword=0) for p in PROFILES}
                for i, part in enumerate(row['promptParts']):
                    text = part['text']
                    if part.get('identity'):
                        text = text.replace('【战斗力】' + row['grade'], '【战斗力】' + grade, 1)
                    if part.get('selection') and grade != row['grade']:
                        text += '\n【综合量级·' + grade + '】'
                    if i < len(row['promptParts']) - 1:
                        text += '\n\n'
                    count = counter.count(text)
                    for profile in PROFILES:
                        totals[profile['id']][part['category']] += count[profile['id']]
                variants[grade] = totals
            row['tokenCounts'] = variants
        print(system['short'] + '：已生成' + str(len(PROFILES)) + '种计数方式及可切换量级的计数。', flush=True)
