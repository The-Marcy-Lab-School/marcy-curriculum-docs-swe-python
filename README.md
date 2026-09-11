---
cover: .gitbook/assets/Screenshot 2024-09-05 at 4.29.43 PM.png
coverY: 0
layout:
  width: default
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Welcome

Welcome to Marcy Lab School's Fullstack Software Engineering Curriculum! Here, you will find all of the lecture notes, recordings, slides, and code examples as well as cheat sheets, guides, and miscellaneous resources.

Over the next year you will learn how to be a software engineer who can build real products and direct AI tools to help build them. You'll learn the basics of Python syntax, how to use Python to solve real problems, how to organize and design a system before you build it, and how to read, verify, and defend code — including code you did not personally write.

{% embed url="https://docs.google.com/presentation/d/1ErVMKugQc4ObNVhreLYplYZP3OsA5AmFyNSDcPKr8PA/embed?delayms=3000&loop=false&start=false" %}

## The Curriculum

In the Software Engineering Fellowship at Marcy Lab School, you will learn how to build full-stack web applications in Python, and how to work alongside AI coding tools without losing ownership of what you build. Along the way you will learn a variety of languages, technologies, developer tools, and more including:

- **Languages:** Python, Bash, HTML, CSS, SQL
- **Frameworks & Libraries**: Flask, Jinja, pytest, the Python standard library
- **Technologies**: PostgreSQL
- **Developer Tools**: VS Code, Git, GitHub, Command-Line, pip, venv, Ruff, AI coding assistants

### The Fellowship Arc

The core curriculum is delivered over four quarters, with individual modules spanning 1 to 6 weeks.

**Q1 — Computational Thinking & Responsible Use of AI (months 0–3).** The command line, Git and GitHub, Python syntax, the Python ecosystem, and object-oriented programming. Alongside it: how AI actually works, how to prompt it, what it costs, and Marcy's academic honesty policy. This is the quarter where you write code by hand, because it is the quarter that builds your sense of what correct code looks like.

- [Module 0: Command Line Interfaces, Git & GitHub](mod-0-command-line-interfaces-git-and-github/)
- Module 1: Python Fundamentals
- Module 2: Object-Oriented Programming and System Design

**Q2 — Fullstack & AI-Assisted Development (months 3–6).** HTML and CSS, APIs, servers with Flask, server-side rendering, and Postgres. Alongside it: model selection, context management, and the research-plan-implement-test-refine workflow. AI moves from tutor to implementer, and your job moves to specifying and verifying.

**Q3 — AI-Led Project Building and Systems Design (months 6–9).** You are handed a working application and asked to extend it under a rotation of real constraints: security, testing, cost, sandboxing, and deployment. Each one is a tight loop — understand the constraint, decide, direct AI to implement it, and defend the decision to a practitioner who has solved that problem for real.

**Q4 — Capstone (months 9–11).** A real stakeholder with real, shifting requirements. The first time nobody hands you the problem already framed.

## Technical Competencies

Software Engineering has always and continues to require mastery over syntax and deep knowledge of relevant technologies, libraries, and APIs.

However, writing code is is simply the medium through which engineers express ideas, design systems, and solve problems. The competencies listed below are the durable skills that will allow a software engineer to transcend any single tech stack and become a leader of their team.

These competencies provide shared vocabulary and alignment between Marcy instructors, who design curriculum and model excellence in the classroom, and Marcy fellows who seek guidance on their strengths and areas of growth.

_Note: these competencies often will overlap and support each other. For example, technical communication requires effective mental modeling and systems-level thinking._

<details>

<summary><strong>1. Technical Communication</strong>: Clearly articulating what you built, how you built it, and why to diverse audiences.</summary>

As a software engineer, you must be able to communicate effectively for a variety of audiences: hiring managers, teammates, junior engineers, AI chatbots. Across the many domains in which you must be able to communicate effectively, the _what_, the _how_, and the _why_ and all three must be delivered with the utmost clarity:

- _Communicating Product Development:_ What are you building and why? What users did you have in mind? How did you prioritize which features to build first and which features did you decide to leave out?
- _Communicating Tool Selection:_ What specific tools and technologies are you using? What alternatives did you consider and why did you choose this specific stack? What were the tradeoffs?
- _Communicating Code Structure:_ How is your solution organized? What are the key components and how do they interact? What considerations were you making for the team members who might have to maintain this code?
- _Communicating Problem Solving:_ What were the key implementation challenges? What limitations did you face? How did you work within or around them?

The ability to communicate well improves team collaboration and instills confidence in your competence as an engineer. The impression you make through your communication may be the single most important factor in securing a job. This is true of all industries, not just software engineering.

**Indicators**

- Shares not just what they did, but how they did it and why it matters.
- Articulates technical decisions and their impact on the project timeline, performance, or user experience
- Uses effective analogies, diagrams, and code snippets to enhance explanations
- Adapts communication style based on audience (technical vs. non-technical stakeholders)
- Can effectively communicate in both writing and in oral presentations.

**Pitfalls:** struggling to explain code clearly, lack of audience awareness, difficulty articulating technical decisions and tradeoffs

</details>

<details>

<summary><strong>2. Building Mental Models</strong>: Simplifying complex concepts such that they can be easily understood.</summary>

Software engineering is full of complexity. Not only is there a vast scope of concepts, tools, and technologies to learn, any given software project can contain millions of lines of code, hundreds or more files, and dozens or more interdependent parts. To deal with this complexity, you need the ability to quickly build mental models for any topic.

A mental model distills a complex concept, system, algorithm, tool or technology into its most essential parts such that it can be used or explained simply without getting lost in the details. In other words, it is an **abstraction**.

Mental models also enable us to organize the great variety of concepts we must learn into recognizable categories. Then, when we encounter problems that we've seen before, we know which tools and technologies to reach for.

**Indicators**

- Can illustrate a concept using an analogy or a diagram.
- Can explain a concept clearly with simplified language.
- Corrects misconceptions when new evidence emerges.
- Can communicate algorithms using pseudocode.
- Can identify essential vs. extraneous details when analyzing a problem.
- Accurately applies known solutions, data structures, and algorithms to new but similar problems.
- Makes informed technical decisions based on understanding of high-level tradeoffs.

**Pitfalls:** memorizing syntax without understanding why, holding misconceptions, difficulty transferring knowledge to new situations.

</details>

<details>

<summary><strong>3. Thinking in Systems</strong>: Analyzing how individual components interact with and depend on each other within a larger system.</summary>

Any set of things that work together can be considered a system. Systems can range in scale from a simple algorithm to a complex, multi-layered application.

_Thinking in Systems_ is the ability to zoom out and see how a system works as a whole, to break down the system into smaller components, and to identify the dependencies between connected components.

For example, the diagram below represents the layers of a full-stack web application. As software engineers, we need to be able to view an application in this manner and understand how the layers communicate with each other. The specific technologies in this diagram are from a JavaScript stack rather than the Python one you will learn — which is the point of this competency. The layers, and the questions you ask about how they talk to each other, do not change when the tools do.

![A full-stack application system diagram, showing the layers of a web application and how they communicate.](.gitbook/assets/full-stack-diagram.svg)

Systems-level thinking enables us to design, reason about, implement, and debug complex algorithms all the way up to complex applications. It is what separates “programmers” (those who can write functional code) from “software engineers” (those who can design reliable and maintainable code).

**Indicators**

- Sees the big picture and how pieces connect (front-end, back-end, DB, APIs).
- Anticipates ripple effects of a change.
- Designs for extensibility, debug-ability, and reliability, not just “getting it to work.”
- Breaks large problems into smaller ones.
- Identifies dependencies between subtasks.

**Pitfalls:** tunnel vision on one layer of the stack, failing to anticipate ripple effects, struggling to “zoom out.”

</details>

<details>

<summary><strong>4. Methodical Problem Solving:</strong> Applying a structured, methodical approach to plan, implement, test, and debug, and refine code.</summary>

Mental models may allow you “vibe-code” your way to a sloppily hacked-together application. However, once things break, a real engineer will know how to follow a methodical approach to debug the problem, identify the root cause, and implement a fix. Randomly trying solutions or guessing at the root cause won’t cut it!

Additionally, code that works today can still cause problems tomorrow if it isn't implemented with care. Experienced engineers will carefully plan before they code and then will review, refine, and refactor existing solutions to reduce redundancy, improve their efficiency, and improve readability.

**Indicators**

- Makes a plan before implementing code
- Can trace through code execution to understand program behavior.
- Tests solutions comprehensively, ensuring edge cases are covered.
- Reads error messages and test output carefully and investigates root causes.
- Tries multiple strategies when initial approach fails.
- Seeks to understand root causes rather than applying surface-level fixes.
- Identifies areas where solutions can be improved to reduce redundancy, improve efficiency, or improve readability

**Pitfalls:** jumping into code without planning an approach first, frequently “guessing” at what the problem is without systematically finding the root, ignoring error messages, not asking for help in a timely manner, giving up too quickly when the initial approach doesn’t work, accepting code that works without evaluating it's long-term effectiveness.

</details>

<details>

<summary><strong>5. Quality Discernment</strong>: Taking professional pride in producing high-quality software, documentation, and presentation materials while having a keen eye for what does not meet the bar.</summary>

Writing functional code is the prerequisite for being a professional Software Engineer. The quality of _how_ you code, communicate, and collaborate is what will distinguish you as an engineer that teams want to work with.

Quality Discernment is about taking pride in every line of code you write (or AI writes for you) and in every document and presentation that you produce.

**Indicators**

- Reads documentation and instructions thoroughly.
- Writes clean, organized and readable code that follows established style guides and coding conventions.
- Creates well-structured, error-free documentation, READMEs, and presentations
- Double-checks work before submitting for review or presentation.
- Reviews code generated by AI with a critical eye.
- Proactively seeks feedback and implements learnings in subsequent work.
- Follows git best practices

**Pitfalls:** Submitting code that raises numerous linting flags and doesn’t adhere to known style guides. Creating documentation, technical writing, and technical presentations that are error-filled or contain typos or technical inaccuracies. Repeating the same mistakes without incorporating feedback. Accepting AI-generated code without evaluating it carefully.

</details>

## Additional Learning Resources

For each of these resources, if you find a definition or explanation confusing, use AI to summarize it for you. But remember, don’t just ask for an answer. Use AI to help refine your understanding.

- **The lazy way**: asking Claude for the answer.
- **A step up**: asking Claude to point you to a few expert resources on it.
- **The way that actually works**: asking Claude to summarize the confusing part, then explaining it back in your own words. If you can't, you don't understand it yet — you've just read it.xt

**Documentation (official, your source of truth).** It might be painful at first, but reading official docs is a skill you must hone; nothing else stays as current or as accurate.

- Python docs — [https://docs.python.org](https://docs.python.org)
- Official docs for whatever you're building with — Flask, Postgres, etc.

**Courses & books (readability over precision).** Pick one of these two, not both — they cover similar ground.

- [_Automate the Boring Stuff with Python_](https://automatetheboringstuff.com/) _(Al Sweigart)_ — free, fully online, and teaches Python by solving real problems (renaming files, scraping a page) instead of opening with abstract syntax. Best if you want to feel useful in chapter one.
- _Python Crash Course_ (Eric Matthes) — the more conventional, project-based alternative (you build a game, a data visualization, and a small web app).

**Alternatives, including YouTube (specific people, not just "watch some videos").** These three are each named repeatedly by working developers for teaching why, not just how:

- [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) — widely considered the standard for Python fundamentals and web frameworks (including Flask). He explains what's happening under the hood and why you'd choose one approach over another, not just that a piece of syntax works, which is what separates programmers who can still read their own code six months later from people who have to re-Google basic syntax every session.
- [ArjanCodes](https://www.youtube.com/arjancodes) — covers SOLID principles applied to Python, common design patterns, dependency injection, and protocol-based interfaces. Go here once you can already write working code and want to know how to structure it well.
- [mCoding (James Murphy)](https://www.youtube.com/@mCoding) — short, dense, and focused on what's actually happening inside Python. Good for once you want to stop treating the language as a black box.

**Tool acquisition (picking up a new framework or tool)**

- [Scrimba](https://scrimba.com/) — its interactive format lets you pause a lesson and edit the instructor's code inline, which makes it a fast way to get oriented in a new tool before you turn to official docs for the real depth. Its Python catalog is thin, so it's not where you go to learn the language itself — but its React and AI-engineering tracks (LLMs, agents, RAG, prompt engineering, the OpenAI/Claude/MCP tooling you'll be using directly) are well-suited to exactly this: a quick, hands-on first pass at a new tool.
