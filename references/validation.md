# Validation

Maintain a traceability matrix:

```text
Source feature -> approved action -> API/backend operation -> Android screen/code -> test -> status
```

Validate:

1. Python backend tests still pass after extraction/refactoring.
2. Android project compiles.
3. API request/response contracts match the Android client.
4. Every approved `preserve`, `modify`, `move`, and `replace` feature has an Android implementation.
5. Removed features are absent intentionally and documented.
6. Added features have explicit tests or acceptance checks.
7. Loading, empty, error, permission, and offline states are handled where relevant.
8. Secrets are not embedded in source, resources, APK configuration, or client code.
9. Critical workflows are exercised end-to-end.
10. Final report distinguishes equivalent behavior from intentional changes and unresolved limitations.

Never claim feature parity solely because the project builds. Parity requires workflow-level evidence.
