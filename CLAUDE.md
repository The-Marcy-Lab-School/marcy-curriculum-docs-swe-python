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

## Verify before claiming

These documents contain instructions fellows follow literally on their own machines. Run the commands before writing that they work, and read the live page before quoting a version number, a filename, or a repository statistic. When something cannot be verified here — anything needing a Windows machine, a clean install, or a screenshot — say so plainly and put it on the list of things Ben has to check, rather than asserting it.
