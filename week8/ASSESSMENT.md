# Week 8 Assessment — The Price is Right Finale

## What the assessment is

The Week 8 assessment is **completing the agentic finale**: get "The Price is Right" running end-to-end. There is no separate rubric document; the video (captions) and Day 5 describe the deliverable:

- A **Gradio UI** that:
  - Shows **memory** (deals surfaced so far) in a table (Description, Price, Estimate, Discount, URL).
  - Streams **agent logs** (scanner, ensemble, frontier, specialist, messaging, planning).
  - Optionally shows a **3D plot** of the vector database (t-SNE of product embeddings).
  - Re-runs the pipeline **every 5 minutes** via a Gradio timer.
- The app is **launchable** from the command line (e.g. `uv run price_is_right.py`) so it runs as a standalone process and stays responsive.

So the assessment is: **demonstrate a working agentic workflow with a proper user interface**, using the deal agent framework (memory, planning agent, tools, multiple models).

---

## Prerequisites (what must be in place)

| Prerequisite | Where it comes from | Why |
|-------------|---------------------|-----|
| **Vector DB** (`products_vectorstore`) | Day 2 notebook: load product data, embed, add to Chroma | `DealAgentFramework` and `EnsembleAgent` need RAG over this DB. |
| **Modal specialist** | Day 1: deploy fine-tuned model on Modal | `EnsembleAgent` uses Specialist (Modal) + Frontier + Neural Net. |
| **Env vars** | `.env` in repo root or week8 | `OPENAI_API_KEY` (frontier/scanner), `OPENROUTER_API_KEY` (messaging + preprocessor use OpenRouter with Claude Sonnet 4.6), `PUSHOVER_USER` and `PUSHOVER_TOKEN` (for push notifications when a deal is found), `HF_TOKEN` for embeddings, Modal credentials. |
| **Python env** | `uv` or `pip` from repo root | Run from `week8` so `deal_agent_framework`, `agents`, `log_utils` are importable. |

You do **not** need to use `AutonomousPlanningAgent` for this assessment; the main `deal_agent_framework` uses `PlanningAgent` (scanner → ensemble → messenger), which is what Day 5 and the captions describe.

---

## Course of action (steps to complete the assessment)

1. **Confirm Week 8 days 1–4 are done**
   - Day 1: Modal app and SpecialistAgent working.
   - Day 2: Vector DB created and populated (e.g. Day 2 notebook run in LITE_MODE or full); RAG + Frontier + Ensemble run.
   - Day 3: ScannerAgent and MessagingAgent run (RSS scan, message crafting).
   - Day 4: `DealAgentFramework` runs (e.g. `DealAgentFramework().run()` in a notebook or script) and memory read/write works.

2. **Run from the `week8` directory**
   - All imports (`deal_agent_framework`, `agents`, `log_utils`) assume the current working directory is `week8` (or that `week8` is on `PYTHONPATH` and cwd for `memory.json` and `products_vectorstore`).
   - From repo root:  
     `cd week8 && uv run price_is_right.py`  
   - Or from a notebook: set `os.chdir(week8_dir)` then `!uv run price_is_right.py` (see assessment notebook).

3. **Optional: reset memory**
   - To start with a clean, small state:  
     `DealAgentFramework.reset_memory()`  
   - This truncates `memory.json` to the first two entries (as in the video).

4. **Launch the app**
   - Run:  
     `uv run price_is_right.py`  
   - The Gradio UI should open (e.g. in browser). On load it runs the pipeline once (scanner → ensemble → messenger), shows the deals table and logs; then the 5-minute timer re-runs the pipeline.

5. **Verify success**
   - UI shows title and subtitle.
   - Table shows "Deals found so far" (from memory); may start with 0 or with existing rows after reset.
   - Logs panel shows colored agent messages (Planning, Scanner, Ensemble, Frontier, Specialist, Messaging).
   - 3D plot loads (or shows "Loading vector DB..." then plot if DB exists).
   - After a full run, if a deal exceeds the threshold, memory updates and the table updates; optionally you get a push notification if configured.

---

## Reasoning behind this plan

- **Single deliverable**: The video and Day 5 frame the finale as one runnable app (Gradio + framework + timer). The assessment is “get that app running,” not a separate exam.
- **Prerequisites first**: The app depends on Chroma, Modal, and env vars; without Day 1–2 (and 3–4) the UI would load but the pipeline would fail or be incomplete.
- **Run from `week8`**: The codebase uses relative paths and local imports (`deal_agent_framework`, `agents`, `log_utils`); running from `week8` avoids import and path errors.
- **Reset memory**: Optional but matches the video and gives a predictable starting state for demos.
- **Success = UI + pipeline + timer**: If the UI launches, logs stream, the table can update, and the timer re-runs the pipeline, you’ve shown the full agentic loop (LLM in the loop with tools, orchestration, memory, and autonomy) and the assessment is satisfied.

---

## Optional improvements (not required for assessment)

- **Empty vector DB**: If the DB is missing or empty, the 3D plot can show a “Vector Database Empty” message (see e.g. solisoma’s `price_is_right_fixed.ipynb`) so the UI doesn’t error.
- **Deals table during run**: Some contributions keep the table showing current memory while the pipeline runs, so existing deals don’t disappear until the run completes; the main `price_is_right.py` updates the table when the run finishes, which is acceptable for the assessment.
- **OpenRouter / API keys**: The messenger (and optionally other agents) can be configured to use OpenRouter or other providers so the app runs without direct Anthropic/OpenAI keys if that’s your setup.

---

## Summary

| Item | Action |
|------|--------|
| **Goal** | Have "The Price is Right" Gradio app running with deal agent framework, memory, logs, and 5‑minute timer. |
| **Prerequisites** | Days 1–4 done; vector DB populated; env vars set; run from `week8`. |
| **Steps** | 1) Confirm days 1–4. 2) From `week8`, optionally reset memory. 3) Run `uv run price_is_right.py`. 4) Confirm UI, table, logs, and timer. |
| **Success** | UI launches, pipeline runs, logs stream, table reflects memory, timer re-runs every 5 minutes. |

This keeps the assessment **solid** (one clear deliverable, clear prerequisites) and **workable** (concrete steps and success criteria you can follow and verify).
