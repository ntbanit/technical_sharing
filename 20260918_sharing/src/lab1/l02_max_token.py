import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=20,
    messages=[
        {"role": "user", "content": "Explain what a token is, in 2 sentences."}
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)

print("\n--- Usage ---")
print("Input tokens:", message.usage.input_tokens)
print("Output tokens:", message.usage.output_tokens)
print("Stop reason:", message.stop_reason)

"""
A token is the smallest unit of text that an AI language model processes, typically representing a word,

--- Usage ---
Input tokens: 20
Output tokens: 20
Stop reason: max_tokens
"""