# Scope and Sequence: F26 Transition Year

This document assigns every Technical Lecture session of the F26 fellowship to a week, a day, and a topic. Environment setup and virtual environments are covered in orientation, before day 1, so the first Technical Lecture session is Command Line Interfaces. Technical Lecture is one 90-minute session per day, Monday through Thursday. Sessions below are given as a week number within the quarter and a position within that week, so day 1 is the week's first session and day 4 its last. A holiday makes a short week of three sessions rather than moving the days that remain. Technical Interview Prep runs in the daily Code Challenge block and Labs run in their own block, so neither appears here. The fellowship starts on Monday, September 28, 2026 and the capstone begins on Monday, June 7, 2027.

The three breaks fall on the quarter boundaries. Q1 ends on Friday, December 18 before winter recess. Q2 ends on Friday, March 19 before spring break. Q3 ends on Friday, May 28 before the summer office closure. There is no review week between units; every session carries content or assessment, apart from two unassigned sessions in Q1: week 5 day 4, just before the Mod 1 project week, and week 12 day 4, the last teaching day before winter recess.

## Calendar

Breaks: winter recess December 21 to January 4, spring break March 22 to 26, summer office closure May 31 to June 4.

Holidays assumed off and removed from the counts below: Indigenous Peoples' Day (October 12), Veterans Day (November 11), Thanksgiving (November 26), MLK Day (January 18), Presidents' Day (February 15), and Independence Day observed (July 5). The Wednesday before Thanksgiving is a teaching day.

| Quarter                                             | Dates             | Weeks | Sessions |
| --------------------------------------------------- | ----------------- | ----- | -------- |
| Q1 Computational Thinking and Responsible Use of AI | Sept 28 to Dec 18 | 12    | 44       |
| Q2 Fullstack and AI-Assisted Development            | Jan 5 to Mar 19   | 11    | 41       |
| Q3 AI-Led Project Building and Systems Design       | Mar 29 to May 28  | 9     | 36       |
| Q4 Capstone                                         | Jun 7 to Aug 27   | 12    | 47       |

## Q1: Computational Thinking and Responsible Use of AI

Scope and sequence lives here now: https://docs.google.com/spreadsheets/d/12tpWg-vkxx6Roa_qjMLCf87RBAZnYIxk6WIIt3t7Uu0/edit?gid=0#gid=0

## Q2: Fullstack and AI-Assisted Development

Forty-one sessions. The quarter opens on January 5 with the mode inversion: AI moves from tutor to implementer, and the first session teaches the workflow fellows will use for the rest of the year. HTML, CSS, and Jinja take six sessions, HTTP and APIs take three, Flask takes seven, Postgres takes ten, the AI strand takes three including the opening, verification takes four, and the project with its architecture defense takes eight.

Four chapters run as assigned reading with a Lab rather than a lecture: the Box Model, Grid and Media Queries, Accessibility, and Aggregates and Seeding. The personal portfolio project runs in Lab and Friday time. The essential tools and libraries unit lives in Q3 as framing-context material rather than in Q2. Passwords, sessions, authorization, and user-owned resources are compressed to two sessions because the Q3 Security module hardens the authentication those two sessions establish. Production deployment is the Q3 Deployment module.

The four verification sessions are Group 5 material and are named sessions so that Flask and Postgres content does not absorb them. The remaining Q2 AI topics not covered in the three lecture sessions run in Leadership Seminar.

| #   | Week | Day | Unit         | Session                                                                             |
| --- | ---- | --- | ------------ | ----------------------------------------------------------------------------------- |
| 1   | 1    | 1   | AI           | Q2 Opening: AI as Implementer. The research, plan, implement, test, refine workflow |
| 2   | 1    | 2   | Mod 3        | HTML                                                                                |
| 3   | 1    | 3   | Mod 3        | CSS                                                                                 |
| 4   | 2    | 1   | Mod 3        | Flexbox                                                                             |
| 5   | 2    | 2   | Mod 3        | Forms                                                                               |
| 6   | 2    | 3   | Mod 3        | Jinja Templating: Variables, Loops, and Conditionals                                |
| 7   | 2    | 4   | Mod 3        | Jinja Templating: Template Inheritance, Blocks, and Macros                          |
| 8   | 3    | 1   | Mod 5        | How the Internet Works: HTTP, Requests, and Responses                               |
| 9   | 3    | 2   | Mod 5        | JSON and APIs                                                                       |
| 10  | 3    | 3   | Mod 5        | Consuming APIs from Python with an HTTP Client                                      |
| 11  | 4    | 1   | Mod 5        | Intro to Flask: Routing and the Request-Response Cycle                              |
| 12  | 4    | 2   | Mod 5        | Flask: Handling Forms and POST-Redirect-GET                                         |
| 13  | 4    | 3   | Mod 5        | Flask: Rendering Templates and Serving Static Files                                 |
| 14  | 4    | 4   | Mod 5        | Flask: Blueprints, the Application Factory, and MVC                                 |
| 15  | 5    | 1   | Mod 5        | Flask: Configuration, Environment Variables, and Secrets                            |
| 16  | 5    | 2   | Mod 5        | Flask: A Server-Rendered CRUD Application                                           |
| 17  | 5    | 3   | Mod 5        | Case Study: Bookmark Manager                                                        |
| 18  | 5    | 4   | Verification | The Flask and Postgres Defect Taxonomy                                              |
| 19  | 6    | 1   | Mod 6        | Intro to Databases and Postgres                                                     |
| 20  | 6    | 2   | Mod 6        | Intro to SQL                                                                        |
| 21  | 6    | 3   | Mod 6        | Creating Tables                                                                     |
| 22  | 6    | 4   | Mod 6        | Schema Design and Normalization                                                     |
| 23  | 7    | 1   | Mod 6        | JOIN Queries                                                                        |
| 24  | 7    | 2   | Mod 6        | Connecting Flask to Postgres with psycopg                                           |
| 25  | 7    | 3   | Mod 6        | Postgres-Backed Models                                                              |
| 26  | 8    | 1   | Mod 6        | Passwords, Sessions, and Login                                                      |
| 27  | 8    | 2   | Mod 6        | Authorization and User-Owned Resources                                              |
| 28  | 8    | 3   | Mod 6        | Case Study: Social Bookmark Manager                                                 |
| 29  | 8    | 4   | Verification | Debugging Code You Did Not Write                                                    |
| 30  | 9    | 1   | AI           | Model Selection and Evaluation; What AI Is Good and Bad At                          |
| 31  | 9    | 2   | AI           | Context Windows, Skills, and Memory                                                 |
| 32  | 9    | 3   | Verification | Scope Containment                                                                   |
| 33  | 9    | 4   | Verification | The Context-Management Exercise: a degraded session                                 |
| 34  | 10   | 1   | Project      | Q2 Project, day 1: problem selection and plan review                                |
| 35  | 10   | 2   | Project      | Q2 Project, day 2: spec artifact submission                                         |
| 36  | 10   | 3   | Project      | Q2 Project, day 3: build                                                            |
| 37  | 10   | 4   | Project      | Q2 Project, day 4: build                                                            |
| 38  | 11   | 1   | Project      | Q2 Project, day 5: build                                                            |
| 39  | 11   | 2   | Project      | Q2 Project, day 6: build                                                            |
| 40  | 11   | 3   | Project      | Q2 Project, day 7: build and defense preparation                                    |
| 41  | 11   | 4   | Project      | Architecture Defense                                                                |

## Q3: AI-Led Project Building and Systems Design

Thirty-six sessions. Every fellow rotates through five systems modules built against a shared CRUD application. Each module runs the 24-hour spec loop over seven sessions, and the mentor stack review takes the final session. Deployment runs first so that the application is live from the second week of the quarter and every later module's presentation happens against a running URL rather than a local server. Technical Lecture in Q3 is structured build time with instructor check-ins; each module's ideas are introduced in seminar on its first day.

| Module                      | First session | Last session | Sessions |
| --------------------------- | ------------- | ------------ | -------- |
| Deployment and Environments | Week 1 Day 1  | Week 2 Day 3 | 7        |
| Security                    | Week 2 Day 4  | Week 4 Day 2 | 7        |
| Testing                     | Week 4 Day 3  | Week 6 Day 1 | 7        |
| Cost                        | Week 6 Day 2  | Week 7 Day 4 | 7        |
| Bottlenecks and Sandboxing  | Week 8 Day 1  | Week 9 Day 3 | 7        |
| Mentor stack review         | Week 9 Day 4  | same day     | 1        |

Each module follows the same seven-session shape:

| Session | Activity                                                          |
| ------- | ----------------------------------------------------------------- |
| 1       | State the problem; interrogate the stakeholder about requirements |
| 2       | Return with a spec; receive feedback                              |
| 3       | Return with tools and approach                                    |
| 4 to 6  | Implement                                                         |
| 7       | Present; constraint-specific salted review                        |

Q3 has no slack. Thirty-six sessions of demand sit in thirty-six sessions of supply, and the spec loop is clock-bound, so a mentor absence or a closed day removes a module's presentation rather than delaying it. The cost-and-failure audit pairs with the Cost module's session 7. Live interview practice runs in Code Challenge.

## Q4: Capstone

June 7 to August 27, forty-seven sessions across twelve weeks, for a real stakeholder. The stakeholder requirement translation assessment runs in the first two weeks; the handoff test, cold-context handoff, and full-cycle review run in the final week.

## Decisions this schedule depends on

- Leadership Seminar carries the ethics, academic-impact, and policy content of the AI strand in Q1, and the AI topics not given lecture sessions in Q2. If it cannot, Q1 needs two more sessions and Q2 needs two more, and neither quarter has them.
- Q3 runs five modules. Folding Bottlenecks and Sandboxing into Security, or pairing it with Cost, would free seven sessions and give Q3 its only buffer.
