# Build notes — news-image-20261126

Front page: **THE WORLD TODAY — Thursday 26 November 2026**.
40 stories (1 lead + 39), 7 regions. Rendered deterministically with
Python PIL from `stories.json` via `render.py`; `main.py` is the entrypoint.

## How the date was verified

Every story below was checked against a live source on 26 Nov 2026 (WIB)
and was reported that day in at least one time zone. Where an event
happened on the evening of 25 Nov in the Americas, it was first reported
on 26 Nov in Asia-Pacific time zones — the competition's own rule counts
events that happened, or were first reported, on 26 Nov in any time zone.
No headline, quote or figure was invented; casualty figures use the
source's own "at least" wording.

## Sources (story → source, as found 26 Nov 2026)

Lead — US tariffs on 14 economies: Reuters (26 Nov, "US proposes new
tariffs aimed at factory overcapacity"; "Trump administration set to unveil
new tariffs after probe"), AP ("US plans to hike tariffs on China, EU,
Brazil and others"), BBC (26 Nov video explainer, Jonathan Josephs).

Asia-Pacific
- Bank of Korea 3.25%: Reuters, 26 Nov ("BOK raises base rate by 25 bps
  to 3.25%").
- Asia shares bounce: Reuters, 26 Nov ("Asia shares bounce, AI and
  tariffs lurk in background").
- China / Nvidia chips: Reuters world news summary, 26 Nov ("How China got
  access to Nvidia's AI chips despite rules to stop them").
- Japan data-centre revolt: Reuters via BusinessWorld, 26 Nov ("Japan's
  data center boom faces growing revolt from urban residents").
- Java gold mine, 13 dead / 13 trapped: Reuters, 26 Nov.
- Roo-ver radiation tests: electronicsonline.net.au, 26 Nov 2026.

South Asia
- Bangladesh garment wage +36% to Tk17,000: AP, 25 Nov (reported 26 Nov
  by Reuters / National Herald / BusinessWorld lists); workers demanded
  more, factories had shut in protests.
- Bangladesh typhoid drive, 50m children: Access24, 26 Nov.
- Uber India/South Asia chief: Reuters, 26 Nov (Rakesh Ranjan, from
  4 Jan 2027).
- Tamil Nadu lamp row: CuriousCats breaking-news digest, 26 Nov 00:28 UTC.
- Shenzhou-24 / Pakistani astronaut: BusinessWorld Reuters list, 26 Nov
  ("China's Shenzhou-24 docks at space station with Pakistani national as
  first foreign astronaut"); launch 25 Nov, docking reported 26 Nov.

Middle East
- Houthi refinery claim + oil: Reuters, 26 Nov ("Oil rises on supply
  concerns as Iran claims mine strikes on ships"); IBC Global Times, 26 Nov.
- Iran tankers / mines: Reuters, 26 Nov (same story).
- Netanyahu judges: BBC/Jabulani/IBC, 26 Nov ("Israeli judges recommend
  dropping most serious charges against Netanyahu").
- Knesset 7 October inquiry: lamediterranee.eu global news, 26 Nov 03:36.
- Riyadh tower drone, 11 wounded: Reuters Gulf Currents, 26 Nov.
- Hamas official killed, Gaza City: Jabulani Radio top international
  news, 26 Nov.

Europe
- Poland / NATO missiles: lamediterranee.eu, 26 Nov 02:26 / 03:20.
- NATO chief war warning: lamediterranee.eu, 26 Nov 03:05.
- Ukraine air-base strike, 5 planes: Reuters world news summary, 26 Nov;
  Samara refineries: lamediterranee.eu, 26 Nov 03:20.
- Murmansk governor detained: Reuters world news summary, 26 Nov.
- Spain TikTok probe: Nexus Europa, 26 Nov 02:30 UTC.
- Andy Taylor dies, 65: The Business Standard, 26 Nov 08:00 ("died aged
  65 on Monday 23 November … statement released Wednesday 25 November");
  AP, 26 Nov. The death was announced 25 Nov; he died 23 Nov.
- Sinner knee surgery: BusinessWorld Reuters list, 26 Nov ("Sinner set
  for extended spell on sidelines after knee surgery").

Africa
- Cairo tanker fire, at least 30 dead: BBC/Jabulani, 26 Nov ("Thirty-one
  killed in massive fire as fuel tanker crashes on Cairo highway"); IBC,
  26 Nov (at least 30). Image uses "at least 30".
- Nigeria militants, at least 30 killed: Reuters, 25 Nov 18:40 UTC
  (26 Nov in Pacific time zones).
- Kenya cult leader convicted: Reuters, 25 Nov (Paul Mackenzie, new
  child-cruelty counts; 200-year sentence already imposed).
- Nigeria $227m meth seizure: Reuters, 25 Nov 12:44 UTC.
- Tinubu / Borno: Reuters, 25 Nov.
- OECD/AU Africa debt: Reuters, 25 Nov.

North America
- Macy's parade postponed: azcentral / The Traveler, 26 Nov (100th
  parade moved to Saturday, first postponement in its history).
- Nor'easter + king tides: USA Today, 25–26 Nov (Thanksgiving Day storm;
  record tides in California/Oregon).
- Iowa lead-azide blast: BusinessWorld Reuters, 26 Nov 09:00 ("US Army
  declares success in detonation of lead-based explosives stockpile in
  Iowa"); CuriousCats, 26 Nov 00:51 UTC.
- Birthright order blocked (2nd judge): Reuters world news summary,
  26 Nov.
- FCC / SpaceX Starmind, 1m satellites: The Hindu BusinessLine, 26 Nov;
  Breitbart, 25 Nov (FCC announcement Wednesday); The Neuron AI digest,
  26 Nov.

Latin America
- Colombia hostages rescued (~30): lamediterranee.eu, 26 Nov 03:28.
- Colombia bomb, 23 hurt: lamediterranee.eu, 26 Nov.
- Ecuador / US talks: Reuters world news summary, 26 Nov.
- Peru ports closed: sangaku-journal.eu, 26 Nov 02:46.

## Render checks

- 1024×1024 PNG, target < 1 MiB (aim 600–850 KiB).
- Run `python3 main.py` twice with OUTPUT_PATH set; sha256 must match.
- Read the PNG back and check every headline: no overflow, no cut-off
  words, date reads "THURSDAY 26 NOVEMBER 2026" in the masthead.
