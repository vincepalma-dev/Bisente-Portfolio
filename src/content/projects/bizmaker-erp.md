---
title: "BizMaker HRIS ERP"
date: "2026"
ongoing: true
featured: true
client: "BizMaker Consultancy Inc."
role: "Sole Developer & Architect (SaaS)"
skills: ["Vue.js", "TypeScript", "Python", "Django", "GitHub Actions", "Docker", "PostgreSQL", "Redis", "Pinia"]
related: []
outcome: "Payroll and HR SaaS that cut payroll processing time by 95%. A real product already running payroll for 30+ employees in-house ahead of its public release."
logo: "/images/projects/bizmaker.png"
shot: "/images/projects/shots/bizmaker-erp.jpg"
links: { live: "https://bizmaker-payroll.vercel.app/" }
---

### Overview

Philippine businesses need payroll that gets every government deduction right, every cutoff. That's hard because SSS, PhilHealth, Pag-IBIG and withholding tax each have their own brackets and ceilings, and biometric attendance arrives with missed punches. I designed and built a multi-tenant payroll and HR platform that pulls attendance from ZKTeco devices, fills the gaps and computes pay automatically. Payroll processing time dropped by 95%, with 0 contribution errors across 12 cutoffs.

- **Role:** Sole developer and architect: database design, Django REST API, Vue 3 frontend, CI/CD and deployment
- **Timeline:** March 2026 to now, 1,280 commits over 8 months. In use in-house, public SaaS release in progress
- **Built for:** Philippine businesses and their HR teams · real product
- **Impact:** 95% less payroll processing time, with 0 contribution errors

### The Challenge
Every Philippine payslip stacks several government rules: SSS, PhilHealth and Pag-IBIG contributions, withholding tax, and the year-end BIR 2316 certificate. Each has its own brackets and ceilings, and one wrong figure is someone's paycheck or a tax filing.

Attendance came from ZKTeco biometric devices, where missed punches and shift changes had to be resolved before payroll could run. And because it is built to serve many companies as a SaaS, one tenant's data can never leak into another's.

### Solution & Architecture
**Data flow:** Vue 3 app (Pinia) → Django REST API → PostgreSQL, with Redis for caching. ZKTeco devices feed attendance through the biometric SDK.

- **Payroll engine:** Statutory rules run inside database transactions, so a payroll run either completes fully or changes nothing.
- **Attendance sync:** Backfill logic fills missed punches and shift variations before payroll reads the hours.
- **Multi-tenancy:** Every company's records are isolated per tenant, and Redis caches repeated lookups.
- **Quality gates:** A multi-stage GitHub Actions pipeline starts throwaway PostgreSQL and Redis containers and runs Pytest, Vitest and Playwright on every change, including checks on the statutory formulas. A pre-commit gate blocks committed credentials.
- **Reporting:** Payslips, government remittance summaries and bank payroll sheets export through SheetJS and jsPDF.
- **Deployment:** Frontend on Vercel, API on Render, released without downtime.

### Results
- **30+ employees** paid through it inside the company, ahead of the public SaaS release.
- **5 statutory outputs automated:** SSS, PhilHealth, Pag-IBIG, withholding tax and BIR 2316 certificates.
- **Payroll math tested automatically** on every change, including SSS, PhilHealth, Pag-IBIG and withholding tax, before it can ship.
- **53 data models** and **150+ API routes**, built over **1,280 commits**.
- **0 manual deploy steps:** releases go out from CI to Vercel and Render.
- **95% less time per payroll cutoff** across 2 semi-monthly cutoffs.
- **0 contribution errors** across 12 payroll cutoffs since it went into internal use.

### Key Takeaways
- Payroll leaves no margin for error, so the test suite is part of the product, not an afterthought.
- The project started as a single-company calculator. Next time I would design for multiple tenants from day one instead of adding isolation as it grew.
