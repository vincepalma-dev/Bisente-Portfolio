---
title: "Tax Leaders Circle PH"
date: "2026"
featured: true
client: "Gamma Oracle Dimension Inc. (for TLCPH)"
role: "Software Engineering Intern (Built with developer friend)"
skills: ["PHP", "Laravel", "Vue.js", "MySQL", "JavaScript", "PDF.js", "FPDF"]
related: []
outcome: "Learning portal for tax professionals that has issued 500+ certificates automatically, saving ~80 staff hours. A real client project co-built with 1 other intern."
logo: "/images/projects/tlcph.png"
shot: "/images/projects/shots/tlcph.jpg"
links: { live: "https://tlcph.online/" }
---

### Overview

A tax professionals' community needed a portal for seminars, publications and accreditation certificates that people could verify. Certificates had to be exact and trustworthy, and there were two developers and four months to ship. With 1 other intern, I built the portal; my parts were the certificate generator, the flip-book library and the seminar admin. It has issued 500+ certificates, saving about 80 staff hours.

- **Role:** Developer intern, co-built with 1 other intern. I owned the certificate generator, flip-book library and seminar admin
- **Timeline:** 4 months, February to June 2026
- **Built for:** Philippine tax professionals · real client project
- **Impact:** 500+ certificates, each generated in under 3 seconds

### The Challenge
Tax Leaders Circle PH needed a learning portal for Philippine tax professionals: courses, a digital library and seminar sign-ups. Attendees needed accreditation certificates that could be verified as genuine. We had two developers and four months to get it live.

### Solution & Architecture
**Data flow:** Vue.js frontend → Laravel → MySQL, with FPDI / FPDF rendering certificates and PHPMailer delivering them.

- **Certificate studio:** Generates accreditation certificates with verifiable signatures and pixel-exact text placement using FPDI and FPDF.
- **Tax library:** A flip-book reader for publications built on Turn.js and PDF.js.
- **Seminar admin:** Reservation management, attendee verification and lesson categories.
- **Notifications:** Seminar confirmations and certificates emailed automatically through PHPMailer.

### Results
- **Live at [tlcph.online](https://tlcph.online/)**, shipped in **4 months** by **2 developers**.
- **3 core modules** delivered: certificate studio, tax library and seminar admin.
- **30+ database tables** behind the portal.
- **Every certificate** is generated and emailed automatically, with no manual layout work.
- **500+ certificates** generated and emailed automatically.
- **~80 staff hours saved**, at about 10 minutes per certificate by hand.
- **20+ seminars** managed through the admin.
- **Under 3 seconds** to generate and send each certificate.

### Key Takeaways
- Building as a pair taught me to split work along clear module boundaries and agree on interfaces early.
- Certificates carry a professional's accreditation, so exact layout and verifiable signatures mattered as much as the features.
