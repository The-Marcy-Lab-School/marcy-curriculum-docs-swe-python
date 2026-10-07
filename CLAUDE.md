# CLAUDE.md — Marcy Curriculum Docs (Python)

## What this repository is

This is the GitBook curriculum documentation for the Marcy Lab School fellowship — a textbook that fellows read. It is not where assignments, assessments, rubrics, or grading live; those are separate artifacts that this documentation supports.

The repository currently holds a mix of converted Python content and the original JavaScript content still awaiting conversion. `SUMMARY.md` marks which is which.

## The JavaScript original is next door

`../marcy-curriculum-docs/` is the unmodified JavaScript curriculum, and its file paths mirror this repository's exactly. For any document being converted, `../marcy-curriculum-docs/<same path>` is the original. Read it before converting, and compare against it after. Do not use git history for this — the sibling repository stays put when this one is committed.

## What conversion means

Replace the JavaScript with Python. Keep everything else.

Specifically, three things carry over and must be actively protected rather than assumed:

**The voice.** Ben wrote the original documents in a particular register — direct, second person, plain, occasionally funny, willing to say "wayyy faster" in a heading. Converted prose should be indistinguishable in voice from the paragraph above and below it. When a sentence survives the conversion unchanged, leave it unchanged; do not improve it.

**The pedagogical devices.** The hidden `<details>` questions, the callouts, the analogies (the abacus, the camera and GitHub, the "you are here" map icon), the comparison tables, the learning objectives, the challenges, the images. These are teaching decisions someone made deliberately. **They must survive, though not necessarily in the same place.** A hidden question may move to a different section, merge with another, or attach to a different example — that is fine. Silently losing one is not. If a device genuinely cannot survive because the concept it taught does not exist in Python, say so explicitly and say what replaced it.

**The concept coverage.** Every idea taught in the original is taught in the conversion, unless a decision was made to drop it. A dropped idea is always a stated decision, never an omission.

## The review contract

Ben reviews every converted document. His time is the constraint, so the goal is that he can scan a document, approve it or ask for changes, and move on. **After drafting or converting any document, produce a conversion report before saying the work is done.** Never skip this and never ask whether it is wanted.

Step one, run the tool:

```sh
python3 scripts/conversion-report.py <path-relative-to-repo-root>
```

It reports the objective half — which sections and which pedagogical devices exist in each version, compared as sets so that moving something does not read as losing it, plus leftover JavaScript, code fence languages, and broken links. Show its output.

Step two, write the three things the tool cannot judge:

**Decisions.** One line for every section the tool reports as DROPPED or ADDED, and for every device whose count fell. Say what happened and why: moved into another section, merged, replaced by a Python equivalent, or deliberately cut. A DROPPED line with no explanation is an unfinished report. Add any decision that will recur across chapters to `conversion-decisions.md` so later chapters make the same call.

**Voice check.** Quote two or three sentences of newly written prose beside two or three from the original, so Ben can judge the register himself rather than take a claim that it matches.

**Look here first.** Three to five specific places, ranked, each with a `file.md:line` reference and one sentence on why it needs his eyes. Rank by risk: wholly new prose that no original existed to check against outranks a mechanical substitution. This section is the point of the report — it is what lets him scan rather than read.

## The module document comes first

Once every chapter of a module has been converted, write `learning-objectives-key-terms.md` in the module's directory before reporting the module as done. It is the first thing Ben reviews for a module, before any chapter, because it shows in two pages whether the module teaches the right things in the right order.

It has one entry per chapter, including the case study and the project, in chapter order. Each entry has three parts:

- **Key terms**, copied verbatim from the chapter's Key Terms section, definitions included. `scripts/sync-key-terms.py <module-dir>` does the copying: each entry carries a `<!-- key-terms-from: <chapter>.md -->` marker under its heading, and the script replaces the block between `**Key terms**` and `**You will be able to…**` with the chapter's section. Edit terms in the chapter, never in this document, and rerun the script. If a chapter has no Key Terms section, add one to the chapter first.
- **Learning objectives**, which the chapters do not state and which this document supplies. Write each as a "You will be able to…" bullet that could be checked with a short task: predict this output, write this function, explain this error. Each bullet begins with a Bloom verb and follows "Writing Learning Objectives" in the repository's root `CLAUDE.md`. Follow the chapter's predict-then-run boxes and challenges closely, since those are the tasks an instructor will reach for. Split each list into _In the session_, the three or four objectives the 90-minute lecture must introduce, practice, and check, and _By the end of the module_, the rest, which the reading, the assignments, and the project carry.

- **Exit ticket**, a `### Exit Ticket` subsection placed after the objectives list. An instructor gives it at the end of the session, and an AI model later receives the ticket's learning objective, its question, its two examples, and one fellow's response, and returns short feedback and the understanding level the fellow reached. Write every part so that it gives that model enough to grade by. The ticket has four parts, in this order:
  - **Learning Objective** — one sentence that names the most important high-level takeaway of the lesson, following "Writing Learning Objectives" in the repository's root `CLAUDE.md`: "Fellows will be able to [Bloom verb] …". The objective describes the lesson, not the question, so it names no scenario-specific condition: write "predict the values produced by expressions and explain how operator precedence and the data types determine that result", not "given a program that averages two quiz scores, predict…". The question supplies the scenario, and the same objective should still fit if the question were replaced by a different scenario that tests the same idea. The objective is not one of the objectives in the list above. It states the idea that the listed objectives add up to, such as how the pieces relate or why a practice exists, so its verb sits at the Understand level or higher.
  - **Question** — one question built on a small concrete scenario (a file tree, a sequence of commands, a short piece of code, or a situation involving teammates) that asks the fellow to predict what happens and to explain why. The "why" is what separates the two levels, so the question must ask for it. A fellow who understands the lesson should be able to answer the question in a paragraph. When the lesson's takeaway is a reason rather than a behaviour, the question may ask the fellow to compare two ways of working instead of predicting an output.
  - **Level 2 Example** — a response at the unistructural and multistructural levels of the SOLO framework. The response is correct, or nearly correct, and names the right facts or steps, but it does not connect them or explain the mechanism. The response is usually one or two sentences long.
  - **Level 3 Example** — a response at the relational and extended abstract levels of the SOLO framework. The response reaches the same answer and explains the chain of cause and effect that produces it, using the lesson's key terms correctly. Where the question includes a variation, the response carries the explanation over to that variation.

  Write both examples in a fellow's voice, in plain first person or second person, and never make the Level 3 example longer only by adding facts that do not connect to the answer. Use only commands, terms, and analogies that the chapter itself teaches. If the question names a person, choose a name and refer to that person by name rather than by a pronoun. `mod-0-command-line-interfaces-git-and-github/learning-objectives-key-terms.md` is the model for exit tickets. The sync script replaces only the Key terms block, so it leaves exit tickets alone.

`mod-1-python-fundamentals/learning-objectives-key-terms.md` is the model for key terms and objectives. Rerun `python3 scripts/sync-key-terms.py <module-dir>` whenever a chapter's Key Terms section changes; `--check` reports without writing.

## Tables of contents

**Never put a bare `&` in a heading. Write "and".** GitBook drops the ampersand when it builds an anchor, so "Key Terms & Commands" publishes with the broken anchor `#key-terms--commands` and every link to it fails. `scripts/update-toc.py` makes this substitution automatically at every heading level and retargets any link pointing at an anchor it changed. An ampersand inside inline code is left alone, because `` `&&` `` is a shell operator rather than a conjunction, and an ampersand with no surrounding spaces such as "Q&A" is reported for a person to decide rather than mangled into "QandA".

Do not write or edit a table of contents by hand. The "Markdown All in One" extension regenerates them when Ben saves a file, and `scripts/update-toc.py` reproduces its output exactly — it has been checked byte-for-byte against 53 files the extension itself generated, including two with 34 entries.

After changing any heading, run:

```sh
python3 scripts/update-toc.py <file.md> [<file.md> ...]
```

Add `--check` to report without writing; it exits non-zero when something is out of date, so it also works as a guard. The script matches `markdown.extension.toc.levels` of `2..6`, a `-` marker, two-space indent, GitHub slugs, and the Prettier pass that escapes a bare `&` but leaves one inside inline code alone. Do not spend tokens reproducing a table of contents in a message or an edit — run the script.

## Verify before claiming

These documents contain instructions fellows follow literally on their own machines. Run the commands before writing that they work, and read the live page before quoting a version number, a filename, or a repository statistic. When something cannot be verified here — anything needing a Windows machine, a clean install, or a screenshot — say so plainly and put it on the list of things Ben has to check, rather than asserting it.
