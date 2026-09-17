import anthropic

client = anthropic.Anthropic()

from pathlib import Path

long_docs = ""
for i in range(0, 2) :
    long_doc = (
        Path(__file__).resolve().parents[2] / "docs" / f"ccdvf_module{i}.md"
    ).read_text(encoding="utf-8")
    long_docs += long_doc

long_docs *= 2

def ask(question):
    return client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        system=[
            {
                "type": "text",
                "text": long_docs,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": question}],
    )
count = client.messages.count_tokens(
    model="claude-haiku-4-5-20251001",
    system=[
        {
            "type": "text",
            "text": long_docs,
            "cache_control": {"type": "ephemeral"},
        }
    ],
    messages=[{"role": "user", "content": "Test"}],
)

print("Input tokens:", count.input_tokens)

first = ask("Summarize the document in one sentence.")
cache_first = f"Cache write tokens:{first.usage.cache_creation_input_tokens}"

second = ask("What is the second most important point in the document?")
cache_second = f"Cache read tokens:{second.usage.cache_read_input_tokens}"

print(cache_first)
print(cache_second)

output_path = Path(__file__).resolve().parents[2] / "output" / "lab2" / "l02_caching.txt"
output_path.parent.mkdir(parents=True, exist_ok=True)
output = f"{cache_first}\n\n{first}\n\n{cache_second }\n\n{second}"
with output_path.open("a", encoding="utf-8") as file:
    file.write(output)

# The default cache lifetime is 5 minutes, so requests executed later may miss the cache