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
    }
]

def ask_question(order_id: str) :
    messages = [{"role": "user", "content": f"What's the status of order {order_id}?"}]

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        tools=tools,
        messages=messages,
    )

    # Handle the tool-use turn
    if response.stop_reason == "tool_use":
        tool_use_block = next(b for b in response.content if b.type == "tool_use")
        result = get_order_status(**tool_use_block.input)

        messages.append({"role": "assistant", "content": response.content})
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": json.dumps(result, indent=2),
                }
            ],
        })

        final = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=500,
            tools=tools,
            messages=messages,
        )
        for block in final.content:
            if block.type == "text":
                print(block.text)

# ask_question("A101")
ask_question("Z999")