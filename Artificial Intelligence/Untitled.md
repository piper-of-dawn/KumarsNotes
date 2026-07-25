

• # Deep Agents: From Tool Calls to Multi-Step Work

  A tool-calling loop works well for a narrow request. A deep-agent runtime becomes useful when the work needs a plan, several passes, isolated research, and managed context.

  The distinction matters because “deep agent” is not a formal level in an AI hierarchy.
  Teams use the label for agent systems built to handle longer, messier tasks. Deep
  research is one application of this design, not a synonym for the design itself. ChatGPT,
  Claude, Manus, and other products offer research or coding workflows with related
  features, but their internal architectures differ.

  The useful question is simpler: what changes when an agent must finish a complex task
  instead of making one tool call?

  ## From an LLM to an agent

  An LLM receives messages and produces a response. Give the model tools and a control
  loop, and the model gets another option: answer or request a tool.

  Suppose you ask for the current temperature in Paris. A model without live weather data
  should not invent an answer. An agent might call a weather service, receive a result, and
  use the result in its response.

  The flow looks like this:

  1. The user sends a request.
  2. The model decides whether a tool is needed.
  3. The runtime executes the selected tool.
  4. The tool result returns to the model.
  5. The model produces an answer or requests another tool.

  People sometimes call a short version of this flow a shallow agent. Treat the phrase as
  informal shorthand. A single tool call is not bad engineering. For a small job, a small
  loop is often the right design.

  Problems appear when the task contains several dependent questions. “Find today’s
  important AI news, explain the economic effects, and connect relevant developments to
  physics research” is not one search. The system must define the scope, gather material
  from several sources, compare claims, retain useful evidence, and assemble a coherent
  answer.

  A plain tool loop might complete such work, but no structure guarantees good
  decomposition or context control.

  ## ReAct

  ReAct is a stronger pattern than a one-shot tool call. The name comes from reasoning and
  acting. In a ReAct loop, the model alternates among reasoning, an action such as a tool
  request, and an observation returned by the environment. The next step depends on the
  latest observation.

  For example, a research agent might:

  6. Search for a company announcement.
  7. Read the primary source.
  8. Notice a reference to a regulatory filing.
  9. Retrieve the filing.
  10. Compare both sources.
  11. Answer once enough evidence exists.

  ReAct supports repeated tool use. Repetition alone does not provide a durable plan,
  delegated context, long-term memory, or reliable state management. Those features require
  more infrastructure.

  The surrounding runtime creates the practical distinction used here. A deep agent still
  uses a model-and-tool loop.

  ## The four-part framework

  The framework used in this tutorial includes four components.

  ### 1. Planning

  Before doing expensive work, the agent writes or maintains a plan. A plan might be a task
  list with status markers, dependencies, and revised steps.

  Take this request:

  > Plan a three-night trip to Paris within a budget of ₹100,000.

  A useful plan separates the work:

  12. Confirm dates, departure city, traveler count, and budget rules.
  13. Estimate flights and local transport.
  14. Find accommodation for three nights.
  15. Build a daily itinerary.
  16. Price meals, tickets, and a contingency amount.
  17. Check the total against the budget.

  Planning does not require a checklist for every question. “What is LangGraph?” needs a
  concise answer or a focused lookup. Planning helps when dependencies, uncertainty, or
  cost make uncontrolled tool use wasteful.

  ### 2. Subagents

  A supervisor agent often delegates a bounded task to another agent with a separate
  context. One subagent might research flights. Another might compare hotels. A third might
  check the budget.

  The main benefit is context isolation. Search results, failed attempts, and intermediate
  notes stay inside the subagent’s run. The supervisor receives a smaller result instead of
  every token produced during the investigation.

  A single synchronous task call makes the supervisor wait for its subagent. If the model
  issues several task calls in one turn, those calls run in parallel. Background work needs
  async subagents or separate orchestration. More agents also add latency, cost, and
  coordination errors. Use a subagent when isolation or specialization is worth the added
  overhead.

  ### 3. System prompts

  The system prompt defines the agent’s role, operating rules, tool policy, evidence
  standard, and expected output. A research agent needs instructions about primary sources,
  citations, uncertainty, and stopping conditions. A coding agent needs rules for
  repository inspection, tests, security, and file edits.

  The exact prompt used by a commercial coding product is neither required nor a reliable
  template. The useful lesson is structural. State what the agent owns, which actions need
  approval, how tools should be used, and what counts as completion.

  ### 4. Filesystem and state

  Long tasks produce more information than a model should keep in its active context.
  Filesystem tools give the agent a place for notes, plans, extracted evidence, and
  intermediate drafts.

  “Filesystem” does not always mean files on your laptop. The Deep Agents library supports
  several backends. Its default StateBackend stores a virtual filesystem in LangGraph state
  scoped to one thread. A checkpointer preserves those files across turns in the same
  thread. Cross-thread storage requires StoreBackend or another durable backend. Local disk
  access requires FilesystemBackend. Persistence is a configuration choice, not an
  automatic property of every deep agent. The official backend documentation
  (https://docs.langchain.com/oss/python/deepagents/backends) explains the distinction.

  Shared state also needs discipline. If every subagent writes arbitrary notes into one
  directory, the result is clutter with filenames. Define paths, formats, ownership, and
  retention rules.

  ## A second example: researching and writing a blog post

  Suppose the user provides a topic and asks for a researched article. A sensible plan
  might include:

  18. Define the question and intended audience.
  19. Search current web sources.
  20. Find relevant papers or primary documents.
  21. Build an evidence ledger.
  22. Draft the article.
  23. Check claims, citations, and originality.

  Separate subagents might handle web research, academic sources, and factual review. A
  writing agent then uses the evidence ledger. The supervisor decides whether each result
  meets the brief.

  Some tasks are independent and suitable for parallel execution. Others depend on earlier
  findings. Drafting before research finishes wastes work. A deep-agent design should
  represent those dependencies instead of launching every task at once.

  ## Build a small deep agent with Python

  The following example creates a research agent with a Tavily search tool. The deepagents
  package is a standalone library built on LangChain components and the LangGraph runtime.
  According to the Deep Agents overview
  (https://docs.langchain.com/oss/python/deepagents/overview), the framework includes
  planning, filesystem tools, context management, and subagent delegation around the same
  core tool-calling loop used by simpler agents.

  ### 1. Create the project

  Start in an empty directory:

  uv init
  uv venv
  source .venv/bin/activate

  On Windows PowerShell, activate the environment with:

  .venv\Scripts\Activate.ps1

  Install the libraries:

  uv add deepagents langchain tavily-python python-dotenv ipykernel

  Add the provider integration required by your model. For OpenAI, for example:

  uv add langchain-openai

  If you use a Jupyter notebook, register the environment as a kernel:

  uv run python -m ipykernel install --user --name deep-agents-demo

  uv add records dependencies in pyproject.toml and updates the lockfile. Use uv pip
  install -r requirements.txt only when a project already uses a requirements file. uv -r
  requirements.txt is not a valid installation command.

  ### 2. Add environment variables

  Create .env in the project root:

  TAVILY_API_KEY=replace-with-your-key
  MODEL=openai:replace-with-a-model-name-supported-by-your-account

  Add secret files and the virtual environment to .gitignore:

  .env
  .venv/

  The model value above is a placeholder. Use a provider and model identifier supported by
  your installed LangChain integration and account. This avoids tying the tutorial to a
  model name likely to change.

  ### 3. Create the Tavily search tool

  The Tavily Search API
  (https://docs.tavily.com/documentation/api-reference/endpoint/search) currently accepts
  general, news, and finance as search topics. Sports stories belong under news. Keyword
  argument order has no effect in Python, so match names correctly and favor readability
  over positional ordering.

  import os
  from typing import Literal

  from dotenv import load_dotenv
  from tavily import TavilyClient

  load_dotenv()

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


  def web_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ) -> dict:
      """Search the web for current information."""
      return tavily_client.search(
          query=query,
          topic=topic,
          max_results=max_results,
          include_raw_content=include_raw_content,
      )

  The type annotation narrows the topic values exposed to the model. The docstring tells
  the agent when the tool is useful. In a production system, add timeouts, retries, result-
  size limits, domain rules, and error handling.

  ### 4. Create the deep agent

  import os

  from deepagents import create_deep_agent
  from langchain.chat_models import init_chat_model

  model = init_chat_model(os.environ["MODEL"], temperature=0)

  SYSTEM_PROMPT = """
  You are a research assistant.

  For multi-step requests, create and maintain a concise plan.
  Use web search for current or source-dependent claims.
  Prefer primary sources when available.
  Separate sourced facts from your own inference.
  Return a direct answer with source links.
  Do not delegate or create files when a short answer is enough.
  """

  agent = create_deep_agent(
      model=model,
      tools=[web_search],
      system_prompt=SYSTEM_PROMPT,
  )

  The core call is small. Most behavior comes from the model, system prompt, tool
  descriptions, built-in middleware, and selected backend.

  Deep Agents exposes a planning tool named write_todos, filesystem tools, and a task tool
  for subagent delegation. The model chooses whether to call those tools. A trivial prompt
  does not guarantee a task list, a file, or a subagent run.

  Middleware summarizes older context and offloads large tool results when configured
  thresholds are reached. The model does not need to request either operation as a normal
  tool call.

  ### 5. Compare the result with a normal LangChain agent

  from langchain.agents import create_agent

  simple_agent = create_agent(
      model=model,
      tools=[web_search],
      system_prompt="You are a concise research assistant.",
  )

  Both agents use a model, messages, and tools. The simple agent is a good default for
  short workflows. The deep agent adds a prebuilt framework for planning, context
  management, filesystem access, and delegation.

  This distinction prevents a common mistake. A deep agent is not a different kind of LLM.
  The term describes an agent runtime with more operating structure.

  ### 6. Invoke the agent

  Use a request complex enough to exercise research behavior:

  result = agent.invoke(
      {
          "messages": [
              {
                  "role": "user",
                  "content": (
                      "Explain what LangGraph is, using current primary sources. "
                      "Compare its role with LangChain agents and list two cases "
                      "where a graph workflow is the better choice."
                  ),
              }
          ]
      }
  )

  For a long run, streaming gives better visibility than waiting for one final object. A
  later implementation should inspect stream events by type instead of printing every
  internal message without filtering.

  ### 7. Inspect the answer and state

  final_message = result["messages"][-1]
  print(final_message.content)

  print(result.keys())

  files = result.get("files", {})
  for path, metadata in files.items():
      print(path, metadata)

  The final message contains the user-facing answer. Other state fields depend on the
  installed package version, middleware, and backend. Some versions expose virtual files in
  returned graph state. Other backends expect inspection through filesystem tools or their
  storage interface.

  Do not infer local-disk persistence from a files field. With StateBackend, files are
  scoped to one agent thread. A checkpointer preserves them across turns in the same
  thread. Cross-thread memory needs StoreBackend or another durable backend. Local disk
  access needs FilesystemBackend and strict path controls.

  ## What this first version does not solve

  The small example verifies agent construction and invocation. Successful execution does
  not establish research quality.

  Several failure modes remain:

  - The model might create a weak plan or skip planning.
  - Search results might contain stale, duplicated, or low-quality claims.
  - A subagent might return a confident summary without enough evidence.
  - Extra agent calls increase latency and token cost.
  - Large tool results still need limits and careful summarization.
  - Local filesystem and shell access create security risk.
  - Long-term memory needs explicit storage, namespaces, and retention rules.
  - Reproducibility needs pinned dependencies, traces, and evaluations.

  A single synchronous subagent call blocks the supervisor until completion. Several task
  calls issued in one model turn run in parallel. Background work requires async subagents
  or separate orchestration. The subagent documentation
  (https://docs.langchain.com/oss/python/deepagents/subagents) explains these execution
  modes.

  The right test is not whether the agent produced many steps. The right test is whether
  each step improved correctness, context control, or auditability. Extra activity without
  extra reliability adds cost and irrelevant output.

  ## What part two should add

  The next version should move beyond defaults and cover:

  1. Model selection and provider configuration.
  2. A stronger system prompt with evidence and stopping rules.
  3. Multiple tools with narrow descriptions and permissions.
  4. Custom subagents with separate prompts, models, and tool access.
  5. Backend selection for ephemeral files, local files, and durable memory.
  6. Streaming and tracing for long runs.
  7. Interrupts and human approval before sensitive actions.
  8. Evaluation of plans, sources, final answers, cost, and latency.

  A deep-agent framework helps when a task requires decomposition, context isolation, and
  managed state. For a weather lookup or a small calculation, use the simpler agent. Add
  structure only when the result improves.
