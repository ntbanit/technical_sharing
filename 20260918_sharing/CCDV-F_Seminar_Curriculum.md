# Claude Certified Developer – Foundations (CCDV-F)
## Complete 3-Day Seminar Curriculum

**Based on:** Anthropic Exam Guide v1.0 (effective July 2026)
**Exam facts:** 53 items · 120 minutes · Pearson VUE (online proctored or test center) · Passing score 720/1000 · Fee $125 · Valid 12 months
**Audience:** AI/ML engineers, technical leads, senior software engineers with 1–5 years of experience, ideally 6+ months hands-on with Claude, fluent in Python/TypeScript and REST APIs.

This curriculum covers all 8 official domains and all 25 weighted sub-skills. Sessions are sequenced for learning (fundamentals → building blocks → composition → hardening) rather than in blueprint order, and time is roughly proportional to each domain's exam weight.

---

## Domain Weights (official blueprint)

| # | Domain | Weight |
|---|--------|--------|
| 2 | Applications and Integration | 33.1% |
| 5 | Model Selection and Optimization | 16.8% |
| 1 | Agents and Workflows | 14.7% |
| 6 | Prompt and Context Engineering | 11.0% |
| 8 | Tools and MCPs | 10.6% |
| 7 | Security and Safety | 8.1% |
| 3 | Claude Code | 3.1% |
| 4 | Eval, Testing, and Debugging | 2.6% |

---

## DAY 1 — Building on Claude: Foundations & Applications

### Session 1 (90 min) — LLM & Technical Fundamentals *(Domain 5: 5.2% + 6.1%)*
- How transformer-based LLMs generate text; tokens, context windows, temperature/top-p
- Claude model family, generations, and capability tiers
- Latency, throughput, and streaming basics
- Reading model cards and release notes for capability changes
- **Lab:** Make your first Messages API call; inspect token usage in the response

### Session 2 (120 min) — Claude API Mechanics *(Domain 2: 6.8%)*
- Messages API structure: system prompts, roles, content blocks
- Multi-turn conversation state management
- Vision inputs, PDFs/documents, multimodal messages
- Streaming responses (SSE) vs. synchronous calls
- Prompt caching mechanics and cache-hit economics
- Message Batches API for asynchronous, high-volume workloads
- **Lab:** Build a streaming chat loop; add prompt caching to a repeated-context prompt

### Session 3 (90 min) — Understanding Requirements & Systems Life Cycle *(Domain 2: 3.4% + 2.8%)*
- Translating business requirements into an LLM-solvable problem
- Build vs. buy vs. fine-tune decision framework
- SDLC considerations specific to non-deterministic systems: versioning prompts, rollout strategy, rollback
- **Exercise:** Requirements-to-architecture case study (small group)

### Session 4 (150 min) — Claude Application Design *(Domain 2: 8.6%)* — heaviest single sub-skill
- Architecture patterns: single-call, chained, orchestrator, agentic
- Designing for statelessness and idempotency
- Error boundaries, retries, timeouts, circuit breakers around model calls
- Designing for observability from day one
- **Lab:** Design and diagram a production application architecture for a support-ticket triage system

### Session 5 (120 min) — Software Engineering Foundations & Configuration Management *(Domain 2: 7.4% + 4.1%)*
- SDKs (Python/TypeScript), environment and secrets management
- Config-driven prompts/models (feature flags, environment tiers)
- Version control practices for prompts and agent configs
- CI/CD considerations for AI-powered features
- **Lab:** Wire environment-based model/config switching (dev/staging/prod)

---

## DAY 2 — Agents, Tools, and the Developer Toolchain

### Session 6 (120 min) — Agent Architecture *(Domain 1: 4.5%)*
- Workflow vs. autonomous agent: when each is the right call
- Manager-worker, planner-executor, and subagent patterns
- Memory: short-term (context) vs. long-term (external stores)

### Session 7 (150 min) — Agent Construction with Claude *(Domain 1: 5.3%)*
- The agent loop: perceive → plan → act → observe
- Using the Claude Agent SDK to build and run agents
- Handling multi-step task state and long-running tasks
- **Lab:** Build a research agent that plans, calls tools, and self-corrects

### Session 8 (90 min) — Agent Patterns and Frameworks *(Domain 1: 4.9%)*
- Orchestration frameworks and when to reach for one vs. rolling your own
- Parallelizing subagents; aggregating subagent results
- Failure recovery and graceful degradation in multi-agent systems

### Session 9 (120 min) — Tool Implementation *(Domain 8: 4.4%)*
- Defining custom tools: schemas, descriptions that guide correct use
- Tool-use loop: tool call → execution → tool result → continuation
- Parallel tool calls and error surfaces back to the model
- **Lab:** Implement and register two custom tools; handle a failing tool call gracefully

### Session 10 (90 min) — MCP Server Development *(Domain 8: 2.1%)*
- What MCP is and the client/server/host model
- Building a minimal MCP server exposing a resource and a tool
- Connecting Claude to an MCP server
- **Lab:** Stand up a local MCP server and call it from a Claude client

### Session 11 (90 min) — Agentic Customisation *(Domain 8: 4.1%)*
- Built-in tools vs. custom tools vs. Skills vs. MCP — the decision framework
- Composing multiple extension mechanisms in one system
- **Exercise:** Given four scenarios, choose and justify the right extension mechanism for each

### Session 12 (60 min) — Claude Code Operation *(Domain 3: 3.1%)*
- Configuration hierarchy (project vs. user vs. global)
- Rules, Skills, custom commands, and subagents in Claude Code
- Headless, streaming, and auto modes; when to use each
- **Lab:** Configure a project-level Rule and a custom Skill in Claude Code

---

## DAY 3 — Prompting, Optimization, Security, and Exam Readiness

### Session 13 (90 min) — Context Engineering *(Domain 6: 3.8%)*
- Context rot: why more context isn't always better
- Attention budget and structuring long contexts
- Just-in-time context retrieval vs. front-loading everything
- RAG fundamentals and when retrieval beats stuffing context

### Session 14 (110 min) — Prompt Engineering *(Domain 6: 4.6%)*
- Prompt structure: role, task, constraints, examples, format
- Few-shot vs. zero-shot; when examples help vs. hurt
- Chain-of-thought and step-by-step reasoning prompts
- Prompt templates for reusable, parameterized prompts
- **Lab:** Iteratively improve a underperforming prompt using a rubric

### Session 15 (70 min) — Output Handling *(Domain 6: 2.6%)*
- Structured output (JSON mode / schema-constrained generation)
- Parsing, validating, and repairing model output
- Handling partial/streamed structured output

### Session 16 (90 min) — Model Selection & Trade-offs, Cost and Token Management *(Domain 5: 2.7% + 2.8%)*
- Opus vs. Sonnet vs. Haiku: quality/latency/cost trade-off framework
- Token usage tracking and cost modeling at scale
- Cost-optimization order of operations: caching → batching → model right-sizing → prompt trimming
- **Lab:** Model a cost estimate for a workload at three different model/config choices

### Session 17 (100 min) — AI Application Security & Guardrails *(Domain 7: 3.2% + 2.3%)*
- Prompt injection: attack patterns and layered defenses
- Input/output sanitization and allow-listing for tool actions
- Guardrails for safe deployment: content filters, human-in-the-loop gates
- **Lab:** Red-team a sample agent for prompt-injection vulnerabilities, then patch it

### Session 18 (60 min) — Claude Hooks & Identity/Secrets/Key Management *(Domain 7: 1.0% + 1.6%)*
- Hooks for intercepting and controlling agent behavior at runtime
- Managing API keys, credential rotation, least-privilege access for tools/MCP servers

### Session 19 (70 min) — Debugging and Error Handling *(Domain 4: 2.6%)*
- Common failure modes: hallucination, tool-call loops, context overflow
- Structured logging and tracing for multi-step agent runs
- Building lightweight evals to catch regressions before shipping
- **Lab:** Diagnose and fix a broken agent trace

### Session 20 (90 min) — Full-Blueprint Review & Timed Mock Exam
- Rapid review pass across all 8 domains, weighted by exam percentage
- 53-question timed mock exam (120 minutes, format-matched: multiple-choice and multiple-response)
- Debrief: score breakdown by domain, targeted re-study plan

---

## Suggested Pre-Reading / Reference Materials
- Anthropic's official CCDV-F Exam Guide v1.0 (authoritative source — confirm current weights/policies before exam day)
- `docs.claude.com` — Messages API, Claude Agent SDK, Claude Code, prompt engineering guides
- Model Context Protocol specification (github.com/modelcontextprotocol)
- Anthropic's own prompt engineering and context engineering documentation

## Logistics Notes
- Total seminar time: ~3 days / ~22 hours instruction, matching domain weights so no area is under-prepared relative to its exam share.
- Each lab is designed to be completable with just the Claude API/SDK and no other paid infrastructure.
- Recommend spacing the mock exam (Session 20) at least a few days before the real exam so gaps can still be closed.
- Since this is a partner-network credential as of writing, confirm current registration eligibility and exam-guide version before finalizing seminar content — weights and policies can change between versions.
