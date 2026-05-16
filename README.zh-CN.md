# VirtualOCstory

一个用于与 AI 共同创作原创角色（OC）并为其编写故事的 [Claude Code](https://claude.ai/code) 技能。
[Switch to English](https://github.com/Okbackv/VirtualOCstory/blob/main/README.md)

## 概述

VirtualOCstory 将 Claude Code 变成你的个人 OC（原创角色）助手。它可以帮助你创建详细的角色档案、构建虚构世界、追踪角色关系、管理专有术语、生成故事，并导出为 `.txt` 或 `.docx` 文件——同时在此过程中逐步了解你的创作偏好。

## 功能特性

- **OC 档案管理** — 创建和编辑结构化角色档案，涵盖 MBTI、性格特征、外貌、背景故事、口头禅、说话风格、爱好、能力等字段
- **世界观构建** — 定义世界设定、魔法体系、科技水平、势力派系和地点
- **关系图谱** — 追踪 OC 之间的关系，支持关联角色之间的交叉引用
- **术语表管理** — 记录你世界中独有的专有术语（魔法体系、文化概念等）
- **故事生成** — 基于你的 OC 及其世界进行小说创作，提供适用于不同类型和篇幅的结构化故事模板
- **AI 学习与总结** — 每次互动后，AI 会总结它对角色所了解的新内容，并保存这些洞察供未来参考
- **智能召回** — 当你提到某个 OC 的名字、专有术语或过去的事件时，技能会自动调取相关上下文
- **导出功能** — 将故事导出为 `.txt`（纯文本）或 `.docx`（带中文字体支持的格式化 Word 文档）

## 安装

1. 将 `virtualocstory` 文件夹复制到项目的 `.agents/skills/` 目录（项目级使用）或 `~/.claude/skills/`（全局使用）。
2. 安装 Python 依赖：

```bash
pip install python-docx
```

3. 完成 — Claude Code 会自动发现该技能。

## 快速开始

在 Claude Code 中输入：

```
调用virtualOCstory skill。我想创建一个OC，名字叫林月。
```

AI 将引导你创建第一个原创角色，通过贴切的追问来丰富角色档案。

## 使用方法

### 创建 OC

只需告诉 Claude 你想创建一个角色。技能会逐步提示你输入：
- 姓名、性别、性格（MBTI）、生日、身高、外貌
- 爱好、口头禅、说话风格
- 背景故事、喜好/厌恶、能力、职业

你提到的所有未定义的术语（例如名为"化形"的魔法体系）都会被记录，AI 会后续询问以明确其含义。

### 构建世界观

定义世界的规则、历史、地理和文化。技能同时维护叙述性的 `world.md` 和结构化的 `world.json`，后者涵盖魔法体系、科技水平、势力派系和地点等字段。

### 编写故事

让 Claude 编写一个涉及你的 OC 的故事。技能将：
1. 加载所有相关的角色档案、关系网络和世界设定
2. 确认故事范围（涉及哪些 OC、故事前提、基调、篇幅）
3. 在 OC 的 stories 目录下以 Markdown 格式起草故事
4. 根据需要导出为 `.txt` 或 `.docx`

### 导出

```
请把「林月第一次化形」的故事导出为docx文件。
```

## 数据结构

所有 OC 数据存储在 `virtualocstory_data/` 目录中：

```
virtualocstory_data/
├── ocs/
│   └── <oc-name>/
│       ├── profile.json          # 结构化角色档案数据
│       ├── profile.md            # 叙述性简介 + AI 笔记
│       ├── experiences/
│       │   ├── key-events.md     # 重要故事里程碑
│       │   └── daily.md          # 日常片段
│       ├── relationships.md      # 角色关系
│       └── stories/              # 故事草稿
├── world-settings/
│   ├── world.md                  # 世界观叙述
│   └── world.json                # 结构化世界观规则
├── glossary/
│   └── glossary.md               # 专有术语
├── global-summaries/
│   └── ai-insights.md            # 跨 OC 观察总结
└── output/                       # 导出的 .txt / .docx 文件
```

## 脚本

提供辅助脚本用于自动化操作：

| 脚本 | 用途 |
|--------|---------|
| `scripts/init_oc_project.py` | 初始化项目结构和 OC 文件夹 |
| `scripts/export_txt.py` | 将 Markdown 故事导出为纯文本 |
| `scripts/export_docx.py` | 将 Markdown 故事导出为格式化 .docx |
| `scripts/summary_helper.py` | 管理 AI 笔记、经历、术语表和搜索 |

### 脚本用法

```bash
# 初始化新的 OC 项目并创建角色
python scripts/init_oc_project.py --name "林月" --base "virtualocstory_data"

# 将故事导出为文本
python scripts/export_txt.py --source "path/to/story.md" --output "output/story.txt"

# 将故事导出为 Word 文档
python scripts/export_docx.py --source "path/to/story.md" --output "output/story.docx" --title "Story Title"

# 添加重要经历
python scripts/summary_helper.py --base "virtualocstory_data" add-experience --oc "林月" --category key-events --content "..."

# 搜索所有 OC 数据
python scripts/summary_helper.py --base "virtualocstory_data" search --keyword "birthday"

# 添加术语表条目
python scripts/summary_helper.py --base "virtualocstory_data" add-glossary --term "化形" --definition "一种变形魔法"
```

## OC 档案结构

每个角色的 `profile.json` 包含以下字段：

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `name` | string（必填） | OC 名字 |
| `gender` | string | 男/女/非二元/等 |
| `mbti` | string | 4 字母 MBTI 类型（如 INFJ、ENTP） |
| `birthday` | string | 自由格式日期 |
| `age` | string | 年龄或年龄描述 |
| `height` | string | 如 "168cm" |
| `appearance` | string | 外貌描述 |
| `hobbies` | string[] | 兴趣与爱好 |
| `catchphrases` | string[] | 标志性口头禅 |
| `speaking_style` | string | 语气、语速、语言习惯 |
| `personality_traits` | string[] | 关键性格特征 |
| `background` | string | 背景故事与出身 |
| `likes` | string[] | OC 喜欢的事物 |
| `dislikes` | string[] | OC 厌恶的事物 |
| `abilities` | string[] | 技能、能力、天赋 |
| `occupation` | string | 职业、角色或头衔 |
| `custom_fields` | object | 用户自定义额外字段 |

## MBTI 参考

技能内置了 MBTI 参考资料，涵盖全部 16 种类型，包含认知功能栈、核心特征、弱点分析和写作技巧——帮助你塑造行为与其人格类型一致的角色。

## 故事模板

内置的故事结构模板适用于：
- 短篇故事（1000–5000 字）
- 章节/剧集（3000–8000 字）
- 小说弧光（多章节）
- 类型特定节拍（爱情、悬疑、动作、日常）

## 设计理念

- **用户是作者** — AI 是共创者和工具。你始终对你的 OC 和世界观拥有最终决定权。
- **真诚的好奇心** — 技能自然地提出追问，而非像审问一样。
- **默认使用 Markdown** — 所有草稿和笔记均为 `.md` 文件，除非你另有要求。
- **有选择地归类** — 并非每次互动都需要归类。有些对话只是对话。
- **主动召��** — 当存在相关的过往上下文时，AI 会自然地引入。

## 依赖

- Python 3.10+
- `python-docx`（仅用于 `.docx` 导出）

## 项目结构

```
virtualocstory/
├── SKILL.md                       # 技能定义（由 Claude Code 加载）
├── README.md                      # 英文版 README
├── README.zh-CN.md                # 本文件（中文版 README）
├── assets/
│   └── oc_template.json           # 默认角色档案模板
├── evals/
│   └── evals.json                 # 评估用例
├── references/
│   ├── mbti_reference.md          # MBTI 人格类型指南
│   ├── oc_profile_schema.md       # 角色档案结构文档
│   └── story_templates.md         # 故事结构模板
└── scripts/
    ├── init_oc_project.py         # 项目/OC 初始化
    ├── export_txt.py              # TXT 导出
    ├── export_docx.py             # DOCX 导出
    └── summary_helper.py          # AI 笔记、搜索、术语表
```

## 许可证

MIT
