#!/usr/bin/env python3
"""Compare a converted Python document against its JavaScript original.

Usage:  python3 scripts/conversion-report.py <path-relative-to-repo-root> [<original-path-relative-to-old-repo>]
Example: python3 scripts/conversion-report.py mod-0-command-line-interfaces-git-and-github/1-clis.md
Example: python3 scripts/conversion-report.py mod-1-python-fundamentals/8-lists.md mod-1-javascript-fundamentals/6-arrays.md

The second argument is for a converted document whose directory or file name
differs from the original's. Without it, the same relative path is used.

Reports the objective half of a conversion review: which headings and which
pedagogical devices exist in each version, and what JavaScript residue is left.
Placement is ignored throughout — a device that moved still counts as kept.
Judgment (was a decision right, does the voice match) is not attempted here.
"""

import os
import re
import sys

OLD_REPO = "../marcy-curriculum-docs"

# Things that teach, as opposed to things that merely inform. Each entry is a
# label and a pattern whose matches are listed so they can be compared as sets.
DEVICES = [
    ("Hidden Q&A (<details>)", re.compile(r"<summary>(.*?)</summary>", re.S)),
    ("Callout ({% hint %})",   re.compile(r"\{%\s*hint style=\"(\w+)\"\s*%\}")),
    ("Image / diagram",        re.compile(r"!\[[^\]]*\]\(([^)]+)\)")),
    ("Challenge prompt",       re.compile(r"^.*\*\*(?:Challenge|Quiz|Predict[^*]*)\*\*.*$", re.M)),
    ("Learning objectives",    re.compile(r"You will be able to")),
    ("Follow-along repo",      re.compile(r"https://github\.com/The-Marcy-Lab-School/([\w.-]+)")),
]

# Left-over JavaScript. Flagged, never failed: some of these are legitimate
# (a sentence explaining that browsers run JavaScript, for instance).
RESIDUE = [
    ("node / nodejs",   re.compile(r"\bnode(?:js)?\b", re.I)),
    ("npm / nvm",       re.compile(r"\bn[pv]m\b", re.I)),
    (".js filename",    re.compile(r"[\w-]+\.js\b")),
    ("console.log",     re.compile(r"console\.log")),
    ("arrow function",  re.compile(r"=>")),
    ("const / let",     re.compile(r"\b(?:const|let)\s+\w+\s*=")),
    ("undefined",       re.compile(r"\bundefined\b")),
    ("JavaScript",      re.compile(r"\bJavaScript\b")),
    ("JS-only tooling", re.compile(r"\b(?:Jest|React|Express|Knex|Vite|ESLint|Prettier)\b")),
    ("```js fence",     re.compile(r"^```\s*(?:js|javascript)\s*$", re.M)),
]

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.M)
FENCE = re.compile(r"^```\s*(\w+)?\s*$", re.M)


def read(path):
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def strip_code(text):
    """Remove fenced code so prose scans do not match code samples."""
    return re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)


def headings(text):
    # Strip fenced code first: a shell comment such as "# Run a file" is not a
    # heading, and counting it as one reports a section that never existed.
    return [(len(h), t) for h, t in HEADING.findall(strip_code(text))]


def normalise(title):
    """Compare heading titles loosely, so a rename that keeps the concept matches."""
    t = title.lower()
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    stop = {"the", "a", "an", "and", "with", "to", "of", "in", "for", "your", "using", "part"}
    return " ".join(w for w in t.split() if w not in stop)


def section(title, rows):
    print("\n" + title)
    print("-" * len(title))
    if not rows:
        print("  (none)")
    for row in rows:
        print("  " + row)


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    rel = sys.argv[1]
    old_rel = sys.argv[2] if len(sys.argv) == 3 else rel
    new = read(rel)
    if new is None:
        sys.exit("No converted file at %s" % rel)
    old = read(os.path.join(OLD_REPO, old_rel))

    print("=" * 72)
    print("CONVERSION REPORT  %s" % rel)
    print("=" * 72)

    if old is None:
        print("\nNo JavaScript original at %s/%s." % (OLD_REPO, old_rel))
        print("This document is new or was rewritten from scratch, so there is no")
        print("coverage baseline. Review it as original writing.")
    else:
        print("\n%d lines in the original  ->  %d lines now" % (
            old.count("\n") + 1, new.count("\n") + 1))

        old_h, new_h = headings(old), headings(new)
        old_map = {normalise(t): t for _, t in old_h}
        new_map = {normalise(t): t for _, t in new_h}

        dropped = [old_map[k] for k in old_map if k not in new_map]
        added = [new_map[k] for k in new_map if k not in old_map]
        kept = len(old_map) - len(dropped)

        section("SECTIONS  (%d of %d kept)" % (kept, len(old_map)),
                ["DROPPED  %s" % t for t in dropped] +
                ["ADDED    %s" % t for t in added])
        if dropped:
            print("\n  Each DROPPED line is a concept that was in the original and is not")
            print("  in a same-named section now. It may have moved into another section,")
            print("  been merged, or been deliberately cut — say which, for each one.")

        print("\nPEDAGOGICAL DEVICES  (placement ignored)")
        print("-" * 39)
        print("  %-26s %8s %8s" % ("device", "original", "now"))
        for label, pattern in DEVICES:
            o = pattern.findall(old)
            n = pattern.findall(new)
            flag = "  <-- fewer" if len(n) < len(o) else ""
            print("  %-26s %8d %8d%s" % (label, len(o), len(n), flag))

        # Hidden questions get listed, not just counted: they are the densest
        # teaching device in these documents and the easiest to quietly lose.
        q = DEVICES[0][1]
        old_q = [re.sub(r"<[^>]+>|\*\*", "", s).strip() for s in q.findall(old)]
        new_q = [re.sub(r"<[^>]+>|\*\*", "", s).strip() for s in q.findall(new)]
        section("HIDDEN QUESTIONS IN THE ORIGINAL (%d)" % len(old_q), old_q)
        section("HIDDEN QUESTIONS NOW (%d)" % len(new_q), new_q)

    prose = strip_code(new)
    found = []
    for label, pattern in RESIDUE:
        hits = pattern.findall(new if "fence" in label else prose)
        if hits:
            sample = ", ".join(sorted({str(h) for h in hits})[:4])
            found.append("%-18s %3d  e.g. %s" % (label, len(hits), sample))
    section("JAVASCRIPT RESIDUE  (flagged, not necessarily wrong)", found)

    langs = [l or "(none)" for l in FENCE.findall(new)]
    counts = {l: langs.count(l) for l in set(langs)}
    section("CODE FENCE LANGUAGES",
            ["%-12s %d" % (l, c) for l, c in sorted(counts.items())])

    broken = []
    base = os.path.dirname(rel)
    # GitBook wraps targets in <> when the filename contains parentheses,
    # e.g. ![](<../.gitbook/assets/merge-conflict (1).png>) — handle both forms.
    for bracketed, plain in re.findall(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^)\s]+))", new):
        target = bracketed or plain
        if target.startswith(("http", "#", "mailto")):
            continue
        path = os.path.normpath(os.path.join(base, target.split("#")[0]))
        if path and not os.path.exists(path):
            broken.append(target)
    section("BROKEN LOCAL LINKS AND IMAGES", broken)
    print()


if __name__ == "__main__":
    main()
