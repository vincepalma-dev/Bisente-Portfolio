---
title: "STI OMMA Platform"
date: "2026"
featured: true
client: "Organization of Multimedia Artists (STI)"
role: "Freelance Full-Stack Engineer"
skills: ["Next.js", "React", "TypeScript", "GitHub Actions", "PostgreSQL", "Redis", "Prisma", "Supabase Storage", "TailwindCSS", "Socket.io", "Xendit"]
related: []
outcome: "Art-commission marketplace where buyers pay into escrow and a 10% platform fee splits out automatically on every payout. A real project for a college artists' organization."
logo: "/images/projects/omma-sti.png"
shot: "/images/projects/shots/omma-platform.jpg"
links:
  live: "https://omma-art.vercel.app/"
---

### Overview

Student and alumni artists needed a safe place to take commissions and get paid. Buyers and artists are often strangers, so both sides needed protection before money changed hands. I built a marketplace where buyers pay into Xendit escrow and the money is released on delivery, with a 10% platform fee split out automatically. It passed all 36 alpha test cases on a 20-model schema and 91 API routes.

- **Role:** Sole developer: schema, API, frontend, payments and CI/CD
- **Timeline:** May to November 2026, 425 commits
- **Built for:** Multimedia artists and their buyers · real project for a college organization
- **Impact:** 36 of 36 alpha test cases passed before launch

### The Challenge
Student and alumni artists at STI had no shared place to show portfolios, take commissions and get paid safely. Both sides needed protection: buyers wanted the art before paying in full, artists wanted proof the money existed. The platform also had to store large, high-resolution media and support live conversation between artists and buyers.

### Solution & Architecture
**Data flow:** Next.js app → API routes → PostgreSQL through Prisma, with Supabase Storage for media, Upstash Redis and Socket.io for live features, and Xendit for payments.

- **Commissions & escrow:** Xendit holds the buyer's payment in escrow and releases it to the artist on delivery, splitting out a 10% platform fee.
- **Portfolios:** High-resolution uploads go directly to Supabase Storage, with Exif extraction and Algolia instant search.
- **Live features:** Real-time chat and announcements over Socket.io and Upstash Redis.
- **Testing:** API contract tests run in GitHub Actions before every production build, Supabase CLI migrations sync the schema on deploy, and Lighthouse CI enforces performance, accessibility and SEO budgets.
- **Security & reliability:** Static security scans run weekly and on every pull request, credential checks gate every commit, and a health check pings PostgreSQL and Redis every 30 minutes.

### Results
- **36 of 36** alpha test cases passed.
- **20-model** PostgreSQL schema behind **91 API routes**.
- **Commission, escrow and payout flows tested automatically** before every release.
- **10% platform fee** split out automatically on every escrow payout.
- **Every 30 minutes**, production health is checked automatically.

### Key Takeaways
- Escrow is what makes a marketplace trustworthy for both sides, so the payment flow got the strictest testing.
- With 91 routes to keep in sync, contract tests are the only practical way to know the API still matches what the frontend expects.
