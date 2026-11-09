---
title: "Gamma Oracle PM"
date: "2026"
featured: true
client: "AAA and Co., CPAs (for Gamma Oracle Dimension Inc.)"
role: "Software Development Associate (Employed Jun 1, 2026 – Present)"
skills: ["React", "TypeScript", "Node.js", "Express", "PostgreSQL", "Supabase", "TailwindCSS"]
related: []
outcome: "Construction cost-control platform that cut contractor billing prep from ~3 hours to under 45 minutes, with 0 deduction errors in 40+ test billings. Private software I lead at my current job."
logo: "/images/projects/aaa-cpas.png"
links: {}
---

### Overview

Construction projects need contractor billings that are accurate and traceable to the peso. Each billing stacks withholding tax, VAT, retention and mobilization recoupment, and doing that by hand invites errors that auditors catch later. I'm leading development of a cost-control platform that applies those rules automatically and posts each result to the ledger in one atomic transaction. Billing prep dropped from about 3 hours to under 45 minutes, with 0 errors across 40+ test billings.

- **Role:** Lead developer: architecture, API, ledger logic and security
- **Timeline:** June 2026 to present
- **Built for:** Project managers and accountants on construction projects · private client software
- **Impact:** About 75% less time per contractor billing

*This is private client software. Client names, proprietary business rules and internal figures are generalized here.*

### The Challenge
Construction projects bill contractors in stages, and each billing carries several deductions: expanded withholding tax, VAT, contract retention and mobilization recoupment. Calculated by hand, these are easy to get wrong, and every peso has to be traceable for audit. The platform also had to keep budgets, change orders and contractor documents in one place.

### Solution & Architecture
**Data flow:** React and TypeScript app → Node.js / Express API → PostgreSQL on Supabase.

- **Billing rules:** 1% and 2% expanded withholding, 12% VAT, 10% CIAP 102 retention and 15% mobilization recoupment are computed by the system, not typed in.
- **Cost governance:** Budget tracking, change orders and automatic cost-variance calculations per project.
- **Ledger integrity:** Ledger allocations run in atomic transactions, so a partial update can never leave the books out of balance.
- **Security:** Role-based permissions, JWT authentication, rate limiting and Helmet security headers.
- **Documents:** One hub for contractor contracts, tax withholding records and payment orders.

### Results
- **5 deduction rates automated** on every contractor billing.
- **Every ledger allocation** is atomic and recorded in the audit trail.
- **4 security layers** on the API: role-based access, JWT auth, rate limiting and security headers.
- **Billing prep cut from ~3 hours to under 45 minutes** per contractor progress billing (~75%).
- **0 deduction errors** across 40+ test billings, checked against the CPA team's manual computations.
- **12 projects** loaded and reconciled during acceptance testing.

### Key Takeaways
- In financial software, correctness is the feature. Atomic transactions and an audit trail come before anything visual.
- Working next to CPAs taught me to model the accounting rules first and build screens second.
