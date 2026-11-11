---
title: "JULI (Jolly Universe of Little Intelligences)"
date: "2025"
ongoing: true
featured: true
client: "Personal open-source project"
role: "Creator & AI Engineer"
skills: ["Python", "FastAPI", "Vue.js", "TailwindCSS", "Ollama", "MCP", "WebSockets", "Playwright"]
related: []
outcome: "A local-first crew of 6 AI agents that plans, writes, reviews and tests software on your own machine, with a Privacy Mode that keeps everything on-device. An open-source personal project that grew out of Jarvis.AI."
shot: "/images/projects/shots/juli.jpg"
links:
  repo: "https://github.com/vincepalma-dev/JULI"
---

### Overview

Developers who want an AI coding crew usually have to send their code to the cloud and pay per token. That's hard to avoid, because most agent tools assume cloud models, and local models vary wildly in what a given laptop can run. I built JULI, a crew of 6 agents that plans, writes, reviews and tests software on your own machine, using local models that fit your hardware or your own cloud keys. It started in 2025 as Jarvis.AI, an AutoGen experiment, and I rebuilt it as JULI on an agent engine of my own.

- **Role:** Sole developer: agent engine, FastAPI backend, Vue 3 dashboard, CLI and CI
- **Timeline:** 2025 to present. Started as Jarvis.AI, rebuilt as JULI in 2026
- **Built for:** Developers who want AI help without giving up their code or their budget · open-source personal project (MIT)
- **Impact:** Runs fully offline in Privacy Mode, with no token limits

### The Challenge
Jarvis.AI showed that agents could cooperate, but it depended on cloud APIs and AutoGen, and it couldn't be trusted with real files. JULI had to:

- Run on whatever machine the user has, from a laptop CPU to a gaming GPU, and say honestly which models fit.
- Keep code private when the user asks, enforced in code rather than hidden in the UI.
- Let agents write real files and run commands, but only with the user's approval.
- Keep going when a cloud key runs out of credit instead of crashing mid-run.

### Solution & Architecture
**Data flow:** Vue 3 dashboard or `juli` CLI ⇄ FastAPI backend (127.0.0.1 only, session token) → agent engine → Ollama, OpenAI-compatible local servers, or cloud providers (OpenAI, Anthropic, Gemini, OpenRouter).

- **Agent crew:** Planner/Researcher, Coder, Reviewer/Security, DevOps, Test Monitor and Docs/Diagram agents share one plan, and review and test results feed the next pass. The Tester sends a failing test straight back to the Coder.
- **Least-privilege tools:** Each role gets only the tools it needs. The Reviewer can run the tests but never edit the code it reviews. More tools plug in from any MCP server.
- **Hardware-aware models:** JULI reads RAM, GPU and free disk, greys out models that won't fit with the reason, benchmarks each download for real tokens per second, and Auto-Crew picks the best model for every role.
- **Privacy, Hybrid and Cloud modes:** Privacy Mode blocks every outside call in the code that calls models, so nothing leaves the device.
- **Real workspace:** Generated code lands in a file tree with diffs, a built-in terminal, zip export and git commits. Agent commands ask for approval unless they're test commands inside the Docker sandbox.
- **Key guardrails:** Keys live in the OS keychain, are checked when saved, warn when running low, and a run pauses instead of crashing when credit runs out.
- **Quality:** CI runs Ruff, mypy, Pytest, Vitest, Playwright end-to-end tests and Gitleaks. A nightly job runs the crew on a real local model.

### Results
- **6-agent crew** working from one shared plan.
- **3 modes:** Privacy (fully on-device), Hybrid (planning and review in the cloud) and Cloud.
- **6 model sources:** Ollama, OpenAI-compatible local servers, OpenAI, Anthropic, Gemini and OpenRouter.
- **58 API routes and 13 CLI commands**, so everything in the dashboard also works from the terminal.
- **0 token caps:** local models get the largest context window the machine's memory allows.

### Key Takeaways
- Rebuilding beat patching. Replacing AutoGen with a lean engine of my own put middleware around every model call, which made the crew easier to test and debug.
- Privacy has to live in the code path, not the settings screen. Enforcing Privacy Mode where models are called is what makes the promise checkable.
