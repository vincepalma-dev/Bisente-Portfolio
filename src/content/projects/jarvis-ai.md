---
title: "Jarvis.AI Multi-Agent"
date: "2025"
featured: false
client: "Personal Exploration"
role: "Creator & AI Engineer"
skills: ["Python", "FastAPI", "AutoGen", "Vue.js", "TailwindCSS", "WebSockets", "Claude", "Gemini"]
related: []
outcome: "Multi-agent AI platform where specialized agents split up engineering tasks while a live dashboard shows every step. A personal project."
links:
  repo: "https://github.com/vincepalma-dev/Jarvis.AI"
---

### Overview

I wanted to see how far AI agents could get on engineering tasks by working together. Multi-agent runs are hard to follow, and I didn't want to be locked to one model provider. I built a platform where specialized AutoGen agents split up a task while a live dashboard streams every step, with OpenAI, Claude or Gemini behind any agent. You can watch where a task goes wrong and compare models on the same task.

- **Role:** Sole developer
- **Timeline:** 2025
- **Built for:** Myself, as an experiment · personal project
- **Impact:** 3 agent roles and 3 model providers in one live view

### The Challenge
I wanted to see how far autonomous agent cooperation could go on real engineering tasks. A single chat model handles one prompt at a time, and when several agents work together it's hard to see what each one is doing or why. I also didn't want to lock the system to one model provider.

### Solution & Architecture
**Data flow:** Vue 3 dashboard ⇄ WebSocket ⇄ FastAPI backend → AutoGen agents → OpenAI, Anthropic Claude or Google Gemini.

- **Agent roles:** Specialized AutoGen agents for code generation, research and data synthesis pass work to each other over an internal message bus.
- **Live visibility:** The backend streams each agent's reasoning, output tokens and task handoffs to the dashboard over WebSockets.
- **Provider-agnostic:** One integration layer lets any agent run on OpenAI, Claude or Gemini.
- **Dashboard:** Responsive Vue 3 frontend built with Vite and TailwindCSS.

### Results
- **3 specialized agent roles** cooperating on a single task.
- **3 model providers** swappable behind one interface.
- **Every step streamed live:** reasoning, tokens and handoffs show up as they happen.
- **16 API endpoints** in the FastAPI backend, including the live WebSocket feed.

### Key Takeaways
- Multi-agent systems are only debuggable if you can watch them. The live feed turned out to be more useful than any single agent.
- Keeping providers swappable means the same task can run on different models side by side.
