Checkpoint question: Why is it dangerous to hardcode a model string directly inside business logic instead of a config layer like this?
Copilot said:
Checkpoint Answer:

Hardcoding a model name inside business logic is dangerous because it makes the application harder to maintain, update, and deploy across environments.

For example:




Python
# Bad
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    ...
)
If the model is deprecated, upgraded, or you want a different model in production, you must search through the codebase and change business logic. This increases the risk of bugs and inconsistent configurations.

Using a configuration layer separates business logic from deployment settings:




Python
CONFIGS = {
    "dev": {"model": "claude-haiku-4-5-20251001"},
    "prod": {"model": "claude-sonnet-4-5-20251001"},
}
Benefits:

Easier model upgrades without modifying application logic.
Different environments can use different models, token limits, or settings.
Reduces accidental production changes.
Makes testing cheaper by using smaller models in development.
Centralizes configuration, improving maintainability and operational safety.
In short, hardcoding couples your business logic to a specific model, while a configuration layer provides flexibility, maintainability, and safer deployments.