import argparse
from pathlib import Path
from .processor import process_markdown


def main():
    parser = argparse.ArgumentParser(
        prog="md_cleaner",
        description=(
            "A Markdown formatter that removes unnecessary spaces between\n"
            "Chinese / Japanese / English / Emoji characters."
        ),
        epilog=(
            "EXAMPLES:\n"
            "  md_cleaner README.md\n"
            "  md_cleaner post.md -o cleaned.md\n"
            "  md_cleaner notes.md --in-place\n\n"
            "NOTES:\n"
            "  - Code blocks (``` ``` ) and inline code (`code`) are preserved\n"
            "  - English internal spacing is NOT modified"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ======================
    # Positional arguments
    # ======================
    parser.add_argument(
        "input",
        metavar="INPUT",
        help="Input Markdown file",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="md-cleaner 1.0",
    )

    # ======================
    # Optional arguments
    # ======================
    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        default="Output.md",
        help="Output file path (default: Output.md)",
    )

    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Modify the input file in place",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress non-error output",
    )

    args = parser.parse_args()

    input_file = Path(args.input)

    if not input_file.exists():
        print(f"File not found: {input_file}")
        return

    # in-place
    output_file = input_file if args.in_place else Path(args.output)

    content = input_file.read_text(encoding="utf-8")
    cleaned = process_markdown(content)
    output_file.write_text(cleaned, encoding="utf-8")

    if not args.quiet:
        if args.in_place:
            print(f"✔ Cleaned in place: {input_file}")
        else:
            print(f"✔ Cleaned → {output_file}")
