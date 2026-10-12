---
name: animated-resume
description: Turn someone's resume into an animated, interactive one-page profile (game-style career levels, animated avatar, "why hire me", projects graph, personality section). Use when the user asks for an animated, interactive or gamified resume, CV, portfolio or profile page.
---

# Animated Resume

This skill turns a resume into a single, self-contained HTML page with:

- a hero with an animated illustrated avatar (blinks, types, waves, speech bubbles), a typing headline and an XP bar
- "achievements unlocked" counters
- the career as numbered **levels** on a rail that lights up while scrolling, each role unlocking a skill
- an optional stack-evolution timeline
- "why hire me" cards backed by proof
- an optional character sheet: an animated scene (sunrise, breathing exercise) and personality "perks"
- an optional projects section with an interactive project ↔ technology graph
- skills, education, languages, certificates and contact
- optional language toggle (EN/DE built in, any language possible)
- a drifting particle background, scroll reveals, 3D card tilt, reduced-motion support

The page is generated from one `profile.json` file. You never edit the template by hand: you interview the user, write `profile.json`, and run the build script.

```
animated-resume/
├── SKILL.md                    ← this file
├── assets/template.html        ← the page (HTML + CSS + vanilla JS, no build step)
├── assets/example-profile.json ← a complete fictional example (bilingual)
├── references/schema.md        ← every profile.json field
└── scripts/build.py            ← profile.json → index.html (with validation)
```

## Workflow

### 1. Collect the sources

Ask for whatever they have, in one message:

- their resume or CV (PDF, DOCX, pasted text, or a LinkedIn "Save to PDF" export). **Required.**
- optional: GitHub username or project links, portfolio and LinkedIn URLs, and the email to show

### 2. Interview (one round, short)

Ask these together in one message. If an ask-user/multiple-choice tool is available, use it. Otherwise list each question on its own line with the options. Offer a sensible default for each so the user can answer "defaults".

1. **Languages on the page:** English only (default), English + German, or other (name them).
2. **Color theme:** `ocean-dark` (blue/green, default), `forest-dark` (greens), `violet-dark` (purple/pink), `ember-dark` (warm orange/red) or `paper-light` (light page), or "custom" with their own colors.
3. **Avatar look:** hairstyle (`bun`, `long`, `short`, `curly`, `bald`), skin tone, hair color, top color, and whether to add glasses, a beard or earrings. Tell them they can send a photo instead and you'll pick the values from it. Only describe what's visible, and never guess gender, ethnicity or age.
4. **Personality and hobbies:** 4 or 6 traits and habits (for example calm, great communicator, runs every morning).
5. **Happy-place scene:** `beach-sunrise`, `mountain-lake`, `city-skyline` or `none`.
6. **Target:** the kind of role they want next. This decides what "why hire me" leads with.

If they skip the personality questions, leave out `character` entirely. Don't make up traits.

### 3. Read the sources and extract facts

- Use only facts that are in the resume, the repos or the interview answers. **Never invent numbers, titles, employers, dates or traits.** If a claim can't be traced to a source, leave it out.
- `achievements`: 2–4 numbers that appear literally in the resume (years of experience, users, % improvements, team size). If there are none, omit the section.
- `roles`: oldest first. Each one gets a short `unlock` phrase naming what that role added (for example "Cross-platform: React Native"), plus the resume bullets, lightly shortened. Put explicit numbers into `metrics`.
- `why`: 4 or 7 cards. With 7, the first one is wide and the other 6 fill two rows of three. Each card needs a `proof` that names where it comes from (a company, a degree, a time span).
- `eras` (optional): build it only when role dates clearly show the focus shifting. Each row spans the years a technology appears in the roles.
- `projects` (optional): if they gave a GitHub username, clone or read their public repos' READMEs. Describe each project from its README only, and skip repos without a README. Use 2–3 `categories` and give each project 3–6 `tags`, so the graph has shared technology nodes.
- Bilingual pages: translate faithfully and keep official names (companies, degrees, products) as they are.

### 4. Write `profile.json`

Start from `assets/example-profile.json` and read `references/schema.md`. Keep the voice first person, short and specific. Write `lede` as 2–3 sentences. Use 4–9 speech `bubbles`, each a fun fact taken from the resume.

### 5. Build

```bash
python3 <skill-dir>/scripts/build.py profile.json index.html
```

The script validates the file and lists any problems. Fix them and rebuild. If Python isn't available, copy `assets/template.html` and replace the text `/*__PROFILE_JSON__*/null` with the JSON (escape `</` as `<\/`). Replace `{{TITLE}}`, `{{DESCRIPTION}}` and `{{LANG}}` too.

### 6. Check once

If you can render pages (a browser tool, Playwright, or the host's preview), look at the page once at desktop and phone width. Check that there are no console errors and that long titles wrap. Then deliver it. Don't loop on polish. The user will ask for changes.

### 7. Deliver

Give the user `index.html`, and offer to host it:

- **GitHub Pages:** create a repo, add `index.html` at the root, then go to Settings → Pages → Deploy from a branch → `main` / `(root)`. It goes live at `https://<user>.github.io/<repo>/`.
- Any static host (Netlify, Vercel, Cloudflare Pages) also works, because it's a single file.

If the host can publish HTML pages directly (for example claude.ai artifacts), publish it there too. The file works as-is.

## Iterating

Most follow-ups are one-field edits to `profile.json` followed by a rebuild:

| User says | Change |
|---|---|
| "the avatar doesn't look like me" | `avatar.*` (hairstyle, skin, hair, shirt, glasses, beard, earrings) |
| "different colors" / "no orange" | `theme.preset`, or set `bg surface ink muted line a1 a2 a3 a4` directly |
| "add my hobbies" | `character.perks`, `character.intro`, `character.scene` |
| "add my GitHub" | `projects` |
| "German too" | `langs: ["en","de"]` and turn the strings into `{ "en": …, "de": … }` |
| "change a heading" | `sections.<name>` |

Keep one source of truth: edit the JSON and rebuild. Never patch the generated HTML.
