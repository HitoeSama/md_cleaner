import re

# ASCII punctuation and symbols commonly used in text
_SYMBOL_CHARS = [
    ",",
    "!",
    "?",
    ";",
    ":",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    '"',
    "'",
    "<",
    ">",
    "@",
    "$",
    "%",
    "^",
    "&",
    "*",
    "+",
    "=",
    "/",
    "\\",
]

# Character classes
CN = r"[\u4e00-\u9fff]"
JP = r"[\u3040-\u309F\u30A0-\u30FF]"
EN = r"[A-Za-z0-9]"
EMOJI = r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF]"

# Build regex character class for symbols
SYMBOLS = "[" + re.escape("".join(_SYMBOL_CHARS)) + "]"
