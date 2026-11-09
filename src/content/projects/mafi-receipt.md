---
title: "MAFI Invoicing & DR Automation"
date: "2024"
featured: false
client: "Michael Anthony's Fashion Inc."
role: "Freelance Software Developer"
skills: ["Node.js", "Express", "SQLite", "JavaScript", "HTML5", "CSS3"]
related: []
outcome: "Front-desk invoicing tool that saves ~5 hours a week of handwritten receipts and keeps working offline. A real client project, built in 2024 and rebuilt in 2026."
logo: "/images/projects/mafi-fashion.png"
links: {}
---

### Overview

A shop's front desk needed to stop handwriting invoices and delivery receipts. The internet was unreliable and they didn't want a subscription, so the tool had to run offline at no monthly cost. I built a receipt tool that calculates totals, fills BIR-aligned templates and prints to thermal or dot-matrix printers from a local database. It saves about 5 hours a week and removed math errors from receipts.

- **Role:** Sole developer
- **Timeline:** Built in 2024, rebuilt in 2026
- **Built for:** Front-desk staff at a garment business · real client project
- **Impact:** About 5 hours a week saved

### The Challenge
MAFI's front desk was handwriting every delivery receipt and invoice, losing hours each week and risking math mistakes on documents that had to match BIR layouts. The shop's internet wasn't reliable, so the tool had to work offline, and they didn't want another subscription.

### Solution & Architecture
**Data flow:** Front-desk browser → Node.js / Express (2026) → local SQLite file → printer.

- **2024 version:** Plain HTML, CSS and JavaScript with local SQLite storage, so staff could save billing progress without anything complicated.
- **2026 rebuild:** As order volume grew, MAFI asked for a smoother workflow. I added a lightweight Node.js and Express backend for a faster, desktop-like interface with instant totals.
- **Receipt templates:** Pre-formatted to match BIR invoice and delivery receipt layouts, with all math done by the system.
- **Offline-first storage:** Records and customer history stay on a local SQLite database with simple backups, so work continues when the internet drops.
- **Print layouts:** CSS print stylesheets tuned for thermal rolls and dot-matrix continuous-feed printers.

### Results
- **~5 hours a week** of handwriting saved at the front desk.
- **0 handwritten math errors**, since every total is calculated.
- **2 printer types** supported: thermal and dot-matrix.
- **₱0 subscription cost**, and it keeps working offline.

### Key Takeaways
- Starting small was right. The simple 2024 version earned the trust that led to the 2026 rebuild.
- Offline-first isn't an edge case for small shops in the Philippines. It's the default.
