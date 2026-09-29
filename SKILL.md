---
name: python-to-android-migrator
description: Analyze a Python application, with specialized Streamlit analysis when present, and plan or execute a native Kotlin/Jetpack Compose Android migration. Use when converting a Python/Streamlit app to Android, preserving selected functionality, adding/removing/modifying/moving features, introducing an API boundary, or validating feature parity. Always obtain user decisions before implementation of meaningful product or architecture changes.
---

# Python to Android Migrator

Migrate the application, not the source syntax. Treat the existing repository as the behavioral baseline and create a platform-independent migration specification before writing Android code.

## Workflow

1. **Discover** the repository: entry points, package manager, Python modules, databases, external services, authentication, environment variables, tests, and deployment assumptions.
2. **Analyze architecture**: separate presentation, business logic, AI/ML pipelines, persistence, integrations, and configuration. Detect Streamlit and analyze `st.*`, session state, forms, pages, widgets, callbacks, uploads, downloads, and navigation when present.
3. **Extract features and workflows** from code, README/docs, tests, and UI paths. Do not infer undocumented product behavior as fact; mark uncertainty.
4. **Audit security** for credentials, tokens, secrets, unsafe client exposure, filesystem assumptions, and server-only capabilities. Report findings before implementation.
5. **Write the migration artifacts** under `.migration/` using the schemas in `references/migration-spec.md`.
6. **STOP for user review.** Present the discovered feature inventory and ask the user to classify meaningful features as `preserve`, `modify`, `remove`, `add`, `move`, or `replace`. Natural-language answers are valid. Do not start Android implementation until feature decisions are resolved.
7. **Propose architecture** for the approved product. Prefer keeping Python/AI/data logic server-side and exposing a clear API when the existing UI is tightly coupled to Python. Propose native Android replacements for browser-only interactions. Ask for approval on consequential architecture choices.
8. **Implement incrementally**: backend/API boundary first where required, then Kotlin/Compose screens, state, networking, persistence, permissions, and Android-native integrations. Preserve business behavior unless the approved specification says otherwise.
9. **Validate continuously**: build, test, exercise workflows, and maintain a traceability matrix from original feature → backend operation → Android screen/code → validation status.
10. **Finish with a parity audit** listing preserved, intentionally changed, removed, and newly added functionality plus unresolved limitations.

## Decision rules

- Never silently remove or materially change a user-facing feature.
- Never expose server-side API keys, database credentials, or privileged operations in the APK.
- Do not mechanically reproduce Streamlit layout; translate user intent into Android-native UX.
- Keep AI/ML, database, filesystem, and secret-dependent operations on the backend unless the user explicitly approves an on-device design.
- If a feature is ambiguous, ask rather than guessing.
- Use the existing repository's actual code as evidence; distinguish observed behavior from proposed behavior.

## Supporting material

- `references/migration-spec.md` — schemas and required migration artifacts.
- `references/streamlit-to-compose.md` — Streamlit behavior mapping and Android UX guidance.
- `references/backend-and-api.md` — extracting Python services and designing API boundaries.
- `references/android-architecture.md` — recommended Kotlin/Compose architecture and implementation conventions.
- `references/feature-review.md` — interactive feature-review protocol and question templates.
- `references/validation.md` — parity, build, test, and traceability procedure.
- `scripts/analyze_repository.py` — deterministic local repository inventory helper.
- `scripts/detect_streamlit.py` — Streamlit-specific static inventory helper.
- `scripts/detect_secrets.py` — heuristic secret/credential detector; findings require human verification.
