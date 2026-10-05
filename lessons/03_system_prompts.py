"""Lesson 03: System prompts.

A system prompt shapes Claude's role, tone, and approach. The API
doesn't accept system=None, so we only include it when provided.
"""
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text


TUTOR_SYSTEM = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

if __name__ == "__main__":
    question = "How do I solve 5x + 2 = 3 for x?"

    messages = []
    add_user_message(messages, question)
    print("WITHOUT SYSTEM PROMPT:\n", chat(messages), "\n")

    messages = []
    add_user_message(messages, question)
    print("WITH TUTOR SYSTEM PROMPT:\n", chat(messages, system=TUTOR_SYSTEM))
