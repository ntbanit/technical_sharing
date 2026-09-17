import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async def main():
    async for message in query(
        prompt="Review this project's README and suggest 3 improvements.",
        options=ClaudeAgentOptions(model="claude-haiku-4-5-20251001"),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
        if isinstance(message, ResultMessage):
            print("--- done ---")

asyncio.run(main())