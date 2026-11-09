---
title: "MAFI 3D Custom Clothing"
date: "2025"
featured: true
client: "Michael Anthony's Fashion Inc."
role: "Lead Capstone Developer"
skills: ["PHP", "MySQL", "JavaScript", "SVG", "Bootstrap", "PHPMailer"]
related: []
outcome: "Browser clothing customizer that cut design approval from ~3 in-person visits to 1 and remakes from ~12% to ~5%. A 12-month capstone built with a real garment manufacturer."
logo: "/images/projects/mafi-fashion.png"
---

### Overview

A garment manufacturer needed customers to specify custom clothing without slow in-person reviews and hand sketches. Sketches left cutters guessing, which led to remakes. I led a capstone that built a browser customizer with 30+ options, where each finished design becomes a production work order. Design approval dropped from about 3 visits to 1, and remakes fell from about 12% to about 5%.

- **Role:** Lead developer: system design, the customizer and the order pipeline
- **Timeline:** 12 months, 2025
- **Built for:** A garment manufacturer and its customers · academic capstone with a real client
- **Impact:** Remakes down from about 12% to about 5% of custom orders

### The Challenge
While building MAFI's invoicing tool, I watched them sketch collar cuts and sleeve patterns by hand. Customizations were reviewed in person, which was slow, and the cutters had to work from sketches, leaving room to guess. The goal was to let customers design the garment themselves and hand the cutting floor an exact specification.

### Solution & Architecture
**Data flow:** Customer designs in the browser customizer → PHP → MySQL → production work order on the cutting floor, with PHPMailer sending status updates.

- **Garment customizer:** Customers pick fabric colors, textures and trims, adjust collars and sleeves, and see the garment from different angles in the browser.
- **Order pipeline:** Each finished design becomes a production work order automatically, with no re-drawing.
- **Admin dashboard:** Fabric inventory, pricing formulas and job status in one place.
- **Customer portal:** Order tracking with automatic email updates at each stage.

### Results
- **12-month** capstone delivered with a real manufacturing client.
- **Hand sketches replaced:** customer specs reach the cutting floor as structured work orders.
- **Every order** sends automatic status emails as it moves through production.
- **17-table database** behind **100+ PHP pages**.
- **30+ customization options** across fabrics, colors, collars, sleeves and trims.
- **Design approval cut from ~3 in-person visits to 1.**
- **Remake rate down from ~12% to ~5%** of custom orders during the pilot.

### Key Takeaways
- The best project came from watching the client work. The invoicing job revealed a much bigger bottleneck.
- Client problems evolve, so the schema has to leave room for it.
