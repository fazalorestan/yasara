# Apply Sprint 48 Enterprise Release Manager v2

1. Extract the ZIP into the YaSara repository root and allow replacement of the Sprint 48 Release Manager files.
2. Do not replace or edit `yasara.py`.
3. Run diagnostics:

```bash
python scripts/yasara_release.py --diagnostics
```

4. Run the Sprint 48 tests:

```bash
pytest backend/tests/test_sprint48_release_manager.py -q
```

5. Execute the normal project command:

```bash
python yasara.py release
```

Optional direct commands:

```bash
python scripts/yasara_release.py --no-push
python scripts/yasara_release.py --skip-exe --no-push
python scripts/yasara_release.py --timeout 7200
```

The default timeout is 3600 seconds per step and can also be configured with `YASARA_RELEASE_TIMEOUT_SECONDS`.
Tool overrides are supported through `YASARA_GIT_PATH`, `YASARA_NODE_PATH`, and `YASARA_NPM_PATH`.
