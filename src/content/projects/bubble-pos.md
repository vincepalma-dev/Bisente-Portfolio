---
title: "Bubble Hideout POS"
date: "2024"
featured: true
client: "Bubble Hideout (CAA Las Piñas)"
role: "Freelance Full-Stack Developer"
skills: ["PHP", "MySQL", "JavaScript", "FPDF", "PhpSpreadsheet", "HTML5", "CSS3"]
related: []
outcome: "Restaurant POS that handles 50+ orders a day and cut end-of-day closing time by 89%. A real client project for a local restaurant."
logo: "/images/projects/bubble-hideout.png"
---

### Overview

A busy restaurant counter needed one system to take orders, print receipts, track stock and report daily sales. It had to be fast with a line of customers waiting, and stock had to stay accurate without staff counting after every order. I built a POS where every completed order prints a receipt, deducts inventory and feeds the daily Excel report. It handles 50+ orders a day, and stock discrepancies dropped from about 15% to under 3%.

- **Role:** Full-stack developer: database, PHP backend, cashier screen and receipt printing
- **Timeline:** 2024
- **Built for:** A restaurant's cashiers and owner · real client project
- **Impact:** End-of-day closing time cut by 89%

### The Challenge
The restaurant needed one system for taking orders, printing receipts, tracking stock and reporting daily sales. A cashier with a line of customers waiting only cares about two things: is it fast, and does it work every time? Stock also had to stay accurate without staff counting it after every order.

### Solution & Architecture
**Data flow:** Cashier screen in the browser → PHP → MySQL, with FPDF for receipts and PhpSpreadsheet for Excel reports.

- **Cashier & orders:** Fast order entry with live pricing, customizations and split checks.
- **Inventory:** Stock deducts automatically the moment an order is completed.
- **Receipts:** Thermal receipts generated instantly with FPDF.
- **Reporting:** Daily sales export straight to Excel through PhpSpreadsheet.
- **Access control:** Role-based accounts with login history. Records are archived rather than deleted, so the audit trail stays intact.

### Results
- **50+ orders a day** handled through the system.
- **4 jobs in 1 system:** orders, receipts, inventory and sales reporting.
- **Every completed order** updates stock automatically, with no manual counting.
- **18-table MySQL database** behind the whole system.
- **120+ menu and stock items** tracked in one inventory.
- **End-of-day closing time cut by 89%**, with sales totals exported straight to Excel.
- **Stock discrepancies down from ~15% to under 3%** in monthly counts, since every sale deducts inventory.

### Key Takeaways
- Nobody cares about your tech stack if the receipt doesn't print. Reliability at the counter mattered more than any framework choice.
- Archiving instead of deleting cost almost nothing to build and made the sales history trustworthy.
