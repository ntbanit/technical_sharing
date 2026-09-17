# Claude Certified Developer – Foundations (CCDV-F)

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

## Getting Started

### Prerequisites
- Python 3.10+
- Anthropic API key

### Installation

1. **Clone and create a virtual environment:**
```bash
git clone <repo-url>
cd ccdv-f-labs
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables: Create a .env file in the project root:
```bash
export ANTHROPIC_API_KEY=your_api_key     # Windows: set ANTHROPIC_API_KEY=...
```

4. Run a lab:
```bash
python src/lab1/l01_first_call.py
```


---

#### 2. Add a Lab Directory Map & Syllabus Tracker
**Why:** Lab implementations in [`src/`](./src) (covering API fundamentals, streaming, prompt caching, tool use, and the Claude Agent SDK) and study notes in [`docs/`](./docs). A directory map connects the exam domains directly to the code artifacts.

**Suggested addition:**

## Repository Structure & Labs

| Directory | Topic | Key Concepts Covered | Official Domain |
|---|---|---|---|
| [`src/lab1/`](./src/lab1) | API Basics & Tokens | First call, `max_tokens`, system persona | Domain 2 & 6 |
| [`src/lab2/`](./src/lab2) | Streaming & Optimization | Response streaming, prompt caching | Domain 5 |
| [`src/lab3/`](./src/lab3) | Configuration | Client configuration and settings | Domain 2 |
| [`src/lab4/`](./src/lab4) | Tools & MCPs | Tool definitions, function calling, execution loops | Domain 8 |
| [`src/lab5/`](./src/lab5) | Agents & Workflows | Manual agent loops vs. Claude Agent SDK | Domain 1 |
| [`docs/`](./docs) | Study Guides | Module 0–2 lecture notes and exam concepts | All |

---

## Exam Preparation Roadmap (Target: 2027)

- [x] **Phase 1: Foundations** (Lab 1 & Module 0–1) — API basics, message structures, token budgets.
- [x] **Phase 2: Core Optimization** (Lab 2–3) — Prompt caching, streaming, rate limits.
- [ ] **Phase 3: Tools & Integration** (Lab 4) — Tool use schemas, error handling, MCP servers.
- [ ] **Phase 4: Agentic Architectures** (Lab 5 & Module 2) — Agent loops, routing, Agent SDK.
- [ ] **Phase 5: Safety, Eval & Mock Exams** — Guardrails, red teaming, practice exams.