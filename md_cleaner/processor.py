import re
from .rules import CN, EN, JP, EMOJI, SYMBOLS

"""
    Remove unnecessary spaces between specific character boundaries:
    Chinese ↔ English/number
    Japanese ↔ English/number
    Chinese ↔ English symbols
    Japanese ↔ English symbols
    Chinese ↔ Emoji
    Japanese ↔ Emoji
    English/number ↔ Emoji
    Chinese ↔ Chinese
    Japanese ↔ Japanese
    English/number ↔ English symbols
"""
# ==================================================
# Precompiled spacing rules
# ==================================================
_RAW_RULES = [
    # ===== Chinese (CN) boundaries =====
    # CN ↔ EN
    (rf"({CN})\s+({EN})", r"\1\2"),
    (rf"({EN})\s+({CN})", r"\1\2"),
    # CN ↔ JP
    (rf"({CN})\s+({JP})", r"\1\2"),
    (rf"({JP})\s+({CN})", r"\1\2"),
    # CN ↔ CN
    (rf"({CN})\s+({CN})", r"\1\2"),
    # CN ↔ SYMBOLS
    (rf"({CN})\s+({SYMBOLS})", r"\1\2"),
    (rf"({SYMBOLS})\s+({CN})", r"\1\2"),
    # CN ↔ EMOJI
    (rf"({CN})\s+({EMOJI})", r"\1\2"),
    (rf"({EMOJI})\s+({CN})", r"\1\2"),
    # ===== Japanese (JP) boundaries =====
    # JP ↔ EN
    (rf"({JP})\s+({EN})", r"\1\2"),
    (rf"({EN})\s+({JP})", r"\1\2"),
    # JP ↔ JP
    (rf"({JP})\s+({JP})", r"\1\2"),
    # JP ↔ SYMBOLS
    (rf"({JP})\s+({SYMBOLS})", r"\1\2"),
    (rf"({SYMBOLS})\s+({JP})", r"\1\2"),
    # JP ↔ EMOJI
    (rf"({JP})\s+({EMOJI})", r"\1\2"),
    (rf"({EMOJI})\s+({JP})", r"\1\2"),
    # ===== English / Numbers (EN) boundaries =====
    # EN ↔ SYMBOLS
    (rf"({EN})\s+({SYMBOLS})", r"\1\2"),
    (rf"({SYMBOLS})\s+({EN})", r"\1\2"),
    # EMOJI ↔ EN
    (rf"({EMOJI})\s+({EN})", r"\1\2"),
    (rf"({EN})\s+({EMOJI})", r"\1\2"),
]
# Compile once at import time
SPACING_RULES: list[tuple[re.Pattern, str]] = [
    (re.compile(pattern), repl) for pattern, repl in _RAW_RULES
]


def remove_spacing(text: str) -> str:
    """
    Apply precompiled spacing rules to plain text.
    """
    for pattern, repl in SPACING_RULES:
        text = pattern.sub(repl, text)
    return text


def process_markdown(content: str) -> str:
    """
    Process Markdown content:
    - Fully skip fenced code blocks (``` ```).
    - Only apply spacing cleanup to normal text.
    """

    lines = content.splitlines(keepends=True)
    result = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        # 代码块切换
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # 处理行内代码：分段
        parts = re.split(r"(`[^`]*`)", line)
        for i, part in enumerate(parts):
            if i % 2 == 0:
                parts[i] = remove_spacing(part)
        result.append("".join(parts))

    return "".join(result)
