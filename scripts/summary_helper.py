#!/usr/bin/env python3
"""Helper for AI to manage summaries, categorizations, and recall for virtualOCstory."""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def append_experience(base_path: str, oc_name: str, category: str, content: str):
    """Append a categorized experience entry to an OC's experience file."""
    valid_categories = {"key-events", "daily"}
    if category not in valid_categories:
        print(f"Error: category must be one of {valid_categories}", file=sys.stderr)
        sys.exit(1)

    filename = f"{category}.md"
    exp_path = os.path.join(base_path, "ocs", oc_name, "experiences", filename)

    if not os.path.exists(exp_path):
        print(f"Error: OC '{oc_name}' not found. Run init_oc_project.py first.", file=sys.stderr)
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n### {timestamp}\n\n{content}\n"

    with open(exp_path, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Appended to {exp_path}")


def append_ai_note(base_path: str, oc_name: str, note: str):
    """Append an AI insight to the OC's profile.md."""
    profile_path = os.path.join(base_path, "ocs", oc_name, "profile.md")

    if not os.path.exists(profile_path):
        print(f"Error: OC '{oc_name}' not found.", file=sys.stderr)
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n### {timestamp}\n{note}\n"

    with open(profile_path, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Appended AI note to {profile_path}")


def append_global_insight(base_path: str, insight: str):
    """Append a cross-OC insight to global insights."""
    insights_path = os.path.join(base_path, "global-summaries", "ai-insights.md")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n### {timestamp}\n{insight}\n"

    with open(insights_path, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Appended to {insights_path}")


def search_oc_data(base_path: str, keyword: str):
    """Search all OC data for a keyword and return matching files."""
    results = []
    ocs_dir = os.path.join(base_path, "ocs")

    if not os.path.exists(ocs_dir):
        print("No OC data found.", file=sys.stderr)
        return

    for oc_name in os.listdir(ocs_dir):
        oc_dir = os.path.join(ocs_dir, oc_name)
        if not os.path.isdir(oc_dir):
            continue
        for root, dirs, files in os.walk(oc_dir):
            for fname in files:
                if not fname.endswith((".json", ".md")):
                    continue
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read()
                    if keyword.lower() in content.lower():
                        results.append({
                            "oc": oc_name,
                            "file": fname,
                            "path": fpath,
                            "preview": _extract_context(content, keyword)
                        })
                except Exception:
                    pass

    # Also search glossary
    glossary_path = os.path.join(base_path, "glossary", "glossary.md")
    if os.path.exists(glossary_path):
        with open(glossary_path, "r", encoding="utf-8") as f:
            content = f.read()
        if keyword.lower() in content.lower():
            results.append({
                "oc": "—",
                "file": "glossary.md",
                "path": glossary_path,
                "preview": _extract_context(content, keyword)
            })

    return results


def _extract_context(content: str, keyword: str, context_lines: int = 2) -> str:
    """Extract surrounding context lines for a keyword match."""
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if keyword.lower() in line.lower():
            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            return "\n".join(lines[start:end])
    return ""


def add_glossary_term(base_path: str, term: str, definition: str, details: str = "", related: str = ""):
    """Add or update a term in the glossary."""
    glossary_path = os.path.join(base_path, "glossary", "glossary.md")

    entry = f"\n### {term}\n"
    entry += f"- **定义**: {definition}\n"
    if details:
        entry += f"- **详细说明**: {details}\n"
    if related:
        entry += f"- **关联**: {related}\n"

    with open(glossary_path, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Added term '{term}' to glossary at {glossary_path}")


def main():
    parser = argparse.ArgumentParser(description="virtualOCstory summary and recall helper")
    parser.add_argument("--base", default="virtualocstory_data", help="Base project path")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # add-experience
    p_exp = subparsers.add_parser("add-experience", help="Append a categorized experience")
    p_exp.add_argument("--oc", required=True, help="OC name")
    p_exp.add_argument("--category", required=True, choices=["key-events", "daily"], help="Category")
    p_exp.add_argument("--content", required=True, help="Content to append")

    # add-note
    p_note = subparsers.add_parser("add-note", help="Append an AI note to OC profile.md")
    p_note.add_argument("--oc", required=True, help="OC name")
    p_note.add_argument("--note", required=True, help="Note content")

    # add-insight
    p_insight = subparsers.add_parser("add-insight", help="Append a global insight")
    p_insight.add_argument("--insight", required=True, help="Insight content")

    # search
    p_search = subparsers.add_parser("search", help="Search OC data by keyword")
    p_search.add_argument("--keyword", required=True, help="Keyword to search for")

    # add-glossary
    p_gloss = subparsers.add_parser("add-glossary", help="Add a glossary term")
    p_gloss.add_argument("--term", required=True, help="Term name")
    p_gloss.add_argument("--definition", required=True, help="Short definition")
    p_gloss.add_argument("--details", default="", help="Detailed explanation")
    p_gloss.add_argument("--related", default="", help="Related OCs or systems")

    args = parser.parse_args()

    if args.command == "add-experience":
        append_experience(args.base, args.oc, args.category, args.content)
    elif args.command == "add-note":
        append_ai_note(args.base, args.oc, args.note)
    elif args.command == "add-insight":
        append_global_insight(args.base, args.insight)
    elif args.command == "search":
        results = search_oc_data(args.base, args.keyword)
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif args.command == "add-glossary":
        add_glossary_term(args.base, args.term, args.definition, args.details, args.related)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
