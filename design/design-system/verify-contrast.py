"""
WCAG 2.1 contrast verification for the DeskTrace design system (v2).

Evidence, not decoration: every colour pair in desktrace.css is checked here
rather than judged by eye. Run it after any palette change.

    python verify-contrast.py

Thresholds (WCAG 2.1 Level AA):
    1.4.3  Text                     >= 4.5:1
    1.4.11 Non-text UI components   >= 3.0:1
           (control borders, focus rings, meter fills)

Note on card borders: a decorative edge around a card is NOT a "UI component
that conveys information or is required to identify a control", so it is not
held to 3:1. That is why the system has two border tokens — --ds-line for
decorative edges and --ds-line-control for anything you can type into.

CSM 399 Capstone · Group 16 · UI/UX
"""


def luminance(hex_colour):
    """Relative luminance per WCAG 2.1, formula in Understanding SC 1.4.3."""
    h = hex_colour.lstrip("#")
    channels = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        channels.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(foreground, background):
    a, b = luminance(foreground), luminance(background)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def grade(r):
    return "AAA" if r >= 7.0 else "AA" if r >= 4.5 else "AA-large" if r >= 3.0 else "fail"


# --- Tokens, mirrored from desktrace.css ---------------------------------- #

LIGHT = {
    "bg": "#F6F8FA", "surface": "#FFFFFF", "surface2": "#EEF2F6", "surface3": "#E3E9F0",
    "line": "#E2E8F0", "line-control": "#64748B",
    "ink": "#0F172A", "ink2": "#475569",
    "brand": "#0F1E2E", "brand2": "#13324A",
    "accent": "#0E7489", "accent-hover": "#0B5F70", "accent-tint": "#E0F3F7",
    "ok": "#047857", "ok-soft": "#E7F7F0",
    "warn": "#B45309", "warn-soft": "#FDF3E3",
    "bad": "#BE123C", "bad-soft": "#FDEAEF",
}

DARK = {
    "bg": "#070E18", "surface": "#101C2B", "surface2": "#1A2B3F", "surface3": "#24394F",
    "line": "#243C55", "line-control": "#7F93AC",
    "ink": "#E8EFF7", "ink2": "#9FB3C8",
    "accent": "#38BDD4", "accent-tint": "#0C3A47",
    "ok": "#34D399", "ok-soft": "#06301F",
    "warn": "#FBBF24", "warn-soft": "#3A2A08",
    "bad": "#FB7185", "bad-soft": "#3D1220",
}

TEXT_LIGHT = [
    ("body", "ink", "bg"), ("body on card", "ink", "surface"),
    ("secondary", "ink2", "bg"), ("secondary on card", "ink2", "surface"),
    ("secondary on inset", "ink2", "surface2"),
    ("accent as text", "accent", "surface"),
    ("white on accent fill", "#FFFFFF", "accent"),
    ("white on accent hover", "#FFFFFF", "accent-hover"),
    ("white on app bar", "#FFFFFF", "brand"),
    ("white on bar gradient end", "#FFFFFF", "brand2"),
    ("accent on its tint", "accent", "accent-tint"),
    ("SLA ok on card", "ok", "surface"), ("SLA ok on tint", "ok", "ok-soft"),
    ("SLA warn on card", "warn", "surface"), ("SLA warn on tint", "warn", "warn-soft"),
    ("SLA bad on card", "bad", "surface"), ("SLA bad on tint", "bad", "bad-soft"),
    ("white on ok fill", "#FFFFFF", "ok"),
    ("white on bad fill", "#FFFFFF", "bad"),
    ("neutral chip", "ink2", "surface2"),
]

TEXT_DARK = [
    ("body", "ink", "bg"), ("body on card", "ink", "surface"),
    ("secondary on card", "ink2", "surface"),
    ("secondary on inset", "ink2", "surface2"),
    ("accent as text", "accent", "surface"),
    ("accent on its tint", "accent", "accent-tint"),
    ("SLA ok on card", "ok", "surface"), ("SLA ok on tint", "ok", "ok-soft"),
    ("SLA warn on card", "warn", "surface"), ("SLA warn on tint", "warn", "warn-soft"),
    ("SLA bad on card", "bad", "surface"), ("SLA bad on tint", "bad", "bad-soft"),
    ("neutral chip", "ink2", "surface2"),
]

NONTEXT_LIGHT = [
    ("control border on card", "line-control", "surface"),
    ("control border on page", "line-control", "bg"),
    ("focus ring on card", "accent", "surface"),
    ("focus ring on page", "accent", "bg"),
    ("ok meter on track", "ok", "surface2"),
    ("warn meter on track", "warn", "surface2"),
    ("bad meter on track", "bad", "surface2"),
    ("chart bar on track", "accent", "surface2"),
]

NONTEXT_DARK = [
    ("control border on card", "line-control", "surface"),
    ("focus ring on card", "accent", "surface"),
    ("chart bar on track", "accent", "surface2"),
]


def run(title, palette, checks, threshold):
    print(f"\n{'=' * 68}\n{title}   (needs {threshold}:1)\n{'=' * 68}")
    failures = []
    for name, fg, bg in checks:
        f = palette.get(fg, fg)
        b = palette.get(bg, bg)
        r = ratio(f, b)
        passed = r >= threshold
        if not passed:
            failures.append((title, name, f, b, r))
        print(f"  {name:<26} {f} on {b}  {r:5.2f}:1  {grade(r):<9} "
              f"{'pass' if passed else '** FAIL **'}")
    return failures


def main():
    failures = []
    failures += run("LIGHT MODE · text", LIGHT, TEXT_LIGHT, 4.5)
    failures += run("DARK MODE · text", DARK, TEXT_DARK, 4.5)
    failures += run("LIGHT MODE · non-text UI", LIGHT, NONTEXT_LIGHT, 3.0)
    failures += run("DARK MODE · non-text UI", DARK, NONTEXT_DARK, 3.0)

    total = len(TEXT_LIGHT) + len(TEXT_DARK) + len(NONTEXT_LIGHT) + len(NONTEXT_DARK)
    print(f"\n{'=' * 68}")
    if failures:
        print(f"{len(failures)} of {total} pairs FAIL:")
        for t, n, f, b, r in failures:
            print(f"  - [{t}] {n}: {f} on {b} = {r:.2f}:1")
        raise SystemExit(1)
    print(f"All {total} colour pairs pass WCAG 2.1 AA.")


if __name__ == "__main__":
    main()
