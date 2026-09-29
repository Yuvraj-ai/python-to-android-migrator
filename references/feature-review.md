# Feature Review Protocol

After analysis, do not implement yet. Present a concise inventory grouped by feature area.

For each meaningful feature show:

- name
- observed current behavior
- source files
- proposed Android representation
- backend requirement
- proposed action
- uncertainty, if any

Ask the user to choose among:

- preserve
- modify
- remove
- add
- move
- replace

Allow natural language. Translate it into `decisions.yaml`, show the resulting changes, and ask for confirmation when the decisions materially alter scope or architecture.

Also ask about high-impact Android additions only when relevant:

- notifications
- background processing
- offline/cache behavior
- share-to-app
- camera/gallery/document picker
- authentication
- local data storage
- deep links
- widgets

Do not ask dozens of trivial implementation questions. The agent can decide ordinary Kotlin/Compose details. Ask only for product behavior, data ownership, security/trust-boundary, navigation, or architecture decisions that materially affect the result.
