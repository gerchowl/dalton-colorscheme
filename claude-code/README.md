# Claude Code — Dalton-friendly theming

Claude Code ships a **built-in `dark-daltonized`** theme (and a matching
`light-daltonized`) tuned for deuteranopia/protanopia. It is **not** the same
palette as the terminal Dalton Dark in this repo — Claude Code's TUI uses its
own internal color model (autoAccept, bashBorder, diffAdded, etc.) rather than
ANSI slots, so the two themes target different layers but share the same
design principle: avoid red/green discrimination, lean on the blue-yellow axis.

If you're using Claude Code in a terminal, you'll get the best result by
combining both:

1. The terminal emulator (WezTerm / Ghostty / etc.) renders ANSI output using
   Dalton Dark from this repo — that handles `git diff`, test output, syntax
   highlighting, and everything else that uses raw ANSI escapes.
2. Claude Code's own UI chrome (borders, spinners, permission prompts, diff
   blocks rendered inside Claude Code) uses its built-in `dark-daltonized`.

## Enable

Set the theme in `~/.claude/settings.json`:

```json
{
  "theme": "dark-daltonized"
}
```

Or pick it interactively with `/config` inside Claude Code.

## Why not override the colors?

Claude Code does not (as of this writing) expose user-defined theme color
overrides — the theme name is the only knob. The internal color objects
(`fv5` / `Nv5` / `Vv5` in the bundled CLI) are not surfaced through any
public config schema. If that changes, this folder is the place a
`settings.json` colour fragment would live.

Verified against `@anthropic-ai/claude-agent-sdk` cli.js — `dark-daltonized`
is one of the shipped theme keys alongside `dark`, `light`, `dark-ansi`,
`light-ansi`, and `light-daltonized`.
