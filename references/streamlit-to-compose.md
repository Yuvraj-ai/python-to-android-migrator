# Streamlit to Android Guidance

Analyze semantics rather than performing textual translation.

| Streamlit | Typical Android equivalent |
|---|---|
| `st.text_input` | Compose `TextField` / `OutlinedTextField` |
| `st.text_area` | multiline Compose text field |
| `st.button` | `Button` / `FilledTonalButton` |
| `st.checkbox` | `Checkbox` / switch |
| `st.selectbox` | dropdown / exposed menu |
| `st.multiselect` | multi-select dialog/chips |
| `st.radio` | radio group / segmented control |
| `st.slider` | `Slider` |
| `st.file_uploader` | Android document picker / photo picker / camera |
| `st.dataframe` | `LazyColumn`, cards, or a purpose-built table |
| `st.tabs` | `TabRow` / navigation |
| `st.sidebar` | navigation drawer, bottom navigation, or settings depending on purpose |
| `st.chat_input` + `st.chat_message` | Compose chat screen |
| `st.session_state` | ViewModel + `StateFlow`/`SavedStateHandle` |
| `st.spinner` | loading state / progress indicator |
| `st.success` / `st.error` | snackbar, banner, inline error state |
| `st.download_button` | Android document creation/share/save flow |

Do not preserve a web layout when a native interaction is materially better. Ask the user before changing meaningful navigation or behavior.

For every screen, identify: inputs, outputs, actions, state, loading, error, empty state, navigation, permissions, and backend operations.
