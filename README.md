# ResilientCity AI — Real Flood Cases Research
Author: Raquel Cruz • Version 0.1.0

Independent research prototype for retrospective flood-case analysis. No imports, writes or dependency on V6. V6 remains the synthetic-scenario project. This is a new implementation inspired by the agreed roles, not a verified copy of V6 internals.

## Quick start — PyCharm / Windows
1. Extract this ZIP into a **new folder**. Open that folder as a PyCharm project.
2. Select Python 3.10 or newer. Run `main.py`. The Tkinter GUI opens in **offline** mode without pip dependencies or API key.
3. Select the Pas-de-Calais seed case and click **Run research**. Expect `BLOCKED`: the dossier currently has no verified evidence. Inspect each agent and the actual trace.
4. To use Gemini, run `python -m pip install -r requirements.txt` in the project terminal.
5. In **Run → Edit Configurations → Environment variables**, set `GEMINI_API_KEY` to your private key. `.env.example` documents variable names; the application does **not** automatically load `.env` files. Keep secrets out of JSON, screenshots and GitHub.
6. Import a case JSON, add short evidence excerpts, verify their provenance manually, and select `gemini`. The app requests confirmation before transmitting case evidence to Google. Default model: `gemini-2.5-flash`; override with `GEMINI_MODEL`.

Command-line workflow:
```bash
python main.py --case data/evidence_template.json --mode offline
python -m unittest discover -s tests -v
```
On Linux, Tkinter may require the distribution's tkinter package. No database or extra web server is required.

## Research contract
- Every case stays **retrospective validation pending**. An LLM output never validates a case.
- `verified: true` is a researcher attestation, not automated source verification.
- Both `published_at` and `available_at` must be at/before `evidence_cutoff`. Later evidence is excluded from all agent prompts. Availability means the evidence existed for the retrospective decision point, not the date it was downloaded today.
- Missing, unverified or post-cutoff evidence leads to abstention. No observed flood outcomes are inferred from the case title.
- No live forecasting, emergency instructions or calibrated confidence percentage.
- Gemini mode sends admitted excerpts, case ID/location/cutoff and earlier outputs; it does not browse source URLs.
- No auto-validation, operational approval or real human-review completion is implemented.

## Agents and execution
Coordinator (`Engine`) executes dependent research roles with shared state:
Planner → Evidence → RiskImpact → Decision → Critic → deterministic Safety → pending HumanGate → Communication.
Each LLM role receives prior outputs. This is a **fixed dependent multiagent pipeline**, not an autonomous delegation system. Critic can require revisions; v0.1 blocks the result and requires a new researcher-led run rather than silently revising it. Safety blocks offline, degraded, abstaining or revision-required runs. Otherwise the result is `REVIEW_REQUIRED`, never operationally approved.

Offline mode emits conservative stubs for workflow testing. Gemini mode makes up to five role calls. Transient 429/5xx errors receive at most three attempts per role with backoff; other errors stop immediately. Failure stops remaining API calls, produces labelled fallback and blocks the result. Errors are recorded by type rather than raw response to reduce secret leakage.

Each run creates `outputs/<run_id>/report.json`, `report.md` and real `trace.jsonl`. JSON contains original input, input hash, admitted/excluded evidence, outputs, model, mode and gate. Private evidence excerpts may be present in reports; outputs are git-ignored. Do not publish private source material.

## Case catalogue and migration
Only the visible user-provided Pas-de-Calais ID and cutoff are seeded; its original full dossier is not available here. The other two French cases and seven global cases (including Nepal) must be imported with their original identities and source dossiers. No replacement dates, measurements or source citations have been invented. See `data/evidence_template.json` for the schema; its example URL is a placeholder, not a source. Future case source research is a separate step.

## Validation scope
Automated tests cover cutoff leakage, duplicate IDs, malformed timestamps, unknown citations, downstream state, abstention, API fallback and no automatic approval. Mocked Gemini tests prove integration flow only, not provider behavior or factual quality. GUI visual execution and a live Gemini request must be validated on the user's computer. Dependency range is not a lockfile; record the installed SDK version during live validation.

Retrospective evaluation still requires frozen pre-cutoff evidence, a separately held outcome/reference dossier, a manual baseline, reviewer labels and metrics (traceability, unsupported claims, abstention, missed/unnecessary escalation and reproducibility). v0.1 records research artifacts but does not calculate event accuracy or claim field readiness.

## Future GitHub repository
Suggested name: `resilientcity-real-flood-cases-research`.
Create it after local validation and upload the project contents (not private outputs, secrets or virtual environments). No new remote repository has been created by this package.

SDK reference: https://googleapis.github.io/python-genai/
