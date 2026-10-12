#!/usr/bin/env python3
"""Build an animated profile page from profile.json.

Usage: python3 build.py profile.json [output.html]
Writes index.html next to profile.json when no output path is given.
"""
import html
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "template.html"
PLACEHOLDER = "/*__PROFILE_JSON__*/null"

REQUIRED = ["name", "title", "roles"]


def text(v, lang):
    if isinstance(v, dict):
        return v.get(lang) or next(iter(v.values()), "")
    return v or ""


def check(p):
    problems = [f"missing required key: {k}" for k in REQUIRED if k not in p]
    if "name" in p and not p["name"].get("first"):
        problems.append("name.first is empty")
    for i, r in enumerate(p.get("roles", [])):
        for k in ("title", "company", "when"):
            if k not in r:
                problems.append(f"roles[{i}] is missing {k}")
    langs = p.get("langs", ["en"])
    for i, a in enumerate(p.get("achievements", [])):
        if "value" not in a:
            problems.append(f"achievements[{i}] is missing value")
    if p.get("theme", {}).get("preset") not in (None, "ocean-dark", "forest-dark", "violet-dark", "ember-dark", "paper-light"):
        problems.append("theme.preset must be one of ocean-dark, forest-dark, violet-dark, ember-dark, paper-light")
    hs = p.get("avatar", {}).get("hairstyle")
    if hs not in (None, "bun", "long", "short", "curly", "bald"):
        problems.append("avatar.hairstyle must be one of bun, long, short, curly, bald")
    sc = (p.get("character") or {}).get("scene")
    if sc not in (None, "beach-sunrise", "mountain-lake", "city-skyline", "none"):
        problems.append("character.scene must be one of beach-sunrise, mountain-lake, city-skyline, none")
    return problems, langs


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name("index.html")
    profile = json.loads(src.read_text(encoding="utf-8"))
    problems, langs = check(profile)
    if problems:
        print("profile.json has problems:\n  - " + "\n  - ".join(problems), file=sys.stderr)
        sys.exit(1)
    lang = langs[0]
    name = f'{profile["name"].get("first", "")} {profile["name"].get("last", "")}'.strip()
    title = profile.get("page_title") or f"{name} · Level Up"
    desc = text(profile.get("lede"), lang)[:300] or f"{name}: {text(profile.get('title'), lang)}"
    page = TEMPLATE.read_text(encoding="utf-8")
    data = json.dumps(profile, ensure_ascii=False).replace("</", "<\\/")
    page = (page.replace(PLACEHOLDER, data)
                .replace("{{TITLE}}", html.escape(title))
                .replace("{{DESCRIPTION}}", html.escape(desc, quote=True))
                .replace("{{LANG}}", html.escape(lang)))
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out} ({len(page) // 1024} KB)")


if __name__ == "__main__":
    main()
