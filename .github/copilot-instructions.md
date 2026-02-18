<!-- Copilot/AI guidance for contributors and coding agents -->
# Copilot instructions — prompt-engineering-for-generative-ai

This file gives focused, actionable guidance for AI coding agents editing this repository.

## Purpose
- Help contributors understand the repo layout, development workflow, and model-integration patterns so edits are safe and productive.

## Big picture
- This repo is a small collection of example scripts and chapters that demonstrate prompt engineering and model usage. The root `main.py` is a trivial entrypoint; the substantive examples live under `chapterone`.
- Key example files: `chapterone/main.py` (Cohere chat demo) and `chapterone/one.py` (Hugging Face model pipeline).

## Developer workflow (discoverable)
- Use the workspace virtualenv (the repo typically uses a `.venv` in the workspace). Activate it before running scripts: `source .venv/bin/activate`.
- Install dependencies from the PEP 621 `pyproject.toml` with:

```bash
python -m pip install -e .
```

- Run examples directly, e.g. `python chapterone/main.py` or `python chapterone/one.py`.

## Required tools & VS Code extensions
- Local CLI tools (macOS):
  - `python` 3.10+ (required by `pyproject.toml`) and `pip` for installs.
  - `git` for source control and commits.
  - `curl` or `httpie` for quick web requests and verifying APIs.
  - `jq` (optional) for parsing JSON CLI responses.
  - `rg` / `ripgrep` (optional) for fast code search.
- Recommended VS Code extensions:
  - `Python` (ms-python.python) — language support, run/debug, testing.
  - `Pylance` (ms-python.vscode-pylance) — type checking and language server.
  - `GitHub Copilot` (GitHub.copilot) — AI coding assistant.
  - `GitHub Copilot Chat` or `Copilot Labs` (if available) — conversational code help and web-assisted lookups.
  - `DotENV` (mikestead.dotenv) — helpful when editing `.env` examples.
  - `GitLens` (eamodio.gitlens) — enhanced git history when reviewing changes.
- Agent / automation needs:
  - Programmatic web search: provide `curl`/`httpie` and an allowed outbound network policy for the agent. If your agent platform supports a web-search or browsing plugin, enable it and document which plugin is in use.
  - File modification: agents must have workspace file write access and `git` available to create branches and commits. Use branch naming convention like `ai/edit-<short-desc>`.

## Project-specific conventions & patterns
- Environment variables: examples use `python-dotenv` and call `load_dotenv()`; secrets are expected in a local `.env` file. Example env var: `COHERE_API_KEY` used in `chapterone/main.py`.
- Model initialization patterns:
  - When loading HF models, code often uses `trust_remote_code=True`, `device_map='cpu'` and explicit `torch_dtype`. Preserve these flags unless you fully understand memory/device implications.
  - Cohere examples use `cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))` and `co.chat(...)` patterns.

## Integrations & dependencies to be aware of
- Declared dependencies are in `pyproject.toml`: `transformers`, `torch`, `cohere`, `openai`, `huggingface-hub`, `fastapi`, etc. Changes to CI or packaging should respect `pyproject.toml`.
- Model heavy operations may require GPU and extra configuration; examples default to CPU and small pipelines.

## Safe edit rules for agents (concrete)
- Do not commit API keys or `.env` contents. If adding an example that requires credentials, read from env vars only and document the env var name in `README.md`.
- When modifying model-loading code, keep `device_map` and `trust_remote_code` options explicit. If changing device usage, update `README.md` and call out memory/repro implications.
- Keep example scripts simple and self-contained; prefer adding new example files under `chapter*` instead of editing existing ones when experimenting.

## Debugging & testing notes
- There are no automated tests in the repo. Validate changes by running the relevant example locally after activating `.venv`.
- Use prints or short runners — the files already use `print(response)` and `print(...)` for quick validation.

## Where to document changes
- Add usage notes or env var instructions to `README.md` (currently empty). If you add a new dependency, update `pyproject.toml` and add a short note to `README.md` about installation.

## If you need to update this guidance
- Keep this file concise. Only include patterns that are visible in the repository (examples, env var names, dependency usage). If you add infrastructure (tests, CI, Docker), update this document with concrete commands and file references.

---
If any section here is unclear or you want me to expand examples (installation, running with GPU, or adding a CI job), tell me which area and I'll iterate.
