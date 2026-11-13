# Software Engineering Skills Taxonomy

This document is the list of skills the Software Engineering fellowship assesses, in the shape the learning management system reads: a short list of groups and, under each, specific skills. Every graded section of every assignment is tagged with one of these skills, and the figures on the Fellows Skills tab and on each fellow's record are read from those tags. The same list is held as `prisma/skill-taxonomies/skills-taxonomy-swe.csv` in the LMS repository, which is what the LMS seeds from. The Data Analytics program has its own taxonomy in `skills-taxonomy-da.csv` in the same folder; the two lists are kept apart on purpose, and a skill that appears in both is two rows, one per program.

Sources: the F26 scope and sequence, the module overviews and the Mod 1 objectives page, the Mod 1 project specification, the capstone overview, section 3 of the AI curriculum planning document, the competencies proposal, and the sections of the Software Engineering and Leadership & Development assignments on the live LMS as of October 2026.

## 1. How the taxonomy is used

Every graded assignment is made of sections, and a section is one scored unit: one question of a short response, one exercise of a coding assignment, one criterion of a project rubric. The same sections exist whether the model grades the assignment or an instructor does, so a hand-graded short response and a model-graded one have the same shape. Each section is tagged with exactly one skill. Beside the sections, every grading round has a summary, a comment with no score that describes the feedback as a whole.

The LMS shows, for every fellow, points earned over points possible per skill so far in the term, the same figures summed per group, and a history of every assignment that contributed to each skill in due-date order. A group is never tagged. It is a heading over skills and a column on the Fellows grid, and its figure is the sum of its skills' figures.

Three rules govern the rows:

1. **One row per distinct skill.** Each distinct skill receives its own canonical row and definition, even when several skills are grouped together in one project rubric. A rubric that scores several skills under one criterion is divided into one criterion per skill before it is tagged.
2. **Exclusivity.** No section is evidence of two rows at once. Where two rows could both fit the same section, the line between them is drawn in section 3 so that an author can tell which to choose.
3. **Recurrence.** A row has to be assessed often enough to show a trend. A skill assessed once a year gives one data point, and a figure built on one data point is a grade, not a trend. Each row names where its evidence comes from and roughly how many data points a year it gives, and a row with fewer than three is flagged so that its figure is read as a grade.

One more rule shapes the Implementation group. A skill there is a layer of the stack or a programming paradigm that a fellow keeps using after the module that teaches it, so its figure keeps moving across quarters. A topic inside a layer, such as loops, joins or Flexbox, is assessed in one or two weeks and then disappears into the layer, so it is the assignment's unit, not a skill. The test for a candidate is whether a Q3 project or the capstone produces evidence for it.

## 2. The taxonomy

Nine groups. Column meanings: **Group** is the top level the Fellows grid shows. **Canonical Skill ID** is a stable kebab-case identifier. **Skill Definition** names an observable capability and starts with a verb. **Evidence and recurrence** names the assignment types that carry the tag and how many data points a year they give.

### Group 1: Technical Reasoning

Saying what code does, why it was written that way, what a concept means, and what an approach costs. The short responses live here, as do the exit tickets and the prediction exercises. The line between this group and Verification and Quality Control is that this group reasons about code to say what it does and why, and Verification judges whether it is right.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `reading-and-predicting-code` | Reading and Predicting Code | Read code you did not write, build a model of its intent from its names and structure, and predict its output or final state for a given input. | Short response prediction questions weekly in Q1 (about 12), prediction-before-execution exercises weekly in Q1, the reading-unfamiliar-code unit, case studies, salted reviews. Over 20 a year. |
| `explaining-a-concept` | Explaining a Concept | Explain a programming concept accurately in plain language, using its correct terminology and an example or analogy. | Short response explanation questions weekly in Q1 and Q2 (about 15), the Mod 1 project reflection, the onboarding blog, the teaching demo. Over 15 a year. |
| `justifying-a-design-choice` | Justifying a Design Choice | Explain, in writing or aloud, why one piece of code or one sub-problem was solved one way rather than another, naming what the choice buys and what it costs, using concepts from the curriculum. | Short response "why was it written this way" questions (about 6 in Q1, more in Q2), case study exit tickets, architecture defense, mentor stack review. About 10 a year. |
| `algorithmic-complexity` | Algorithmic Complexity | Reason about how an approach's runtime or memory grows with input size, including the cost of each operation on a data structure, and choose between approaches on that basis. | Mod 1 lists work on the cost of `insert` versus `append`, Technical Interview Prep in Q1 and Q2, the DSA unit, the Q3 bottlenecks module. About 6 a year. |

### Group 2: Implementation

Writing code that satisfies a specification, shown by passing its tests, passing a visual check, or meeting its listed requirements. One row per layer of the stack or paradigm, so that a fellow who is strong in Python logic and weak in SQL shows as two figures rather than one average.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `python-programming` | Python Programming | Write Python that represents data with the built-in types, expresses logic with functions, conditionals and iteration, handles input and errors, and is organized into modules. | Every Q1 coding assignment, the Mod 1 project, proctored hand-coding, and every later quarter's Python. Weekly all year. |
| `object-oriented-programming` | Object-Oriented Programming | Model data and behavior with classes, using encapsulation, inheritance and polymorphism where they fit. | Mod 2, the Postgres-backed models in Q2, project models, the capstone. About 6 a year. |
| `algorithms-and-data-structures` | Algorithms and Data Structures | Implement a solution to an algorithmic problem using the right data structure and a known pattern, within a stated complexity. | Technical Interview Prep in Q1 to Q3, the DSA unit, live interview practice. Ongoing all year. |
| `markup-and-styling` | Markup and Styling | Build an accessible, responsive page with HTML, CSS and a templating language. | Mod 3 and its portfolio project, every project's interface, the capstone. About 8 a year. |
| `server-side-development` | Server-Side Development | Build a server that handles requests, renders responses, consumes external APIs, and organizes its routes, models and views. | Mod 5, the Flask CRUD application, the Q2 project, every Q3 module, the capstone. About 12 a year. |
| `data-persistence-and-querying` | Data Persistence and Querying | Create tables, write queries with joins and aggregates, and connect an application to its database. | Mod 6, the Q2 project, every Q3 module, the capstone. About 10 a year. |

### Group 3: Problem Framing and Product Judgment

Turning a vague ask into something buildable. Assessed by plan review on every project and by the Q3 spec loop.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `requirement-elicitation` | Requirement Elicitation | Ask a stakeholder the questions that reveal the real constraints behind a request, and record the requirements that result. | Session 1 of each Q3 module loop (5), the Q2 project's problem selection, the capstone's stakeholder requirement translation. About 7 a year. |
| `scope-definition` | Scope Definition | State what the first version must do and what it will not, separate must-have from nice-to-have, and say what "done" means before building. | Plan review on the Q2 project, each Q3 module spec (5), the capstone spec, the capstone learning plan's success criteria. About 8 a year. |
| `prioritization-under-constraint` | Prioritization Under Constraint | Order the work by importance, dependency and available time, and explain the order. | Project plans (about 7), the 24-hour loop's build days, the Mod 1 project's feature-at-a-time rule. About 8 a year. |
| `user-empathy` | User Empathy | Describe who the software is for and what they will actually do with it, and let that description decide the design. | The product spec's "what, who, why" overview on each project (about 7), the capstone learning plan. About 8 a year. |

### Group 4: Architecture and Design

Where the boundaries go and why. The decisions most expensive to reverse.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `code-organization` | Code Organization | Organize code into modules and layers that each have one responsibility, and keep each function at one level of abstraction. | The Mod 1 project's code organization criteria, the case study, Flask MVC and blueprints, the Q2 project, every later project's structure criterion. About 10 a year. |
| `data-modeling` | Data Modeling | Represent an application's data with the shape that fits it, from a list of dictionaries in a command-line program to a normalized relational schema with its relationships, and justify the shape against the operations the application performs on it. | Mod 1 lists and dictionaries work, the Mod 1 project's data structure, the Postgres unit's schema design session and assignments, the Q2 project's ERD, the capstone ERD. About 11 a year. |
| `interface-design` | Interface Design | Design the routes, request and response shapes and error behavior of a server so that a client can rely on them. | The Flask CRUD application, the Q2 project, the Q3 modules. About 4 a year. |
| `extensibility` | Extensibility | Design so that the next change is cheap, and add a feature to an existing codebase without breaking what it already does. | The Q3 testing module ("add features without breaking existing functionality"), extension-under-constraint assessments, the capstone's second iteration. About 3 a year. Flagged: at the threshold. |
| `technology-selection` | Technology Selection | Choose the tool or approach that fits this problem from the options available, and justify the choice against the alternatives. | Session 3 of each Q3 module loop (5), the mentor stack review, the capstone learning plan's tech stack. About 7 a year. |
| `evaluating-code-quality` | Evaluating Code Quality | Judge a piece of code or a proposed solution for readability, simplicity and fit for its purpose, and justify the judgment with curriculum concepts. | Short response "is this a good solution" questions, salted reviews' architectural tier, code review in Q2 and Q3, the taste ladder's spine questions. About 10 a year. |

### Group 5: Delegation and Context Engineering

Directing a model. Nothing in Q1 grades it; from Q2 the spec artifact submission grades it on every project.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `spec-writing-for-models` | Spec Writing for Models | Write an instruction precise enough that a model produces the intended artifact, naming the task, the constraints, the context and the expected output. | Spec artifact submission on every project from Q2 (about 7), the Q2 opening session's workflow. About 8 a year. |
| `task-decomposition-for-delegation` | Task Decomposition for Delegation | Break a piece of work into units a model can execute reliably, and say why that unit size. | The research-plan-implement workflow on every project (about 7), the Q3 build days. About 7 a year. |
| `context-management` | Context Management | Decide what a model receives, what persists across sessions and what is left out, and recognize when a session has degraded and needs a reset. | The Q2 context windows session, the context-management exercise (once), the spec artifacts' context sections. About 3 a year. Flagged: at the threshold. |
| `scope-containment` | Scope Containment | Detect when generated output exceeds what was asked, and reject the excess rather than accept it. | The Q2 scope containment session, salted reviews from Q2 (about 8), the Q3 module reviews. About 10 a year. |
| `iterative-correction` | Iterative Correction | Steer wrong output toward right output without restarting, and recognize when restarting or typing it yourself is cheaper. | Spec artifact submissions that show the correction history (about 7), the AI-interaction transcript reviews. About 7 a year. |

### Group 6: Verification and Quality Control

If output is nearly free, this group is most of the job. The salted review and the regression hunt are its instruments.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `detecting-plausible-wrong` | Detecting Plausible-Wrong Code | Find the defects in generated code that is well named, well formatted and subtly incorrect, at the obvious, subtle and architectural tiers. | Salted code review biweekly in Q1 and Q2 (about 11), the constraint-specific reviews in Q3 (5), the Q1 endgame critique unit. About 17 a year. |
| `reading-a-traceback` | Reading a Traceback | Read a traceback from the bottom up to name the error type, the failing line and the call that supplied the value, and state the cause. | Short response debugging questions weekly in Q1 (about 8), the Mod 1 objectives on tracebacks across modules. About 8 a year, nearly all in Q1. |
| `methodical-debugging` | Methodical Debugging | Reproduce a failure in code you did not write, form a hypothesis, isolate the cause with a targeted check, and repair it minimally while preserving the rest. | Regression hunts biweekly in Q2 (about 5), the longitudinal debugging log in Q1, the "debugging code you did not write" session, the Q3 modules. About 8 a year. |
| `requirement-verification` | Requirement Verification | Judge whether a piece of code satisfies a stated requirement, and name what is missing or extra. | Short response "does this meet the requirement" questions, the acceptance step of every delegated task, salted reviews' architectural tier. About 8 a year. |
| `testing-strategy` | Testing Strategy | Decide what to test and at what level, write tests that prove it, and say what a passing test does and does not show. | The Mod 1 TDD unit and its assignment, the Mod 1 project's tests, the Q3 testing module, the capstone's regression tests. About 5 a year. |
| `edge-case-reasoning` | Edge-Case Reasoning | Identify the empty, missing, oversized and malformed inputs a function or a program will receive, and handle each one. | The Mod 1 project's input validation criteria, the Flask forms session, the Q3 security module, test suites. About 6 a year. |

Three rows here and in Group 4 are judgments about code the fellow did not write, told apart by the question each answers: Evaluating Code Quality asks whether the code is good, Detecting Plausible-Wrong asks whether it is wrong, and Requirement Verification asks whether it is complete. A salted review divided into its three tiers tags one row per tier. A review graded as a single section has no default tag: the instructor chooses the row most relevant to what that review asked for, and a model assigning the tag chooses by the same relevance rather than by a fixed rule.

### Group 7: Systems, Operations and Constraints

The Q3 modules, each a seven-session loop against a shared application, plus Git from Mod 0 and configuration from Flask.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `version-control` | Version Control | Work from the command line to keep a readable history with small commits and clear messages, work on a branch, open and merge pull requests, and resolve a merge conflict. | The Mod 0 command line and collaboration assignments, every project's commit and branch criteria (about 8). About 10 a year. |
| `security` | Security | Implement authentication and authorization, reject hostile input, and manage secrets so that the application resists the common attacks on its stack. | The Q2 passwords and authorization sessions and their assignments, the Q3 security module, the sandboxing half of the Q3 bottlenecks module. About 5 a year. |
| `deployment-and-environments` | Deployment and Environments | Run the application somewhere real and configure it correctly across development and production with environment variables. | The Flask configuration session, the Q3 deployment module, the capstone deployment. About 4 a year. |
| `scalability-reasoning` | Scalability Reasoning | Identify where a system will break as load, data or users grow, and tell the actual bottleneck from the one that feels likely. | The Q3 bottlenecks module, constraint-shift redesign assessments. About 3 a year. Flagged: at the threshold. |
| `cost-awareness` | Cost Awareness | Estimate what a design costs to run, including service and token costs, and reduce it without losing what the feature is for. | The Q3 cost module and its paired cost-and-failure audit. About 2 a year. Flagged: below the threshold. |

### Group 8: Handoff and Communication

Writing and speaking so that the work survives changing hands. The planning document names this the strongest differentiator fellows have, and the group most aligned with the competencies.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `technical-writing` | Technical Writing | Write prose that is clear, organized, free of spelling and grammar errors, and rendered as intended. | The writing section of every short response (about 25 a year), README and reflection criteria on every project, the onboarding blog. Over 30 a year. |
| `code-readability` | Code Readability | Name, structure and comment code so that a reader can follow what it does and why, following the language's style conventions. | Every project's craftsmanship criterion (about 8), the Q1 case study, code review in Q2 and Q3. About 10 a year. The weekly coding assignments do not count here: the model scores style inside each exercise's one score, never as a section of its own. |
| `documentation` | Documentation | Write a README, setup instructions and decision notes that let someone else, or a fresh model session, set up, run and extend the project. | Every project's README criterion (about 8), the capstone handoff test and cold-context handoff. About 10 a year. |
| `architecture-articulation` | Architecture Articulation | Explain and defend the design of an entire system, in writing or aloud, to a technical audience that has not seen it, including decisions made by a model. | Architecture defense at Q2 module ends, each Q3 module presentation (5), the mentor stack review, Yoodli project questions. About 9 a year. |
| `stakeholder-presentation` | Stakeholder Presentation | Present what was built, for whom and why to a non-technical audience, and translate technical constraints into their terms. | Q3 presentations to mentors, the capstone engineering fair, the teaching demo. About 4 a year. |
| `interview-communication` | Interview Communication | Answer a technical or behavioral interview question aloud with a clear structure and specific evidence from your own work. | Yoodli assignments, live interview practice in Q3, behavioral interview recordings in Q4. Frequency depends on the Yoodli cadence; at least 10 a year in Q4 alone. |

### Group 9: Leadership and Development

The skills the Leadership & Development course assesses, derived from the criteria on its assignments on the live LMS. Completion criteria ("Completion & Effort", "Completion & Focus", "Complete Outline") map to no skill, because they record that work was handed in rather than how well.

| Canonical Skill ID | Skill Name | Skill Definition | Evidence and recurrence |
| --- | --- | --- | --- |
| `self-reflection` | Self-Reflection | Connect an experience, reading, film or discussion to your own identity, values and growth, with specific evidence from your life. | The "Reflection & Insight", "Thoughtfulness & Self-Reflection" and "Self-Awareness & Identity" criteria, roughly weekly in each unit; the Mod 1 project reflection. Over 10 a year. |
| `applying-leadership-concepts` | Applying Leadership Concepts | Apply a named concept from the leadership curriculum, such as social identity, intersectionality or socialization, accurately to a case or an experience. | The "Application of Course Concepts", "Understanding of Intersectionality", "Unit 1 Connections" and "Socialization & Intersectionality" criteria, roughly weekly. Over 10 a year. |
| `evidence-based-reasoning` | Evidence-Based Reasoning | Support a claim with specific evidence and a line of reasoning the reader can follow. | The "Development & Evidence" and "Communication & Evidence-Based Reasoning" criteria, roughly weekly. Over 10 a year. |
| `ethical-reasoning` | Ethical Reasoning | Reason about equity, power and responsibility in a workplace situation and propose a recommendation someone could act on. | The "Systems, Equity & Ethical Reasoning", "Actionable Workplace Recommendations" and "Professional Responsibility" criteria on the film reflection and the closeout assessment. About 4 a year. |
| `storytelling` | Storytelling | Craft a narrative with a throughline, a structure that guides the reader, and development from one part to the next. | The "Story Development", "Meaning & Throughline", "Storytelling & Development" and "Organization & Cohesion" criteria across the Mosaic of Me sequence. About 5 a year. |
| `writing-conventions` | Writing Conventions | Write with correct grammar, spelling and punctuation in a leadership assignment. | The "Clarity & Writing Conventions" criterion on the Mosaic final and the closeout assessment. About 3 a year. Flagged: at the threshold. A separate row from Technical Writing because the two courses grade writing separately. |
| `professional-identity` | Professional Identity | Articulate your strengths, values and professional identity, and connect them to the career you are preparing for. | The "Strengths, Values & Professional Identity" criterion, the capstone learning plan's motivation, behavioral interview preparation. About 4 a year. |
| `career-materials` | Career Materials | Produce a resume, cover letter or profile tailored to one specific employer or audience. | Resume and cover letter assignments, the GitHub profile and README guide, the published blog. Frequency depends on the career curriculum; at least 3 a year. |

Forty-eight rows in nine groups. Five are flagged for recurrence: Extensibility, Context Management, Scalability Reasoning and Writing Conventions sit at three data points a year, and Cost Awareness at two. Their figures are read as grades rather than trends.

## 3. Lines between neighboring rows

Exclusivity holds across groups as well as within them. These pairs sit close together, and the line between each is where an author decides which to tag.

- **Technical Reasoning and Implementation.** Saying what code does or why against writing code that works. A short response question is reasoning; a coding exercise is implementation, whatever topic either is about.
- **Data Modeling and Data Persistence and Querying.** Deciding the shape of the data is a design judgment; creating the tables and writing the queries that read them is implementation. The same line separates Interface Design from Server-Side Development.
- **Python Programming and the other Implementation rows.** A Flask route handler is written in Python, and it counts toward Server-Side Development, because the layer being built decides the row. Python Programming is for work whose subject is the language itself: the Q1 exercises, the command-line project, proctored hand-coding.
- **Algorithms and Data Structures and Algorithmic Complexity.** Implementing the solution against reasoning about its cost. An interview-prep exercise that asks for working code is the first; one that asks for the Big-O is the second; one that asks for both is two sections.
- **Edge-Case Reasoning and Security.** Edge-case reasoning is about the inputs a function or program receives: empty, missing, oversized, malformed. Rejecting hostile input is one specific concern of security, beside authentication, authorization and secrets.
- **Justifying a Design Choice and Architecture Articulation.** The difference is scale, not medium. Either can be written or spoken. Justifying a design choice is about one piece of code or one sub-problem; articulating an architecture is about an entire system.
- **Evaluating Code Quality, Detecting Plausible-Wrong and Requirement Verification.** Is it good, is it wrong, is it complete. See the note under Group 6 on tagging a single-section review.
- **Scope Containment and Requirement Verification.** Too much against too little, measured against the same requirement. An instructor wants to know which way a fellow errs.
- **Explaining a Concept and Technical Writing.** Content against form. A short response's question sections carry the first and its writing section the second.
- **Technical Writing and Writing Conventions.** The same capability graded in two courses, with a row in each so that the Software Engineering and Leadership & Development figures read separately.
- **Data Modeling and Algorithmic Complexity.** Choosing the shape that represents the data is Data Modeling, whether the shape is a list of dictionaries or a schema. Knowing what each operation on that shape costs is Algorithmic Complexity.
- **Code Organization covers both module boundaries and abstraction levels**, because every project rubric scores them as one criterion.
- **Methodical Debugging covers debugging the fellow's own code and code the fellow did not write**, because from Q2 onward almost all debugging is of code the fellow did not write and no assignment separates the two.
- **Version Control covers the command line**, because the command line is taught in Mod 0 beside Git and assessed with it.

## 4. Where the planning document's skills are found

Section 3 of the AI curriculum planning document lists skills under seven groups. Each is found here as follows.

| Planning document skill | Here |
| --- | --- |
| Core concept models; Language semantics | Reading and Predicting Code and Explaining a Concept for the reasoning; Python Programming for the building |
| Data structures & algorithms | Algorithms and Data Structures; Data Modeling; Algorithmic Complexity |
| Reading unfamiliar code | Reading and Predicting Code |
| Ecosystem literacy | Technology Selection, which is where the "return with tools and approach" session scores it |
| Failure catalogue | Detecting Plausible-Wrong, which is what the catalogue is used for |
| Requirement elicitation; Scope negotiation; Success definition; Prioritization under constraint; User empathy | Requirement Elicitation; Scope Definition (scope and success together); Prioritization Under Constraint; User Empathy |
| Data modeling; API interface design; Extensibility; Technology selection | The rows of the same names, with Interface Design for the API row |
| Separation of concerns; Abstraction-level discipline | Code Organization |
| Taste & discernment | Evaluating Code Quality, its gradable form |
| Spec writing for models; Task decomposition for delegation; Scope containment | The rows of the same names |
| Context construction; Context hygiene | Context Management |
| Iterative correction; Delegation boundary | Iterative Correction |
| Tool-chain fluency | Not a row: practiced daily, never graded as a section |
| Detecting plausible-wrong; Expectation-driven review | Detecting Plausible-Wrong |
| Methodical debugging; Debugging code you didn't write | Methodical Debugging |
| Testing strategy; Edge-case reasoning | The rows of the same names |
| Verification triage | Not a row: a judgment about how much scrutiny to give, never graded on its own |
| Security; Scalability reasoning; Cost awareness; Version control; Deployment & environments | The rows of the same names |
| Observability | Not a row: no module in the F26 scope and sequence assesses it on its own |
| Documentation; Decision records | Documentation |
| Code readability | Code Readability |
| Architecture articulation; Cross-functional translation | Architecture Articulation; Stakeholder Presentation |
| Code review (giving); Code review (receiving) | Evaluating Code Quality is the gradable form of giving one; receiving one is a disposition the competencies cover |

The rows with no counterpart in the planning document are the Implementation group, which the planning document leaves to the model, and the ones the weekly Q1 short responses assess: Reading and Predicting Code, Explaining a Concept, Justifying a Design Choice, Reading a Traceback and Requirement Verification. Interview Communication and all of Group 9 are also new.

## 5. How assignments are tagged

Examples over real assignments: the Software Engineering and Leadership & Development assignments on the live LMS, the Mod 1 project from the curriculum documents, and the Q2 to Q4 assessments the scope and sequence and the planning document name. Each section is one scored unit with one tag.

| Assignment | Sections and tags |
| --- | --- |
| Short Response: swe-sr-1-4-loops-python (2 questions) | Question 1 (3) `justifying-a-design-choice`; Question 2 (3) `reading-and-predicting-code`; Writing Quality (3) `technical-writing`. |
| Short Response: swe-sr-1-6-tdd-python | Question 1 (3) `explaining-a-concept` or `testing-strategy` by what it asks; Writing Quality (3) `technical-writing`. |
| Code: swe-1-4-loops-python (42 points, 14 exercises) | One section per exercise (3 each), every one `python-programming`. |
| Code: swe-0-1-git-collaboration (4 hand-graded checks) | Merge conflicts, alternating pushes, 10 messages: `version-control`. REFLECTIONS.md answers: `self-reflection`. |
| Mod 1 Case Study Investigation #1 (4 hand-graded) | `reading-and-predicting-code`. |
| Mod 1 Project: CLI Application (22 points, 16 criteria) | Core Python Concepts 7: `python-programming`. Code Organization 4: `code-organization`. User Interaction 4, divided: `edge-case-reasoning` 2 and `technical-writing` 2 (message spelling and spacing). Reflection 2, divided: `explaining-a-concept` 1 and `self-reflection` 1. Craftsmanship 5, divided: `code-readability` 2, `version-control` 2, `documentation` 1. |
| Proctored hand-coding, Mod 1 end | One section per exercise, `python-programming`. |
| Salted code review (Q1, biweekly) | `detecting-plausible-wrong`, with one section per planted defect tier where the review is divided. |
| Q2 Project: plan review, spec artifact, build, architecture defense | Plan: `scope-definition`, `user-empathy`, `data-modeling`, `prioritization-under-constraint`. Spec artifact: `spec-writing-for-models`, `task-decomposition-for-delegation`, `iterative-correction`. Build: `server-side-development`, `data-persistence-and-querying`, `markup-and-styling`, `code-organization`, `security`, `code-readability`, `version-control`, `documentation`. Defense: `architecture-articulation`, `justifying-a-design-choice`. |
| Q3 Security module: spec loop and presentation | Session 1: `requirement-elicitation`. Session 2: `scope-definition`. Session 3: `technology-selection`. Build: `security`, `server-side-development`. Session 7: `stakeholder-presentation`, and `detecting-plausible-wrong` for the salted review. |
| Yoodli: explain how you built your project | `architecture-articulation` or `interview-communication` by question type. |
| Capstone: learning plan, blog, teaching demo, spec sheet, build, handoff, presentation | Plan: `scope-definition`, `technology-selection`, `professional-identity`. Blog: `explaining-a-concept`, `technical-writing`. Demo: `stakeholder-presentation`. Spec: `user-empathy`, `data-modeling`. Build: the Implementation rows of the chosen stack, `extensibility`, `deployment-and-environments`. Handoff: `documentation`. Presentation: `stakeholder-presentation`. |
| L&D: Intersectionality Reflection (4 criteria of 1) | Completion: none. Understanding of Intersectionality: `applying-leadership-concepts`. Development & Evidence: `evidence-based-reasoning`. Reflection & Insight: `self-reflection`. |
| L&D: Mosaic of Me Final (6 criteria of 4) | Self-Awareness & Identity: `self-reflection`. Strengths, Values & Professional Identity: `professional-identity`. Storytelling & Development and Organization & Cohesion: `storytelling`. Unit 1 Connections: `applying-leadership-concepts`. Clarity & Writing Conventions: `writing-conventions`. |
| L&D: Unit Closeout Assessment (5 criteria of 4) | Identity & Assumptions and Socialization & Intersectionality: `applying-leadership-concepts`. Systems, Equity & Ethical Reasoning and Actionable Workplace Recommendations: `ethical-reasoning`. Communication & Evidence-Based Reasoning: `evidence-based-reasoning`. |

Most of the year's data points come from Q1 and the short responses. Twelve weeks of weekly pairs give Python Programming, Reading and Predicting Code, Explaining a Concept and Technical Writing many data points each by December. Most other rows start accumulating in January, and the Q3 rows in April. A grid read in November shows a few columns with a trend and the rest nearly empty.

## 6. The competencies, and which indicators are gradable

The competencies proposal describes dispositions observed in coaching, and the taxonomy does not replace it. Each group gives evidence for these competencies:

| Group | Competencies it evidences |
| --- | --- |
| Technical Reasoning | Building Mental Models; Learning and Retaining Information |
| Implementation | Methodical Problem Solving; Learning and Retaining Information |
| Problem Framing and Product Judgment | Thinking in Systems; Critical Thinking |
| Architecture and Design | Thinking in Systems; Quality Discernment |
| Delegation and Context Engineering | Ethical Technology Use; Technical Communication |
| Verification and Quality Control | Methodical Problem Solving; Quality Discernment; Ethical Technology Use |
| Systems, Operations and Constraints | Thinking in Systems; Time and Task Management |
| Handoff and Communication | Technical Communication; Storytelling; Quality Discernment |
| Leadership and Development | Critical Thinking; Career and Self-Development; Equity and Inclusion Lens; Storytelling; Curiosity |

Competency indicators that are graded skills: "writes clean, organized and readable code that follows established style guides" (Code Readability); "creates well-structured, error-free documentation, READMEs, and presentations" (Documentation, Technical Writing); "can trace through code execution to understand program behavior" (Reading and Predicting Code); "tests solutions comprehensively, ensuring edge cases are covered" (Testing Strategy, Edge-Case Reasoning); "reads error messages and test output carefully and investigates root causes" (Reading a Traceback, Methodical Debugging); "reviews code generated by AI with a critical eye" (Detecting Plausible-Wrong); "can explain and defend their own work, regardless of tools used" (Architecture Articulation); "breaks large problems into smaller ones" (Task Decomposition); "follows git best practices" (Version Control).

Competency indicators observed only in coaching: everything under Growth Mindset, Presence and Participation, Timely and Transparent Communication, and Collaboration; "asks for help when stuck"; "responds positively to constructive criticism"; "maintains positive energy and momentum"; "seeks out additional resources"; "proactively seeks feedback". None of these has a graded section, and none should be made into one.

## 7. Open questions

1. **The Yoodli cadence and format.** Interview Communication's recurrence depends on how often Yoodli assignments are set and whether each is one section or several. The capstone sets them weekly; the earlier quarters are not written down.
2. **How projects arrive on the LMS.** The tags above need the Q2 project graded as about fifteen criteria and a Q3 module as seven. A project that arrives as one hand-graded section carries one tag.
3. **Writing Conventions beside Technical Writing.** Two rows by decision. Merging them later would add the Leadership & Development writing criteria to the short response writing figure, about eight data points a year.
4. **The Q1 session sheet.** The Q1 schedule lives in a Google Sheet that was not read; the Q1 rows rest on the Mod 1 objectives page and the live assignments.
5. **The five flagged rows.** Extensibility, Context Management, Scalability Reasoning and Writing Conventions sit at the three-data-point threshold and Cost Awareness below it. Each could be merged into a neighbor or kept with its figure read as a grade.
6. **Rows the instructors should check.** Interface Design, whose Q2 evidence is thin because the quarter is server-rendered; Requirement Verification, whose separation from Detecting Plausible-Wrong is a judgment; Object-Oriented Programming, whose evidence after Mod 2 depends on how the Q2 models are graded; and the division of the Leadership & Development criteria among Self-Reflection, Applying Leadership Concepts and Evidence-Based Reasoning, which the L&D instructors should confirm.
