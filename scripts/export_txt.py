#!/usr/bin/env python3
"""Export a markdown story file to plain text (.txt)."""

import argparse
import re
import sys
from pathlib import Path


def strip_markdown(text: str) -> str:
    """Strip common markdown formatting to produce readable plain text."""
    # Remove heading markers but keep the text
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    # Remove inline code
    text = re.sub(r"`(.+?)`", r"\1", text)
    # Remove links, keep text
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    # Remove images
    text = re.sub(r"!\[.*?\]\(.+?\)", "", text)
    # Horizontal rules become a line
    text = re.sub(r"^[-*_]{3,}$", "—" * 40, text, flags=re.MULTILINE)
    # Remove blockquote marker
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    return text


def md_to_txt(md_path: str, output_path: str):
    """Convert a markdown file to plain text."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    text = strip_markdown(content)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Exported to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Export markdown story to plain text")
    parser.add_argument("--source", required=True, help="Path to source .md file")
    parser.add_argument("--output", required=True, help="Path to output .txt file")
    args = parser.parse_args()

    if not Path(args.source).exists():
        print(f"Error: source file not found: {args.source}", file=sys.stderr)
        sys.exit(1)

    md_to_txt(args.source, args.output)


if __name__ == "__main__":
    main()
