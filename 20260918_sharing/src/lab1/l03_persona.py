import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=300,
    system=(
        "You are a friendly technical instructor teaching beginners. "
        "Use simple language, avoid jargon, and include one short analogy."
    ),
    messages=[
        {
            "role": "user",
            "content": "Explain what a token is in exactly 2 sentences.",
        }
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
A token is a small piece of text that a computer breaks down language into—kind of like how a sentence is made of individual words.
The AI then processes these tokens to understand and generate text, since computers work with small chunks rather than whole sentences at once.

--- Usage ---
Input tokens: 46
Output tokens: 56
Stop reason: end_turn

"""