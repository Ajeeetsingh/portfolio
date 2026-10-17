# Ajeet Singh - Portfolio Website

A three-page portfolio: Home, Knowra case study and Document Intelligence case study.
Plain HTML, CSS and vanilla JavaScript. No framework, no build step, nothing to install.
Fonts, résumé and every script are inside this zip, so the site also works fully offline.

---

## 1. What's inside

```
ajeet-portfolio/
├── README.md                        ← this file
├── site/                            ← THE WEBSITE (open or upload this folder)
│   ├── index.html                   Home page (start here)
│   ├── knowra.html                  Knowra case study
│   ├── document-intelligence.html   Document Intelligence case study
│   ├── Ajeet-Singh-Resume.pdf       Opened by every "Résumé" button
│   └── assets/
│       └── fonts/
│           ├── fonts.css            Loads the fonts below
│           ├── Geist-400/500/600/700.woff2
│           ├── GeistMono-400/500.woff2
│           └── OFL-LICENSE.txt      Font licence (free to use, SIL Open Font License)
└── design-source/                   Editable files from the Claude Design canvas
    ├── Main.dc.html
    ├── Knowra.dc.html
    ├── DocumentIntelligence.dc.html
    └── canvas.json
```

---

## 2. Extract the zip

**Windows**
1. Right-click `ajeet-portfolio.zip` → **Extract All…** → choose a folder → **Extract**.

**macOS**
1. Double-click `ajeet-portfolio.zip`. A folder named `ajeet-portfolio` appears next to it.

**Linux**
```bash
unzip ajeet-portfolio.zip
```

Keep the folder structure exactly as it is — the pages link to each other, the fonts and
the résumé using relative paths.

---

## 3. Run it on your computer

### Option A - just open it (works everywhere, no tools needed)

Open `ajeet-portfolio/site/index.html` by double-clicking it. It opens in your default
browser (Chrome, Edge, Firefox, Safari). All pages, links, animations, fonts and the
Knowra demo work this way.

### Option B - run a local web server (closest to how it behaves online)

Use whichever of these you already have installed. Run the command from inside the
`ajeet-portfolio` folder, then open the address it prints in your browser.

**Python 3** (Windows, macOS, Linux)
```bash
cd ajeet-portfolio
python -m http.server 8000 --directory site      # on macOS/Linux you may need: python3
```
Open http://localhost:8000

**Node.js**
```bash
cd ajeet-portfolio
npx serve site
```
Open the address it shows (usually http://localhost:3000).

**VS Code**
Install the "Live Server" extension, open the `site` folder, right-click `index.html` →
**Open with Live Server**.

Press `Ctrl + C` in the terminal to stop the server.

---

## 4. Put it online

Upload the **contents of the `site/` folder** (not the whole zip) to any static host.
`index.html` is the home page.

- **Netlify** - go to app.netlify.com/drop and drag the `site` folder onto the page.
- **Vercel** - `npx vercel site` and follow the prompts.
- **GitHub Pages** - create a repository, upload the files from `site/` to it, then
  Settings → Pages → Source: *Deploy from a branch* → `main` / root.
- **Cloudflare Pages, AWS S3, cPanel, any Nginx/Apache server** - upload the files from `site/`.

---

## 5. Editing common things

Open the `.html` files in any text editor (VS Code, Notepad++, Sublime Text…).

| What | How |
|---|---|
| **Your photo** | Put `photo.jpg` in `site/assets/`. In `index.html`, search for `Photo placeholder` (two places: the "AS" circle in the hero and the box in About). In each, replace the text inside the `<div>` (`AS` or `[Your photo]`) with `<img src="assets/photo.jpg" alt="Ajeet Singh" style="width:100%;height:100%;object-fit:cover;border-radius:inherit">`, and add `overflow: hidden;` to that `<div>`'s `style`. |
| **Knowra screenshot** | Put `knowra.png` in `site/assets/`. In `knowra.html`, search for `[Screenshot:` and replace that text with `<img src="assets/knowra.png" alt="Knowra chat with citations" style="width:100%;height:100%;object-fit:cover;border-radius:inherit">`, adding `overflow: hidden;` to the box's `style`. |
| **Résumé** | Replace `site/Ajeet-Singh-Resume.pdf` with a new file of the same name. |
| **Text** | Edit it directly in the HTML. |
| **Colours** | Find-and-replace these hex codes across the three files: teal accent `#0F6E6E`, dark teal `#0B5252`, light teal tint `#DDEDEA`, page background `#F4F2EE`, alternate section `#ECE9E3`, cards `#FBFAF7`, text `#16181D`. |
| **Knowra demo answers** | In `index.html`, the last `<script>` contains a `roles` list — edit the `answer` and `sources` text there. |

### How the animations work (script at the bottom of each page)

- **Reveal on scroll** - any element with `data-reveal="up"` (or `left`, `right`, `scale`,
  `fade`, `clip`) animates in when it scrolls into view. Add `data-reveal-delay="200"`
  (milliseconds) to stagger it.
- **Count-up numbers** - an element with `data-count="80"` counts up to 80 when it appears.
- **Scroll progress bar** - the thin teal line at the very top.
- Visitors who have "reduce motion" turned on in their system settings see the page without animation.

---

## 6. About `design-source/`

These are the editable versions used in the Claude Design canvas. They need the canvas to
render, so they will not display correctly if opened directly in a browser. Use them only
to continue editing in the canvas - always run and deploy from `site/`.

---

## 7. Licences

- Site code and content: © 2026 Ajeet Singh.
- Geist and Geist Mono fonts: © The Geist Project Authors, SIL Open Font License 1.1
  (see `site/assets/fonts/OFL-LICENSE.txt`). Free to use and redistribute with the site.
