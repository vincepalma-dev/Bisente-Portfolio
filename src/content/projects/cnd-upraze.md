---
title: "CND Upraze"
date: "2026"
featured: true
client: "CND Upraze Solutions (Technopreneurship)"
role: "Lead Full-Stack Developer & Architect"
skills: ["React", "Laravel", "PHP", "GitHub Actions", "Docker", "Three.js", "PostgreSQL", "Redis", "Groq AI", "TailwindCSS"]
related: []
outcome: "Digital services and e-commerce platform with checkout, a 3D studio and an AI assistant, deployed automatically on every change. A venture project for a 4th-year Technopreneurship course."
logo: "/images/projects/cnd-upraze.png"
logoBg: "#1F2A33"
links:
  repo: "https://github.com/vincepalma-dev/CND-Upraze"
---

### Overview

Our Technopreneurship course needed a launchable business platform, not a mockup: a service catalog, working checkout and an admin side to run it. The hard part was time. I was building it while interning, so testing and deploys couldn't be manual. I built a React and Laravel platform with Xendit and PayMongo payments, a Three.js studio and a Groq AI assistant, plus a pipeline that checks and deploys every change on its own. Releases need no manual server steps.

- **Role:** Lead developer: wrote 46 of the 48 commits, covering frontend, backend, CI/CD and server setup
- **Timeline:** April to May 2026
- **Built for:** Small businesses buying digital services · academic venture project
- **Impact:** Automated releases: build, migrate and reload run from CI with no manual steps

### The Challenge
Technopreneurship asked for a real, launchable business platform, not a mockup: a services catalog, working checkout, an admin side to run the business, and something that set the product apart.

The constraint was time. I was the only developer and was interning at the same time, so I couldn't afford manual testing or hand-run deploys. Anything repetitive had to be automated.

### Solution & Architecture
**Data flow:** React 19 app → Laravel 11 API → PostgreSQL 16, with Redis 7 for cache and queues. Xendit and PayMongo call back into the API on payment, and the AI assistant runs on Groq.

- **Admin command center:** Revenue charts, client activity and service package management on one screen.
- **3D studio:** Interactive model viewer built with Three.js and React Three Fiber.
- **Payments & orders:** Checkout with automatic invoices, Xendit and PayMongo payment callbacks, and instant customer notifications.
- **AI assistant:** A Groq-powered chatbot for customer support and task automation.
- **Quality gate:** CI starts PostgreSQL 16 and Redis 7 containers, runs migrations and the test suite with an **80% coverage** floor, and checks the backend with PHPStan level 5.
- **Deployment:** Docker Buildx builds multi-platform images (cached in GitHub Actions) and pushes them to Docker Hub. CI then deploys to the VPS over SSH with a Docker Compose rolling reload, runs migrations, and warms the route and config caches.

### Results
- **2 payment gateways** integrated: Xendit and PayMongo.
- **0 manual server steps** per release: build, migrate and reload all run from CI.
- **1 developer** covering frontend, backend, CI/CD and infrastructure.
- **13 data models** across a **22-table** PostgreSQL schema.

### Key Takeaways
- When time is the tightest constraint, automation is worth setting up first. Every release after that ran on its own.
- Containerizing early paid off: the same Docker image runs in CI and in production.
