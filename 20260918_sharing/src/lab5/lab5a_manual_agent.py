import json
import anthropic

client = anthropic.Anthropic()


fake_db = {
    "A100": {
        "name": "Bruce Wayne",
        "date": "2026-09-17",
        "address": "Batcave",
        "product": "Mask",
        "amount": "$123.4",
        "status": "Shipped",
    },
    "A101": {
        "name": "Clark Kent",
        "date": "2026-09-16",
        "address": "Metropolis",
        "product": "Glasses",
        "amount": "$89.9",
        "status": "Delivered",
    },
    "A102": {
        "name": "Diana Prince",
        "date": "2026-09-15",
        "address": "Themyscira",
        "product": "Shield",
        "amount": "$299.0",
        "status": "Processing",
    },
    "A103": {
        "name": "Barry Allen",
        "date": "2026-09-14",
        "address": "Central City",
        "product": "Running Shoes",
        "amount": "$149.5",
        "status": "Shipped",
    },
    "A104": {
        "name": "Arthur Curry",
        "date": "2026-09-13",
        "address": "Atlantis",
        "product": "Trident",
        "amount": "$499.9",
        "status": "Pending",
    },
}
def get_order_status(order_id: str) -> dict:
    return fake_db.get(order_id, "Order not found")

def get_return_policy(product: str) -> str:
    policies = {
        "Mask": "Returns accepted within 30 days.",
        "Glasses": "Returns accepted within 14 days.",
        "Shield": "Returns accepted within 60 days.",
        "Running Shoes": "Returns accepted within 30 days.",
        "Trident": "Returns not accepted.",
    }
    return policies.get(product, "No return policy found.")

tools = [
    {
        "name": "get_order_status",
        "description": "Look up the shipping status of a customer order by its ID.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string", "description": "The order ID, e.g. A100"}
            },
            "required": ["order_id"],
        },
    },
    {
        "name": "get_return_policy",
        "description": "Look up the return policy for a product.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product": {
                    "type": "string",
                    "description": "The product name"
                }
            },
            "required": ["product"],
        },
    }
]


def run_agent(user_prompt, tools, tool_impls, max_turns=5):
    messages = [{"role": "user", "content": user_prompt}]
    for _ in range(max_turns):
        response = client.messages.create(
            model="claude-haiku-4-5-20251001", max_tokens=200, tools=tools, messages=messages
        )
        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if b.type == "text")

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                fn = tool_impls[block.name]
                result = fn(**block.input)
                tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": str(result)})
        messages.append({"role": "user", "content": tool_results})
    return "Max turns reached without a final answer."

tool_impls = {
    "get_order_status": get_order_status,
    "get_return_policy": get_return_policy,
}

answer = run_agent(
    "What's the status of order A104 and what is the return policy for that product?",
    tools,
    tool_impls,
)

print(answer)

print(
    run_agent(
        "What's the status of order A101 and what is the return policy for that product?",
        tools,
        tool_impls,
    )
)

print(
    run_agent(
        "Can I return the product in order A100?",
        tools,
        tool_impls,
    )
)