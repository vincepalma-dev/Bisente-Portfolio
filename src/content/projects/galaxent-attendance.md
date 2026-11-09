---
title: "Galaxent Attendance Portal"
date: "2024"
featured: false
client: "Galaxent Perfume"
role: "Freelance Web Developer"
skills: ["PHP", "MySQL", "JavaScript", "Bootstrap"]
related: []
outcome: "Retail attendance portal that cut timesheet discrepancies from ~5% to under 1% for 10 staff across 2 branches. A real client project for a retail business."
logo: "/images/projects/galaxent-perfume.png"
links: {}
---

### Overview

A retail business needed to track staff attendance across branches without paper time sheets. On paper, lateness and absences were hard to spot and entries were easy to get wrong. I built a portal where every clock-in gets a server timestamp and admins see each person's month on one calendar. Timesheet discrepancies fell from about 5% of entries to under 1%.

- **Role:** Sole developer: database, PHP backend and admin screens
- **Timeline:** 2024
- **Built for:** Retail staff and branch administrators · real client project
- **Impact:** About 4 hours a month saved on attendance summaries

### The Challenge
Galaxent Perfume tracked staff attendance and shifts across its retail branches on paper time sheets. Seeing who was late, absent or working overtime meant going through sheets by hand, and the monthly records were hard to keep in order.

### Solution & Architecture
**Data flow:** Staff clock in from the browser → PHP → MySQL → admin calendar view and CSV export.

- **Daily clock-in:** A simple time-logging screen that records a verified timestamp for every punch.
- **Calendar grid:** A monthly view that marks absences, on-time arrivals and overtime at a glance.
- **Admin tools:** Staff profiles, password resets and CSV exports of attendance records.

### Results
- **Up to 10 staff** clocking in through the portal.
- **Paper time sheets retired**, replaced by timestamped digital logs.
- **1 calendar view** shows a full month of attendance per person.
- **2 retail branches** on one attendance system.
- **Timesheet discrepancies cut from ~5% of entries to under 1%**, since every punch carries a server timestamp.
- **~4 hours a month** saved preparing attendance summaries.

### Key Takeaways
- For a small team, the win was not fancy features but having one trustworthy record everyone agreed on.
- A calendar view did more for the admins than any report table would have, because it matched how they already thought about shifts.
