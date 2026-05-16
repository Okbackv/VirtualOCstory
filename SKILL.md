---
name: virtualOCstory
description: Create, manage, and write stories for user-created Original Characters (OCs). Use this skill whenever the user mentions OCs, original characters, character creation, character profiles, world-building, or wants to write fiction based on their own characters. Also trigger when the user says "调用virtualOCstory skill" or asks to create/manage OC profiles, world settings, character relationships, special terminology glossaries, or export stories to files.
---

# VirtualOCstory

A skill for co-creating Original Characters (OCs) with the user and writing stories based on them.

## Core Capabilities

1. **OC Profile Management** — Create and edit structured profiles for multiple OCs (name, gender, MBTI, birthday, hobbies, catchphrases, speaking style, appearance, backstory, etc.)
2. **World-Building** — Define and maintain world settings and rules
3. **Relationship Mapping** — Track character relationships
4. **Glossary Management** — Record special terminology (e.g., "化形" magic system) and allow follow-up questions about undefined terms
5. **Story Generation** — Write stories based on OCs and their world, then export as .txt or .docx
6. **AI Learning & Summarization** — After each interaction, summarize what was learned about each OC and save insights
7. **Smart Recall** — Categorize OC information (关键经历, 日常, etc.) and surface relevant context when referenced

## Data Organization

All OC data lives under `virtualocstory_data/` in the project root (or user-specified location):

```
virtualocstory_data/
├── ocs/
│   └── <oc-name>/
│       ├── profile.json          # Structured profile data
│       ├── profile.md            # Narrative bio + AI's understanding
│       ├── experiences/
│       │   ├── key-events.md     # 关键经历 — major milestones
│       │   └── daily.md          # 日常 — everyday moments
│       ├── relationships.md      # Who they know and how
│       └── stories/
│           └── <story-title>.md  # Drafts (before export)
├── world-settings/
│   ├── world.md                  # World setting narrative
│   └── world.json                # World rules, magic systems, etc.
├── glossary/
│   └── glossary.md               # Special terminology with definitions
├── global-summaries/
│   └── ai-insights.md            # Cross-OC observations and patterns
└── output/
    └── <story-title>.txt|docx    # Exported stories
```

## Workflow

### Phase 1: OC Profile Creation

When a user wants to create or update an OC:

1. **Gather core info** — Ask for (or confirm existing) name, gender, personality/MBTI, birthday, hobbies, catchphrases, speaking tone, appearance, background story.

2. **Ask follow-up questions** — If the user mentions anything undefined (a special term, an unexplained relationship, a vague event), pause and ask for clarification. Record all new terminology in the glossary.

3. **Fill the profile.json** — Use the schema defined in `references/oc_profile_schema.md`. Save to `virtualocstory_data/ocs/<oc-name>/profile.json`.

4. **Write profile.md** — A narrative version including the AI's initial understanding and any observed patterns. Save to `virtualocstory_data/ocs/<oc-name>/profile.md`.

5. **Run init script** for folder structure, or manually create directories as needed:
   ```bash
   python scripts/init_oc_project.py --name "<oc-name>" --base "virtualocstory_data"
   ```

### Phase 2: World-Building & Relationships

- Maintain `world-settings/world.md` with the world's rules, history, geography, culture
- Maintain `world-settings/world.json` for structured world rules (magic systems, technology levels, etc.)
- Each OC's relationships are tracked in their own `relationships.md`, plus cross-referenced in linked OCs

### Phase 3: Story Generation

When the user asks to write a story:

1. **Confirm scope** — Which OCs are involved? What's the premise? Desired length or tone?
2. **Load relevant data** — Read all involved OCs' profiles, relationships, world settings, and relevant experiences/key-events
3. **Write the story** — Draft in markdown first under `<oc>/stories/<title>.md`
4. **Export** — Use the export scripts when the user wants a file:
   - `.txt`: `python scripts/export_txt.py --source "<path>" --output "virtualocstory_data/output/<title>.txt"`
   - `.docx`: `python scripts/export_docx.py --source "<path>" --output "virtualocstory_data/output/<title>.docx" --title "<Story Title>"`

### Phase 4: AI Learning & Summarization

After every meaningful interaction about an OC:

1. **Update profile.md** — Append a brief "AI Notes" section with new insights about the character's traits, the user's preferences, or patterns observed
2. **Categorize experiences** — If the interaction contained storyline content, add it to either:
   - `key-events.md` — for significant, plot-defining moments
   - `daily.md` — for casual, everyday interactions
3. **Update global insights** — If the interaction revealed cross-OC patterns or user storytelling preferences, add to `global-summaries/ai-insights.md`

### Phase 5: Smart Recall

When a user mentions a topic (e.g., "birthday", "化形", a specific OC name):

1. **Search OC profiles** — Check all `profile.json` and `profile.md` files for relevant info
2. **Search glossary** — Check `glossary/glossary.md` for special terms
3. **Search experiences** — Check `key-events.md` and `daily.md` for past context
4. **Present contextually** — Weave the recalled info naturally into the response without being mechanical about it

## OC Profile JSON Structure

The `profile.json` follows this structure (see `references/oc_profile_schema.md` for full schema):

```json
{
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
```

## Glossary Management

The glossary (`virtualocstory_data/glossary/glossary.md`) tracks special terms unique to the user's world:

- Every time the user introduces a new term (magic system, cultural concept, unique noun), ask "Can you tell me more about [term]?" and record it
- Format each entry as: `### <Term> — <One-line definition> — <Detailed explanation> — <Related OCs or systems>`
- When a term appears in conversation, briefly recall its definition

## Interaction Principles

- **Genuine curiosity** — Ask follow-up questions naturally, as if genuinely interested in the user's creative world. Don't interrogate.
- **Default to markdown** — All drafts and notes are .md files unless the user requests otherwise
- **User is the author** — AI is a co-creator and tool. The user always has final say over their OCs and world
- **Categorize thoughtfully** — Don't force every interaction into a category. Some things are just conversation.
- **Proactive recall** — When relevant past context exists, bring it in naturally: "This reminds me of when [OC] did X..."
