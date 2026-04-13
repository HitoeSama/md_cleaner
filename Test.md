# md-cleaner Test Data

This file is used to verify spacing cleanup behavior.

English is the primary language.
Other scripts are used only at clear boundaries.

---

## 1. English and Chinese

This is a test 文档.
English 中文 spacing should be cleaned.

Version 文档 123 test.

---

## 2. English and Japanese

This is a test 日本語 document.
English 日本語 spacing should be removed.

---

## 3. Chinese and Japanese

This section tests direct Chinese 日本語 boundaries.

中文 日本語 test.
日本語 中文 test.

---

## 4. Symbols and Text

This is a test , with incorrect spacing before punctuation !

Check spacing before ? and ; 

Symbols ( test ) [ test ] { test } should be handled correctly.

---

## 5. Emoji and Text

This is a test 😄 document.
Emoji 😄 English boundary should be cleaned.
English 😄 中文 boundary should be cleaned.
日本語 😄 中文 boundary should be cleaned.

---

## 6. Inline Code (Must Be Preserved)

Inline code must remain unchanged.

Example: `for i in range(10): print(i)`
Mixing 中文 `variable_name = 10` should not break inline code.

---

## 7. Code Blocks (Must Be Preserved)

The content inside code blocks must never be modified.

```python
def example():
    # English 中文 日本語 😄 mixed here
    print("Hello 世界")
