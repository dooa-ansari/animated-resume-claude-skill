# profile.json reference

**Text values (T)** are either a plain string or one string per language, for example `{ "en": "Toolbox", "de": "Werkzeugkasten" }`. Lists that change per language work the same way: `{ "en": ["a","b"], "de": ["a","b"] }`. If a language is missing, the page falls back to the first entry of `langs`.

Colors named `a1`…`a4` refer to the theme's four accent colors. `muted` is also allowed.

Only `name`, `title` and `roles` are required. Every optional section that's missing is hidden.

## Top level

| Field | Type | Notes |
|---|---|---|
| `langs` | string[] | Page languages, default first. Example: `["en","de"]`. Built-in UI strings exist for `en` and `de`. For any other language, add `ui` and `sections`. |
| `name` | `{first, last}` | The last name gets the animated gradient. |
| `handle` | string | Shown top-left. Defaults to `first.last`. |
| `page_title` | string | Browser tab title. Defaults to "First Last · Level Up". |
| `eyebrow` | T | Small label above the name. Default: "Player profile". |
| `title` | T | Job title on the headline line. |
| `rotating` | T[] | Words the typing effect cycles through after the title. |
| `headline_tail` | T | Fixed text after the rotating words, such as "Applied AI & Automation". |
| `location` | string | Shown with a pin icon. |
| `stack_line` | string | Core stack, shown with a `</>` icon, for example "React · Node.js · TypeScript". |
| `lede` | T | 2–3 sentence summary. |
| `xp` | object | `label` (T, left above the bar), `right` (T), `start` (T, under the bar on the left), `now` (T, under the bar on the right), `fill` (0–100). |
| `bubbles` | T[] | Speech-bubble lines shown when the avatar is clicked. |
| `footer` | T | Footer line. |
| `ui` | `{lang: {key: string}}` | Overrides built-in UI strings: `details unlocked perk all today copy copied tap sunUp sunDown breathe stop bin bout levelUp graph hello`. |
| `sections` | object | Overrides section headings. Keys: `ach`, `path`, `eras`, `why`, `me`, `quests`, `skills` and `contact` take `[eyebrow, title, intro?]` as an array of T. `edu`, `langs` and `certs` take a single T. In `path.title`, `{n}` becomes the number of roles. |

## theme

```json
"theme": { "preset": "ocean-dark" }
```

The presets are `ocean-dark` (default), `forest-dark`, `violet-dark`, `ember-dark` and `paper-light`. You can override any single token next to the preset: `mode` ("dark"/"light"), `bg`, `surface`, `ink`, `muted`, `line`, `a1`, `a2`, `a3`, `a4` (hex colors). Accent `a1` is the main highlight, `a2` is blue-ish, `a3` is green-ish, and `a4` is a fourth highlight. For contrast on dark themes, keep accents bright. For light themes, keep them deep.

## avatar

| Field | Values |
|---|---|
| `hairstyle` | `bun` (default), `long`, `short`, `curly`, `bald` |
| `skin`, `skin_shadow` | hex colors (the shadow is for the nose line, about 15% darker) |
| `hair`, `hair_highlight` | hex colors |
| `shirt`, `shirt_shadow` | hex colors |
| `lips`, `eyes` | hex colors (`eyes` is the iris) |
| `glasses`, `beard`, `earrings` | booleans |
| `lashes` | boolean, default true |
| `glyphs` | 4 short strings floating around the avatar, for example `["</>","{ }","AI","MCP"]` |
| `backdrop` | `[hexFrom, hexTo]` for the circle gradient. Defaults to the theme accents. |

The same colors are reused for the small meditating figure in the character scene.

## achievements[]

`{ "value": "+20%", "label": T, "text": T }`. The value counts up from 0 when it starts with an optional sign followed by digits (for example `8+`, `2M` or `+20%`).

## roles[] (oldest first)

| Field | Type |
|---|---|
| `when` | T, for example "03/2020 – 09/2021" |
| `company` | T |
| `place` | T, optional |
| `title` | T |
| `unlock` | T: a short phrase for what this level added |
| `bullets` | T[] |
| `metrics` | T[], optional: short number chips |

Level colors run green, then yellow-green, then blue, then the main accent as the career progresses. The latest role opens by default.

## eras (optional)

```json
"eras": { "start": 2016, "end": 2027, "ticks": [2016,2018,2020,2022,2024,2026], "show_today": true,
  "rows": [ { "label": T, "from": 2016.2, "to": 2022.3, "color": "a3", "striped": false } ] }
```

Years can be decimals (for example `2020.5` for mid-2020). `ticks` is optional.

## why[]

`{ "icon": "ai", "color": "a1", "title": T, "text": T, "proof": T }`. The first card is wide unless it sets `"big": false`. Use 4 or 7 cards.

## character (optional)

```json
"character": { "scene": "beach-sunrise", "intro": T, "caption": T,
  "perks": [ { "icon": "calm", "color": "a2", "title": T, "text": T } ] }
```

The scenes are `beach-sunrise`, `mountain-lake`, `city-skyline` and `none` (`none` shows only the perks). Use 4 or 6 perks.

## projects (optional)

```json
"projects": { "base_url": "https://github.com/USER/",
  "categories": { "ai": { "color": "a1", "label": T } },
  "items": [ { "id": "repo-name", "url": "optional full URL", "cat": "ai", "tags": ["React","Neo4j"],
               "title": T, "short": "optional shorter graph label", "text": T } ] }
```

The link is `url`, or `base_url + id` when `url` is missing. Shared `tags` become shared nodes in the graph.

## skills[], education[], languages[], certificates[], contact

- `skills`: `[{ "group": T, "items": T[] }]`, shown as tabs
- `education`: `[{ "when": T, "degree": T, "school": T }]`
- `languages`: `[{ "name": T, "level": T, "pct": 0-100 }]`
- `certificates`: `string[]`
- `contact`: `{ "email": "…", "links": [{ "label": "LinkedIn", "url": "…" }] }`

## Icons

Use these for `why[].icon` and `character.perks[].icon`: `scale ai ship impact both learn qa team lead design data cloud code calm talk grow zen fit food heart book music travel coffee camera game sun star`
