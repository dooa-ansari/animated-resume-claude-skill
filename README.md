# Animated Resume · Claude Skill

A Claude skill that turns your resume or LinkedIn PDF into an **animated, interactive one-page portfolio**: an illustrated avatar, your career as game levels, a projects graph, five themes, and a single HTML file that's ready for GitHub Pages.

**Live example:** [`index.html`](index.html) shows *Sam Carter*, a fictional person, built from [`example-profile.json`](skills/animated-resume/assets/example-profile.json).

## What you get

- **Animated avatar** that blinks, types, waves and shows speech bubbles. Choose from 5 hairstyles, any skin, hair and outfit colors, and optional glasses, beard or earrings.
- **Career as levels** on a glowing rail, with a "LEVEL UP!" pop for each role and the skill it unlocked
- **Achievement counters**, a **stack-evolution timeline** and **"why hire me"** cards, each tied to proof from your CV
- A **character sheet** with an animated happy-place scene (beach sunrise, mountain lake or city skyline), a breathing exercise and personality perks
- **GitHub projects** with an interactive project ↔ technology graph
- **Language toggle** (English and German built in, any language possible)
- **5 color themes:** `ocean-dark`, `forest-dark`, `violet-dark`, `ember-dark` and `paper-light`, or your own colors
- A drifting particle background, scroll reveals, 3D card tilt and full `prefers-reduced-motion` support
- Plain HTML, CSS, inline SVG and vanilla JavaScript, with no framework and no build step needed to host it

## How it works

When you ask Claude something like *"Make me an animated resume from my CV"*, the skill:

1. asks for your resume (PDF, DOCX, text or a LinkedIn "Save to PDF" export) and, optionally, your GitHub username
2. asks a few quick questions: page languages, color theme, what your avatar looks like (or reads it from a photo), your personality and hobbies, your happy-place scene, and your target role
3. writes a `profile.json` using **only facts from your sources**, with no invented numbers or titles
4. runs `scripts/build.py` to generate your `index.html`

## Install

**Claude Code**

```bash
git clone https://github.com/dooa-ansari/animated-resume-claude-skill
cp -r animated-resume-claude-skill/skills/animated-resume ~/.claude/skills/
```

**Claude apps (claude.ai / desktop):** download [`animated-resume-skill.zip`](animated-resume-skill.zip) and upload it under Settings → Capabilities → Skills.

Then ask Claude: *"Make me an animated resume from my CV."*

## Build by hand

```bash
python3 skills/animated-resume/scripts/build.py my-profile.json index.html
```

Every field is documented in [`references/schema.md`](skills/animated-resume/references/schema.md).

## Host it on GitHub Pages

Put `index.html` in a repo, then go to Settings → Pages → Deploy from a branch → `main` / `(root)`. It goes live at `https://<user>.github.io/<repo>/`.

## Structure

```
skills/animated-resume/
├── SKILL.md                    # instructions Claude follows (interview → profile.json → build)
├── assets/template.html        # the animated page
├── assets/example-profile.json # complete bilingual example (fictional person)
├── references/schema.md        # every profile.json field
└── scripts/build.py            # profile.json → index.html, with validation
```

## License

MIT. See [LICENSE](LICENSE).
