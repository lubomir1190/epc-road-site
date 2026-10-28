"""Page copy for the service and area pages — English.

"key" is the slug of the matching Bulgarian page (used for hreflang).
"""
from common import D, KG, H, PLANNED_SOFIA, PHONE, PHONE_HREF, BOOKING_URL

PRICE_SOFIA = f"""
<div class="pricing-table">
  <p class="pricing-subtitle">Tow truck — cars and SUVs up to {KG} kg</p>
  <div class="pricing-rows">
    <div class="pricing-row"><span class="pricing-label">Within Sofia city</span><span class="pricing-value">60 € <em>/ 117.35 BGN</em></span></div>
    <div class="pricing-row"><span class="pricing-label">Outside Sofia city</span><span class="pricing-value">1 € / km <em>/ 1.95 BGN</em> per direction</span></div>
  </div>
  <ul class="pricing-notes">
    <li>Price includes loading, transport and unloading</li>
    <li>Night rate (21:00 – 07:00) and public holidays <strong>+ 50%</strong></li>
    <li>Planned transport <a href="/en/car-transport/">booked online</a> <strong>− {D}%</strong></li>
  </ul>
  <p class="landing-more"><a href="/en/prices/">All prices →</a></p>
</div>"""

PRICE_OUTSIDE = f"""
<div class="pricing-table">
  <p class="pricing-subtitle">Tow truck — cars and SUVs up to {KG} kg</p>
  <div class="pricing-rows">
    <div class="pricing-row"><span class="pricing-label">Outside Sofia city</span><span class="pricing-value">1 € / km <em>/ 1.95 BGN</em> per direction</span></div>
  </div>
  <ul class="pricing-notes">
    <li>We confirm the exact price on the phone before we set off</li>
    <li>Price includes loading, transport and unloading</li>
    <li>Night rate (21:00 – 07:00) and public holidays <strong>+ 50%</strong></li>
  </ul>
  <p class="landing-more"><a href="/en/prices/">All prices →</a></p>
</div>"""

PRICE_ON_REQUEST = """
<div class="pricing-table">
  <p class="pricing-subtitle">Roadside assistance on the spot</p>
  <div class="pricing-rows">
    <div class="pricing-row"><span class="pricing-label">Price</span><span class="pricing-value">on request</span></div>
  </div>
  <ul class="pricing-notes">
    <li>Depends on location and time — we confirm it on the phone up front</li>
    <li>Night rate (21:00 – 07:00) and public holidays <strong>+ 50%</strong></li>
    <li>If the car has to be towed — within Sofia city from 60 €</li>
  </ul>
  <p class="landing-more"><a href="/en/prices/">All prices →</a></p>
</div>"""

SERVICES = [
  {
    "key": "repatrak-sofia",
    "slug": "tow-truck-sofia",
    "nav": "Tow truck Sofia",
    "title": "Tow Truck Sofia 24/7 — from 60 € | EPC Roadside Assistance",
    "description": f"24/7 tow truck in Sofia — from 60 € for cars and SUVs up to {KG} kg. Loading, transport and unloading included. Call: {PHONE}",
    "service_type": "Towing",
    "eyebrow": "Tow truck • Sofia & region • 24/7",
    "h1": "Tow truck in Sofia — 24/7, from 60 €",
    "lead": "Car won't start, had an accident, or just needs to get to a garage? We send a flatbed tow truck to wherever you are in Sofia and the region — day or night.",
    "image": ("photos/real1.webp", "EPC tow truck loading a car in Sofia"),
    "body": f"""
<h2>When you need a tow truck</h2>
<ul>
  <li>A breakdown that stops the car from going any further</li>
  <li>After an accident — when the car can't move or isn't safe to drive</li>
  <li>Seized engine, gearbox or clutch</li>
  <li>Flat tyres with no spare, or a missing wheel</li>
  <li>Moving a car to a garage, home or a new owner without driving it</li>
</ul>

<h2>How it works</h2>
<ol>
  <li>Call <a href="tel:{PHONE_HREF}">{PHONE}</a> and tell us where you are, what car it is and what happened.</li>
  <li>We give you the price and an estimated arrival time.</li>
  <li>We load the car onto the flatbed and secure it for the trip.</li>
  <li>We take it wherever you need — a garage, your home, a car park.</li>
</ol>

<h2>Driving a rental car?</h2>
<p>Most rental companies have their own assistance line — check your rental papers first. If they can't help quickly, or you'd rather arrange it yourself, call us directly.</p>

<h2>What we carry</h2>
<p>The 60 € Sofia price is for cars and SUVs up to {KG} kg. We also move motorbikes, vans and other vehicles — the price for those is agreed on the phone.</p>
<p>Not urgent? <a href="/en/car-transport/">Book online</a> and save {D}%.</p>
""",
    "price": PRICE_SOFIA,
    "faq": [
      ("How much is a tow truck in Sofia?", f"Within Sofia city — 60 € (117.35 BGN) for cars and SUVs up to {KG} kg. Outside the city — 1 € per km per direction. Between 21:00 and 07:00 and on public holidays a +50% night rate applies, e.g. 90 € instead of 60 €."),
      ("Is loading charged separately?", "No. The price includes loading, transport and unloading."),
      ("How fast will the tow truck arrive?", "It depends on where you are and on traffic. We give you an estimated arrival time when you call."),
    ],
  },
  {
    "key": "podavane-na-tok",
    "slug": "jump-start",
    "nav": "Jump start",
    "title": "Car Jump Start in Sofia 24/7 — Flat Battery Help | EPC",
    "description": f"Car won't start? We come to you anywhere in Sofia and the region and jump-start your battery — 24/7. If it still won't start, we tow it to a garage. {PHONE}",
    "service_type": "Battery jump start",
    "eyebrow": "Roadside assistance • Sofia & region • 24/7",
    "h1": "Battery jump start — Sofia, 24/7",
    "lead": "A cold morning, lights left on, or an old battery — and the car won't start. We come to you and jump-start it so you can get going.",
    "image": None,
    "body": f"""
<h2>Signs of a flat battery</h2>
<ul>
  <li>The starter clicks but the engine doesn't turn over</li>
  <li>Dashboard and lights are dim or dead</li>
  <li>Central locking doesn't respond</li>
  <li>The car has been parked for a long time, especially in the cold</li>
</ul>

<h2>While you wait</h2>
<ul>
  <li>Switch off the headlights, air conditioning, radio and anything else that draws power.</li>
  <li>Don't keep trying to start the engine — it drains the battery further.</li>
  <li>On a busy street, switch on the hazard lights and put out the warning triangle.</li>
</ul>

<h2>If it still won't start</h2>
<p>Sometimes the problem isn't the battery but the starter, the alternator or the electrics. Then we can load the car onto the <a href="/en/tow-truck-sofia/">tow truck</a> and take it to a garage — no need to wait for a second vehicle.</p>
""",
    "price": PRICE_ON_REQUEST,
    "faq": [
      ("How much is a jump start?", "It depends on location and time — we confirm the price on the phone up front."),
      ("What if the battery is completely dead?", "A jump start works in most cases. If the battery won't hold a charge or the fault is elsewhere, we can tow the car to a garage."),
      ("Do you come out at night?", "Yes, 24/7, including weekends and public holidays. A +50% night rate applies between 21:00 and 07:00."),
    ],
  },
  {
    "key": "smyana-na-guma",
    "slug": "flat-tyre",
    "nav": "Flat tyre",
    "title": "Flat Tyre Help in Sofia 24/7 — Roadside Tyre Change | EPC",
    "description": f"Flat tyre in Sofia, on the Ring Road or the motorway? We fit your spare on the spot or tow the car to a tyre shop. 24/7: {PHONE}",
    "service_type": "Roadside tyre change",
    "eyebrow": "Roadside assistance • Sofia & region • 24/7",
    "h1": "Flat tyre help — Sofia, 24/7",
    "lead": "Flat tyre on a boulevard, the Ring Road or the motorway? We come out and fit your spare — or tow the car to a tyre shop if there isn't one.",
    "image": ("photos/real14.webp", "EPC tow truck loading a car on the motorway"),
    "body": """
<h2>When not to change it yourself</h2>
<ul>
  <li>On the motorway or a narrow hard shoulder, with traffic right next to you</li>
  <li>When the jack or wheel brace is missing, or the bolts are stuck</li>
  <li>In the dark, in the rain or on ice</li>
</ul>

<h2>No spare wheel?</h2>
<p>Many newer cars come with only a repair kit, or nothing at all. If the tyre can't be fixed on the spot, we load the car onto the <a href="/en/tow-truck-sofia/">tow truck</a> and take it to a tyre shop or any address you choose.</p>
<p>If the car is missing a wheel, loading costs an extra 50 € (97.79 BGN) per wheel.</p>

<h2>On the motorway</h2>
<p>While you wait, stand behind the crash barrier wearing a hi-vis vest — not next to the car. More tips on our <a href="/en/motorway-breakdown/">motorway breakdown</a> page.</p>
""",
    "price": PRICE_ON_REQUEST,
    "faq": [
      ("How much is a roadside tyre change?", "It depends on location and time — we confirm the price on the phone up front."),
      ("Do you change tyres on the motorway?", "Yes — on A1 Trakia, A2 Hemus and the Sofia Ring Road."),
      ("What if I have no spare wheel?", "We tow the car to a tyre shop or any address you choose."),
    ],
  },
  {
    "key": "transport-na-avtomobil",
    "slug": "car-transport",
    "nav": "Car transport",
    "title": f"Car Transport in Sofia — {D}% Off When Booked Online | EPC",
    "description": f"Car transport to a garage, home or new owner in Sofia and the region. Book online at least {H} hours ahead and get {D}% off.",
    "service_type": "Car transport",
    "eyebrow": "Planned transport • Book online",
    "h1": f"Car transport — plan ahead and save {D}%",
    "lead": f"The car hasn't broken down, but it needs to get somewhere: to a garage, home, or to its new owner. Book a day and time online at least {H} hours ahead and get {D}% off.",
    "image": ("photos/real18.webp", "EPC tow truck transporting a Ford Mustang sports car"),
    "booking": True,
    "body": f"""
<h2>When it makes sense</h2>
<ul>
  <li>Taking a car to a garage for repairs or diagnostics</li>
  <li>A car you've just bought — from the seller to you or to a garage</li>
  <li>A car that has been parked for a long time and isn't roadworthy</li>
  <li>A sports, classic or lowered car you'd rather not drive in traffic</li>
  <li>Moving a car between two addresses</li>
</ul>

<h2>How booking works</h2>
<ol>
  <li>Pick a day and time in our <a href="{BOOKING_URL}" target="_blank" rel="noopener">online calendar</a>.</li>
  <li>Enter the pick-up and drop-off addresses and the make and model of the car.</li>
  <li>We arrive at the agreed time.</li>
</ol>

<h2>Conditions</h2>
<ul>
  <li>Cars and SUVs up to {KG} kg</li>
  <li>Book at least {H} hours ahead</li>
  <li>The discount is for planned transport only. In an emergency, call <a href="tel:{PHONE_HREF}">{PHONE}</a>.</li>
</ul>
<p>For example, planned transport within Sofia city costs {PLANNED_SOFIA} € instead of 60 €.</p>
""",
    "price": PRICE_SOFIA,
    "faq": [
      ("Can I book for the same day?", f"Online bookings need at least {H} hours' notice. For urgent transport, call us — the standard price applies."),
      ("Do you transport cars outside Sofia?", "Yes. The price for the distance is confirmed when you book or on the phone."),
      ("What is the discount?", f"{D}% off planned transport of cars and SUVs up to {KG} kg, booked online at least {H} hours ahead."),
    ],
  },
  {
    "key": "patna-pomosht-magistrala",
    "slug": "motorway-breakdown",
    "nav": "Motorway breakdown",
    "title": "Motorway Breakdown — Trakia, Hemus & Sofia Ring Road 24/7 | EPC",
    "description": f"Broken down on A1 Trakia, A2 Hemus or the Sofia Ring Road? 24/7 tow truck and roadside assistance, plus what to do while you wait. {PHONE}",
    "service_type": "Motorway roadside assistance",
    "eyebrow": "Motorways • A1 • A2 • Sofia Ring Road",
    "h1": "Motorway breakdown and Ring Road assistance",
    "lead": "Breaking down on the motorway is dangerous. We cover the Sofia Ring Road, A1 Trakia (Sofia section) and A2 Hemus to Botevgrad — 24/7.",
    "image": ("photos/real7.webp", "EPC roadside assistance on the motorway"),
    "body": f"""
<h2>What to do straight away</h2>
<ol>
  <li>Pull over as far right as you can — onto the hard shoulder or the verge.</li>
  <li>Switch on the hazard lights and put on your hi-vis vest before getting out.</li>
  <li>Place the warning triangle behind the car.</li>
  <li>Get out on the right-hand side and wait behind the crash barrier with your passengers.</li>
  <li>If anyone is hurt, call 112 first — the EU emergency number works in Bulgaria and operators speak English.</li>
  <li>Then call us on <a href="tel:{PHONE_HREF}">{PHONE}</a> and tell us your direction of travel and the nearest landmark.</li>
</ol>

<h2>How to tell us where you are</h2>
<p>On the motorway your “address” is the direction and the kilometre. Look for the kilometre markers by the road, or remember the last exit or petrol station you passed. You can also share your location from your phone.</p>

<h2>Roads we cover</h2>
<ul>
  <li>Sofia Ring Road — the full circuit</li>
  <li>A1 Trakia Motorway — the Sofia section, towards Plovdiv</li>
  <li>A2 Hemus Motorway — from Sofia to <a href="/en/roadside-assistance-botevgrad/">Botevgrad</a></li>
</ul>
""",
    "price": PRICE_OUTSIDE,
    "faq": [
      ("How much is towing from the motorway?", "Outside Sofia city it's 1 € per km per direction. We confirm the exact price on the phone before we set off."),
      ("Should I stay in the car while I wait?", "Not on the motorway. The safest place is behind the crash barrier, away from moving traffic."),
      ("Do you work on the motorway at night?", "Yes, 24/7, including weekends and public holidays."),
    ],
  },
  {
    "key": "ceni",
    "slug": "prices",
    "nav": "Prices",
    "title": "Tow Truck & Roadside Assistance Prices in Sofia | EPC",
    "description": f"Tow truck prices in Sofia: 60 € in the city, 1 €/km outside. Night rate, missing wheel, −{D}% for planned transport. No hidden fees.",
    "service_type": "Roadside assistance and towing",
    "eyebrow": "Prices • 2026",
    "h1": "Tow truck and roadside assistance prices",
    "lead": "We tell you the price before we set off. Loading and unloading are included — no hidden fees.",
    "image": None,
    "body": f"""
<h2>Price list</h2>
<div class="pricing-table">
  <p class="pricing-subtitle">Tow truck — cars and SUVs up to {KG} kg</p>
  <div class="pricing-rows">
    <div class="pricing-row"><span class="pricing-label">Within Sofia city</span><span class="pricing-value">60 € <em>/ 117.35 BGN</em></span></div>
    <div class="pricing-row"><span class="pricing-label">Outside Sofia city</span><span class="pricing-value">1 € / km <em>/ 1.95 BGN</em> per direction</span></div>
    <div class="pricing-row"><span class="pricing-label">Missing wheel</span><span class="pricing-value">+ 50 € <em>/ 97.79 BGN</em> per wheel</span></div>
    <div class="pricing-row"><span class="pricing-label">Night rate (21:00 – 07:00) and public holidays</span><span class="pricing-value">+ 50%</span></div>
    <div class="pricing-row"><span class="pricing-label">Planned transport booked online</span><span class="pricing-value">− {D}%</span></div>
  </div>
  <div class="pricing-rows">
    <div class="pricing-row"><span class="pricing-label">Jump start, tyre change</span><span class="pricing-value">on request</span></div>
    <div class="pricing-row"><span class="pricing-label">Motorbikes, vans and other vehicles</span><span class="pricing-value">on request</span></div>
  </div>
</div>

<h2>Example prices within Sofia city</h2>
<ul>
  <li>Daytime — 60 €</li>
  <li>Night (21:00 – 07:00) or public holiday — 90 €</li>
  <li>Planned transport <a href="/en/car-transport/">booked online</a> — {PLANNED_SOFIA} €</li>
</ul>

<h2>What affects the price</h2>
<ul>
  <li>Distance — outside Sofia city it's charged per kilometre</li>
  <li>Time — night rate between 21:00 and 07:00 and on public holidays</li>
  <li>The vehicle — prices are for cars and SUVs up to {KG} kg</li>
  <li>Its condition — for example a missing wheel</li>
</ul>
<p>Prices are in euro; BGN amounts are shown for reference. We confirm the final price on the phone before we set off.</p>
""",
    "price": "",
    "faq": [
      ("Are there hidden fees?", "No. The price includes loading, transport and unloading, and we tell you up front."),
      ("How can I pay?", "Cash or card."),
      ("How much is a tow truck at night?", "Between 21:00 and 07:00 and on public holidays +50% applies — 90 € within Sofia city."),
    ],
  },
]

AREAS = [
  {
    "key": "patna-pomosht-lyulin",
    "slug": "roadside-assistance-lyulin",
    "nav": "Lyulin",
    "place": "Lyulin",
    "kind": "district",
    "title": "Roadside Assistance & Tow Truck Lyulin, Sofia — 24/7 | EPC",
    "description": f"Roadside assistance in Lyulin, Sofia, 24/7: tow truck from 60 €, jump start, flat tyre help. Lyulin 1–10 and nearby. Call: {PHONE}",
    "h1": "Roadside assistance in Lyulin — 24/7",
    "lead": "Tow truck, jump start and flat tyre help across Lyulin 1–10 and the neighbouring districts. We come to you — outside your block, in the car park or on the boulevard.",
    "body": """
<h2>Roadside assistance in Lyulin</h2>
<p>Lyulin is one of Sofia's largest districts, with busy boulevards such as Tsaritsa Yoanna, Dzhavaharlal Neru and Slivnitsa, and quick access to the Ring Road and the Lyulin motorway towards Pernik. If your car breaks down here, tell us the block number, the street or the nearest landmark — a bus stop, a shop or a junction.</p>
""",
    "faq": [
      ("How much is towing from Lyulin to a garage in another district?", "Within Sofia city — 60 €. Between 21:00 and 07:00 and on public holidays a +50% night rate applies."),
      ("Do you work in Lyulin at night?", "Yes, 24/7, including weekends and public holidays."),
    ],
  },
  {
    "key": "patna-pomosht-mladost",
    "slug": "roadside-assistance-mladost",
    "nav": "Mladost",
    "place": "Mladost",
    "kind": "district",
    "title": "Roadside Assistance & Tow Truck Mladost, Sofia — 24/7 | EPC",
    "description": f"Roadside assistance in Mladost 1–4 and Business Park Sofia: tow truck from 60 €, jump start, flat tyre help — 24/7. Call: {PHONE}",
    "h1": "Roadside assistance in Mladost — 24/7",
    "lead": "Tow truck, jump start and flat tyre help in Mladost 1, 1A, 2, 3 and 4 and at Business Park Sofia — 24/7.",
    "body": """
<h2>Roadside assistance in Mladost</h2>
<p>Mladost sits between Tsarigradsko Shose and the Ring Road, with Aleksandar Malinov and Andrey Saharov as its main boulevards. We also come out to office car parks in Business Park Sofia, to shops and to the street outside your home. If the car won't start after work, tell us the building and exactly where it's parked.</p>
""",
    "faq": [
      ("Do you come to Business Park Sofia?", "Yes. Tell us the building and where exactly the car is parked."),
      ("How much is a tow truck in Mladost?", "Within Sofia city — 60 €. Between 21:00 and 07:00 and on public holidays a +50% night rate applies."),
    ],
  },
  {
    "key": "patna-pomosht-nadezhda",
    "slug": "roadside-assistance-nadezhda",
    "nav": "Nadezhda",
    "place": "Nadezhda",
    "kind": "district",
    "title": "Roadside Assistance & Tow Truck Nadezhda, Sofia — 24/7 | EPC",
    "description": f"Roadside assistance in Nadezhda 1–4, Svoboda and Tolstoy: tow truck from 60 €, jump start, flat tyre help — 24/7. Call: {PHONE}",
    "h1": "Roadside assistance in Nadezhda — 24/7",
    "lead": "Tow truck, jump start and flat tyre help in Nadezhda 1–4 and the neighbouring Svoboda and Tolstoy districts.",
    "body": """
<h2>Roadside assistance in Nadezhda</h2>
<p>Nadezhda is in the north of Sofia, around Lomsko Shose and Rozhen boulevards, with quick access to the Northern Speed Tangent. From here we can easily reach the garages in the industrial areas north of the city. Tell us the street, the block or the nearest landmark and we're on our way.</p>
""",
    "faq": [
      ("How much is a tow truck in Nadezhda?", "Within Sofia city — 60 €. Between 21:00 and 07:00 and on public holidays a +50% night rate applies."),
      ("Do you work in Nadezhda at night?", "Yes, 24/7, including weekends and public holidays."),
    ],
  },
  {
    "key": "patna-pomosht-bankya",
    "slug": "roadside-assistance-bankya",
    "nav": "Bankya",
    "place": "Bankya",
    "kind": "town",
    "title": "Roadside Assistance & Tow Truck Bankya — 24/7 | EPC",
    "description": f"Roadside assistance in Bankya, Ivanyane and Klisura: tow truck, jump start, flat tyre help — 24/7. We take the car to Sofia or a garage. {PHONE}",
    "h1": "Roadside assistance in Bankya — 24/7",
    "lead": "Tow truck, jump start and flat tyre help in Bankya and nearby Ivanyane and Klisura. We take the car to a garage in Bankya, in Sofia, or any address you choose.",
    "body": """
<h2>Roadside assistance in Bankya</h2>
<p>Bankya is about 17 km west of central Sofia and is part of Sofia Municipality. We get there via the Ring Road and Ivanyane, and cover both the road to Sofia and the streets of the town itself — just tell us the street or the nearest landmark.</p>
""",
    "faq": [
      ("How much is towing from Bankya to Sofia?", "Outside Sofia city it's 1 € per km per direction. We confirm the exact price on the phone before we set off."),
      ("Do you come to Bankya at night?", "Yes, 24/7, including weekends and public holidays."),
    ],
  },
  {
    "key": "patna-pomosht-kostinbrod",
    "slug": "roadside-assistance-kostinbrod",
    "nav": "Kostinbrod",
    "place": "Kostinbrod",
    "kind": "town",
    "title": "Roadside Assistance & Tow Truck Kostinbrod — 24/7 | EPC",
    "description": f"Roadside assistance in Kostinbrod and on the Sofia – Slivnitsa road: tow truck, jump start, flat tyre help — 24/7. Call: {PHONE}",
    "h1": "Roadside assistance in Kostinbrod — 24/7",
    "lead": "Tow truck, jump start and flat tyre help in Kostinbrod, the surrounding villages and on the road from Sofia to Slivnitsa.",
    "body": """
<h2>Roadside assistance in Kostinbrod</h2>
<p>Kostinbrod is about 20 km north-west of Sofia, on the E80 towards Slivnitsa and the Kalotina border crossing. The road carries a lot of heavy goods traffic, so if you break down, get out of the car and wait somewhere safe. We also cover nearby Bozhurishte and <a href="/en/roadside-assistance-bankya/">Bankya</a>.</p>
""",
    "faq": [
      ("How much is towing from Kostinbrod to Sofia?", "Outside Sofia city it's 1 € per km per direction. We confirm the exact price on the phone before we set off."),
      ("Do you cover the road to Slivnitsa?", "Yes — Kostinbrod, Bozhurishte, Slivnitsa and the road between them."),
    ],
  },
  {
    "key": "patna-pomosht-samokov",
    "slug": "roadside-assistance-samokov-borovets",
    "nav": "Samokov & Borovets",
    "place": "Samokov",
    "kind": "town",
    "title": "Roadside Assistance & Tow Truck Samokov and Borovets — 24/7 | EPC",
    "description": f"Car trouble on the way to Borovets? Roadside assistance in Samokov, Borovets and on the Sofia – Samokov road: tow truck, jump start — 24/7. {PHONE}",
    "h1": "Roadside assistance in Samokov and Borovets",
    "lead": "Tow truck, jump start and flat tyre help in Samokov, Borovets and on the road from Sofia via Pancharevo and past the Iskar reservoir.",
    "body": """
<h2>Roadside assistance in Samokov</h2>
<p>Samokov is about 55 km from Sofia on road II-82, via Pancharevo and along the Iskar reservoir. It's a winding mountain road that is often snow-covered in winter.</p>

<h2>Ski season in Borovets</h2>
<p>Borovets is just 10 km from Samokov. In winter the most common problems are batteries drained after a cold night, cars stuck in snow, and cars without winter tyres or chains. If your car won't start in the morning in Borovets, call us — we can <a href="/en/jump-start/">jump-start it</a> or bring it down to Sofia on the tow truck.</p>
""",
    "faq": [
      ("How much is towing from Samokov to Sofia?", "Outside Sofia city it's 1 € per km per direction. We confirm the exact price on the phone before we set off."),
      ("Do you come up to Borovets?", "Yes, we cover Samokov, Borovets and the road to Sofia."),
    ],
  },
  {
    "key": "patna-pomosht-botevgrad",
    "slug": "roadside-assistance-botevgrad",
    "nav": "Botevgrad",
    "place": "Botevgrad",
    "kind": "town",
    "title": "Roadside Assistance & Tow Truck Botevgrad and Hemus — 24/7 | EPC",
    "description": f"Roadside assistance in Botevgrad, Pravets and on the A2 Hemus motorway through the Vitinya pass: tow truck, jump start — 24/7. {PHONE}",
    "h1": "Roadside assistance in Botevgrad and on Hemus",
    "lead": "Tow truck, jump start and flat tyre help in Botevgrad, Pravets and on the Hemus motorway between Sofia and Botevgrad.",
    "body": """
<h2>Roadside assistance in Botevgrad</h2>
<p>Botevgrad is about 60 km from Sofia on the A2 Hemus motorway, through the Vitinya pass. The stretch with the tunnels and gradients is hard work for engines and brakes. If you break down in a tunnel, follow the signs and call 112 if you're in danger.</p>
<p>We also cover nearby Pravets. More on what to do in a <a href="/en/motorway-breakdown/">motorway breakdown</a>.</p>
""",
    "faq": [
      ("How much is towing from Botevgrad to Sofia?", "Outside Sofia city it's 1 € per km per direction. We confirm the exact price on the phone before we set off."),
      ("Do you help on Hemus towards Botevgrad?", "Yes — along the whole stretch from Sofia to Botevgrad."),
    ],
  },
  {
    "key": "patna-pomosht-elin-pelin",
    "slug": "roadside-assistance-elin-pelin",
    "nav": "Elin Pelin",
    "place": "Elin Pelin",
    "kind": "town",
    "title": "Roadside Assistance & Tow Truck Elin Pelin — 24/7 | EPC",
    "description": f"Roadside assistance in Elin Pelin, Lesnovo and Ravno Pole: tow truck, jump start, flat tyre help — 24/7. Call: {PHONE}",
    "h1": "Roadside assistance in Elin Pelin — 24/7",
    "lead": "Tow truck, jump start and flat tyre help in Elin Pelin and the villages around it — Lesnovo, Ravno Pole and nearby.",
    "body": """
<h2>Roadside assistance in Elin Pelin</h2>
<p>Elin Pelin is about 25 km east of Sofia, close to the A1 Trakia motorway. As well as the town itself, we work in the industrial areas and warehouses on the way to Sofia. If you need a car taken to a garage in Sofia and it isn't urgent, <a href="/en/car-transport/">book online</a> and save.</p>
""",
    "faq": [
      ("How much is towing from Elin Pelin to Sofia?", "Outside Sofia city it's 1 € per km per direction. We confirm the exact price on the phone before we set off."),
      ("Do you work in Elin Pelin at night?", "Yes, 24/7, including weekends and public holidays."),
    ],
  },
]

AREA_SERVICES = """
<h2>What we do in {place}</h2>
<ul>
  <li><a href="/en/tow-truck-sofia/">Tow truck</a> — after a breakdown, an accident, or to a garage</li>
  <li><a href="/en/jump-start/">Jump start</a> when the car won't start</li>
  <li><a href="/en/flat-tyre/">Flat tyre help</a> on the spot</li>
  <li><a href="/en/car-transport/">Planned transport</a> with {d}% off when booked online</li>
</ul>
"""

PREPARE = """
<h2>Before you call, have ready</h2>
<ol>
  <li>Your exact location or a landmark</li>
  <li>The make and model of the car</li>
  <li>What the problem is</li>
  <li>Where the car needs to go</li>
</ol>
"""
