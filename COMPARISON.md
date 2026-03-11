# Why another colorblind theme?

A comparison of Dalton Dark with existing colorblind-aware palettes and the science behind the design.

## The problem with standard terminal palettes

The 16-color ANSI palette was designed in the 1970s-80s with zero consideration for color vision deficiency (CVD). The standard names — **red** and **green** — are the exact pair that deuteranopes and protanopes confuse. Yet nearly every terminal tool relies on them:

- `git diff`: additions in green, deletions in red
- Test frameworks: green pass, red fail
- Lazygit: green active borders, red for unstaged changes

For the ~8% of men with red-green CVD, these are functionally the same color.

## Existing approaches and their limitations

### 1. Okabe-Ito / Wong palette (2008/2011)

The gold standard for scientific visualization, recommended by Nature journals.

| Color | | Hex |
|---|---|---|
| Orange | ![#E69F00](https://placehold.co/16x16/E69F00/E69F00) | `#E69F00` |
| Sky Blue | ![#56B4E9](https://placehold.co/16x16/56B4E9/56B4E9) | `#56B4E9` |
| Bluish Green | ![#009E73](https://placehold.co/16x16/009E73/009E73) | `#009E73` |
| Yellow | ![#F0E442](https://placehold.co/16x16/F0E442/F0E442) | `#F0E442` |
| Blue | ![#0072B2](https://placehold.co/16x16/0072B2/0072B2) | `#0072B2` |
| Vermillion | ![#D55E00](https://placehold.co/16x16/D55E00/D55E00) | `#D55E00` |
| Reddish Purple | ![#CC79A7](https://placehold.co/16x16/CC79A7/CC79A7) | `#CC79A7` |
| Black | ![#000000](https://placehold.co/16x16/000000/000000) | `#000000` |

**Why it doesn't translate to terminals:**
- Designed for **data visualization** (discrete categorical marks on white backgrounds), not **text on dark backgrounds**
- Only 8 colors — terminals need 16 (normal + bright) plus background/foreground/selection
- High saturation optimized for scatter plots, not for hours of code reading
- No concept of "bold" vs "dim" variants that terminal workflows need
- The bluish green `#009E73` still falls in the deuteranopia confusion zone with the vermillion

### 2. Modus Vivendi Deuteranopia (Protesilaos Stavrou)

A WCAG AAA-compliant Emacs theme. Very well researched.

| Color | | Hex |
|---|---|---|
| Background | ![#000000](https://placehold.co/16x16/000000/000000) | `#000000` |
| Foreground | ![#ffffff](https://placehold.co/16x16/ffffff/ffffff) | `#ffffff` |
| Red | ![#ff5f59](https://placehold.co/16x16/ff5f59/ff5f59) | `#ff5f59` |
| Green | ![#44bc44](https://placehold.co/16x16/44bc44/44bc44) | `#44bc44` |
| Yellow | ![#cabf00](https://placehold.co/16x16/cabf00/cabf00) | `#cabf00` |
| Blue | ![#2fafff](https://placehold.co/16x16/2fafff/2fafff) | `#2fafff` |
| Magenta | ![#feacd0](https://placehold.co/16x16/feacd0/feacd0) | `#feacd0` |
| Cyan | ![#00d3d0](https://placehold.co/16x16/00d3d0/00d3d0) | `#00d3d0` |

**Strengths:** WCAG AAA (7:1 minimum), massive color vocabulary (40+ named colors).

**Limitations for terminal use:**
- Pure black `#000000` background and pure white `#ffffff` foreground create maximum 21:1 contrast — exceeds comfort for extended terminal sessions, causes halation for some users
- Optimized for **Emacs faces** (syntax highlighting in an editor), not TUI applications like lazygit where borders, selections, and status lines matter
- The "red" `#ff5f59` is still a high-saturation warm red — under deuteranopia simulation it converges with the green `#44bc44` more than necessary
- No matched lazygit/TUI theme provided
- Magenta `#feacd0` is a pink that sits close to the red-faint `#ff9580` under deuteranopia

### 3. EF Deuteranopia Dark (Protesilaos Stavrou)

A newer, less strict alternative from the same author.

| Color | | Hex |
|---|---|---|
| Background | ![#000a1f](https://placehold.co/16x16/000a1f/000a1f) | `#000a1f` |
| Foreground | ![#ddddee](https://placehold.co/16x16/ddddee/ddddee) | `#ddddee` |
| Red | ![#cf8560](https://placehold.co/16x16/cf8560/cf8560) | `#cf8560` |
| Green | ![#3faa26](https://placehold.co/16x16/3faa26/3faa26) | `#3faa26` |
| Yellow | ![#aa9f32](https://placehold.co/16x16/aa9f32/aa9f32) | `#aa9f32` |
| Blue | ![#3f90f0](https://placehold.co/16x16/3f90f0/3f90f0) | `#3f90f0` |
| Magenta | ![#b379bf](https://placehold.co/16x16/b379bf/b379bf) | `#b379bf` |
| Cyan | ![#5faaef](https://placehold.co/16x16/5faaef/5faaef) | `#5faaef` |

**Strengths:** Blue-tinted background reduces harshness, desaturated reds.

**Limitations:**
- The "red" `#cf8560` is actually orange-brown — it avoids confusion but loses the semantic meaning of "red" (errors, deletions, warnings)
- Cyan `#5faaef` is essentially another blue, reducing the palette's effective diversity
- Same editor-focused design without TUI/lazygit consideration

### 4. Solarized (Ethan Schoonover) + colorblind issue #91

The most popular terminal theme. Has an open, unresolved issue (#91) for colorblind support since 2012.

| Color | | Hex |
|---|---|---|
| Base03 (bg) | ![#002b36](https://placehold.co/16x16/002b36/002b36) | `#002b36` |
| Base0 (fg) | ![#839496](https://placehold.co/16x16/839496/839496) | `#839496` |
| Red | ![#dc322f](https://placehold.co/16x16/dc322f/dc322f) | `#dc322f` |
| Green | ![#859900](https://placehold.co/16x16/859900/859900) | `#859900` |
| Yellow | ![#b58900](https://placehold.co/16x16/b58900/b58900) | `#b58900` |
| Blue | ![#268bd2](https://placehold.co/16x16/268bd2/268bd2) | `#268bd2` |
| Magenta | ![#d33682](https://placehold.co/16x16/d33682/d33682) | `#d33682` |
| Cyan | ![#2aa198](https://placehold.co/16x16/2aa198/2aa198) | `#2aa198` |
| Orange | ![#cb4b16](https://placehold.co/16x16/cb4b16/cb4b16) | `#cb4b16` |
| Violet | ![#6c71c4](https://placehold.co/16x16/6c71c4/6c71c4) | `#6c71c4` |

**The core problem:** Solarized uses precisely calibrated L\*a\*b\* values for perceptual uniformity — but this uniformity means the red `#dc322f` and green `#859900` are almost identical in luminance. For deuteranopes, same luminance + same perceived hue = invisible distinction.

### 5. Catppuccin Mocha

The most popular modern terminal theme, with ports for virtually every application.

| Color | | Hex |
|---|---|---|
| Base (bg) | ![#1e1e2e](https://placehold.co/16x16/1e1e2e/1e1e2e) | `#1e1e2e` |
| Text (fg) | ![#cdd6f4](https://placehold.co/16x16/cdd6f4/cdd6f4) | `#cdd6f4` |
| Red | ![#f38ba8](https://placehold.co/16x16/f38ba8/f38ba8) | `#f38ba8` |
| Green | ![#a6e3a1](https://placehold.co/16x16/a6e3a1/a6e3a1) | `#a6e3a1` |
| Yellow | ![#f9e2af](https://placehold.co/16x16/f9e2af/f9e2af) | `#f9e2af` |
| Blue | ![#89b4fa](https://placehold.co/16x16/89b4fa/89b4fa) | `#89b4fa` |
| Mauve | ![#cba6f7](https://placehold.co/16x16/cba6f7/cba6f7) | `#cba6f7` |
| Teal | ![#94e2d5](https://placehold.co/16x16/94e2d5/94e2d5) | `#94e2d5` |
| Peach | ![#fab387](https://placehold.co/16x16/fab387/fab387) | `#fab387` |
| Lavender | ![#b4befe](https://placehold.co/16x16/b4befe/b4befe) | `#b4befe` |

**Limitations for deuteranopia:**
- The pastel aesthetic means many colors cluster in high lightness (70–90%) — red `#f38ba8`, green `#a6e3a1`, peach `#fab387`, and yellow `#f9e2af` all sit in a narrow luminance band
- Red and green are both desaturated pastels — under deuteranopia simulation they converge to nearly the same warm beige
- Teal `#94e2d5` and green `#a6e3a1` are very close in both hue and lightness for deuteranopes
- Beautiful theme, but the pastel uniformity that makes it pleasant for normal vision makes it hostile to CVD

### 6. Dracula

One of the most ported themes, with a distinctive purple-heavy palette.

| Color | | Hex |
|---|---|---|
| Background | ![#282a36](https://placehold.co/16x16/282a36/282a36) | `#282a36` |
| Foreground | ![#f8f8f2](https://placehold.co/16x16/f8f8f2/f8f8f2) | `#f8f8f2` |
| Red | ![#ff5555](https://placehold.co/16x16/ff5555/ff5555) | `#ff5555` |
| Green | ![#50fa7b](https://placehold.co/16x16/50fa7b/50fa7b) | `#50fa7b` |
| Yellow | ![#f1fa8c](https://placehold.co/16x16/f1fa8c/f1fa8c) | `#f1fa8c` |
| Purple | ![#bd93f9](https://placehold.co/16x16/bd93f9/bd93f9) | `#bd93f9` |
| Cyan | ![#8be9fd](https://placehold.co/16x16/8be9fd/8be9fd) | `#8be9fd` |
| Orange | ![#ffb86c](https://placehold.co/16x16/ffb86c/ffb86c) | `#ffb86c` |
| Pink | ![#ff79c6](https://placehold.co/16x16/ff79c6/ff79c6) | `#ff79c6` |

**Limitations for deuteranopia:**
- Red `#ff5555` and green `#50fa7b` are high-saturation primaries — the classic deuteranopia trap. Under simulation they merge into the same muddy yellow-brown
- Pink `#ff79c6` and red `#ff5555` converge under deuteranopia (both become yellowish)
- Orange `#ffb86c` and yellow `#f1fa8c` are already close in hue and compress further without M-cone input
- Nearly-white foreground `#f8f8f2` against light cyan/yellow creates low contrast pairs

### 7. Gruvbox Dark

A retro-groove palette inspired by vintage computing. Widely used in vim/neovim.

| Color | | Hex | Bright | | Hex |
|---|---|---|---|---|---|
| Background | ![#282828](https://placehold.co/16x16/282828/282828) | `#282828` | | | |
| Foreground | ![#ebdbb2](https://placehold.co/16x16/ebdbb2/ebdbb2) | `#ebdbb2` | | | |
| Red | ![#cc241d](https://placehold.co/16x16/cc241d/cc241d) | `#cc241d` | | ![#fb4934](https://placehold.co/16x16/fb4934/fb4934) | `#fb4934` |
| Green | ![#98971a](https://placehold.co/16x16/98971a/98971a) | `#98971a` | | ![#b8bb26](https://placehold.co/16x16/b8bb26/b8bb26) | `#b8bb26` |
| Yellow | ![#d79921](https://placehold.co/16x16/d79921/d79921) | `#d79921` | | ![#fabd2f](https://placehold.co/16x16/fabd2f/fabd2f) | `#fabd2f` |
| Blue | ![#458588](https://placehold.co/16x16/458588/458588) | `#458588` | | ![#83a598](https://placehold.co/16x16/83a598/83a598) | `#83a598` |
| Purple | ![#b16286](https://placehold.co/16x16/b16286/b16286) | `#b16286` | | ![#d3869b](https://placehold.co/16x16/d3869b/d3869b) | `#d3869b` |
| Aqua | ![#689d6a](https://placehold.co/16x16/689d6a/689d6a) | `#689d6a` | | ![#8ec07c](https://placehold.co/16x16/8ec07c/8ec07c) | `#8ec07c` |
| Orange | ![#d65d0e](https://placehold.co/16x16/d65d0e/d65d0e) | `#d65d0e` | | ![#fe8019](https://placehold.co/16x16/fe8019/fe8019) | `#fe8019` |

**Limitations for deuteranopia:**
- Red `#cc241d` and green `#98971a` are near-identical in luminance — the same fundamental problem as Solarized
- Aqua `#689d6a` is literally a green — for deuteranopes it merges with green `#98971a`, losing a whole color slot
- Orange `#d65d0e` and red `#cc241d` collapse into the same brownish tone
- The warm, earthy aesthetic relies heavily on the red-green axis, which is exactly what deuteranopes can't see

### 8. Nord

A cool, blue-tinted Arctic palette. Restrained and cohesive.

| Color | | Hex |
|---|---|---|
| Polar Night (bg) | ![#2e3440](https://placehold.co/16x16/2e3440/2e3440) | `#2e3440` |
| Snow Storm (fg) | ![#d8dee9](https://placehold.co/16x16/d8dee9/d8dee9) | `#d8dee9` |
| Red | ![#bf616a](https://placehold.co/16x16/bf616a/bf616a) | `#bf616a` |
| Green | ![#a3be8c](https://placehold.co/16x16/a3be8c/a3be8c) | `#a3be8c` |
| Yellow | ![#ebcb8b](https://placehold.co/16x16/ebcb8b/ebcb8b) | `#ebcb8b` |
| Blue | ![#5e81ac](https://placehold.co/16x16/5e81ac/5e81ac) | `#5e81ac` |
| Purple | ![#b48ead](https://placehold.co/16x16/b48ead/b48ead) | `#b48ead` |
| Cyan | ![#88c0d0](https://placehold.co/16x16/88c0d0/88c0d0) | `#88c0d0` |

**Limitations for deuteranopia:**
- Deliberately muted palette means colors are already close together — red `#bf616a` and green `#a3be8c` are both desaturated and sit at similar luminance
- Purple `#b48ead` and red `#bf616a` converge under deuteranopia (both become a dull ochre)
- The restrained saturation that gives Nord its elegance removes the very contrast deuteranopes need to differentiate colors

### 9. Tokyo Night

A modern, anime-inspired dark theme popular in neovim and VS Code.

| Color | | Hex |
|---|---|---|
| Background | ![#1a1b26](https://placehold.co/16x16/1a1b26/1a1b26) | `#1a1b26` |
| Foreground | ![#c0caf5](https://placehold.co/16x16/c0caf5/c0caf5) | `#c0caf5` |
| Red | ![#f7768e](https://placehold.co/16x16/f7768e/f7768e) | `#f7768e` |
| Green | ![#9ece6a](https://placehold.co/16x16/9ece6a/9ece6a) | `#9ece6a` |
| Yellow | ![#e0af68](https://placehold.co/16x16/e0af68/e0af68) | `#e0af68` |
| Blue | ![#7aa2f7](https://placehold.co/16x16/7aa2f7/7aa2f7) | `#7aa2f7` |
| Magenta | ![#bb9af7](https://placehold.co/16x16/bb9af7/bb9af7) | `#bb9af7` |
| Cyan | ![#7dcfff](https://placehold.co/16x16/7dcfff/7dcfff) | `#7dcfff` |

**Limitations for deuteranopia:**
- Red `#f7768e` is a pink-red that converges with green `#9ece6a` under deuteranopia — both become a similar warm tan
- Yellow `#e0af68` and red `#f7768e` also compress toward each other without M-cone differentiation
- Shares Dalton Dark's blue `#7aa2f7` (coincidence) — that one works well. The rest of the palette does not account for CVD

## The science: why most themes fail for deuteranopia

### What deuteranopia actually does

The retina has three cone types: L (red-sensitive), M (green-sensitive), S (blue-sensitive). Deuteranopia means the M-cones are absent. The brain receives only L+S signals, collapsing the red-green axis into a single dimension.

**Perceptually, a deuteranope sees approximately two hue categories:**
1. **Blue ↔ yellow axis** (intact, driven by S-cones vs L-cones)
2. **Luminance** (light vs dark)

Colors that differ only on the red-green axis (the missing M-cone dimension) become identical.

### The three principles for deuteranopia-safe terminal color

1. **Separate by luminance, not just hue.** Two colors at the same brightness that differ only in red/green content will merge. Every color pair should have measurably different luminance.

2. **Use the blue-yellow axis as the primary differentiator.** This is the axis that remains fully functional. Blue, yellow, and purple (which contains blue) are safe. Pure red and pure green are not.

3. **Keep red and green if you must, but shift them.** A terminal *needs* something called "red" and something called "green" — tools expect it. The trick is to shift red toward orange/coral (adding yellow) and green toward lime/grass (adding yellow), so they separate on the blue-yellow axis rather than relying on the broken red-green axis.

### How Dalton Dark applies these principles

| Principle | Implementation |
|---|---|
| Luminance separation | Every color has a distinct luminance value (verified via WCAG contrast matrix). No two foreground colors have <1.3:1 luminance ratio. |
| Blue-yellow axis | Primary accent is blue (`#7aa2f7`). Yellow (`#c4c40c`) is punchy. Magenta is purple (`#a050d0`), not pink. |
| Shifted red/green | Red is `#d85050` (shifted slightly orange from pure red). Green is `#5b914e` (shifted toward grass). Under deuteranopia simulation, they diverge on the yellow axis. |
| Comfort range | 5:1–10:1 contrast on background. Not WCAG AAA's harsh 7:1 minimum with pure white. |
| Matched TUI theme | WezTerm ANSI palette + lazygit hex theme designed and validated together. |

### What Dalton Dark does differently

1. **Designed by a deuteranope.** Not simulated — actually tested by someone who can't distinguish standard red from green.
2. **TUI-first.** Built for lazygit, not retrofitted from an editor theme. Borders, selections, and status lines are first-class citizens.
3. **Iteratively tuned.** Not calculated from formulas and shipped — each color was adjusted in real terminal sessions with contrast matrix validation at each step.
4. **Comfort over compliance.** WCAG AA (4.5:1) rather than AAA (7:1). The extra contrast of AAA with saturated colors causes visual fatigue over long sessions.

## References

- Wong, B. (2011). "Color blindness." *Nature Methods*, 8(6), 441. [doi:10.1038/nmeth.1618](https://www.nature.com/articles/nmeth.1618)
- Okabe, M. & Ito, K. (2008). "Color Universal Design." [jfly.uni-koeln.de](https://jfly.uni-koeln.de/color/)
- Krzywinski, M. "Designing for Color Blindness." [mk.bcgsc.ca/colorblind](https://mk.bcgsc.ca/colorblind/palettes.mhtml)
- Protesilaos Stavrou. "Modus Themes." [protesilaos.com/emacs/modus-themes](https://protesilaos.com/emacs/modus-themes)
- Protesilaos Stavrou. "Ef Themes." [github.com/protesilaos/ef-themes](https://github.com/protesilaos/ef-themes)
- Solarized colorblind issue: [github.com/altercation/solarized/issues/91](https://github.com/altercation/solarized/issues/91)
