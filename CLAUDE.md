# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- SSH push from Claude Code verified working on 2026-03-16 -->

## Package Management

This project uses `uv` (not pip) for dependency management:

```bash
uv sync                          # Install all dependencies
uv add <package>                 # Add a new dependency
uv pip compile pyproject.toml -o requirements.txt  # Regenerate requirements.txt
```

CrewAI projects in `3_crew/*/` each have their own `pyproject.toml` and must be managed independently with `uv` from within each project directory.

## Running Code

**Jupyter Notebooks** — the primary format for labs:
```bash
jupyter lab          # Launch Jupyter Lab
```

**Gradio Apps** (found in `1_foundations/`, `4_langgraph/`, `6_mcp/`):
```bash
python app.py        # Start local Gradio server
```

**CrewAI Projects** (run from inside each project directory):
```bash
cd 3_crew/<project>/
crewai run           # Execute the crew
```

**MCP Servers** (run as separate processes):
```bash
python 6_mcp/accounts_server.py
python 6_mcp/market_server.py
```

**Environment diagnostics:**
```bash
python setup/diagnostics.py
```

## Linting

```bash
ruff check .         # Lint
ruff format .        # Format
```

## Notebook Output Management

`nbstripout` is configured to strip outputs before commits. Do not commit notebooks with outputs. To manually strip:
```bash
nbstripout <notebook>.ipynb
```

## Architecture Overview

This is a **6-week AI agents curriculum**, organized as weekly labs that progressively introduce agent frameworks:

| Week | Directory | Framework |
|------|-----------|-----------|
| 1 | `1_foundations/` | Direct LLM APIs (OpenAI, Anthropic) |
| 2 | `2_openai/` | OpenAI Agents SDK |
| 3 | `3_crew/` | CrewAI multi-agent orchestration |
| 4 | `4_langgraph/` | LangGraph stateful workflows |
| 5 | `5_autogen/` | AutoGen AgentChat |
| 6 | `6_mcp/` | Model Context Protocol (MCP) |

Supporting content: `guides/` (12 technical notebooks), `setup/` (OS-specific install instructions), `assets/`.

### Key Architectural Patterns

**LangGraph (Week 4)** — `4_langgraph/sidekick.py` is the most complete example:
- `TypedDict` state passed through graph nodes
- Worker LLM node + Evaluator node in a feedback loop
- Playwright browser tools for web automation
- `MemorySaver` for checkpointing; SQLite for persistence
- Gradio UI in `app.py` wires async calls to the graph

**CrewAI (Week 3)** — Each subdirectory in `3_crew/` is an independent project:
- Agents defined with roles/goals/backstory
- Tasks defined separately and assigned to agents
- `Crew` object orchestrates execution
- Each project is a standalone `uv` workspace

**MCP (Week 6)** — Most complex architecture:
- `accounts_server.py` / `market_server.py` / `push_server.py` expose resources via MCP
- `trading_floor.py` orchestrates multiple trader agents
- `database.py` handles SQLite persistence (accounts, transactions, portfolio history)
- `tracers.py` integrates LangSmith for observability
- Gradio app (`app.py`) visualizes trader performance with Plotly charts

**AutoGen (Week 5)**:
- Agent definitions in `agent.py`, message handling in `messages.py`
- SQLite (`tickets.db`) for state persistence

### Environment Variables

The `.env` file at the repo root is loaded by most notebooks/scripts via `python-dotenv`. Expected keys include API credentials for OpenAI, Anthropic, LangSmith, Polygon, SendGrid, and others depending on the lab.

## Workflow (from AGENTS.md)

- Work from the repository root; keep changes scoped to the requested task.
- For non-trivial tasks: search for relevant files → open key files → propose changes → apply edits.
- Keep edits minimal; avoid formatting-only churn.

## MCP Server Preference

- Prefer MCP server `pycharm_2025` when available (PyCharm 2025.3.3).
- Fall back to `pycharm_2026` only when `pycharm_2025` is unavailable.
- If `pycharm_2026` shows no tools, ignore it when running PyCharm 2025.3.3.