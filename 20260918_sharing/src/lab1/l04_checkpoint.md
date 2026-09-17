## Checkpoint question:
- Why does  matter for a production application that pipes output into another system?

## Checkpoint answer
- `stop_reason` matters because a downstream production system must know whether the output is complete and safe to process or whether generation stopped for another reason.

For example:
`end_turn`: The response completed normally, so the next system can process it.
`max_tokens`: The response was truncated, so parsing or storing it as complete data may produce invalid results.
`stop_sequence`: A configured stopping sequence was reached.
`tool_use`: Claude expects the application to execute a tool rather than treat the response as final text.
`refusal`: The request was declined and should be handled appropriately.

Therefore, an application should inspect `stop_reason` before piping the output into a database, JSON parser, notification system, or another API.

A simple production check could be:
```python
if message.stop_reason == "end_turn":
    # Safe to send to the next system
    process_output(message.content)
elif message.stop_reason == "max_tokens":
    raise RuntimeError("Claude's response was truncated.")
else:
    raise RuntimeError(f"Unexpected stop reason: {message.stop_reason}")
```
