from dotenv import load_dotenv
load_dotenv()  # no .env file needed here; the key is already in the environment

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"  # cheaper than Sonnet

message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "What is quantum computing? Answer in one sentence"}
    ],
)

print("TEXT:", message.content[0].text)
print("STOP REASON:", message.stop_reason)
print("USAGE:", message.usage.input_tokens, "in /", message.usage.output_tokens, "out")
