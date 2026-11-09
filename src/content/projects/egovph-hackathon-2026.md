---
title: "eGovPH National Hackathon 2026"
date: "2026"
featured: true
event: true
client: "DICT - eGovPH Hackathon (SMX Aura, BGC)"
role: "Team 'Println New Gen' Lead / Developer"
skills: ["React", "APIs", "Cybersecurity", "Identity & SSO", "Civic Tech"]
related: []
outcome: "Civic-tech prototype built in 48 hours on 3 government APIs, letting citizens reach local government services with a verified digital ID. A hackathon project built with a 5-member team."
links: {}
---

### Overview

Citizens need a way to reach local government services without proving who they are in person every time. The challenge was building it in 48 hours on the government's own sandbox APIs. Our team built a prototype where citizens sign in with eGov SSO, get verified through eVerify and pay fees through eGovPay. We shipped a working demo on 3 live government APIs within the 48 hours.

- **Role:** Team lead and developer: led the 5-member team and built the sign-in and identity verification flows
- **Timeline:** 48 hours, July 2026
- **Built for:** Filipino citizens and local government offices · hackathon prototype
- **Impact:** Working demo on 3 government sandbox APIs in 48 hours

### The Challenge
Build a working civic-tech product in 48 hours on the government's own developer infrastructure: the eGov Single Sign-On, eVerify and eGovPay APIs. Our focus was public verification, connecting citizens to local government services using a verified digital ID.

### Solution & Architecture
**Data flow:** Web app → eGov SSO for sign-in → eVerify to confirm identity → local government service request, with eGovPay for fees.

- **Sign-in:** Citizens log in through eGov SSO instead of creating yet another account.
- **Identity verification:** eVerify confirms the person before a request reaches the government office.
- **Working prototype:** A deployed web interface calling live sandbox endpoints, not slides.

### Results
- **Working prototype in 48 hours**, built on **3 live government sandbox APIs**.
- **5-member team** coordinated from idea to demo.
- We didn't take the championship. That went to Bryl Lim's team for their fact-checking AI, *Tunai*.

### Key Takeaways
- Two days of building under real pressure taught us more than months of reading. With no time to spare, you cut everything that doesn't solve the problem in front of you.
- The people were half the value. We finally met people we'd only watched on screen: we talked with **Bryl Lim** and took photos with **Boss Rod** (*Code with Boss Rod*).

### Photo Gallery

<div class="carousel-wrapper" id="egov-gallery">
  <div class="carousel-header-bar">
    <div class="carousel-status">
      <span class="status-indicator"></span>
      <span class="carousel-counter" id="carousel-count">6 Photos • Swipe or click arrows</span>
    </div>
    <div class="carousel-arrows">
      <button type="button" class="arrow-btn" id="prev-slide" aria-label="Previous photo">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
      <button type="button" class="arrow-btn" id="next-slide" aria-label="Next photo">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
    </div>
  </div>
  <div class="carousel-track" id="gallery-track" tabindex="0" role="region" aria-label="eGovPH Hackathon 2026 Photo Gallery">
    <figure class="carousel-card"><div class="img-frame"><img src="/images/hackathons/egovph-2026/team-backdrop.jpg" alt="Team Println New Gen at eGovPH Hackathon 2026 stage" loading="lazy" /></div><figcaption>Team Println New Gen at the official eGovPH stage</figcaption></figure>
    <figure class="carousel-card"><div class="img-frame"><img src="/images/hackathons/egovph-2026/with-bryl-lim.jpg" alt="Team with AI engineer Bryl Lim" loading="lazy" /></div><figcaption>With tech idol Bryl Lim</figcaption></figure>
    <figure class="carousel-card"><div class="img-frame"><img src="/images/hackathons/egovph-2026/with-boss-rod.png" alt="With Code with Boss Rod" loading="lazy" /></div><figcaption>With Boss Rod (Code with Boss Rod)</figcaption></figure>
    <figure class="carousel-card"><div class="img-frame"><img src="/images/hackathons/egovph-2026/badges.jpg" alt="Hackathon Participant Badges - Vince, Julius, Adrian" loading="lazy" /></div><figcaption>Our official DICT eGovPH delegate badges</figcaption></figure>
    <figure class="carousel-card"><div class="img-frame"><img src="/images/hackathons/egovph-2026/hall-session.jpg" alt="Auditorium hall at SMX Aura BGC" loading="lazy" /></div><figcaption>In the SMX Aura main auditorium</figcaption></figure>
    <figure class="carousel-card"><div class="img-frame"><img src="/images/hackathons/egovph-2026/smart-cards.jpg" alt="Futuristic collectible NFC badges" loading="lazy" /></div><figcaption>Commemorative NFC badges from the event</figcaption></figure>
  </div>
</div>
