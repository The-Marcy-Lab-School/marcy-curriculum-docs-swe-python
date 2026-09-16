# AI Policy

**Table of Contents**:

- [What Kind Of Policy Is This?](#what-kind-of-policy-is-this)
- [The Two Modes](#the-two-modes)
- [Tutor Mode: The Baseline Standard](#tutor-mode-the-baseline-standard)
  - [The One-Sentence Test](#the-one-sentence-test)
  - [The Same Question, Asked Two Ways](#the-same-question-asked-two-ways)
  - [A Standing Instruction You Can Paste](#a-standing-instruction-you-can-paste)
  - [A Note on Autocomplete](#a-note-on-autocomplete)
- [Implementer Mode: The Q2 Standard (But only if you are ready)](#implementer-mode-the-q2-standard-but-only-if-you-are-ready)
  - [When the Mode Changes](#when-the-mode-changes)
  - [What Happens If I'm Not Ready?](#what-happens-if-im-not-ready)
- [Where AI Is Never Permitted](#where-ai-is-never-permitted)
- [What Happens When the Policy Is Broken](#what-happens-when-the-policy-is-broken)
- [What AI Tools Cost](#what-ai-tools-cost)

## What Kind Of Policy Is This?

This policy defines rules that you are expected to follow. Rules typically carry with them the baggage of punishment and are often created in environments that seek to restrict its subjects and make the lives of those making the rules easier. This policy is different as it is designed to serve _your_ best interests.

You are going to spend your career working alongside AI coding tools. Marcy is not going to pretend otherwise, and this policy is not an attempt to keep you away from them. Directing an AI tool well is a professional skill, and teaching it is part of what you are here for.

But a tool that writes code for you also hides whether you could have written it. That is the problem this policy solves. An engineer who ships code they cannot explain, cannot debug, and cannot defend is not a fast engineer — they are an engineer who has not noticed yet that they are stuck. The industry is currently full of people in exactly that position, and the fastest way to stand out is to not be one of them. Studies have shown time and time again that relying on AI too early eliminates understanding which is precisely what you need to succeed in this career.

So this policy does not ask whether you used AI. It asks **what job you gave it.** That question has a different answer in your first three months than it does afterward, and the policy changes with it.

{% hint style="info" %} **Ownership without authorship.** The standard Marcy holds you to, in every quarter, is this: you are responsible for every line of code in your project even if you did not personally type every line of it. You will be asked to explain your code, defend the decisions inside it, and fix it when it breaks. "The AI wrote that part" is never an answer since it is always assumed. {% endhint %}

## The Two Modes

At any moment you are using AI in one of two modes.

|                                | Tutor mode                                                            | Implementer mode                                              |
| :----------------------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------ |
| What the AI does               | Explains, questions, quizzes, critiques, points you at the right idea | Writes code from a specification you wrote                    |
| Who writes the code you submit | You do, by hand                                                       | The AI does, under your direction                             |
| What you are being graded on   | Whether you understand it                                             | Whether you specified it well, verified it, and can defend it |

Both modes are professional. Neither is a punishment or a reward. They train different halves of the same job, and "Tutor mode" comes first because the implementation can only come once your personal understanding is sufficient enough to delegate implementation to someone or something else (AI).

## Tutor Mode: The Baseline Standard

At the start of the year, **AI does not produce code that ends up in your submission.** It can teach you anything you want to know about code. It cannot write it for you.

### The One-Sentence Test

> _Did any content in the file I am submitting arrive there because I copied it from a model, accepted a completion, or typed it out from a model's answer without understanding it first?_

If the answer is yes, that is generation, and it is in violation of the "Tutor Mode" policy. Retyping a model's answer by hand is the same act as pasting it. What matters is whether the understanding came before the keystroke.

If the answer is no, you are inside the policy no matter how much you talked to the model, how many questions you asked it, or how long the conversation ran. Ask it a hundred questions. That is the point.

### The Same Question, Asked Two Ways

Every situation where you would reach for AI has a tutor-mode version and a generator-mode version. The difference is almost always one sentence in how you ask.

**<details><summary>You are stuck and do not know how to start</summary>**

**Generator mode:** "Write a function that takes a list of numbers and returns the average."

**Tutor mode:** "I need to find the average of a list of numbers. I think I need to add them up and divide by how many there are, but I do not know how to add up a list in Python. What should I look up? Do not write the code for me."

The tutor-mode version gets you the name of the thing you are missing, which is the part you did not have. You still write the function.

</details>

**<details><summary>You have an error you do not understand</summary>**

**Generator mode:** "Fix this error." _(pastes the code and the traceback)_

**Tutor mode:** "Here is a traceback I do not understand. Walk me through what each line of it is telling me, starting from the bottom. Do not tell me what the fix is — I want to find it myself."

Reading a traceback is a skill with a ceiling you will hit in about two weeks of practice, and then you will have it for the rest of your career. Handing the traceback to a model instead means you never start the two weeks.

</details>

**<details><summary>You suspect there is a built-in tool for what you are doing by hand</summary>**

**Generator mode:** "Rewrite this loop to be more Pythonic."

**Tutor mode:** "I wrote a loop that counts how many times each word appears in a list. I have a feeling Python has something built in for this. What should I search the standard library documentation for?"

You are allowed to learn that collections.Counter exists. You are not allowed to have the model swap it into your file.

</details>

**<details><summary>You finished and want to know if it is any good ⭐️</summary>**

**Generator mode:** "Improve this code."

**Tutor mode:** "Here is code I wrote. Do not change it. Ask me five questions about it that I would only be able to answer correctly if I actually understood what I wrote. Then tell me which of my answers were weak."

This is the single highest-value thing you can do with an AI tool in Tutor Mode, and almost nobody does it. A model that quizzes you finds the gap in your understanding faster than you will find it yourself.

</details>

**<details><summary>You do not understand something in the curriculum</summary>**

**Generator mode:** "Explain closures and show me an example." _(then copying the example)_

**Tutor mode:** "Explain closures to me using an analogy that has nothing to do with programming. Then ask me to explain it back to you in my own words and tell me what I got wrong."

Explaining a concept back and being corrected is how you find out that you only half-understood it. Reading a good explanation and nodding along in agreement is not.

</details>

### A Standing Instruction You Can Paste

Paste this at the start of a chat session and it will hold for the rest of the conversation:

```
I am a student learning Python. For this entire conversation, do not write code
for me and do not fix my code. You may explain concepts, ask me questions, point
me at documentation, tell me what to search for, and tell me when my reasoning is
wrong. If I ask you to write code, remind me of this instruction instead. When I
share code with you, ask me questions about it rather than rewriting it.
```

This is a genuinely useful habit, not a compliance step. It changes what the tool is good for.

### A Note on Autocomplete

Your editor's inline suggestions are generation, and the one-sentence test above already covers them: accepting a completion puts content in your file that you did not decide on. Turn the feature off — the setup guide for [Mac](https://file+.vscode-resource.vscode-cdn.net/Users/benspector/Documents/curriculum-development/marcy-curriculum-docs-swe-python/environment-setup/local-environment-setup-mac.md) and [Windows](https://file+.vscode-resource.vscode-cdn.net/Users/benspector/Documents/curriculum-development/marcy-curriculum-docs-swe-python/environment-setup/local-environment-setup-windows.md) shows you where.

This is not the same restriction as the one on chat, and the difference is worth understanding rather than memorizing:

- A chat window is something you open and ask, which means your intent comes first and you can hold the answer up against what you expected.
  - A completion arrives before you have said anything at all. It is guessing your intent from the characters you have typed so far, which means there is no expectation for it to be measured against.

There is a practical consequence too. Suggested code and code you wrote yourself end up interleaved in the same file with no record of which was which, so afterward you genuinely cannot say which parts were yours. Being able to say which parts were yours is most of what this program is looking at.

Later in the program, once you are working from a written specification, completions become reasonable again — because by then they are filling in something you already decided.

## Implementer Mode: The Q2 Standard (But only if you are ready)

In Implementor mode AI writes code for you, and the work _you_ do becomes what happens on either side of what the AI does: the **specification** you write before, and the **verification** you do after.

What changes:

- **You write a specification first.** Before you generate anything, you write down what you are building, what files it touches, what the interface looks like, and what "working" means. That document is submitted alongside the project and is graded on its own.
- **You are accountable for every line.** You will be asked to explain any part of what you submitted. Code you cannot explain is code you did not own, and it is scored that way regardless of whether it runs.
- **Over-delivery is a defect.** You ask for a fix and get a refactor. You ask for one route and get a restructured application. Accepting that silently is how you stop being the author of your own architecture. Catching it and rejecting it is part of the job.

This depends on the following workflow becoming a habit: research → plan → implement → test → refine → iterate.

### When the Mode Changes

The rule changes from "Tutor mode" to "Implementor mode" but you must be the judge for yourself when you are ready to make the transition.

Q1 is the only quarter where writing code by hand is the default. That makes it the only quarter that reliably builds the skill of **expectation** — a sense, before you read a piece of code, of what correct code for this problem should look like. How many files. Which functions. Where it is likely to break.

That expectation is necessary for when you transition to using AI in "Implementor Mode". When AI writes 200 lines in four seconds, your job is to look at them and notice that something is off. You cannot notice that something is off if you have no picture of what "on" would have looked like. **A fellow who cannot predict cannot verify, and a fellow who cannot verify is shipping code they do not own.**

Expectation is not a thing you can be told. It is the byproduct of having built things yourself, badly, a few times, and seen what went wrong. Three months is a short time to manufacture it so if you enter Q2 without this skill fully developed, you are not expected to move on to Implementor Mode.

Being ready to make this transition means that you can:

- Predict the shape of correct output before you generate it (and identify how to change it if the output isn't correct)
- Find a defect in code you did not write.
- Articulate why output was produced in a particular way
- Identify "code smell" (code written in unorthodox or non-standard ways)

### What Happens If I'm Not Ready?

If you are not there yet, you still move on to Q2's content — Flask, Postgres, all of it — while spending a few more weeks with AI in tutor mode and doing targeted practice. You are never held back a quarter. The mode is what is adjusted, not your pace and not what you have access to.

If your instructor believes you are not there yet and has evidence from assignments, assessments, and projects, they will tell you plainly and name what specifically is still missing — but your perception is important too.

However, if the evidence says one thing and your gut says another, the evidence is usually right, and the direction people get this wrong is nearly always the same: switching early because there is not enough time, rather than because the skill has arrived.

Running out of time is a real problem and it deserves a real answer. However a conversation about your workload will solve a lack-of-time problem, not a change of mode. Switching early to buy back a few hours costs you the quarter that the rest of the program is built on, and you will not feel that cost until much later, when it is most expensive to fix.

## Where AI Is Never Permitted

In any quarter, in any mode:

- During a GCF.
- On the coding portion of a technical assessment.
- To produce writing you submit as your own reflection or short response. You may use it to check grammar and spelling in writing you already wrote.
- To do a teammate's work, or to complete something you are representing as your own independent work when it is not.

## What Happens When the Policy Is Broken

**The first response is almost never disciplinary.** If you generated code during Q1, we understand that the most likely explanation is that you had a submission due but were out of time (e.g. a late-night work shift, a sick family member, a commute that took the whole evening). That is a rational response to an impossible schedule, and it is a scheduling problem before it is an integrity problem. So the first conversation is about your workload: what is due, what is realistic, and what support you need.

The academic integrity process exists, and it is reserved for the case where that support has been offered and declined.

**Tell us early.** If you are underwater, say so before the deadline rather than after. That conversation is easy. The other one is not. Furthermore, conversations about workload do not end when your fellowship ends. Alerting your manager that a deliverable is going to be late is not uncommon in the work world. But experienced engineers always give a heads up well before the deadline. Start building that habit now\!

## What AI Tools Cost

Some AI capabilities cost money, and we are going to name which ones rather than let you assume that everyone else has something you do not.

Everything Tutor Mode requires works on a free tier. You do not need a paid subscription to complete any assignment, and you will not be at a disadvantage for not having one.

Later quarters use tools where the paid tier is genuinely more capable, and Marcy covers what the curriculum requires. When you reach a professional setting, know that tooling budgets are a normal thing for a team to have and a normal thing for an engineer to ask for. If a company hands you a worse tool than the one you trained on, that is a resourcing decision on their end — it is not you being behind.
