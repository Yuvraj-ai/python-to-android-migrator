# Backend and API Migration

Separate Python responsibilities into:

1. presentation code
2. business/domain logic
3. AI/ML orchestration
4. persistence
5. external integrations
6. configuration/secrets

If Streamlit directly imports business functions, do not copy those functions into Kotlin. Prefer extracting them into service modules and exposing explicit API operations.

Typical target:

```text
Android Kotlin/Compose
        |
      HTTPS
        v
Python API (FastAPI or existing API)
        |
        +-- domain services
        +-- AI/LLM workflows
        +-- database
        +-- external services
```

Only introduce FastAPI when an API boundary is actually needed; preserve an existing well-designed API when possible.

API contracts should define request/response models, validation, authentication, errors, long-running job behavior, and file transfer semantics.

Keep secrets server-side. If the current app asks the user for an API key, explicitly ask whether that behavior should remain; do not silently hardcode or ship the key in the APK.
