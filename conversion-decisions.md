# Conversion Decisions

Decisions that recur across chapters, recorded once so that every chapter makes the same call. When converting a document, read this first. When a new decision comes up that will apply to more than one chapter, add it here.

This is a record of what the curriculum does, not a history of what it used to do.

## Language and tooling

**Running a program.** `python3 [filename.py]`. The command always carries the 3, because plain `python` is undefined on both macOS and Ubuntu. Any chapter introducing a runnable file uses this form.

**Environment and packages.** `pip` and `venv`, installed natively: the download button on the python.org macOS page for Mac, and `sudo apt install python3 python3-pip python3-venv` on Ubuntu 26.04 LTS under WSL. `uv` is introduced later in the fellowship, around FastAPI or wherever dependency management first becomes genuinely painful, and must not appear in Q1 material.

**Python version.** 3.14 across the cohort. Patch numbers differ by platform — 3.14.7 on Mac, 3.14.3 on Ubuntu — and that is fine. Python 3.15 was released on 1 October 2026, so the Mac instruction needs rechecking; the setup document guards against it at the `python3 --version` step.

**The interpreter, named.** Where the original said "Node", the conversion says "the Python interpreter" and defines it as the program that reads a `.py` file and executes it.

## Style inherited from the original

**Code fences are frequently untagged in the original**, and conversions keep that. Do not run a pass adding language tags; it is not a defect.

**Second person, direct address, contractions allowed.** Match the paragraph above and below.

**Sentences that survive conversion are left exactly as written**, including the ones that read a little loose. Improving prose that did not need converting is how a document quietly stops sounding like Ben wrote it.

## Pedagogical devices

**Hidden `<details>` questions from the original are kept verbatim** where the concept survives. Three of them in the command-line chapter carried over untouched.

**Predict, then run** is a device added by the conversion, not inherited. It is a `{% hint style="warning" %}` containing a command, an instruction to write the prediction down before running anything, and the answer inside `<details>`. It exists because prediction before execution is the assessment the Q1-to-Q2 transition runs on, and the habit has to be practised daily in the textbook for the assessment to have anything to measure. Use it only for things a fellow can be genuinely wrong about — never where the answer appears in the paragraph above.

**Broken GitBook syntax gets fixed when encountered.** Two callouts in the command-line chapter had escaped braces and were rendering as literal `\{% hint style="info" %\}` text. Fix these; they are not stylistic choices.

## Examples and references

**Real-repository examples point at Python projects.** The command-line chapter's "look at a real repository" exercise moved from `nodejs/node` to `pallets/flask`, which is readable Python and foreshadows Q2. Statistics quoted about a repository must be read off the live page, never adjusted by guess.

**Screenshots showing JavaScript tools need recapturing, not relabelling.** The Node REPL screenshot has no Python equivalent in the repository yet.

## Structure

**Directory names keep the `mod-N-topic` shape.** A directory is renamed only when its unit is converted, and only if the name mentions the language. Quarters appear as framing in `README.md` and `SUMMARY.md`, not as directories.

**Nothing enters `SUMMARY.md` without a file behind it.** Unconverted modules sit under their own heading rather than being listed as though they were ready.

## AI content

**The AI policy is stated as mode, not prohibition** — tutor mode first, implementer mode once a fellow judges the skill of expectation to be there, with the program supplying prediction-accuracy and defect-detection evidence so the judgement is informed. Chapters that mention AI use should be consistent with `guidelines-and-policies/ai-policy.md` and should not restate its rules, which drift.

**Inline autocomplete is off in Q1** and returns once a fellow works from a written specification. Chat is unrestricted throughout Q1.
