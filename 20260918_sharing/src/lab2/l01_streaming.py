import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-haiku-4-5-20251001",
    max_tokens=500,
    messages=[{"role": "user", "content": "List 5 uses for a Claude agent in customer support."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final_message = stream.get_final_message()

print("\n\nFinal stop reason:", final_message.stop_reason)
