# Draft: lazygit issue #4561 comment

---

**Dalton Dark** — a colorblind-friendly lazygit theme

As someone with deuteranopia, I'd love to see better theme support in lazygit. I built [Dalton Dark](https://github.com/gerchowl/dalton-colorscheme) specifically because none of the existing terminal themes account for red-green color blindness (~8% of men).

The theme is available as a mergable config:

```bash
curl -o ~/.config/lazygit/dalton-dark.yml \
  https://raw.githubusercontent.com/gerchowl/dalton-colorscheme/master/lazygit/themes-mergable/dalton-dark.yml

export LG_CONFIG_FILE="$HOME/.config/lazygit/config.yml,$HOME/.config/lazygit/dalton-dark.yml"
```

A built-in theme directory would make this much more discoverable for users who need accessible color schemes but don't know they exist.

---

# Draft: iTerm2-Color-Schemes PR description

---

## Add Dalton Dark

A dark terminal color scheme designed for **deuteranopia and protanopia** (red-green color blindness).

Named after [John Dalton](https://en.wikipedia.org/wiki/John_Dalton), who in 1794 gave the first scientific description of color blindness.

### Design principles

- **No red-green reliance** — every color pair is distinguishable under deuteranopia simulation
- **Blue-yellow axis primary** — uses the intact color axis for maximum differentiation
- **Even luminance spread** — each color has a distinct luminance value
- **Comfort zone targeting** — most colors at 5:1–10:1 contrast ratio

Red-green CVD affects ~8% of men worldwide. This is the first terminal color scheme in the collection designed specifically for colorblind users.

More details: https://github.com/gerchowl/dalton-colorscheme

---
