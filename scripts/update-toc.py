#!/usr/bin/env python3
"""Normalise headings and regenerate the table of contents in a Markdown file.

Two jobs, in order:

1. Replace " & " with " and " in every heading. A bare ampersand is dropped
   entirely from a GitBook anchor, so "Key Terms & Commands" publishes with the
   broken anchor "#key-terms--commands". Any link pointing at an anchor that
   changes is rewritten to match, across every file passed in the same run.
2. Rebuild the table of contents from the corrected headings.

Reproduces what the "Markdown All in One" VS Code extension writes on save,
so that running this and then saving the file in the editor produces no change.
Settings it matches: markdown.extension.toc.levels = "2..6", unordered list
marker "-", GitHub slugs, two-space indent per level. Ampersands are escaped
as "\\&" to match the Prettier pass that runs on save alongside it.

Usage:
  python3 scripts/update-toc.py <file.md> [<file.md> ...]
  python3 scripts/update-toc.py --check <file.md> ...   # report, do not write
"""

import re
import sys

MIN_LEVEL, MAX_LEVEL = 2, 6
MARKER = "-"
INDENT = "  "

# The line introducing the list, in the forms this curriculum uses.
TOC_HEADER = re.compile(
    r"^(?:\*\*Table of Contents\*\*:?|\*\*Table of Contents:\*\*|#{1,6}\s+Table of Contents:?)\s*$", re.M)
LIST_LINE = re.compile(r"^\s*[-*+]\s+\[.*\]\(.*\)\s*$")
HEADING = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*$", re.M)


def strip_code(text):
    return re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)


def slugify(title):
    """GitHub's algorithm: lowercase, drop all but word characters, spaces and
    hyphens, then turn spaces into hyphens. Backticks, punctuation and symbols
    disappear, which is why '`>>`' contributes nothing but leaves its space."""
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s)


def link_text(title):
    """Prettier escapes a bare ampersand in link text, but leaves one inside an
    inline code span alone: "Key Terms \\& Commands", yet "`&&`" unchanged. Split
    on code spans and escape only the prose between them."""
    parts = re.split(r"(`[^`]*`)", title)
    return "".join(p if p.startswith("`") else p.replace("&", r"\&") for p in parts)


AMPERSAND = re.compile(r"(?<=\s)&(?=\s)")
LOOSE_AMPERSAND = re.compile(r"\S&|&\S")


def outside_code(title):
    """The parts of a heading that are not inside an inline code span."""
    return "".join(x for x in re.split(r"(`[^`]*`)", title) if not x.startswith("`"))


def fix_ampersands(title):
    """Replace " & " with " and ", but never inside inline code — "`&&`" is a
    shell operator, not a conjunction. Returns the new title and a warning for
    any ampersand without surrounding spaces, such as "Q&A", which cannot be
    substituted without mangling the word."""
    warning = None
    if LOOSE_AMPERSAND.search(outside_code(title)):
        warning = title
    parts = re.split(r"(`[^`]*`)", title)
    return "".join(p if p.startswith("`") else AMPERSAND.sub("and", p)
                   for p in parts), warning


def normalise_headings(text):
    """Rewrite headings at every level, and report which anchors changed."""
    renames, warnings = {}, []

    def replace(match):
        hashes, title = match.group(1), match.group(2)
        new, warning = fix_ampersands(title)
        if warning:
            warnings.append(warning)
        if new != title:
            renames[slugify(title)] = slugify(new)
        return "%s %s" % (hashes, new)

    # Headings only outside fenced code, so a shell comment is never rewritten.
    chunks = re.split(r"(^```.*?^```)", text, flags=re.S | re.M)
    out = [c if c.startswith("```") else HEADING.sub(replace, c) for c in chunks]
    return "".join(out), renames, warnings


def retarget_links(text, renames):
    """Point links at the new anchors, so fixing a heading does not break a
    cross-reference somewhere else in the document."""
    def replace(match):
        before, anchor, after = match.group(1), match.group(2), match.group(3)
        return before + renames.get(anchor, anchor) + after
    return re.sub(r"(\]\([^)]*#)([^)\s]+)(\))", replace, text)


def build(text):
    lines = []
    for hashes, title in HEADING.findall(strip_code(text)):
        level = len(hashes)
        if MIN_LEVEL <= level <= MAX_LEVEL:
            lines.append("%s%s [%s](#%s)" % (
                INDENT * (level - MIN_LEVEL), MARKER, link_text(title), slugify(title)))
    return lines


def rewrite(text, batch_renames=None):
    """Normalise headings, retarget links, then replace the list under the
    table-of-contents header."""
    text, renames, warnings = normalise_headings(text)
    if batch_renames is not None:
        batch_renames.update(renames)
    text = retarget_links(text, batch_renames if batch_renames is not None else renames)

    m = TOC_HEADER.search(text)
    if not m:
        return text, "headings normalised; no table-of-contents header", warnings

    lines = text.split("\n")
    header_line = text[:m.start()].count("\n")

    start = header_line + 1
    while start < len(lines) and lines[start].strip() == "":
        start += 1
    end = start
    while end < len(lines) and (LIST_LINE.match(lines[end]) or lines[end].strip() == ""):
        if lines[end].strip() == "" and end + 1 < len(lines) and not LIST_LINE.match(lines[end + 1]):
            break
        end += 1
    if end == start:
        return text, "headings normalised; no list under the header", warnings

    new = build(text)
    if lines[start:end] == new:
        return text, "already current (%d entries)" % len(new), warnings
    return "\n".join(lines[:start] + new + lines[end:]), "updated to %d entries" % len(new), warnings


def main():
    args = [a for a in sys.argv[1:] if a != "--check"]
    check = "--check" in sys.argv
    if not args:
        sys.exit(__doc__)
    changed = 0
    # Collected across the whole run so a heading renamed in one file also fixes
    # the links pointing at it from another file in the same batch.
    batch_renames = {}
    for path in args:
        with open(path, encoding="utf-8") as handle:
            rewrite(handle.read(), batch_renames)
    for path in args:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        new, note, warnings = rewrite(text, batch_renames)
        for w in warnings:
            print("%-56s CHECK BY HAND  ampersand with no spaces: %s" % (path, w))
        if new != text:
            changed += 1
            if not check:
                with open(path, "w", encoding="utf-8") as handle:
                    handle.write(new)
        print("%-56s %s%s" % (path, note, "  (not written)" if check and new != text else ""))
    if batch_renames:
        print("\n%d anchor(s) changed. A link from a file outside this run will" % len(batch_renames))
        print("still point at the old anchor — pass those files in too:")
        for old, new in sorted(batch_renames.items()):
            print("  #%s  ->  #%s" % (old, new))
    if check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
