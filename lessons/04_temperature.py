"""Lesson 04: Temperature.

Temperature (0.0-1.0) controls how deterministic vs. creative sampling is.
Low (0.0-0.3): facts, code, extraction. Medium (0.4-0.7): summaries, teaching.
High (0.8-1.0): brainstorming, creative writing, jokes.
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


def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        # anthropic SDK 1.x dropped the `temperature` keyword from
        # messages.create(), but the API still accepts it, so we send it
        # in the request body. (On SDK 0.x: pass temperature=... directly.)
        "extra_body": {"temperature": temperature},
    }
    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text


if __name__ == "__main__":
    prompt = "Generate a one sentence movie idea. Reply with only the sentence."
    for temp in (0.0, 1.0):
        print(f"TEMPERATURE {temp}:")
        for i in range(3):
            messages = []
            add_user_message(messages, prompt)
            print(f"  {i + 1}. {chat(messages, temperature=temp)}")
        print()
