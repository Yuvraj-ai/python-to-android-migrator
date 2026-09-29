# Migration Specification

Create `.migration/` with these artifacts:

- `analysis.md`: observed repository structure, entry points, dependencies, workflows, uncertainties.
- `architecture.yaml`: current architecture and proposed target architecture.
- `features.yaml`: every discovered user-facing capability and its approved migration action.
- `screens.yaml`: target Android screens, navigation, states, and feature mappings.
- `api.yaml`: backend endpoints/contracts required by Android.
- `data-model.yaml`: persisted entities and transformations.
- `security.md`: secrets, permissions, trust boundaries, and remediation notes.
- `decisions.yaml`: user-approved product and architecture decisions.
- `implementation-plan.md`: ordered implementation work.
- `validation.yaml`: traceability and test status.

## Feature schema

```yaml
features:
  - id: stable_snake_case_id
    name: Human-readable name
    source:
      files: [path/to/file.py]
      technology: streamlit|python|other
    current_behavior: Observed behavior; mark uncertainty explicitly.
    migration:
      action: preserve|modify|remove|add|move|replace
      android:
        screen: screen_id
        implementation: native_compose|native_android|other
      backend:
        required: true|false
        operations: [operation_id]
      changes: []
    user_decision:
      status: pending|approved
      decision: free-form summary
```

## Screen schema

```yaml
screens:
  - id: screen_id
    name: Display name
    purpose: Why it exists
    components: []
    states: [idle, loading, success, error]
    navigation:
      enters_from: []
      exits_to: []
    features: []
```

## API schema

```yaml
endpoints:
  - id: operation_id
    method: POST
    path: /api/example
    purpose: What the operation does
    request: {}
    response: {}
    errors: []
    source_functions: []
```

## Decision actions

`preserve` = capability and behavior remain materially equivalent; UI may be redesigned.

`modify` = capability remains but behavior or scope changes.

`remove` = deliberately not migrated.

`add` = new capability not present in the source.

`move` = capability remains but its navigation/location/workflow changes.

`replace` = source mechanism is replaced by a different implementation while retaining the intended capability.
