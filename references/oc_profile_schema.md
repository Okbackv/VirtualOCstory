# OC Profile JSON Schema

The canonical schema for `profile.json`. All fields are optional unless marked required.

```json
{
  "name": "string (required) — OC's name",
  "gender": "string — male/female/non-binary/etc.",
  "mbti": "string — 4-letter MBTI type, e.g. 'INFJ', 'ESTP'",
  "birthday": "string — free format, e.g. 'March 15', '2005-03-15', '农历八月十五'",
  "age": "string — can be a number or description like 'appears 20, actually 300'",
  "height": "string — e.g. '168cm', '5\'6\"'",
  "appearance": "string — free-text description of looks, clothing style, notable features",
  "hobbies": ["string"] — list of hobbies/interests,
  "catchphrases": ["string"] — signature phrases the OC says often,
  "speaking_style": "string — tone, pace, vocabulary level, quirks in speech",
  "personality_traits": ["string"] — key personality descriptors,
  "background": "string — backstory, origin, key life events",
  "likes": ["string"] — things the OC likes,
  "dislikes": ["string"] — things the OC dislikes,
  "abilities": ["string"] — skills, powers, talents,
  "occupation": "string — job, role, or title",
  "custom_fields": {
    "type": "object",
    "description": "Any user-defined extra fields. Examples: blood_type, element, faction, rank, familiar, etc."
  }
}
```

## MBTI Quick Reference

See `mbti_reference.md` for full descriptions of each type. Brief overview:

| Type  | Nickname         | Core Traits                        |
|-------|------------------|------------------------------------|
| INTJ  | Architect        | Strategic, independent, visionary  |
| INTP  | Logician         | Analytical, curious, abstract      |
| ENTJ  | Commander        | Bold, decisive, leader             |
| ENTP  | Debater          | Witty, contrarian, innovative      |
| INFJ  | Advocate         | Idealistic, insightful, quiet      |
| INFP  | Mediator         | Empathetic, creative, values-driven|
| ENFJ  | Protagonist      | Charismatic, inspiring, warm       |
| ENFP  | Campaigner       | Enthusiastic, spontaneous, social  |
| ISTJ  | Logistician      | Practical, reliable, orderly       |
| ISFJ  | Defender         | Protective, diligent, kind         |
| ESTJ  | Executive        | Efficient, organized, traditional  |
| ESFJ  | Consul           | Sociable, caring, dutiful          |
| ISTP  | Virtuoso         | Hands-on, adaptable, reserved      |
| ISFP  | Adventurer       | Artistic, gentle, present-focused  |
| ESTP  | Entrepreneur     | Energetic, risk-taking, persuasive |
| ESFP  | Entertainer      | Lively, playful, people-loving     |
