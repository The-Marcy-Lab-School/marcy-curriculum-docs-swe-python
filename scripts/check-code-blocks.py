#!/usr/bin/env python3
"""Run every Python code block in a lesson the way the LMS runs it, and report each block that fails.

Usage:   python3.14 scripts/check-code-blocks.py [--show] <file.md> [<file.md> ...]
Example: python3.14 scripts/check-code-blocks.py mod-2-oop-python/6-functions-as-values-hof.md

The LMS runs each ```python, ```py or ```python3 block in a fresh interpreter. Before
the block, it runs the hidden setups named in a comment on the line above the fence
(or above the {% code %} line that wraps the fence):

    <!-- uses: event, find-events -->

Each setup is defined once on the same page, in an HTML comment:

    <!-- setup: event
    from datetime import date
    ...
    -->

A block marked with <!-- not-runnable --> is skipped. authoring-guide.md describes
the full format.

The script prints one line for each failing block: the file, the line of the opening
fence, and the last line of the error. Errors that a lesson teaches will appear in
this list, and so will blocks that call input(), because the script gives them no
keyboard input. Add --show to print every block's output, to compare against its
output comments. Run it with the Python version fellows install, so that the results
match what fellows see.
"""

import os
import re
import subprocess
import sys
import tempfile

FENCE = re.compile(r'^(\s*)```(python|py|python3)\s*$')
FENCE_END = re.compile(r'^\s*```\s*$')
SETUP_START = re.compile(r'^<!-- setup: ([a-z0-9-]+)\s*$')
USES = re.compile(r'^<!-- uses: ([a-z0-9, -]+) -->$')
NOT_RUNNABLE = '<!-- not-runnable -->'


def read_setups(lines):
    """Map each setup name on the page to its code."""
    setups = {}
    i = 0
    while i < len(lines):
        start = SETUP_START.match(lines[i])
        if start:
            j = i + 1
            while lines[j].strip() != '-->':
                j += 1
            setups[start.group(1)] = '\n'.join(lines[i + 1:j])
            i = j
        i += 1
    return setups


def comment_above(lines, fence_index):
    """The line holding a block's comment: directly above the fence, or above its {% code %} wrapper."""
    above = fence_index - 1
    if lines[above].strip().startswith('{% code'):
        above -= 1
    return lines[above].strip()


def run(code, folder):
    with open(os.path.join(folder, 'block.py'), 'w') as f:
        f.write(code)
    try:
        return subprocess.run(
            [sys.executable, '-I', 'block.py'],
            cwd=folder, capture_output=True, text=True, timeout=5, stdin=subprocess.DEVNULL,
        )
    except subprocess.TimeoutExpired:
        return None


def check(path, show):
    lines = open(path).read().split('\n')
    setups = read_setups(lines)
    # a setup may depend on another setup, so setups only run in front of a block
    for name, code in setups.items():
        # only a top-level print() runs when the setup runs; one inside a method is fine
        if re.search(r'^print\(', code, re.MULTILINE):
            print(f'{path}  setup {name!r} contains print()')
    i = 0
    while i < len(lines):
        fence = FENCE.match(lines[i])
        if not fence:
            i += 1
            continue
        indent = len(fence.group(1))
        j = i + 1
        while not FENCE_END.match(lines[j]):
            j += 1
        above = comment_above(lines, i)
        if above != NOT_RUNNABLE:
            uses = USES.match(above)
            names = [name.strip() for name in uses.group(1).split(',')] if uses else []
            missing = [name for name in names if name not in setups]
            if missing:
                print(f'{path}:{i + 1}  unknown setup {missing}')
            block = '\n'.join(line[indent:] for line in lines[i + 1:j])
            code = '\n\n'.join([setups[name] for name in names if name in setups] + [block])
            with tempfile.TemporaryDirectory() as folder:
                result = run(code, folder)
            if result is None:
                print(f'{path}:{i + 1}  TIMEOUT')
            elif result.returncode:
                print(f'{path}:{i + 1}  {result.stderr.strip().splitlines()[-1]}')
            if show and result is not None:
                print(f'--- {path}:{i + 1}  {lines[i + 1].strip()[:60]}')
                print(result.stdout.rstrip())
        i = j + 1


if __name__ == '__main__':
    show = '--show' in sys.argv
    paths = [arg for arg in sys.argv[1:] if arg != '--show']
    if not paths:
        print(__doc__)
        sys.exit(1)
    for path in paths:
        check(path, show)
