# The AI-Powered Software Engineer

- [Master Curriculum Design Document — F26 Transition Year](#master-curriculum-design-document--f26-transition-year)
- [Executive Summary](#executive-summary)
  - [How to use this document](#how-to-use-this-document)
- [1. Goal and Constraints](#1-goal-and-constraints)
- [2. Fellowship Arc](#2-fellowship-arc)
  - [Q1 (Months 0–3): Computational Thinking \& Responsible Use of AI](#q1-months-03-computational-thinking--responsible-use-of-ai)
  - [Q2 (Months 3–6): Fullstack \& AI-Assisted Development](#q2-months-36-fullstack--ai-assisted-development)
  - [Q3 (Months 6–9): AI-Led Project Building and Exposure to Systems Design](#q3-months-69-ai-led-project-building-and-exposure-to-systems-design)
  - [Q4 (Months 9–11): Capstone — Real Stakeholder](#q4-months-911-capstone--real-stakeholder)
- [3. Skill Taxonomy](#3-skill-taxonomy)
  - [Group 1 — Foundational Mental Models](#group-1--foundational-mental-models)
  - [Group 2 — Problem Framing \& Product Judgment](#group-2--problem-framing--product-judgment)
  - [Group 3 — Architecture \& Design](#group-3--architecture--design)
  - [Group 4 — Delegation \& Context Engineering](#group-4--delegation--context-engineering)
  - [Group 5 — Verification \& Quality Control](#group-5--verification--quality-control)
  - [Group 6 — Systems, Operations \& Constraints](#group-6--systems-operations--constraints)
  - [Group 7 — Handoff \& Communication](#group-7--handoff--communication)
- [4. Developmental Ladders](#4-developmental-ladders)
  - [4.1 The Taste \& Discernment Ladder](#41-the-taste--discernment-ladder)
    - [Q1 — Recognize obvious quality differences](#q1--recognize-obvious-quality-differences)
    - [Q2 — Justify local choices](#q2--justify-local-choices)
    - [Q3 — Evaluate tradeoffs across a system](#q3--evaluate-tradeoffs-across-a-system)
  - [Q4 — Exercise independent discernment under ambiguity](#q4--exercise-independent-discernment-under-ambiguity)
  - [4.2 The Debugging Ladder](#42-the-debugging-ladder)
    - [Q1 — Orient without panic](#q1--orient-without-panic)
    - [Q2 — Form and test local hypotheses](#q2--form-and-test-local-hypotheses)
    - [Q3 — Trace across boundaries](#q3--trace-across-boundaries)
    - [Q4 — Repair minimally and preserve intent](#q4--repair-minimally-and-preserve-intent)
- [5. Skill-to-Quarter Mapping](#5-skill-to-quarter-mapping)
  - [Q1 — Substrate](#q1--substrate)
  - [Q2 — Delegation Under Supervision](#q2--delegation-under-supervision)
  - [Q3 — AI-Led Systems Exposure](#q3--ai-led-systems-exposure)
  - [Q4 — Capstone](#q4--capstone)
- [6. Assessment Mode Catalogue](#6-assessment-mode-catalogue)
  - [Low cost, high frequency](#low-cost-high-frequency)
  - [Medium cost](#medium-cost)
  - [High cost, use sparingly](#high-cost-use-sparingly)
- [7. Assessment Calendar](#7-assessment-calendar)
  - [Q1](#q1)
  - [Q2](#q2)
  - [Q3](#q3)
  - [Q4](#q4)
- [8. Gates and Transitions](#8-gates-and-transitions)
  - [The Q1→Q2 gate](#the-q1q2-gate)
  - [Handling the Q1 AI policy](#handling-the-q1-ai-policy)
- [9. Build Order for This Year](#9-build-order-for-this-year)
  - [Build now — before Q1 starts](#build-now--before-q1-starts)
  - [Build during Q1 — for Q2](#build-during-q1--for-q2)
  - [Build during Q2 — for Q3](#build-during-q2--for-q3)
  - [Additional build items — from this revision](#additional-build-items--from-this-revision)
  - [Defer — decide with evidence](#defer--decide-with-evidence)
  - [Instrument while building](#instrument-while-building)
- [10. Known Risks](#10-known-risks)

## Master Curriculum Design Document — F26 Transition Year

---

## Executive Summary

If the fellowship is moving from hand-coded full-stack implementation toward AI-assisted product engineering, the curriculum needs to shift from measuring whether fellows can produce code to measuring whether they can frame problems, direct AI, read and critique generated code, verify correctness, and defend technical decisions. This document names the competencies behind that shift and proposes an assessment model that identifies genuine understanding and repeatable engineering process, rather than mistaking polished AI-assisted output for engineering competence.

**The Problem.** The entire software industry is currently struggling with the Juniors-with-AI Paradox. Generative tooling lets early-career engineers ship polished code on day one, while simultaneously masking whether they understand what they built, how to debug it when it breaks, or why specific architectural tradeoffs were made.

**The Marcy Differentiator.** While traditional CS programs double down on abstract theory and bootcamps continue teaching mechanical syntax generation — which AI is rapidly automating — Marcy trains and certifies autonomous engineering judgment. By evaluating prediction before execution, ownership without authorship, and defensible technical reasoning, Marcy produces the rarest and most valuable profile in today's hiring market: junior engineers who can direct, critique, and debug AI-accelerated output with the discernment of engineers years ahead of them.

_Ownership without authorship, in plain language: a fellow remains responsible for every line of code in a project even if they didn't personally write every line of it._

---

### How to use this document

This merges two source documents: the **Curriculum Transition Plan** (vision, constraints, fellowship arc) and the **AI-Assisted Software Engineering Skills** framework (skill taxonomy, assessment modes). It is a design reference, not a syllabus. Sections 1–4 are stable and should change slowly. Sections 5–8 are working design specs for this year. Section 9 is the build queue.

**Integration notes — decisions made in merging, open to revision:**

1. The skills framework was originally written against a PERN/JavaScript assumption. All language-specific content needs to be converted to Python/Flask.
2. The taste-and-discernment progression has been promoted from a sub-note to its own section (§4.1). It is the clearest developmental ladder in the taxonomy, and other skill groups should be calibrated against it rather than assessed as binary have/have-not. As of this revision, debugging has a parallel ladder at §4.2 — §4 as a whole is titled "Developmental Ladders" to hold both.
3. A build-order queue (§9) has been added to reflect the transition plan's staging constraint.
4. Quarter labels are consistent throughout: **Q1** = months 0–3, **Q2** = months 3–6, **Q3** = months 6–9, **Q4** = months 9–11 (capstone).
5. **Revision pass:** Q3 has been restructured from four full-quarter specialization tracks into a rotating systems-module design ("AI-Led Project Building and Exposure to Systems Design"). Technical Interview Prep now threads through Q1–Q3 rather than being absent from the arc. This changes §2, §5 (Q3), §6, §7 (Q1–Q3), §9, and §10 (the DSA-gap risk). Where the restructure resolves or changes a previously flagged risk, that's noted inline rather than silently removed, so the reasoning stays visible.
6. An Executive Summary has been added above this section as an external-facing framing layer — it argues the case for the shift (the "Juniors-with-AI Paradox" and the Marcy differentiator); Sections 1–10 remain the internal design reference.
7. **Second revision pass:** added the Debugging Ladder (§4.2), a direct behavioral definition of "ownership without authorship" for Q4 — see the cross-reference there. Also added two open design questions (Group 2's reframe-as-strength question in §3, Group 4's token-cost-as-standing-expense question in §3) and one build item (§9) generalizing the Q3 cost-module funding question into a program-wide policy question.

---

## 1. Goal and Constraints

**Goal.** Produce fellows fluent in Python and capable of using AI-assisted coding tools to solve ambiguous business problems, owning the full product development process from inception through implementation to iteration.

**Constraints.**

The current program is optimized for a different language and a different end goal, and transition time is limited. Three principles follow:

- **Coherence before perfection.** The first-year plan creates a teachable transition path — meaningful Python fluency, responsible introduction of AI-assisted development, and room for instructors to run experiments and gather evidence about what a Python-native, AI-assisted product engineering program actually requires.
- **Decisions in stages.** The immediate design priority is the first units — Command Line Interface, Computational Thinking, and Object-Oriented Programming — because they determine whether fellows can succeed in everything downstream. Later units get redesigned with evidence from fellow progress and instructor experience.
- **Scope of the first step, not scope of the ambition.** We are not lowering the target. We are managing the first move, using existing curriculum as raw material and letting real constraints force creative, evidence-generating choices.

**The premise underneath all of it.** _Writing code by hand_ is decreasingly necessary as a description of daily work. _Being able to_ write code by hand remains necessary, because every skill in §3 is a verification and judgment skill, and judgment is residue from having built things badly a few times. The curriculum's central problem is manufacturing that residue on a compressed timeline.

---

## 2. Fellowship Arc

### Q1 (Months 0–3): Computational Thinking & Responsible Use of AI

**Python topics:** CLI, Git & GitHub · Python syntax · Python ecosystem (pip, venv, requirements.txt — _confirm this is still the right stack to teach, or whether a modern, more abstracted tool like `uv` now serves the pedagogical goal better_) · OOP (everything is an object)

**AI topics:** Basic AI fluency — how prediction engines work · Prompting · Risks, ecological and ethical implications · Academic impact of reliance · Marcy's AI usage and academic honesty policy

**Technical Interview Prep:** Solving level-1 GCF-style problems using Python's built-in list methods · Array, string, and dictionary manipulation. By the end of the Python unit, instructors should have identified which fellows need targeted support with computational thinking fluency.

**Outcomes.** Fellows can build a CLI application with organized file structure, separation of concerns, and consistent abstraction levels. Fellows can leverage AI as a sparring partner to push their learning and understanding of code — not to generate it for them, and not to shortcut to a quick answer.

**Design intent:** This is the only quarter where hand-writing is the default, which makes it the only quarter that reliably builds _expectation_. Everything in Q2 depends on fellows arriving with a predictive model of what correct code looks like.

**Open questions carried from this design pass:**

- What are the actual operational norms for AI use in Q1 — what does "sparring partner, not generator" look like moment to moment, not just as a policy statement?
- How can AI be used to teach classes and OOP specifically? Fellows need to grasp the basic shape of a class without getting lost in syntax, and need to be able to identify when an implementation is missing something from that shape. Does AI help build that recognition, or does it let fellows skip past the confusion that would otherwise build it?
- How do we deliberately expose fellows to the pain of a poorly designed class, given they won't be hand-writing enough broken ones to feel it by accident at this pace?
- What's the fast, low-noise way to identify who's struggling with computational fluency during Technical Interview Prep, and what precisely they're struggling with? Willingness to talk through an idea out loud may be a better early signal than correctness.

### Q2 (Months 3–6): Fullstack & AI-Assisted Development

**Format:** Given a list of problems, fellows choose one and build a fullstack solution to it — the first quarter where the problem isn't fully handed to them.

**Topics:** HTML & CSS · APIs · Servers (Flask) and Server-Side Rendering · Databases (Postgres, SQL) · Essential tools and libraries (pandas, itertools, etc.)

**AI topics:** Model selection and evaluation · What AI is good at and bad at · Token and context window management · Skills and memory · AI-assisted workflow (research → plan → implement → test → refine → iterate)

**Technical Interview Prep:** Big O · Algorithm patterns (sliding window, two pointers, binary search, sorting) · Abstract data types (linked lists, stacks, queues, trees, recursion).

**Outcomes.** Fellows can build a fullstack SSR application using Flask, HTML/CSS, and Postgres for a stakeholder (_simulated or real — TBD, see §9_). They can create thorough documentation and application architecture and leverage AI to implement their plans. They can communicate technical and product decisions to teammates and their engineering manager. They can form preferences and speak intelligently about their AI workflow. They take ownership over their AI-assisted work product.

**Design intent:** The mode inverts here — AI moves from tutor to implementer. The failure mode inverts with it (see §3, Group 5).

### Q3 (Months 6–9): AI-Led Project Building and Exposure to Systems Design

**Reframed from a four-track specialization quarter into a systems-exposure quarter.** Fellows no longer commit to one of four tracks for the full quarter. Instead, they're given a functioning full-stack CRUD application and asked to leverage AI to quickly assess options and implement a solution across a rotation of systems constraints:

- **Security** — implement an auth strategy that actually protects the application.
- **Testing** — add 10 new features without breaking existing functionality.
- **Cost** — given a fixed budget (e.g. $30 in Anthropic API credits), build a feature that calls the Claude API for recommendations, and refine the approach to minimize cost.
- **Bottlenecks & sandboxing** — safely execute third-party or untrusted code.
- **Deployment & environments** — get it running somewhere real, and configure environment variables correctly across environments.

**Goals.** Move from exposure to ideas (in seminar) to tangible experience (in the build). The skill being drilled is the same across all five modules: develop a mental model of the constraint fast enough to make a decision, articulate that decision, communicate it to AI so it can implement it, and communicate it to a stakeholder to validate it.

**Other general areas to explore.** These four areas are no longer full-quarter commitments — they're domain contexts a fellow can choose to frame their systems-module work within:

1. **Business Applications** — deployed software tools solving operational or stakeholder problems, using whatever stack fits.
2. **Data & Automation Systems** — Python workflows that move, transform, connect, or automate information across systems.
3. **Cloud & Production Systems** — deployment, infrastructure, and reliability practices that make tools usable by real people.
4. **AI-Enabled Products** — applications and workflows using AI/ML capabilities to solve business problems, without assuming fellows become data scientists.

**Structure.** Ideas are introduced in seminar; the assessment requires fellows to demonstrate the skill directly (see Essential Skill below), not just discuss it.

**Essential skill — the 24-hour spec loop.** State the problem → interrogate the stakeholder about requirements → return in 24 hours with a spec → get feedback → return in 24 hours with the tools/approach → implement → present.

**Technical Interview Prep:** Live interview practice.

**Outcomes.** Fellows can follow a systematic process toward a detailed understanding of a problem. They can explore a new domain area and learn a new set of skills in order to articulate a solution. They can communicate technical and product decisions effectively to teammates, engineering managers, and external stakeholders, both technical and non-technical.

**Stakeholder.** Mentors who have solved the problem in the real world and can give direct, experienced feedback: Did you pick the right stack? What mistakes did you make using that stack — file organization, abstraction levels, and so on?

**Design intent.** This still builds ecosystem literacy and the failure catalogue (Group 1) — but now through repeated, tight loops across systems constraints rather than three months embedded in one domain. It also substantially changes the track-equity risk raised in the original design (see §5): a fellow no longer bets a full quarter, and their income, on which track they picked.

### Q4 (Months 9–11): Capstone — Real Stakeholder

**Design intent:** The first time requirements are genuinely ambiguous and shifting, because a real stakeholder supplies them. Problem framing (§3, Group 2) becomes the primary load.

---

## 3. Skill Taxonomy

Ordered from foundational to surface. The first group is the one that gets skipped and shouldn't be.

### Group 1 — Foundational Mental Models

_Without these, everything downstream is postured or blindly accepted. A fellow can execute the motions and not know when they're wrong._

| Skill                        | Description                                                                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core concept models          | Execution flow, input/output, functions, state, data flow, request/response, async, persistence. The models that let you _predict_ what code should do before you read it. |
| Language semantics           | What Python actually does — the object model, mutability, scope, references vs. copies, iteration protocols, exception flow. Not trivia; it's what makes a bug legible.    |
| Data structures & algorithms | Retained partly for job-market reasons, partly because "what shape is this data and what does that shape cost me" is a real daily judgment.                                |
| Reading unfamiliar code      | Building a model of someone else's intent from artifacts alone. The single most common daily activity in AI-assisted work.                                                 |
| Ecosystem literacy           | The catalogue of tools, frameworks, and patterns that exist — and roughly what each is for.                                                                                |
| Failure catalogue            | The parallel catalogue of what goes wrong with each. N+1 queries, unhandled exceptions, leaky abstractions, mutable default arguments, silent type coercion.               |

**Equity note.** Prior exposure buys the most advantage here, and AI most convincingly papers over its absence. A fellow can ship a working Flask app with none of this. Detection has to be deliberate and early.

### Group 2 — Problem Framing & Product Judgment

| Skill                           | Description                                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------------------- |
| Requirement elicitation         | Turning a vague ask into something buildable. Asking the question that reveals the real constraint. |
| Scope negotiation               | Pushing back on a bad requirement; distinguishing must-have from nice-to-have.                      |
| Prioritization under constraint | What to build first given limited time, and why.                                                    |
| Success definition              | Knowing what "done" and "working" mean before starting.                                             |
| User empathy                    | Who this is for and what they'll actually do with it.                                               |

**Equity note.** Fellows managing work and family obligations often have _more_ real-world experience with constrained decision-making than CS graduates do. This is a group where they can lead. Name that to them explicitly rather than hoping they infer it.

**Open question.** How do we help fellows name this as a strength rather than experience it as something embarrassing, or as a struggle unique to them? The framing needs to be built into how the group is taught — a slide or a one-time pep talk won't hold against months of fellows privately comparing themselves to an imagined "normal" CS background.

### Group 3 — Architecture & Design

| Skill                        | Description                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Data modeling                | Schema design, relationships, normalization tradeoffs. The decision most expensive to reverse.   |
| API interface design         | Contracts, resource shape, error semantics, versioning.                                          |
| Separation of concerns       | Where boundaries go and why. File structure, layering, module responsibility.                    |
| Abstraction-level discipline | Keeping a function operating at one level. What to name, what to hide, what to expose.           |
| Extensibility                | Designing so the next change is cheap. Anticipating the second feature while building the first. |
| Technology selection         | Choosing the option that fits _this_ problem. Requires the Group 1 catalogue plus taste.         |
| Taste & discernment          | The judgment layer over all of the above. Developmental — see §4.1.                              |

### Group 4 — Delegation & Context Engineering

_The genuinely new group. Nothing in most curricula covers this._

| Skill                             | Description                                                                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Spec writing for models           | Writing an instruction precise enough to produce the intended artifact. Same muscle as technical communication, different audience. |
| Context construction              | What to feed the model, what to leave out, what to persist. Project-level vs. session-level memory.                                 |
| Context hygiene                   | Recognizing when a session has degraded and needs a reset vs. a compaction.                                                         |
| Task decomposition for delegation | Breaking work into units a model can execute reliably — and knowing what unit size that is.                                         |
| Scope containment                 | Models over-deliver. Asking for a fix and getting a refactor is a defect, not a bonus. Catching and rejecting it.                   |
| Iterative correction              | Steering wrong output toward right without restarting — and knowing when restarting is cheaper.                                     |
| Delegation boundary               | Knowing when prompting costs more than typing.                                                                                      |
| Tool-chain fluency                | Working effectively across agentic tools, IDE integrations, and CLI workflows.                                                      |

**Equity note.** Access stratification bites hardest here, because frontier tooling costs money. Whatever we teach must degrade to free tiers, and we should say out loud which capabilities are paid-tier — so fellows entering the workforce advocate for tooling budgets rather than assuming they're personally behind.

**Organizational consideration.** To what extent should token and API costs simply be treated as a cost of doing business for Marcy — the same category of expense as laptops or software, baked into each fellow's cost of attendance — rather than something fellows absorb individually or go without? This is a program-budget decision, not a curriculum one, but it determines whether the equity note above is aspirational or actually true. It also generalizes the Q3-specific funding question already raised in §5 and §9 (the $30 API-credit module) into a standing policy rather than a one-quarter patch.

### Group 5 — Verification & Quality Control

_If output is nearly free, this group is most of the job._

**Developmental note.** Debugging has its own four-stage progression across the quarters, parallel to taste in Group 3 — see §4.2.

| Skill                           | Description                                                                                                                                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detecting plausible-wrong       | AI defects are well-named, well-formatted, and subtly incorrect. Hallucinated library methods, a silently swallowed exception, an off-by-one that reads as idiomatic. Surface polish no longer signals correctness. |
| Methodical debugging            | Hypothesis, isolate, test, narrow. Unchanged in method, more important in frequency. Developmental — see §4.2.                                                                                                      |
| Debugging code you didn't write | No memory of intent to fall back on. Distinct from debugging your own. Developmental — see §4.2.                                                                                                                    |
| Expectation-driven review       | _"This looks different from what I expected — is there a reason?"_ Requires having an expectation, which requires Group 1.                                                                                          |
| Testing strategy                | What to test, at what level, and what a test actually proves.                                                                                                                                                       |
| Edge-case reasoning             | Empty, null, huge, malformed, concurrent, hostile.                                                                                                                                                                  |
| Verification triage             | Deciding how much scrutiny a given output warrants. You can't review everything at equal depth.                                                                                                                     |

**Equity note.** Under the old model, a struggling fellow shipped visibly broken code and we caught it in week two. Now they ship deployed, running, subtly broken code — and the feedback signal is _positive_. Early-warning infrastructure has to be rebuilt around this group specifically, and it has to key on process artifacts rather than output inspection.

### Group 6 — Systems, Operations & Constraints

| Skill                     | Description                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Security                  | Auth flows, input validation, injection defense, secret management. AI-generated code has characteristic security gaps. |
| Scalability reasoning     | What breaks at 10x. Where the bottleneck actually is vs. where it feels like it is.                                     |
| Cost awareness            | Service pricing, token costs, what a naive query pattern costs at scale.                                                |
| Version control           | Branching, review flow, meaningful history. More important when a model generates 400 lines in a minute.                |
| Deployment & environments | Getting it running somewhere real, and configuring across environments.                                                 |
| Observability             | Logging, error tracking, knowing something broke before a user tells you.                                               |

### Group 7 — Handoff & Communication

| Skill                        | Description                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| Documentation                | Writing so the project survives changing hands — including into and out of AI context. |
| Code readability             | Naming, structure, and comments that explain _why_, not _what_.                        |
| Architecture articulation    | Explaining and defending a design to someone who's never seen it.                      |
| Code review (giving)         | Identifying the important problem, not the nitpick.                                    |
| Code review (receiving)      | Separating the critique from the ego.                                                  |
| Decision records             | Capturing why a choice was made so future-anyone doesn't relitigate it.                |
| Cross-functional translation | Explaining technical constraints to people who don't have them.                        |

**Equity note.** This is the strongest differentiator our fellows have against CS graduates, and the group most directly aligned with the existing five competencies. Weight it accordingly.

---

## 4. Developmental Ladders

Two skills in the taxonomy have a clean four-stage developmental arc that maps to the quarters: taste & discernment (§3, Group 3) and debugging (§3, Group 5). Use both as calibration spines — when defining outcomes for skills in either group, ask which rung of the relevant ladder the fellow is standing on, rather than treating the skill as binary have/have-not.

### 4.1 The Taste & Discernment Ladder

#### Q1 — Recognize obvious quality differences

Fellows are not yet expected to have mature taste. The goal is exposure and contrast. They should be able to say:

- "This code is easier to read than that code."
- "This function is doing too many things."
- "This variable name helps me predict what the value is."
- "This AI output looks polished, but I don't fully understand it."
- "This solution works, but I can't explain why."

Taste at the level of **noticing.**

**Spine question:** _Can you distinguish understandable from confusing, simple from overcomplicated, and explained from merely working?_

#### Q2 — Justify local choices

Taste becomes more than preference. Fellows explain why one local implementation choice beats another — two function names, two ways to structure a route handler, two data shapes, two test cases, two AI-generated solutions. The move is from "I like this better" to "this is better because it makes the next change easier / exposes the edge case / separates responsibilities / reduces duplication / makes state easier to track."

Taste at the level of **justified local judgment.**

**Spine question:** _Can you give a reason for a design choice using concepts from the curriculum?_

#### Q3 — Evaluate tradeoffs across a system

Fellows reason about consequences across files, features, and users:

- "If we put this logic in the view, it's faster now but harder to test later."
- "This schema works for the first feature but will fight us when we add roles."
- "This abstraction is premature."
- "This duplication is acceptable for now because the second case may diverge."
- "This AI-generated refactor is too broad for the bug we asked it to fix."

Taste at the level of **tradeoff reasoning.**

**Spine question:** _Can you explain what a choice buys, what it costs, and when that tradeoff is acceptable?_

### Q4 — Exercise independent discernment under ambiguity

Not picking the right answer from known options — making a defensible call when the problem is underspecified. Fellows can reject an AI solution that works but is misaligned, choose between competing architectures, identify when a feature request should be narrowed, decide when _not_ to abstract, decide when to rewrite vs. patch, and articulate what they'd monitor or revisit.

Taste at the level of **independent professional judgment.**

**Spine question:** _Can you make and defend a context-sensitive decision when there is no single correct answer?_

### 4.2 The Debugging Ladder

**The spine:** orient → hypothesize → isolate → repair → explain.

Debugging is the second skill in the taxonomy with a clean four-stage developmental arc — distinct from taste, but calibrated against the same quarters. It matters on its own schedule: "debugging code you didn't write" only becomes the dominant daily activity once AI starts implementing, which is Q2 onward.

#### Q1 — Orient without panic

At Q1, the goal isn't independent debugging. The goal is to avoid thrashing. A fellow entering unfamiliar code should be able to answer basic orientation questions:

- What is this app supposed to do?
- Where does the broken behavior show up?
- What files seem relevant?
- What did I try?
- What did I observe?
- What do I know versus what am I guessing?

Debugging at the level of **orientation and observation.**

**Spine question:** _Can you slow down, reproduce the issue, identify the relevant surface area, and describe the failure in concrete terms?_

This matters because novice debugging often collapses into random edits — and in AI-assisted work, that gets worse: random prompting, random patching, asking the model to "fix it," accepting a plausible change, and losing track of what changed. Q1 should reward disciplined observation before intervention.

#### Q2 — Form and test local hypotheses

By Q2, fellows debug with hypotheses instead of vibes. They should be able to say:

- "I think this bug is happening because this value is undefined before render."
- "I expect this route handler to receive this parameter."
- "I'm going to log here because this is the boundary between frontend and backend."
- "If my hypothesis is right, this test/log/output should show X."
- "That didn't happen, so I'm narrowing elsewhere."

Debugging at the level of **local causal reasoning.**

**Spine question:** _Can you form a plausible hypothesis, choose a targeted check, and update your theory based on evidence?_

This is where debugging code you didn't write starts to become meaningfully different from debugging your own. Fellows can't rely on memory of what they meant — they have to infer intent from artifacts alone.

#### Q3 — Trace across boundaries

By Q3, fellows debug across multiple files or layers:

- UI → event handler → API call → route → database query
- test failure → implementation → dependency → fixture
- model output → generated diff → regression
- state update → render behavior → async timing

Debugging at the level of **system tracing.**

**Spine question:** _Can you trace a bug across boundaries, isolate the layer where the actual mismatch occurs, and avoid over-fixing unrelated code?_

This matters especially in AI-assisted development, because models often "fix" by broadening scope. A fellow needs to know whether the problem is a wrong data shape, a wrong assumption, a wrong state lifetime, wrong async sequencing, a wrong boundary contract, a wrong test, or a wrong abstraction. At Q3, fellows should also start recognizing when the first visible error is a symptom, not the cause.

#### Q4 — Repair minimally and preserve intent

By Q4, a fellow can debug unfamiliar code with professional restraint. They can:

- infer the original design intention
- identify the smallest safe change
- avoid rewriting just because they dislike the style
- preserve existing behavior outside the bug
- add a regression test or verification step
- explain the root cause and why the fix is appropriate
- decide when the code is too unclear and needs refactoring, not just patching

Debugging at the level of **ownership without authorship** — the fellow remains accountable for the correctness of code they didn't originally write, in exactly the sense the Executive Summary uses that phrase.

**Spine question:** _Can you make a minimal, justified repair in unfamiliar code while preserving the system's intent and preventing recurrence?_

This is the concrete, behavioral version of what the Executive Summary names abstractly. If "ownership without authorship" ever needs a rubric rather than a slogan, Q4 of this ladder is it.

---

## 5. Skill-to-Quarter Mapping

### Q1 — Substrate

| Group                            | Load                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **1 — Mental models**            | **Primary.** Only quarter where hand-writing is the default; the only quarter that reliably builds expectation. |
| **3 — Architecture (partial)**   | File structure, separation of concerns, abstraction levels. Already in the Q1 outcomes; transfers directly.     |
| **4 — Delegation (foundations)** | Prompting and AI-as-tutor. Not yet delegation.                                                                  |
| **6 — Ops (partial)**            | Git/GitHub, venv, requirements.txt. Environment reasoning starts here.                                          |
| **7 — Communication**            | Code readability, naming, comments. Must habituate now — Q2 output is unreadable otherwise.                     |

**Additions needed:**

- **Reading unfamiliar code** as an explicit, taught Q1 skill — not incidental. Fellows should read code they didn't write, including AI-generated code they're forbidden from using, by roughly week 4. Q2 makes this the dominant daily activity.
- **A Q1 endgame unit** (final two weeks): fellows generate code _specifically in order to critique it_, with no requirement to use it. This eliminates the policy cliff (see §8) and delivers fellows into Q2 already skeptical — which is the disposition the entire second half depends on.

### Q2 — Delegation Under Supervision

| Group                            | Load                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **4 — Delegation & context**     | **Primary.** Context windows, skills/memory, the research→plan→implement→test→refine loop. Already explicit. |
| **5 — Verification**             | **Should be co-primary and currently isn't.** See additions.                                                 |
| **3 — Architecture**             | Data modeling, API design, technology selection. Postgres makes schema design real.                          |
| **7 — Communication**            | Documentation, architecture articulation to teammates and EM. Already explicit.                              |
| **2 — Product judgment (light)** | Emerges through the EM relationship.                                                                         |

**Additions needed:**

- **Plausible-wrong detection as a named unit.** Build a Flask/Postgres-specific defect taxonomy fellows can name by sight: hallucinated library methods, silently swallowed exceptions, N+1 queries through an ORM, string-concatenated SQL, mutable default arguments, missing input validation. Naming a defect class is what makes it findable.
- **Debugging code you didn't write**, explicitly taught. Q2 makes this most of the job and it is currently unlisted.
- **Scope containment.** A fellow asks for a route handler and gets a restructured blueprint. Accepting that silently is how architecture ownership evaporates.
- **Security earlier than feels natural.** Flask + Postgres + AI generation reliably produces confidently insecure code. Input validation and secret management belong in Q2, not deferred to the Q3 Cloud track — only a quarter of fellows take that track.

### Q3 — AI-Led Systems Exposure

| Group                                          | Load                                                                                                                                                                                                    |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **6 — Systems & ops**                          | **Primary, by design this time.** Security, testing, cost, sandboxing, and deployment are now named modules every fellow rotates through, rather than something implied by whichever track they picked. |
| **4 — Delegation & context**                   | "Leverage AI to quickly assess options and implement a solution" is Group 4 under real time pressure — the compressed timeline is the point.                                                            |
| **2 — Problem framing**                        | The 24-hour spec loop (interrogate stakeholder → spec → feedback → tools → implement → present) is a direct, repeated rep of requirement elicitation and success definition.                            |
| **7 — Communication**                          | Presenting to a real-world mentor and defending stack and architecture choices.                                                                                                                         |
| **1 — Ecosystem literacy & failure catalogue** | Still built here, but now through five tight constraint-specific loops rather than one long domain immersion.                                                                                           |

**What this resolves from the prior design.** The "shared ops floor" gap is closed by construction — security, testing, cost, sandboxing, and deployment are no longer something only the Cloud track guaranteed; every fellow does all five. The track cash-barrier risk is also substantially reduced, because Business Applications / Data & Automation / Cloud & Production / AI-Enabled Products are no longer full-quarter bets a fellow's income rides on — they're now framing contexts for the systems-module work.

**What's still open:**

- **Is the cost module ($30 in API credits) funded per fellow, or does it come out of pocket?** If Marcy-funded, the cash-barrier risk from the original design is fully closed for this quarter. If any fellow is expected to supplement it, the risk returns in miniature.
- **Can the "AI-Enabled Products" framing context silently reintroduce the cash-barrier risk** if a fellow chooses to frame multiple modules within it — e.g. running both the cost module and the security module against the same paid model API? Worth checking whether framing choice can stack cost even though tracks are no longer full commitments.
- **Mentor availability.** The Q3 stakeholder is now "mentors who have solved the problem in the real world" — an external recruiting dependency rather than an internal instructor resource. This needs its own build item (see §9) and is flagged as a new risk (see §10).

### Q4 — Capstone

| Group                   | Load                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2 — Problem framing** | **Primary.** Elicitation, scope negotiation, prioritization, success definition. A real stakeholder gives vague, shifting requirements — that's the point, not a defect of the arrangement. |
| **7 — Handoff**         | Documentation and decision records for a project someone else inherits.                                                                                                                     |
| **3 — Extensibility**   | First time "the next change" is a real possibility rather than a hypothetical.                                                                                                              |

**Additions needed:**

- **An explicit handoff deliverable.** The capstone should end with the project genuinely transferable — to the stakeholder, to a successor fellow, or to a fresh AI context with no session history. That last one is a self-administering objective test: if a project can't be picked up cold by a model given only the repo and docs, the documentation is inadequate.

---

## 6. Assessment Mode Catalogue

Grouped by instructor cost, since instructor time is the binding constraint.

### Low cost, high frequency

**Plan review** — Fellow submits a spec and architecture before writing anything. Grade the plan. Cheap to produce, hard to fake, catches a missing mental model before a week of work is built on it.
_Measures:_ Groups 2, 3. _Equity:_ Very low time-cost for the fellow; friendly to constrained schedules.

**Prediction-before-execution** — Fellow states expected output before running or generating. The gap _is_ the measurement.
_Measures:_ Groups 1, 5. _Equity:_ Costs almost nothing and directly targets the invisible-gap problem. Highest leverage-to-effort item in the catalogue.

**Salted code review** — AI-generated code with three planted defects: one obvious, one subtle, one architectural.
_Measures:_ Group 5, detail orientation. _Equity:_ Fully self-contained. No prior-exposure advantage, no tooling required.

**Prompt/spec artifact submission** — Submit the specs used to generate the project alongside the project. Grade the specs.
_Measures:_ Group 4, technical communication. _Equity:_ Rewards clarity of thought over speed of typing.

### Medium cost

**Architecture defense** — Fellow presents a system built with AI. Interrogate a decision they didn't make consciously. The distance between what they shipped and what they can defend is the score.
_Measures:_ Groups 1, 3, 7 simultaneously. Closest thing to a single diagnostic for whether the mental model is real.
_Equity:_ Live verbal defense penalizes anxiety and non-dominant communication styles. Scaffold it — questions in advance, practice rounds, a written option for the first attempt.

**Extension under constraint** — Unfamiliar codebase. Add a feature. Don't break anything.
_Measures:_ Reading and debugging unfamiliar code, systems thinking, extensibility.
_Equity:_ Realistic and fair, but tight time-boxing punishes fellows without quiet uninterrupted blocks. Prefer a generous window over a short timer.

**Regression hunt** — Working app plus a diff that broke something. Find it.
_Measures:_ Methodical debugging, detail orientation. Simulates the most common AI-assisted failure directly.

**Constraint-shift redesign** — "Now it handles 100x traffic / supports offline / is multi-tenant. What changes?" Written, no implementation.
_Measures:_ Group 6, systems thinking. _Equity:_ Zero implementation cost; tests judgment only.

**Handoff test** — Fellow A documents a project. Fellow B, who has never seen it, extends it from documentation alone. Both graded on B's outcome.
_Measures:_ Group 7. Also builds peer relationships, which matters for fellows without professional networks.

**Cold-context handoff** — Fresh AI session, repo and docs only, given a feature request. Objective documentation test.
_Measures:_ Group 7. Nearly free to administer once designed.

**Spec-to-implementation loop (24-hour cycle)** — State the problem, interrogate a stakeholder about requirements, return in 24 hours with a spec, get feedback, return in 24 hours with a tool/approach, implement, present. Each 24-hour turnaround is itself gradable.
_Measures:_ Groups 2, 4, 7 in sequence — the closest thing in the catalogue to a realistic compressed work cycle.
_Equity:_ The 24-hour windows are tight for fellows with outside obligations. Decide whether the clock is calendar hours or fellow-controlled business hours before making this high-stakes.

**Mentor stack review** — A practitioner who has solved a similar problem in the real world reviews the fellow's stack and implementation choices directly: did you pick the right stack, what mistakes did you make with it (file organization, abstraction levels, etc.)?
_Measures:_ Groups 1, 3, 7. Distinct from architecture defense — the reviewer isn't an instructor grading against a rubric, they're an outside practitioner reacting to real tradeoffs, which is a different and valuable kind of pressure.
_Equity:_ Depends entirely on mentor consistency across the pool. Marcy already has a large, established mentor pool, so this isn't a sourcing problem — but without a shared rubric or alignment pass, quality can still vary mentor to mentor, turning this into a stratifying assessment rather than an equalizing one. Match or rotate mentors deliberately once that alignment exists, rather than leaving it to self-sourcing.

### High cost, use sparingly

**Proctored hand-coding** — No AI, limited time, moderate scope.
_Measures:_ Group 1 — the only reliable way to verify the mental model exists independent of tooling.
_Rationale to state openly:_ dual-purpose. It verifies the substrate _and_ the hiring market still gates on it. Don't dress the second reason up as the first. Fellows can tell, and being honest that we're preparing them for a market we didn't design builds more trust than pretending the skill is intrinsically sacred.
_Equity:_ The most exposure-sensitive assessment in the catalogue. Diagnostic first; high-stakes only after fellows have had the practice reps better-resourced candidates got in high school.

**Full-cycle project** — Loose problem → spec → build → test → deploy → feedback → iterate.
_Measures:_ Everything. _Equity:_ Highest burden on fellows with outside obligations. Stage deadlines so no single week is a cliff; make partial-credit paths explicit in advance.

**Longitudinal debugging log** — Fellow logs bugs across a module: symptom, hypotheses, attempts, resolution.
_Measures:_ Methodical debugging as habit rather than event. _Equity:_ Rewards persistence over speed — one of the few assessments where being slow and thorough scores well.

---

## 7. Assessment Calendar

### Q1

| Mode                                                                                 | Cadence                         | Targets                                                                                            |
| ------------------------------------------------------------------------------------ | ------------------------------- | -------------------------------------------------------------------------------------------------- |
| Prediction-before-execution                                                          | Weekly, low stakes              | Group 1                                                                                            |
| Salted code review                                                                   | Bi-weekly                       | Detail orientation, Group 5 foundations                                                            |
| Proctored hand-coding                                                                | Module-end                      | Group 1 — pedagogically justified here, not just market-justified                                  |
| Longitudinal debugging log                                                           | Continuous                      | Methodical debugging as habit                                                                      |
| AI-interaction transcript review                                                     | Occasional                      | Tutor vs. generator usage. **Diagnostic, not punitive**                                            |
| Technical Interview Prep checks (GCF-style problems, array/string/dict manipulation) | Ongoing through the Python unit | Group 1, DSA — also the mechanism for identifying who needs targeted computational-fluency support |

### Q2

| Mode                                                       | Cadence       | Targets                                                                             |
| ---------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------- |
| Plan review                                                | Every project | Groups 2, 3                                                                         |
| Spec artifact submission                                   | Every project | Group 4                                                                             |
| Architecture defense                                       | Module-end    | Groups 1, 3, 7                                                                      |
| Regression hunt                                            | Bi-weekly     | Methodical debugging, detail orientation                                            |
| Salted code review (harder)                                | Bi-weekly     | Group 5, using the Flask/Postgres defect taxonomy                                   |
| Context-management exercise                                | Once          | Group 4 — given a degraded session, what do you do?                                 |
| Technical Interview Prep (Big O, algorithm patterns, ADTs) | Ongoing       | DSA — continues the Q1 thread into complexity reasoning and classic data structures |

### Q3

| Mode                                        | Cadence                                                           | Targets                                              |
| ------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| Spec-to-implementation loop (24-hour cycle) | Once per systems module (5x)                                      | Groups 2, 4, 7 — the primary Q3 assessment mechanism |
| Salted/constraint-specific review           | Once per module (security, testing, cost, sandboxing, deployment) | Group 6, Group 5                                     |
| Mentor stack review                         | Once, near the end of the module rotation                         | Groups 1, 3, 7                                       |
| Cost-and-failure audit                      | Once, paired with the cost module                                 | Cost awareness, failure catalogue                    |
| Live interview practice                     | Ongoing                                                           | DSA, technical communication under pressure          |

### Q4

| Mode                                | Cadence  | Targets                                                               |
| ----------------------------------- | -------- | --------------------------------------------------------------------- |
| Stakeholder requirement translation | Early    | Group 2 — compare fellow's reading against what the stakeholder meant |
| Handoff test                        | Terminal | Group 7                                                               |
| Cold-context handoff                | Terminal | Group 7, objectively                                                  |
| Full-cycle review                   | Terminal | Everything                                                            |

---

## 8. Gates and Transitions

### The Q1→Q2 gate

The central sequencing question: **what is the evidence that a fellow has crossed from "AI as tutor" into "AI as implementer"?**

A calendar date is the wrong answer. The gate is **prediction accuracy**: a fellow is ready to delegate implementation when, given a spec, they can accurately predict the shape of correct output — files touched, functions needed, likely failure points — before generating it. A fellow who can't predict can't verify, and a fellow who can't verify is shipping code they don't own.

**Required evidence:**

1. Prediction accuracy above threshold on the weekly Q1 exercises.
2. Defect detection on a salted review at the _subtle_ and _architectural_ tiers, not just the obvious one.
3. A defensible plan — spec and architecture for a small system, articulated without AI assistance.

**Consequence of not clearing it.** Fellows are **not** held back a quarter. That's punitive and impractical. They proceed to Q2 content — Flask, Postgres, all of it — with AI restricted to tutor/reviewer mode for an additional few weeks while doing targeted prediction reps.

**Differentiate mode, not access, and not pace.** This is the equitable form: evidence-based, individually paced, and it doesn't punish a fellow for arriving with less exposure. It tells us what reps they still need.

### Handling the Q1 AI policy

"Don't generate code" for three months followed by "generate code" is a hard inversion. Two consequences to design around:

**The cliff.** Fellows arrive in Q2 with zero delegation reps and will over-trust output in week one. The Q1 endgame unit (§5) resolves this: generate code specifically to critique it.

**Enforcement as diagnostic.** A fellow generating code during Q1 is most likely a fellow underwater on time — someone working a closing shift with a submission due has a fully rational incentive. The correct first response is scheduling support and workload triage, not discipline. Reserve the honesty-policy response for cases where support has been offered and declined. Policy that ignores material circumstance disciplines poverty and calls it integrity.

---

## 9. Build Order for This Year

The transition plan's constraint is staging. This is the design queue.

### Build now — before Q1 starts

1. **CLI / Computational Thinking / OOP unit redesign.** The stated immediate priority. Every downstream unit assumes these landed.
2. **The prediction-before-execution protocol.** Highest leverage-to-cost assessment in the catalogue and the mechanism the Q1→Q2 gate runs on. Needs a format, a rubric, and a threshold. Build it first; refine the threshold with real data.
3. **The Q1 salted-review bank.** Needs roughly 6–8 Python samples with tiered planted defects. Reusable across cohorts; the highest-return artifact per hour of design time.
4. **The AI usage policy, framed as mode rather than prohibition.** "AI as tutor" needs a concrete operational definition fellows can self-check against — otherwise the policy is enforced by instructor vibes, which is where inequity enters.
5. **Reading-unfamiliar-code exercises for Q1 week 4.**

### Build during Q1 — for Q2

6. **The Flask/Postgres defect taxonomy.** Generate it empirically: have instructors produce AI-built Flask apps during Q1 and catalogue what actually goes wrong. Don't guess it from first principles.
7. **Plan-review and spec-submission rubrics.**
8. **Architecture defense question bank**, with the scaffolding built in from the start rather than added after the first fellow freezes.
9. **The Q1 endgame critique unit.**

### Build during Q2 — for Q3

10. **The shared ops floor**, whatever minimum all four tracks guarantee.
11. **Track selection materials**, including honest cost, difficulty, and market positioning for each.
12. **Track cost budget.** Determine actual per-fellow spend for Cloud and AI-Enabled tracks and secure it, or the tracks stratify by income.

### Additional build items — from this revision

**Build now — before Q1 starts**

- **Python environment tooling decision.** Confirm whether pip/venv/requirements.txt is still the right teaching stack, or whether a more modern, abstracted tool (e.g. `uv`) better serves the pedagogical goal of understanding dependency management without adding unnecessary friction.
- **An AI-assisted OOP/class-teaching exercise.** Fellows need a way to grasp the basic shape of a class and recognize when an implementation is missing something from that shape — and a deliberate way to feel the pain of a poorly designed class, since they won't hand-write enough broken ones to encounter it by accident at this pace.
- **A fast computational-fluency screening method for Technical Interview Prep.** Needs to surface who's struggling and on what, cheaply — willingness to talk through an idea out loud may be a better early signal than a correctness score.

**Build during Q2 — for Q3**

- **The five Q3 systems modules** (security, testing, cost, sandboxing, deployment), each built against a shared starting CRUD application.
- **The 24-hour spec loop rubric and cadence**, including a decision on whether the clock is calendar-hours or fellow-controlled business-hours.
- **Mentor alignment and matching process** for the Q3 stakeholder role. Sourcing isn't the gap — Marcy already has a large mentor pool with a history of supporting fellows. What's missing is a shared rubric or briefing so mentor quality is consistent across the pool (what a good stack review actually covers, concrete feedback vs. vibes), plus a decision on deliberate matching rather than self-sourcing once that alignment exists.
- **A funding decision for the Q3 cost module.** Whether the $30 in API credits (or equivalent) is Marcy-funded per fellow needs to be settled before this quarter runs, or the track cash-barrier risk from the original design returns.
- **A decision on the Q2 stakeholder** — simulated or real. This changes the complexity load of Q2 significantly and should be settled with enough lead time to build supporting material either way.
- **A program-wide AI/token cost policy.** Decide whether AI and token costs are a standing cost of attendance — like laptops or software licenses — rather than something resolved piecemeal each time a paid API shows up in a quarter's curriculum. This is the general case of the Q3 cost-module funding question above (see also §3, Group 4).

### Defer — decide with evidence

13. **Full Q3 track curricula.** The transition plan is right that these should wait.
14. **Interview prep / DSA placement.** See §10.
15. **Capstone stakeholder sourcing and scoping process.**

### Instrument while building

The transition plan's stated purpose includes gathering evidence. Collect deliberately:

- **Prediction accuracy over time, per fellow.** The single most valuable dataset. It tells us where the real Q1→Q2 threshold sits and whether three months is enough.
- **Defect-detection rates by tier.** Where does detection break down — subtle or architectural?
- **Time-to-submission distribution.** Proxy for outside-pressure load. Watch for fellows whose submission times cluster late at night.
- **Q1 policy incidents.** Correlate with workload signals rather than treating them as isolated character events.
- **Q2 architecture-defense gaps.** Distance between shipped and defensible, tracked per fellow. This is the invisible-gap detector.
- **Track selection vs. entering skill level.** If lower-confidence fellows cluster in one track, that track has become a lower track and needs redesign.

---

## 10. Known Risks

**The DSA gap — largely resolved by this revision.** Technical Interview Prep now threads through all three quarters: array/string/dict manipulation and GCF-style problems in Q1, Big O/algorithm patterns/ADTs in Q2, live interview practice in Q3. Keep this labeled honestly as market compliance rather than folded silently into the pedagogical curriculum — the original concern about mismatched framing still applies even though the content gap is closed. Watch for whether TIP crowds out its host quarter's primary skill load (Group 1 in Q1, Group 4/5 in Q2) rather than running alongside it.

**Q3 mentor dependency.** The Q3 stakeholder role now depends on recruiting outside practitioners who've solved the relevant problem in the real world. Sourcing itself isn't a gap — Marcy has a large existing mentor pool with a track record of supporting fellows. The open risk is **consistency, not availability**: there's no current visibility into how evenly matched mentor quality is across that pool, and an uneven bench turns "mentor stack review" into an assessment where the outcome depends partly on who a fellow happened to get. This needs a training/alignment pass before Q3 runs — a shared rubric or briefing for what a good stack review actually covers (did you pick the right stack, what mistakes did you make with it, concrete rather than vibes-based feedback) — not a recruiting effort. Pair this with the matching question already in §6: deliberately assign or rotate mentors rather than letting fellows self-source, once the alignment pass gives you a basis for matching on.

**Q3 restructure needs re-verification, not assumed closure.** Moving away from full-quarter tracks substantially reduces the original track cash-barrier risk (§5), but only if the cost module is fully funded and the "AI-Enabled Products" framing context doesn't let a fellow stack multiple cash-gated modules against the same paid API. Confirm before treating the risk as closed.

**The language transition costs us alignment with hiring.** Moving from PERN to Python/Flask is defensible for an AI-forward curriculum, but it changes our placement surface. Worth an explicit market check before Q3 track design locks.

**Verification has no natural home.** Group 5 is co-primary in Q2 by design intent but is not currently represented in the Q2 topic list. If it doesn't get built into the topics, it will get squeezed out by Flask and Postgres content, which have the advantage of being concrete and demoable.

**Compressed Group 1.** Three months to build mental models for fellows with no prior CS is tight. This is the most likely place for the year to fail quietly, and the prediction data is how we'll find out in time to respond.

**Track stratification by cost.** Named in §5; repeated here because it's the risk most likely to be discovered too late to fix.
