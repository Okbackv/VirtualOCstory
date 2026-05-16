#!/usr/bin/env python3
"""Initialize the folder structure for a new OC in a virtualOCstory project."""

import argparse
import json
import os
import sys

OC_PROFILE_TEMPLATE = {
    "name": "",
    "gender": "",
    "mbti": "",
    "birthday": "",
    "age": "",
    "height": "",
    "appearance": "",
    "hobbies": [],
    "catchphrases": [],
    "speaking_style": "",
    "personality_traits": [],
    "background": "",
    "likes": [],
    "dislikes": [],
    "abilities": [],
    "occupation": "",
    "custom_fields": {}
}

PROFILE_MD_TEMPLATE = """# {name}

## Basic Info
- **Gender**: {gender}
- **MBTI**: {mbti}
- **Birthday**: {birthday}
- **Age**: {age}
- **Height**: {height}

## Appearance
{appearance}

## Personality
{personality}

## Background
{background}

## Hobbies & Interests
{hobbies}

## Catchphrases & Speaking Style
{catchphrases}

*Speaking style*: {speaking_style}

## Likes & Dislikes
- **Likes**: {likes}
- **Dislikes**: {dislikes}

## Abilities & Skills
{abilities}

## Occupation
{occupation}

---

## AI Understanding & Notes
<!-- AI will add observations and insights here over time -->
"""


def init_project(base_path: str):
    """Create the top-level virtualocstory_data directory structure."""
    dirs = [
        os.path.join(base_path, "ocs"),
        os.path.join(base_path, "world-settings"),
        os.path.join(base_path, "glossary"),
        os.path.join(base_path, "global-summaries"),
        os.path.join(base_path, "output"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print(f"Initialized project at {os.path.abspath(base_path)}")
    return dirs


def init_oc(base_path: str, name: str, profile_data: dict | None = None):
    """Create the folder structure for a single OC."""
    oc_dir = os.path.join(base_path, "ocs", name)
    dirs = [
        os.path.join(oc_dir, "experiences"),
        os.path.join(oc_dir, "stories"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # Write profile.json
    profile = OC_PROFILE_TEMPLATE.copy()
    profile["name"] = name
    if profile_data:
        profile.update(profile_data)
    profile_path = os.path.join(oc_dir, "profile.json")
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
    print(f"Created {profile_path}")

    # Write profile.md
    md_content = PROFILE_MD_TEMPLATE.format(
        name=name,
        gender=profile.get("gender", ""),
        mbti=profile.get("mbti", ""),
        birthday=profile.get("birthday", ""),
        age=profile.get("age", ""),
        height=profile.get("height", ""),
        appearance=profile.get("appearance", ""),
        personality=", ".join(profile.get("personality_traits", [])) if profile.get("personality_traits") else "",
        background=profile.get("background", ""),
        hobbies=", ".join(profile.get("hobbies", [])) if profile.get("hobbies") else "",
        catchphrases=", ".join(profile.get("catchphrases", [])) if profile.get("catchphrases") else "",
        speaking_style=profile.get("speaking_style", ""),
        likes=", ".join(profile.get("likes", [])) if profile.get("likes") else "",
        dislikes=", ".join(profile.get("dislikes", [])) if profile.get("dislikes") else "",
        abilities=", ".join(profile.get("abilities", [])) if profile.get("abilities") else "",
        occupation=profile.get("occupation", ""),
    )
    md_path = os.path.join(oc_dir, "profile.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Created {md_path}")

    # Create empty experience files
    key_events_path = os.path.join(oc_dir, "experiences", "key-events.md")
    daily_path = os.path.join(oc_dir, "experiences", "daily.md")
    for p in [key_events_path, daily_path]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(f"# {name} — {'关键经历' if 'key-events' in p else '日常'}\n\n")
        print(f"Created {p}")

    # Create empty relationships file
    rel_path = os.path.join(oc_dir, "relationships.md")
    with open(rel_path, "w", encoding="utf-8") as f:
        f.write(f"# {name} — 人物关系\n\n")
    print(f"Created {rel_path}")

    print(f"\nOC '{name}' initialized at {os.path.abspath(oc_dir)}")


def main():
    parser = argparse.ArgumentParser(description="Initialize a virtualOCstory project or OC")
    parser.add_argument("--name", help="OC name (creates OC subfolder)")
    parser.add_argument("--base", default="virtualocstory_data", help="Base project path (default: virtualocstory_data)")
    parser.add_argument("--project-only", action="store_true", help="Only init project structure, no OC")
    args = parser.parse_args()

    init_project(args.base)

    if not args.project_only:
        if not args.name:
            print("Error: --name is required unless --project-only is set", file=sys.stderr)
            sys.exit(1)
        init_oc(args.base, args.name)

    # Also create default glossary if not exists
    glossary_path = os.path.join(args.base, "glossary", "glossary.md")
    if not os.path.exists(glossary_path):
        with open(glossary_path, "w", encoding="utf-8") as f:
            f.write("# 特殊词条 / Glossary\n\n")
        print(f"Created {glossary_path}")

    # Create world-settings if not exists
    world_md = os.path.join(args.base, "world-settings", "world.md")
    if not os.path.exists(world_md):
        with open(world_md, "w", encoding="utf-8") as f:
            f.write("# 世界观设定 / World Setting\n\n")
        print(f"Created {world_md}")

    world_json = os.path.join(args.base, "world-settings", "world.json")
    if not os.path.exists(world_json):
        with open(world_json, "w", encoding="utf-8") as f:
            json.dump({
                "world_name": "",
                "genre": "",
                "era": "",
                "magic_system": {},
                "technology_level": "",
                "factions": [],
                "locations": [],
                "rules": []
            }, f, ensure_ascii=False, indent=2)
        print(f"Created {world_json}")

    # Create global insights if not exists
    insights_path = os.path.join(args.base, "global-summaries", "ai-insights.md")
    if not os.path.exists(insights_path):
        with open(insights_path, "w", encoding="utf-8") as f:
            f.write("# AI 全局洞察 / AI Global Insights\n\n")
        print(f"Created {insights_path}")


if __name__ == "__main__":
    main()
