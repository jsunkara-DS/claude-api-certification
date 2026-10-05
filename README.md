# Building with the Claude API — Certification Project

My hands-on work for Anthropic Academy's free course
[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api).
The course covers the Messages API, prompting, tool use, RAG, MCP, and agents in Python.

Examples use `claude-haiku-4-5` to keep API costs low.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your ANTHROPIC_API_KEY
```

## Progress

| # | Lesson | Script | Status |
|---|--------|--------|--------|
| 01 | Making a first request (`client.messages.create`) | [lessons/01_first_request.py](lessons/01_first_request.py) | ✅ |
| 02 | Multi-turn conversations (managing message history) | [lessons/02_multi_turn.py](lessons/02_multi_turn.py) | ✅ |
| 03 | System prompts (role and behavior; math tutor demo) | [lessons/03_system_prompts.py](lessons/03_system_prompts.py) | ✅ |
| 04 | Temperature (predictable vs. creative output) | [lessons/04_temperature.py](lessons/04_temperature.py) | ✅ |

## Notes

- `max_tokens` is a safety cap, not a target. `stop_reason` shows `end_turn` when Claude finishes on its own and `max_tokens` when the cap cut it off.
- Messages are a list of `{"role": "user" | "assistant", "content": ...}` dicts representing the conversation.
- Claude is stateless. For multi-turn chat, keep a list of user and assistant messages and send the whole history with every request.
- A system prompt sets Claude's role and behavior. The API rejects `system=None`, so only pass `system` when you actually have one.
- Temperature runs from 0.0 to 1.0. Low values (0.0 to 0.3) suit facts, code, and extraction, middle values (0.4 to 0.7) suit summaries and teaching, and high values (0.8 to 1.0) suit brainstorming and creative writing. Even at 0.0 the output isn't fully guaranteed to repeat.
- SDK note: `anthropic` 1.x removed the `temperature` keyword from `messages.create()`. The API still accepts it, so this repo sends it with `extra_body={"temperature": ...}`.
