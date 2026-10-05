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

## Notes

- `max_tokens` is a safety cap, not a target. `stop_reason` shows `end_turn` when Claude finishes on its own and `max_tokens` when the cap cut it off.
- Messages are a list of `{"role": "user" | "assistant", "content": ...}` dicts representing the conversation.
