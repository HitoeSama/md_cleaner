# md_cleaner

md_cleaner is a command_line tool that removes unnecessary spaces in multilingual Markdown files.

It is designed for Markdown documents that mix Chinese,Japanese,English,symbols,and emoji,while preserving Markdown structure and code.

## Scope

md_cleaner targets Markdown documents that contain a mix of:

- Chinese
- Japanese
- English and numbers
- Symbols
- Emoji

## Features

- Removes unnecessary spaces between different writing systems
- Preserves fenced code blocks(``` ```）
- Preserves inline code(`code`)
- Leaves English internal spacing unchanged
- No external dependencies
- Simple and predictable behavior

## What md_cleaner does not do

- It does not reformat Markdown structure
- It does not modify code blocks or inline code
- It does not normalize spacing around dots(`.`)

## Requirements

- Python 3.9 or higher

## Installation

Clone the repository and run the tool directly:

```bash
git clone https://github.com/
python cleaner.py your_markdown_name.md
```

# md_cleaner(中文)

md_cleaner是一个用于清理多语言Markdown文件中不必要空格的命令行工具。

它适用于包含中文、日文、英文、符号和Emoji的Markdown文档，并在处理过程中严格保留Markdown结构和代码内容。

## 适用范围

md_cleaner面向包含以下内容混排的Markdown文档：

- 中文
- 日文
- 英文与数字
- 符号
- Emoji

## 功能特性

- 清理不同语言体系之间不必要的空格
- 保留代码块（``` ```）
- 保留行内代码（`code`）
- 不修改英文内部的空格
- 无任何外部依赖
- 行为简单、结果可预测

## md_cleaner不会做的事情

- 不重新格式化Markdown结构
- 不修改代码块或行内代码
- 不处理句号（`.`）周围的空格

## 运行环境

- Python 3.9及以上

## 安装

克隆仓库并直接运行该工具：

```bash
git clone https://github.com/
python cleaner.py your_markdown_name.md
```

# md_cleaner(日本語)

md_cleanerは、多言語が混在するMarkdownファイルから不要な空白を除去するコマンドラインツールです。

中国語・日本語・英語・記号・絵文字を含むMarkdown文書を対象とし、Markdownの構造やコードはそのまま保持します。

## 対象範囲

md_cleanerは、以下の要素が混在するMarkdown文書を対象としています。

- 中国語
- 日本語
- 英語および数字
- 記号
- Emoji

## 機能

- 異なる言語体系の文字間にある不要な空白を除去
- コードブロック（``` ```）を保持
- インラインコード（`code`）を保持
- 英語内部のスペースは変更しない
- 外部依存なし
- 挙動がシンプルで予測可能

## md_cleanerが行わないこと

- Markdown構造の再フォーマットは行わない
- コードブロックおよびインラインコードは変更しない
- ピリオド（`.`）前後の空白は正規化しない

## 動作環境

- Python 3.9以上

## インストール

リポジトリをクローンして、ツールを直接実行します：

```bash
git clone https://github.com/
python cleaner.py your_markdown_name.md
```

# Before/After

Input:

```md
这是 test 文本 😀
今日は Python を 使う
記号 ! の前に 空格
`code block 内は そのまま`
```

Output:

```
这是test文本😀
今日はPythonを使う
記号!の前に空格
`code block 内は そのまま`
```
