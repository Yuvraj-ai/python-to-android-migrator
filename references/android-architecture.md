# Android Architecture

Default target unless the user specifies otherwise:

- Kotlin
- Jetpack Compose
- Material 3
- Navigation Compose
- ViewModel
- Coroutines
- StateFlow
- Hilt for dependency injection
- Retrofit/OkHttp or another typed HTTP client
- Kotlin serialization or another explicit JSON serialization mechanism
- Room when local structured persistence is required

Prefer a feature-oriented structure:

```text
app/
  core/
  data/
    remote/
    local/
    repository/
  domain/
  feature/
    home/
    settings/
    ...
```

Use unidirectional state flow where practical. Keep composables focused on rendering and user events; put orchestration in ViewModels/use cases/repositories.

Use Android-native capabilities for document picking, sharing, notifications, background work, permissions, and secure local storage when approved by the migration specification.
