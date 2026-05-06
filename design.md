# Design Contract

This file makes product taste explicit enough for an AI agent to follow and for a reviewer to enforce.

## Principles

- Build the actual user workflow, not a marketing shell.
- Use restrained visual hierarchy: clear spacing, strong typography, useful contrast.
- Prefer semantic tokens over one-off colors.
- Keep application UI dense enough for repeated work.
- Use cards only for repeated items, modals, and genuinely framed tools.
- Do not use decorative gradients, blobs, oversized hero sections, or generic dashboard filler.

## Tokens

```yaml
colors:
  background: "#ffffff"
  foreground: "#161616"
  primary: "#0f62fe"
  border: "#e0e0e0"
  muted: "#f4f4f4"
  success: "#24a148"
  warning: "#ff832b"
  destructive: "#da1e28"
typography:
  sans: "Inter or system sans"
  mono: "IBM Plex Mono or system mono"
radius:
  panel: "6px"
  control: "4px"
spacing:
  base: "4px"
```

## Review Checklist

- Does the UI support the primary workflow directly?
- Are labels, empty states, and errors concise?
- Are colors semantic and consistent?
- Can the longest text fit on mobile and desktop?
- Are keyboard focus states visible?
- Did the change avoid unrelated data/auth/runtime behavior?

