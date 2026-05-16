# VirtualOCstory

A [Claude Code](https://claude.ai/code) skill for co-creating Original Characters (OCs) with AI and writing stories about them.

## Overview

VirtualOCstory turns Claude Code into your personal OC (Original Character) assistant. It helps you create detailed character profiles, build fictional worlds, track character relationships, manage special terminology, generate stories, and export them as `.txt` or `.docx` files — all while learning about your creative preferences along the way.

## Features

- **OC Profile Management** — Create and edit structured profiles with fields like MBTI, personality traits, appearance, backstory, catchphrases, speaking style, hobbies, abilities, and more
- **World-Building** — Define world settings, magic systems, technology levels, factions, and locations
- **Relationship Mapping** — Track how your OCs know each other, with cross-referencing between linked characters
- **Glossary Management** — Record special terminology unique to your world (magic systems, cultural concepts, etc.)
- **Story Generation** — Write fiction based on your OCs and their world, with structured story templates for different genres and lengths
- **AI Learning & Summarization** — After each interaction, the AI summarizes what it learned about your characters and saves these insights for future reference
- **Smart Recall** — When you mention an OC name, special term, or past event, the skill surfaces relevant context automatically
- **Export** — Export stories to `.txt` (plain text) or `.docx` (formatted Word document with Chinese font support)

## Installation

1. Copy the `virtualocstory` folder into your project's `.agents/skills/` directory (for project-level use) or `~/.claude/skills/` (for global use).
2. Install Python dependencies:

```bash
pip install python-docx
```

3. That's it — Claude Code will automatically discover the skill.

## Quick Start

In Claude Code, type:

```
调用virtualOCstory skill。我想创建一个OC，名字叫林月。
```

The AI will guide you through creating your first Original Character, asking thoughtful follow-up questions to flesh out the profile.

## Usage

### Creating an OC

Simply tell Claude you want to create a character. The skill will prompt you for:
- Name, gender, personality (MBTI), birthday, height, appearance
- Hobbies, catchphrases, speaking style
- Background story, likes/dislikes, abilities, occupation

All undefined terms you mention (like a magic system called "化形") will be noted and the AI will ask for clarification.

### Building Your World

Define your world's rules, history, geography, and culture. The skill maintains both a narrative `world.md` and a structured `world.json` with fields for magic systems, technology levels, factions, and locations.

### Writing Stories

Ask Claude to write a story involving your OCs. The skill will:
1. Load all relevant character profiles, relationships, and world settings
2. Confirm the story scope (which OCs, premise, tone, length)
3. Draft the story in markdown under the OC's stories directory
4. Export to `.txt` or `.docx` on request

### Exporting

```
请把「林月第一次化形」的故事导出为docx文件。
```

## Data Structure

All your OC data lives in a `virtualocstory_data/` directory:

```
virtualocstory_data/
├── ocs/
│   └── <oc-name>/
│       ├── profile.json          # Structured profile data
│       ├── profile.md            # Narrative bio + AI notes
│       ├── experiences/
│       │   ├── key-events.md     # Major story milestones
│       │   └── daily.md          # Everyday moments
│       ├── relationships.md      # Character connections
│       └── stories/              # Story drafts
├── world-settings/
│   ├── world.md                  # World narrative
│   └── world.json                # Structured world rules
├── glossary/
│   └── glossary.md               # Special terminology
├── global-summaries/
│   └── ai-insights.md            # Cross-OC observations
└── output/                       # Exported .txt / .docx files
```

## Scripts

Helper scripts are available for automation:

| Script | Purpose |
|--------|---------|
| `scripts/init_oc_project.py` | Initialize project structure and OC folders |
| `scripts/export_txt.py` | Export markdown stories to plain text |
| `scripts/export_docx.py` | Export markdown stories to formatted .docx |
| `scripts/summary_helper.py` | Manage AI notes, experiences, glossary, and search |

### Script Usage

```bash
# Initialize a new OC project and create a character
python scripts/init_oc_project.py --name "林月" --base "virtualocstory_data"

# Export a story to text
python scripts/export_txt.py --source "path/to/story.md" --output "output/story.txt"

# Export a story to Word document
python scripts/export_docx.py --source "path/to/story.md" --output "output/story.docx" --title "Story Title"

# Append a key experience
python scripts/summary_helper.py --base "virtualocstory_data" add-experience --oc "林月" --category key-events --content "..."

# Search all OC data
python scripts/summary_helper.py --base "virtualocstory_data" search --keyword "birthday"

# Add a glossary term
python scripts/summary_helper.py --base "virtualocstory_data" add-glossary --term "化形" --definition "A transformation magic"
```

## OC Profile Schema

Each character's `profile.json` contains:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string (required) | OC's name |
| `gender` | string | male/female/non-binary/etc. |
| `mbti` | string | 4-letter MBTI type (e.g. INFJ, ENTP) |
| `birthday` | string | Free format date |
| `age` | string | Age or age description |
| `height` | string | e.g. "168cm" |
| `appearance` | string | Physical description |
| `hobbies` | string[] | Interests and hobbies |
| `catchphrases` | string[] | Signature phrases |
| `speaking_style` | string | Tone, pace, quirks |
| `personality_traits` | string[] | Key personality descriptors |
| `background` | string | Backstory and origin |
| `likes` | string[] | Things the OC likes |
| `dislikes` | string[] | Things the OC dislikes |
| `abilities` | string[] | Skills, powers, talents |
| `occupation` | string | Job, role, or title |
| `custom_fields` | object | User-defined extra fields |

## MBTI Reference

The skill includes a built-in MBTI reference covering all 16 types with cognitive function stacks, core traits, weaknesses, and writing tips — helping you craft characters that behave consistently with their personality type.

## Story Templates

Built-in story structure templates are provided for:
- Short stories (1000–5000 words)
- Chapters / episodes (3000–8000 words)
- Novel arcs (multi-chapter)
- Genre-specific beats (Romance, Mystery, Action, Slice of Life)

## Design Principles

- **User is the author** — AI is a co-creator and tool. You always have the final say over your OCs and world.
- **Genuine curiosity** — The skill asks follow-up questions naturally, not like an interrogation.
- **Default to markdown** — All drafts and notes are `.md` files unless you request otherwise.
- **Categorize thoughtfully** — Not every interaction needs to be categorized. Some things are just conversation.
- **Proactive recall** — When relevant past context exists, the AI brings it in naturally.

## Dependencies

- Python 3.10+
- `python-docx` (for `.docx` export only)

## Project Structure

```
virtualocstory/
├── SKILL.md                       # Skill definition (loaded by Claude Code)
├── README.md                      # This file
├── assets/
│   └── oc_template.json           # Default profile template
├── evals/
│   └── evals.json                 # Evaluation cases
├── references/
│   ├── mbti_reference.md          # MBTI personality type guide
│   ├── oc_profile_schema.md       # Profile schema documentation
│   └── story_templates.md         # Story structure templates
└── scripts/
    ├── init_oc_project.py         # Project/OC initialization
    ├── export_txt.py              # TXT export
    ├── export_docx.py             # DOCX export
    └── summary_helper.py          # AI notes, search, glossary
```

## License

MIT
