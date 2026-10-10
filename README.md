# ResilientCity AI — Real Flood Cases Research
Author: Raquel Cruz • Version 0.2.0

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

## Real flood cases identified for research

The research list contains **10 previously identified cases: 3 French cases and 7 international candidates**. Locations and periods below preserve the earlier research shortlist; they are **provisional dossier labels, not independently verified event metadata**. Source verification, evidence-cutoff selection and retrospective tests remain pending for every case.

| # | Case / location | Country | Period recorded in the research shortlist | Research status | Available in the v0.2 catalogue |
| --- | --- | --- | --- | --- | --- |
| 1 | Pas-de-Calais — Aa River | France | November 2023 | Real French case received — retrospective validation pending | Registered; verified evidence not imported |
| 2 | Gard / Hérault | France | October 2024 | Real French case received — retrospective validation pending | Registered; original evidence import pending |
| 3 | Nancy | France | May 2012 | Real French case received — retrospective validation pending | Registered; original evidence import pending |
| 4 | Porto Alegre | Brazil | May 2024 | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |
| 5 | Ahr Valley | Germany | July 2021 | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |
| 6 | Sindh | Pakistan | 2022 | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |
| 7 | Rasuwa — Bhote Koshi and Trishuli rivers | Nepal | August 2026 — provisional; exact event date and geographic scope require verification | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |
| 8 | Valencia | Spain | 2024 | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |
| 9 | Texas — Guadalupe River | United States | 2025 | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |
| 10 | Derna | Libya | 2023 | International research candidate — source verification and retrospective validation pending | Registered; evidence preparation pending |

**Listing a case does not mean the system has analysed or validated it.** The three French cases retain the collective status **“real French cases received — retrospective validation pending”**. The seven international cases remain research candidates; no execution or source validation is claimed.

## Registered case catalogue — v0.2

All ten cases are selectable in the GUI from `data/catalog.json`. The catalogue includes 24 source candidates, event periods, missing-data notes and pending-validation labels. These registrations do not imply executed analysis or verified evidence.

- `Sources & registration` displays source URLs, access limitations and missing fields.
- `Register / update` saves the edited case to the local catalogue by incident ID, adding a new registration or updating an existing one. Saving does not approve evidence or validate the event.
- `Export case` writes an individual JSON for later import.
- Nine cases have `evidence_cutoff: null`; Pas-de-Calais preserves the supplied cutoff `2023-11-06T08:00:00Z`. Pending cutoff is permitted for registration and yields a BLOCKED report without API calls.
- `sources` contains research metadata only and is never passed to Gemini. Only manually verified, temporally admissible entries in `evidence` may be admitted. All ten initial evidence lists are empty.
- Gard/Hérault remains an ambiguous episode pending original dossier identification. The other new incident IDs are project research identifiers, not official authority IDs.

Use `data/evidence_template.json` to prepare admitted evidence. Unknown publication/availability timestamps remain pending rather than being replaced with event dates. Local registration changes are saved in the project folder, not automatically pushed to GitHub.

## Internet evidence research — 10 October 2026

An initial source-discovery pass produced **10 research dossiers and 24 source records**:

- [Research report in Portuguese](docs/RESEARCH_EVIDENCE_PT_BR.md): source links, dates, access limitations and case-specific gaps.
- [Structured research dossiers](data/research_dossiers.json): staging data with source roles and unknown timestamps represented as null.

Nancy's municipal history identifies the night of 21–22 May 2012; ICIMOD identifies the Rasuwa event on 26 August 2026. Gard/Hérault still needs a unique episode and catchment because multiple October 2024 episodes were found.

These files are **research staging artifacts, not GUI-importable case inputs**. Their source metadata is included in the v0.2 registered catalogue; it does not enable LLM analysis. Original publication times and historical availability must be established before converting source candidates into admitted evidence. Sources read only through search metadata or blocked during retrieval are explicitly labelled. Retrospective validation remains pending for all ten cases.

## Validation scope
Automated tests cover cutoff leakage, duplicate IDs, malformed timestamps, unknown citations, downstream state, abstention, API fallback and no automatic approval. Mocked Gemini tests prove integration flow only, not provider behavior or factual quality. GUI visual execution and a live Gemini request must be validated on the user's computer. Dependency range is not a lockfile; record the installed SDK version during live validation.

Retrospective evaluation still requires frozen pre-cutoff evidence, a separately held outcome/reference dossier, a manual baseline, reviewer labels and metrics (traceability, unsupported claims, abstention, missed/unnecessary escalation and reproducibility). v0.1 records research artifacts but does not calculate event accuracy or claim field readiness.

## GitHub repository

Project repository: https://github.com/raquelquiterio2014-byte/resilientcity-real-flood-cases-research

Version 0.2 is published on `main`. Desktop visual validation and a live Gemini request remain pending. Keep private outputs, API keys and virtual environments out of published commits.

SDK reference: https://googleapis.github.io/python-genai/
