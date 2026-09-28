#!/usr/bin/env python3
"""Copy each chapter's Key Terms section into the module's learning-objectives-key-terms.md.

Usage:  python3 scripts/sync-key-terms.py <module-dir>
Example: python3 scripts/sync-key-terms.py mod-1-python-fundamentals

In learning-objectives-key-terms.md, an entry that should track a chapter carries a
marker line right after its heading:

    <!-- key-terms-from: 3-functions.md -->

Everything between the line "**Key terms**" and the line "**You will be able to…**"
in that entry is replaced with the chapter's "Key Terms" (or "Key Terms and Commands")
section, verbatim. Entries
without a marker (the case study, the project) are left alone. Run it after any
chapter's Key Terms section changes. Add --check to report without writing.
"""

import os
import re
import sys

MARKER = re.compile(r"^<!-- key-terms-from: (\S+) -->$", re.M)
KEY_TERMS_HEADING = re.compile(r"^## Key Terms(?: and Commands)?\s*$", re.M)
NEXT_HEADING = re.compile(r"^## ", re.M)


def key_terms_section(chapter_text):
    """The body of the chapter's Key Terms section, stripped of surrounding blank lines."""
    m = KEY_TERMS_HEADING.search(chapter_text)
    if not m:
        return None
    rest = chapter_text[m.end():]
    n = NEXT_HEADING.search(rest)
    body = rest[: n.start()] if n else rest
    # Some chapters repeat the label as a bold line inside the section; the
    # document supplies its own label, so drop it.
    body = re.sub(r"^\s*\*\*Key Terms\*\*\s*\n", "", body, count=1)
    return body.strip("\n")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    module = args[0]
    doc_path = os.path.join(module, "learning-objectives-key-terms.md")
    doc = open(doc_path, encoding="utf-8").read()

    out = doc
    changed = []
    for marker in list(MARKER.finditer(doc)):
        chapter = marker.group(1)
        chapter_text = open(os.path.join(module, chapter), encoding="utf-8").read()
        terms = key_terms_section(chapter_text)
        if terms is None:
            print(f"  {chapter}: no Key Terms section, entry left alone")
            continue
        start = out.index("**Key terms**", out.index(marker.group(0)))
        end = out.index("**You will be able to…**", start)
        block = "**Key terms**\n\n" + terms + "\n\n"
        if out[start:end] != block:
            out = out[:start] + block + out[end:]
            changed.append(chapter)

    if changed:
        print("updated from: " + ", ".join(changed))
        if not check:
            open(doc_path, "w", encoding="utf-8").write(out)
        else:
            sys.exit(1)
    else:
        print("already current")


if __name__ == "__main__":
    main()
