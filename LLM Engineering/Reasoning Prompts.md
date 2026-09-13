1
A language model can often answer a simple question immediately. But some problems punish immediacy.

Consider:

> A database has become slow. Should we shard it?

A weak answer may jump straight to _yes_ or _no_. A better answer first asks what kind of problem we actually have: How large is the database? Are queries poorly indexed? Is the bottleneck reads or writes? Would a cache help? Only after establishing those principles should the model decide whether sharding is justified.

That is the basic idea behind **reasoning prompts**: instead of asking only for an answer, we influence **how the model approaches the problem before producing that answer**.

The progression in class was essentially:

```text
Direct answer
    ↓
Reason step by step
    ↓
Give the reasoning a structure
    ↓
Control randomness
    ↓
Notice that reasoning can still fail
    ↓
Step back to general principles
    ↓
Apply those principles to the specific case
```

Each step exists because the previous one has a weakness.

---

## 1. Why not simply ask the question?

Suppose we ask:

```text
Solve this train problem.
```

The model receives the problem and tries to produce an answer.

Conceptually:

```text
Problem ───────────────→ Answer
```

For an easy task, that may be completely sufficient.

The difficulty appears when the answer depends on several intermediate facts.

A train problem might require:

```text
departure times
      ↓
head start
      ↓
remaining distance
      ↓
relative speed
      ↓
travel time
      ↓
clock time
```

If the model mentally loses one of those pieces, the final answer can fail even though every individual calculation is easy. This motivates our first improvement.

---

# 2. Chain-of-Thought: Don't Jump Straight to the Finish Line

**Chain-of-Thought (CoT)** — a prompting technique where a problem is approached through intermediate reasoning steps instead of jumping directly from the question to the final answer.

The simplest version is something like:

```text
Solve the problem.
Reason step by step before giving the final answer.
```

Instead of:

```text
Problem ─────────────────────→ Answer
```

we are encouraging:

```text
Problem
   ↓
Step 1
   ↓
Step 2
   ↓
Step 3
   ↓
Answer
```

This is what the class called **vanilla CoT**.

**Vanilla** — the plain, basic version of something, without additional machinery or customization.

The teacher's train example showed why this can be useful. The model explicitly worked through ideas such as the first train's head start, the remaining distance, the combined relative speed, and finally the meeting time.

The main benefit is not mystical. We have simply turned **one large jump** into **several smaller jumps**.

---

## 3. Zero-Shot CoT: Ask for Reasoning Without Showing an Example

Now suppose we use:

```text
Reason step by step.
```

but we never demonstrate what those steps should look like.

That is **zero-shot Chain-of-Thought**.

**Zero-shot** — asking a model to perform a task without first giving it an example of the desired task and answer.

Compare:

|Prompt style|What the model receives|
|---|---|
|Zero-shot|Instruction only|
|One-shot|Instruction + 1 example|
|Few-shot|Instruction + several examples|

So:

```text
"Reason step by step."
```

is zero-shot.

Whereas:

```text
Example:
Question: ...
Reasoning:
1. ...
2. ...
Answer: ...

Now solve:
Question: ...
```

is no longer zero-shot.

The teacher's practical advice was to **start simple**. If vanilla zero-shot reasoning already solves the problem reliably, there is little reason to construct something more elaborate.

But another problem soon appears.

The model may reason correctly while producing a messy wall of text.

That leads to the next step.

---

# 4. Structured CoT: Give the Reasoning a Skeleton

Instead of merely saying:

```text
Reason step by step.
```

we can tell the model **which steps to perform**.

For the train problem, the class used roughly this progression:

```text
Step 1: Identify the given values.
Step 2: Set up the equation.
Step 3: Perform the arithmetic.
Step 4: Convert the result to clock time.
```

This is **structured Chain-of-Thought**.

**Structured CoT** — Chain-of-Thought where the desired intermediate stages are explicitly defined instead of leaving the model to invent its own reasoning structure.

The difference is important.

### Vanilla CoT

```text
Problem
   ↓
Model decides what reasoning to perform
   ↓
Answer
```

### Structured CoT

```text
Problem
   ↓
Identify facts
   ↓
Construct relationship
   ↓
Calculate
   ↓
Convert result
   ↓
Answer
```

With structured CoT, we are no longer merely saying:

> Think more.

We are saying:

> Think about **these things, in this order**.

That makes the output easier to use inside a larger program.

---

## 5. Why Structure Matters More in Pipelines

Imagine that one LLM's output becomes another component's input.

**Pipeline** — a sequence of processing stages where the output of one stage becomes the input of the next.

For example:

```text
User question
     ↓
LLM reasoning
     ↓
Extract final time
     ↓
Calendar system
```

If the model returns:

```text
Well, first let us consider Chicago and then...
...several paragraphs...
Therefore the answer appears to be 1:13 PM.
```

your program now has to find `1:13 PM` inside all that prose.

But if you request:

```text
<reasoning>
...
</reasoning>

<answer>
1:13 PM
</answer>
```

the two pieces are easier to separate.

**Parsing** — taking some output and mechanically separating it into the pieces a program needs.

Conceptually:

```text
                ┌─ reasoning ─→ useful for inspection
LLM output ─────┤
                └─ answer ────→ useful for next program
```

This is why the teacher preferred structured output for multi-stage systems and agents: you do not want every downstream component digging through free-form prose.

But structure has a cost.

---

# 6. More Reasoning Usually Means More Tokens

If you ask for:

```text
Answer: 1:13 PM
```

the model produces very little text.

If you ask for:

```text
1. Identify all variables.
2. Explain the head start.
3. Derive the equation.
4. Calculate relative speed.
5. Verify the result.
6. Give the final answer.
```

the model does more work and usually generates more text.

That means more **tokens**.

**Token** — a small chunk of text processed by an LLM. A token may be a whole short word, part of a word, punctuation, or another text fragment. API usage is commonly measured partly in tokens.

So there is a trade-off:

|Approach|Reasoning control|Token use|
|---|--:|--:|
|Direct prompt|Low|Low|
|Vanilla CoT|Medium|Higher|
|Structured CoT|High|Usually higher|
|Multi-stage reasoning|Very high|Higher again|

The important lesson is not:

> Always use reasoning.

It is:

> Spend reasoning where the problem deserves reasoning.

A trivial lookup does not need six stages.

A difficult debugging problem might.

---

# 7. Reasoning Is Not the Same as Reliability

This is where the lecture becomes more interesting.

It would be tempting to think:

```text
More reasoning
     ↓
More correctness
```

But that is not guaranteed.

The class tested a small logic puzzle involving people and pets. The prompt explicitly instructed the model to:

```text
1. List the constraints.
2. Apply them one by one.
3. Eliminate impossible assignments.
4. Identify the unique solution.
```

The output looked disciplined.

It had numbered steps.

It appeared to follow the constraints.

And it still produced an answer that contradicted one of the original constraints.

That gives us a crucial distinction:

```text
well-formatted reasoning ≠ correct reasoning
```

A model can produce a beautifully organized mistake.

This is one of the most important ideas in reasoning prompts.

**Constraint** — a rule that a valid solution is not allowed to violate.

If the problem says:

```text
Alice does NOT own the fish.
```

then any solution ending with:

```text
Alice owns the fish.
```

is wrong, regardless of how elegant the preceding explanation looks.

So reasoning traces must not be confused with proof.

---

# 8. Temperature: Why the Same Prompt Can Behave Differently

At this point the class introduced **temperature**.

**Temperature** — a generation setting that changes how strongly the model favors its highest-scoring next-token choices. Lower values generally make generation more conservative; higher values allow more variation.

Very roughly:

```text
Lower temperature
        ↓
prefer the most likely choices more strongly
        ↓
less variation

Higher temperature
        ↓
allow less-likely alternatives more often
        ↓
more variation
```

For tasks where repeatability matters, the teacher recommended keeping temperature low, often around `0`.

But he also emphasized something subtle:

```text
temperature = 0
```

does **not** mathematically guarantee that every call forever will produce an identical result.

**Deterministic** — producing exactly the same output whenever the same input is supplied.

So:

```text
low temperature → more stable
```

is reasonable.

But:

```text
temperature 0 → absolute guarantee of identical output
```

is too strong.

That matters enormously in production systems.

If a prompt works 49 times out of 50, the fiftieth output can still break your application.

And this brings us to a deeper question.

What if the problem is not that the model needs **more steps**?

What if it is reasoning from the wrong starting point?

---

# 9. Step-Back Prompting: Reason About the Rules Before the Case

Suppose we ask:

> We have 10,000 users and two million rows in PostgreSQL. Queries take eight seconds. Should we shard the database?

A direct answer encourages the model to attack the case immediately.

```text
Specific problem
      ↓
Specific answer
```

**Step-back prompting** inserts another layer.

**Step-back prompting** — asking the model to first identify broader principles relevant to a problem, then use those principles to reason about the specific case.

Instead of immediately asking whether to shard, we first ask something like:

> What are the general decision criteria for choosing between indexing, caching, vertical scaling, read replicas, and sharding?

Now the process becomes:

```text
Specific problem
      ↓
Step back
      ↓
General principles
      ↓
Return to the specific problem
      ↓
Decision
```

This is a different kind of reasoning.

CoT says:

> Break this problem into steps.

Step-back prompting says:

> Before solving this instance, identify the rules that should govern the decision.

---

# 10. The Database Example Makes the Difference Clear

Consider the original question:

```text
2 million rows
10,000 users
8-second queries

Should we shard?
```

A direct answer can become anchored on the word _scale_:

```text
Slow database
    ↓
Large data
    ↓
Sharding is a scaling technique
    ↓
Maybe shard
```

But the step-back prompt asks about the full toolbox first:

```text
                    Database is slow
                           │
                           ▼
               What are my options?
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
      Indexing           Cache          Query tuning
         │                 │                 │
         └──────────┬──────┴─────────┬───────┘
                    ▼                ▼
             Read replicas     Vertical scaling
                    │                │
                    └───────┬────────┘
                            ▼
                         Sharding
```

Now sharding is no longer treated as **the** solution.

It is one option among several.

**Index** — an additional data structure maintained by a database so it can locate certain rows faster instead of scanning everything.

**Cache** — a faster temporary storage layer that keeps frequently requested results so they do not have to be recomputed or reread every time.

**Vertical scaling** — giving one machine more resources, such as CPU or memory.

**Read replica** — another copy of a database that can handle read queries, reducing read pressure on the main database.

**Sharding** — splitting a database's data across multiple database servers so that no single server has to contain or handle everything.

Once those principles were generated, the class passed them back into the next call and asked the model to apply them to the actual numbers.

The resulting recommendation became sharper: at that scale, sharding was likely premature; investigate simpler remedies first.

The key improvement was not merely a longer answer.

It was a better **decision frame**.

---

# 11. CoT and Step-Back Prompting Solve Different Problems

This distinction is worth keeping.

|Technique|Main question it asks|
|---|---|
|Direct prompting|“What is the answer?”|
|Vanilla CoT|“What steps lead to the answer?”|
|Structured CoT|“Which specific steps should lead to the answer?”|
|Step-back prompting|“What general principles should govern those steps?”|

A useful mental picture is:

```text
STEP-BACK
"What rules matter here?"
        │
        ▼
GENERAL PRINCIPLES
        │
        ▼
STRUCTURED CoT
"Apply them in this order."
        │
        ▼
SPECIFIC REASONING
        │
        ▼
ANSWER
```

They are not really competitors.

They can sit on top of one another.

---

# 12. Why Step-Back Prompting Is Especially Useful for Decisions

Some questions are calculations.

```text
What is 17 × 23?
```

You probably do not need step-back prompting.

Other questions involve choosing among competing approaches:

```text
Should we shard?
Should we cache?
Should we redesign the API?
What caused this bug?
Which architecture is appropriate?
```

These are different because the model must first decide **what factors deserve attention**.

That is where stepping back can help.

The pattern is:

```text
Specific situation
      ↓
Identify relevant principles
      ↓
Identify relevant evidence
      ↓
Compare alternatives
      ↓
Apply principles to evidence
      ↓
Decision
```

This is much closer to how an experienced engineer often works.

They do not begin with:

> Which technology should I deploy?

They begin with:

> What problem am I actually trying to solve?

---

# 13. Structured Reasoning for Debugging

The class then carried the same idea into code debugging.

Suppose we have:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

It works for:

```python
[2, 4, 6]
```

but fails for:

```python
[]
```

A vague debugging prompt might say:

```text
Fix this code.
```

A structured reasoning prompt can instead force a sequence:

```text
1. Determine what the function is intended to do.
2. Trace representative test cases.
3. Identify the failing case.
4. Determine the root cause.
5. Propose the smallest correction.
6. Verify the corrected behavior.
```

Notice how naturally one stage creates the question for the next.

```text
What should it do?
        ↓
What does it actually do?
        ↓
Where do they differ?
        ↓
Why?
        ↓
What change fixes that difference?
        ↓
Does the change survive the tests?
```

That is the real theme running through the entire lesson:

> **Good reasoning prompts create dependencies between steps.**

Step 2 exists because Step 1 established something.

Step 3 exists because Step 2 exposed something.

The prompt is no longer a checklist of unrelated instructions.

It becomes a small reasoning process.

---

# 14. The Deeper Pattern: Decomposition

All of these techniques are variations of one very simple idea.

**Decomposition** — breaking one difficult problem into smaller problems that can be solved separately and then combined.

Instead of:

```text
BIG PROBLEM
     ↓
   ANSWER
```

we create:

```text
BIG PROBLEM
     │
     ├─ What do we know?
     │
     ├─ What rules apply?
     │
     ├─ What follows from those rules?
     │
     ├─ What alternatives remain?
     │
     └─ Does the result satisfy the original constraints?
                         │
                         ▼
                       ANSWER
```

And that immediately explains why reasoning prompts sometimes work better.

The model is being asked to solve several smaller, more explicit prediction problems instead of one giant ambiguous prediction problem.

But it also explains why they are not magic.

If one intermediate step is wrong:

```text
correct
  ↓
correct
  ↓
WRONG
  ↓
reasonable-looking
  ↓
reasonable-looking
  ↓
wrong final answer
```

later steps can faithfully build on the mistake.

So decomposition improves **organization**.

It does not automatically create **truth**.

---

# 15. A Practical Hierarchy

The cleanest way to use these ideas is to escalate only when necessary.

```text
Start
  │
  ▼
Can a direct prompt solve it reliably?
  │
  ├── Yes ──→ Stop.
  │
  └── No
       │
       ▼
Would explicit intermediate reasoning help?
       │
       ├── Yes ──→ Vanilla CoT
       │
       └── No / still unreliable
                     │
                     ▼
          Do I know the required stages?
                     │
                     ├── Yes ──→ Structured CoT
                     │
                     └── No
                           │
                           ▼
             Is this a decision where general
             principles should be established first?
                           │
                           ├── Yes ──→ Step-back
                           │
                           └── No ──→ Reconsider the task
```

The goal is not to construct the most sophisticated prompt possible.

The goal is to introduce **only enough reasoning structure to make the task reliable and usable**.

---

# Core Intuition

Reasoning prompting is easiest to remember as three increasingly strong instructions:

```text
CoT:
"Don't jump. Work through it."

Structured CoT:
"Work through THESE stages."

Step-back:
"Before working through the case,
decide which principles should govern it."
```

And then one warning must sit underneath all three:

```text
A visible sequence of reasoning
        ≠
a guarantee that the reasoning is correct.
```

Reasoning prompts help the model **organize a difficult problem**.

Validation is what tells you whether it actually solved it.

---

### Source note

**Teacher said:** The Sep 12 class explicitly moved from vanilla/zero-shot CoT to structured CoT, token-cost concerns, temperature and determinism, a logic-puzzle failure, step-back prompting with the PostgreSQL scaling example, and finally structured CoT for debugging. The teacher repeatedly stressed that extra reasoning consumes more tokens and that even structured reasoning can still return a wrong answer.

**Notebook says:** I could not locate the matching Sep 12 prompt-engineering notebook in the uploaded project materials, so I have not attributed notebook content that I could not verify. Your later PR-review notes do independently use the same idea of ordered, inspectable reasoning stages rather than one mega-prompt.