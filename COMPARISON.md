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

| Color | Hex |
|---|---|
| Orange | `#E69F00` |
| Sky Blue | `#56B4E9` |
| Bluish Green | `#009E73` |
| Yellow | `#F0E442` |
| Blue | `#0072B2` |
| Vermillion | `#D55E00` |
| Reddish Purple | `#CC79A7` |
| Black | `#000000` |

**Why it doesn't translate to terminals:**
- Designed for **data visualization** (discrete categorical marks on white backgrounds), not **text on dark backgrounds**
- Only 8 colors — terminals need 16 (normal + bright) plus background/foreground/selection
- High saturation optimized for scatter plots, not for hours of code reading
- No concept of "bold" vs "dim" variants that terminal workflows need
- The bluish green `#009E73` still falls in the deuteranopia confusion zone with the vermillion

### 2. Modus Vivendi Deuteranopia (Protesilaos Stavrou)

A WCAG AAA-compliant Emacs theme. Very well researched.

| Color | Hex |
|---|---|
| Background | `#000000` |
| Foreground | `#ffffff` |
| Red | `#ff5f59` |
| Green | `#44bc44` |
| Yellow | `#cabf00` |
| Blue | `#2fafff` |
| Magenta | `#feacd0` |
| Cyan | `#00d3d0` |

**Strengths:** WCAG AAA (7:1 minimum), massive color vocabulary (40+ named colors).

**Limitations for terminal use:**
- Pure black `#000000` background and pure white `#ffffff` foreground create maximum 21:1 contrast — exceeds comfort for extended terminal sessions, causes halation for some users
- Optimized for **Emacs faces** (syntax highlighting in an editor), not TUI applications like lazygit where borders, selections, and status lines matter
- The "red" `#ff5f59` is still a high-saturation warm red — under deuteranopia simulation it converges with the green `#44bc44` more than necessary
- No matched lazygit/TUI theme provided
- Magenta `#feacd0` is a pink that sits close to the red-faint `#ff9580` under deuteranopia

### 3. EF Deuteranopia Dark (Protesilaos Stavrou)

A newer, less strict alternative from the same author.

| Color | Hex |
|---|---|
| Background | `#000a1f` |
| Foreground | `#ddddee` |
| Red | `#cf8560` |
| Green | `#3faa26` |
| Yellow | `#aa9f32` |
| Blue | `#3f90f0` |
| Magenta | `#b379bf` |
| Cyan | `#5faaef` |

**Strengths:** Blue-tinted background reduces harshness, desaturated reds.

**Limitations:**
- The "red" `#cf8560` is actually orange-brown — it avoids confusion but loses the semantic meaning of "red" (errors, deletions, warnings)
- Cyan `#5faaef` is essentially another blue, reducing the palette's effective diversity
- Same editor-focused design without TUI/lazygit consideration

### 4. Solarized (Ethan Schoonover) + colorblind issue #91

The most popular terminal theme. Has an open, unresolved issue (#91) for colorblind support since 2012.

**The core problem:** Solarized uses precisely calibrated L\*a\*b\* values for perceptual uniformity — but this uniformity means the red `#dc322f` and green `#859900` are almost identical in luminance. For deuteranopes, same luminance + same perceived hue = invisible distinction.

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
