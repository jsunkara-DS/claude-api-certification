"""Lesson 02: Multi-turn conversations.

Claude is stateless: every request is independent. To keep context,
we store the message history ourselves and send all of it each time.
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


def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


if __name__ == "__main__":
    # Without history: Claude has no idea what "another sentence" refers to.
    print("WITHOUT HISTORY:")
    print(chat([{"role": "user", "content": "Write another sentence"}]))
    print()

    # With history: the follow-up builds on the earlier answer.
    messages = []
    add_user_message(messages, "Define quantum computing in one sentence")
    answer = chat(messages)
    add_assistant_message(messages, answer)
    print("TURN 1:", answer)

    add_user_message(messages, "Write another sentence")
    final_answer = chat(messages)
    print("TURN 2:", final_answer)
