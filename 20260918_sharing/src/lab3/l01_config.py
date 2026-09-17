import os
import anthropic

CONFIGS = {
    "dev":  {"model": "claude-haiku-4-5-20251001", "max_tokens": 200},
    "prod": {"model": "claude-haiku-4-5-20251001", "max_tokens": 500},
}

env = os.environ.get("APP_ENV", "dev")
cfg = CONFIGS[env]

client = anthropic.Anthropic()
message = client.messages.create(
    model=cfg["model"],
    max_tokens=cfg["max_tokens"],
    messages=[{"role": "user", "content": f"""

Current environment: {env}

Configuration:{cfg}

Say which environment config is active and why it makes sense.

"""}],
)
print(f"[env={env}] model={cfg['model']}")
for block in message.content:
    if block.type == "text":
        print(block.text)

