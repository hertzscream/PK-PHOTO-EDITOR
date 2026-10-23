# PK PHOTO EDITOR 0.5.1 — editor validation

2026-10-23 Asia/Bangkok. versionCode10, minSdk34, target36. Same application ID and debug certificate. No database, recipe, LUT or source image changes.

- assembleDebug / assembleDebugAndroidTest / testDebugUnitTest / lintDebug: PASS.
- JVM: 25 tests, 0 failures.
- Android14 API34: 27 tests, 0 failures, 0 skipped; 80.145s.
- Android16 API36: 27 tests, 0 failures, 0 skipped; 84.441s.
- Lint: 0 errors, 20 existing warnings.

WorkflowTest now verifies full-width preview and more than65% of available editor height with tools closed; left/right swipes switch photos; tapping enters/exits full-screen; preview grows while dock disappears; pinch and subsequent pan retain active photo; Fit resets zoom to1; swiping works again; preset selection, per-photo undo/redo, manual sliders, tool closure and return to library work. Tool panels keep the image visible, strength and filmstrip use shorter panels, all dock icons have labels and content descriptions. Tone selection, scope application and preview workflow tests explicitly open the new tool panels.

An import snackbar originally intercepted bottom controls. Editor messages now appear at the top, and the final tests pass with import notifications present. Tests wait for Compose to apply panel closure before dispatching Back. No test disables the snackbar or bypasses tool clicks.

Updater integration uses owned code11 fixtures with matching and deliberately different signers; both tests pass without skips. Other project/trash/migration/export/color/preview tests remain unchanged and pass. No user photos enter tests, screenshots, website or source package. Screenshots use the existing synthetic illustration. Evidence: dist/validation/0.5.1/.

Emulator touch validation does not replace physical-device, TalkBack, rotation and foldable QA. APK remains a debug-signed testing build. Previous release validation retained in TEST_REPORT_0.5.0.md.
