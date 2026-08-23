# Project Overview: Master AI Agentic Engineering

This repository is a comprehensive 6-week curriculum designed to teach the development and deployment of autonomous AI Agents. It covers a range of modern frameworks and protocols, including OpenAI Agents SDK, CrewAI, LangGraph, AutoGen, and the Model Context Protocol (MCP).

## Architecture & Structure

The project is organized into weekly modules, each focusing on a specific aspect or framework of Agentic AI:

| Week | Directory | Framework / Focus |
|------|-----------|-------------------|
| 1 | `1_foundations/` | Core LLM APIs (OpenAI, Anthropic) & Tool Calling |
| 2 | `2_openai/` | OpenAI Agents SDK |
| 3 | `3_crew/` | CrewAI (Multi-agent orchestration) |
| 4 | `4_langgraph/` | LangGraph (Stateful, graph-based workflows) |
| 5 | `5_autogen/` | AutoGen (AgentChat & programming workflows) |
| 6 | `6_mcp/` | Model Context Protocol (MCP) & Resource Extensions |

### Supporting Directories
- `guides/`: 12 technical notebooks covering Python foundations, async, and project setup.
- `setup/`: OS-specific installation instructions (Mac, Linux, PC, WSL) and diagnostic tools.
- `assets/`: Static assets and diagrams used in notebooks and apps.

## Building and Running

### Dependency Management
This project uses **`uv`** for fast and reliable dependency management.
- **Install all dependencies:** `uv sync`
- **Add a new dependency:** `uv add <package>`
- **Regenerate requirements.txt:** `uv pip compile pyproject.toml -o requirements.txt`

*Note: CrewAI projects in `3_crew/*/` are independent `uv` workspaces and must be managed from their respective directories.*

### Execution Commands
- **Jupyter Notebooks:** `jupyter lab` (Primary format for labs)
- **Gradio Apps:** `python app.py` (Found in Weeks 1, 4, and 6)
- **CrewAI Executions:** `cd 3_crew/<project> && crewai run`
- **MCP Servers:** `python 6_mcp/accounts_server.py` or `python 6_mcp/market_server.py`
- **Diagnostics:** `python setup/diagnostics.py`

## Development Conventions

### Coding Standards & Linting
- **Linting:** `ruff check .`
- **Formatting:** `ruff format .`
- **Minimalism:** Keep edits surgical and scoped to the task. Avoid formatting-only changes.

### Notebook Management
- **Output Stripping:** Notebook outputs must be stripped before committing to prevent repository bloat and diff noise.
- **Tool:** `nbstripout` is configured. Manually strip with `nbstripout <notebook>.ipynb`.

### Environment Configuration
- **API Keys:** Use a `.env` file at the repository root. Required keys typically include `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `LANGSMITH_API_KEY`, and others depending on the specific lab.
- **Persistence:** SQLite is used for state persistence in LangGraph (Week 4), AutoGen (Week 5), and MCP (Week 6).

### MCP Server Preference
This codebase supports both **PyCharm 2025.3.3** and **PyCharm 2026.1 EAP**.
- Use the MCP server that matches the active IDE version (`pycharm_2025` or `pycharm_2026`).
- If multiple servers are available, default to the one that currently provides tools.
- Do not assume one version is superior; both are valid for development.
