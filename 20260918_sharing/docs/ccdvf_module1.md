## MSO Foundations
- Model
- Sampling
- Operations

## It covers:
- Model: tokens, context windows, model types, and capabilities
- Sampling: how Claude generates responses, including randomness and non-determinism
- Operations: accessing Claude through SDKs, REST APIs, streaming, async requests, and batch processing

Before you write a line of code against Claude, it helps to know what the words mean. This module introduces the model fundamentals and the technical foundations that the rest of the Developer course assumes you already have.

What you will be able to do by the end
Before you write a line of code against Claude, it helps to know what the words mean.

This module introduces the model fundamentals and the technical foundations that the rest of the Developer course assumes you already have.

By the end of this module, you will be able to:
1Explain what a token is, how the context window works as a fixed budget, why sampling makes outputs vary, and what non-determinism means for testing and evals.
2Describe the Claude model family and its capability tiers, and distinguish choosing a model from enabling a reasoning mode such as extended thinking.
3Choose between zero-shot, one-shot, and multi-shot prompting, and weigh the cost and quality trade-off of adding examples.
4Describe how a developer accesses Claude: SDK versus raw REST, synchronous versus streaming responses, and asynchronous patterns for high-volume work.
Disclaimer / Notice for Educational Content
We built this Developer course Module 1: MSO Foundations to help you get real work done with Claude. Treat it as educational content. It doesn't constitute legal, financial, or other professional advice, so adapt what you learn to your own situation. Our products and services evolve quickly, so certain content may contain errors or be outdated; remember to verify on Anthropic’s website or docs. Examples and scenarios used in the course are illustrative and often fictitious. If the course material mentions a company or product, it doesn't mean Anthropic endorses them, they endorse Anthropic, or that we're affiliated. Also note your use of Anthropic products and services is covered by our terms, policies and documentation; if anything in this course conflicts with them, they control.

How LLMs behave: tokens, context, sampling, non-determinism
Tokens
Context Window
Sampling
Non-determinism
Tokens: the unit of input, output, and cost
Claude does not read characters or words directly. It reads tokens, and the characters-per-token average depends on the tokenizer of the model at hand and differs between model generations. Treat any chars-per-token rule of thumb as model-dependent and confirm current tokenizer behavior at build time. Everything the model processes is counted in tokens: your prompt, the conversation history, tool definitions, tool results, and the response the model generates. Tokens are the unit of both pricing and budget, so when you estimate what a feature costs or whether an input fits, you are counting tokens, not words. A useful habit is to think in tokens, since that is the unit the API bills in and the context window measures.

Model options and reasoning modes
The Model Family
Reasoning Modes
How They Work Together
The Claude model family
Claude is a family of models that currently spans four tiers: Fable, Opus, Sonnet, and Haiku. Each model represents a different tradeoff across cost, latency, and capability. Sonnet is the balanced default for most production workloads. Haiku is built for speed and cost efficiency on tasks that fit its capability envelope. Opus handles demanding work above the Sonnet envelope, and Fable is the most capable tier, built for the most demanding reasoning, coding, and agentic work where maximum intelligence is the priority. The practical default is to start with Sonnet, move up a tier only when an eval shows the current tier missing your quality bar, and move down to Haiku only when an eval shows the quality drop is acceptable for the task. Confirm the current model lineup and identifiers against platform.claude.com/docs at build time, since the Claude family is evolving.

Reasoning modes are a separate setting from model choice
Choosing which model to run is one decision. Whether the model reasons before answering is a separate decision you make per call. On current models the reasoning mode is adaptive thinking: the model decides when and how much to think, and you tune depth with an effort setting rather than a fixed token budget (the older budget_tokens control is deprecated and, on the newest model generations, returns a 400 error). Thinking content is omitted from responses by default on the newest models. Request summarized display when you need to show it. Reasoning earns its cost on hard, multi-step problems and is wasted on lookups and classification. The key point for this module is that the two levers compose: model choice picks the family member, while the reasoning mode is configured per request. Per-model defaults differ (some of the newest models think adaptively by default or always), so confirm the current thinking defaults for your model at build time.

How the two work together
Because model choice and reasoning mode are independent, each can be set separately. A capable model with reasoning off is fast and direct, while a smaller model with reasoning on spends more tokens to think. The most demanding tasks pair a capable model with a higher effort setting. Module 2 teaches the mechanics of enabling reasoning and handling the thinking blocks it returns. The decision of which model to run, weighed against cost, latency, and quality, is taken up in Module 4.

Prompting modes: zero-shot, one-shot, multi-shot
The Three Modes
Cost & Quality Trade-off
Mode & Model Choice
The three modes
Separate from how you word a prompt is how many worked examples you give the model inside it. Zero-shot gives the instruction and no examples: you describe the task and ask for the result. One-shot adds one example of the input paired with the desired output. Multi-shot, also called few-shot, includes several such examples. The examples are not training data; they sit in the prompt and show the model the exact shape of the answer you want, which a description alone often fails to pin down.

The cost and quality trade-off
Each example you add costs tokens on every call and consumes context budget, so the choice trades quality against cost. Reach for zero-shot when the task is simple and the output shape is obvious. Move to one-shot or multi-shot when the output has a specific structure, casing, or edge case that a description keeps missing. Often one or two correct examples usually fix the issue faster than another paragraph of instructions. The general discipline, which Module 2 reinforces, is to add the smallest amount of prompt that produces a reliable result.

Mode choice interacts with model choice
Prompting mode and model choice are related levers. A more capable model often succeeds zero-shot on a task where a smaller model needs a few examples to match the structure, so adding examples can let a cheaper model do the job. The two decisions are worth making together: try the simplest model and the fewest examples that meet your eval, and add capability or examples only where the eval says you need them.

The technical substrate: SDKs, REST, streaming, async
SDK vs. REST
Sync, Streaming & Real-time
Async for High-Volume Work
How a developer reaches Claude: SDK versus raw REST
At its core, Claude is reached over an HTTP REST API: your code sends a request to an endpoint with your API key and a JSON body, and reads a JSON response back. You can call that endpoint directly with any HTTP client. More commonly you use an official SDK, available for Python and TypeScript among others, which is a thin convenience layer over the same REST API. It handles authentication, request construction, retries, and response parsing so you write less boilerplate. The SDK and raw REST reach the same API and the same model. The SDK saves you from assembling requests by hand. Module 2 builds against the SDK and the Messages API, which sits on this same foundation.

Synchronous, streaming, and real-time responses
A synchronous request is the simplest pattern: you send the request and wait for the complete response to come back in one piece, then act on it. That is fine for short responses and backend jobs where no one is waiting. When a response is long or a user is watching, streaming sends the response in pieces as the model generates it. Output appears immediately rather than after a blank-screen wait, and your code reassembles the pieces into the final message. Claude exposes streaming over the same HTTP connection using server-sent events. Module 2 teaches how to consume a stream safely and recover when it is interrupted.

Asynchronous patterns for high-volume work
Two patterns address high-volume work, and they solve different problems.

The Python SDK exposes an async client (AsyncAnthropic) that uses non-blocking async/await to make API calls without tying up your application thread. In the TypeScript SDK the standard Anthropic client is Promise-based, so you await calls directly. There is no separate async client class. Either way the request still returns in real time, but your application can handle other work while it waits. This is the right pattern when you need concurrency without blocking.

The Message Batches API is a separate pattern for bulk offline workloads. You submit a large set of requests in one call, receive an identifier, and poll for completion. Batch jobs can take up to 24 hours to complete and run at a lower per-token cost in exchange for that latency. This suits offline pipelines, evaluation runs, and bulk jobs where no user is waiting on each result and cost matters more than turnaround time.

Recap: five takeaways
1
Tokens are the unit of input, output, and cost.
Think and budget in tokens rather than words, since that is what the API meters and the context window measures.

2
The context window is a fixed token budget that holds the whole request at once.
An oversized input errors before generation, while hitting the ceiling mid-generation returns truncated output with a model_context_window_exceeded stop reason, so managing history is the application's job.

3
Sampling makes generation non-deterministic.
The same prompt can return different wording on each run, so testing on exact text is unreliable. This is what evals are built for.

4
Model choice and reasoning mode are separate, composable levers.
Pick the smallest model and the simplest reasoning and prompting that meet your eval and add capability only where the eval says you need it.

5
A developer reaches Claude over a REST API, usually through an SDK.
Choose between synchronous, streaming, async/await, or batch based on whether a user is waiting and whether the workload is real-time or bulk offline.

What comes next: Module 2 puts these foundations to work across prompting craft, tool schemas, streaming, context engineering, and agent construction.

Sources

Claude 101 (Skilljar), Building with the Claude API (Skilljar), AI Fluency: Framework & Foundations (Skilljar), platform.claude.com/docs. Verify product specifics at publish time.

You can now speak the shared vocabulary of the Developer course.
Tokens, context, sampling, model tiers, prompting modes, and the transport mechanics of the API now have names, so the rest of the course can build on them directly.


Congrats! You’ve successfully completed this module.
You can now explain tokens, the context window, sampling, and non-determinism, distinguish model choice from reasoning mode, choose the right prompting mode for the job, and describe how a developer reaches Claude over SDKs, REST, streaming, and async patterns. These foundations are the shared vocabulary the rest of the Developer course builds on.

0
of 2 checkpoints passed
M1
MSO Foundations

Tokens, context, sampling, model tiers, prompting modes, and the technical substrate.

You Are Here
M2
Production-Grade Prompting, Agents & Tool-use

Prompting craft, extended thinking, tool schemas, streaming, context engineering, and agent construction.

Up Next
M3
Claude Code, MCP & Integration

Permission modes, durable project context, plugin packaging, and MCP integration without leaking credentials.

M4
Production Engineering, Evals, and Security

Evals, tracing, failure handling, cost and orchestration budgets, and security boundaries that hold in production.

M5
Accelerators and IP Contribution

Package accelerators, prepare verifiable contributions, choose deployment platforms, and mark trust boundaries.

Review module
Start over