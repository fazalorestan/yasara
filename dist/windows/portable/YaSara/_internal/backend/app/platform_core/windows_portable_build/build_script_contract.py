class WindowsPortableBuildScriptContract:
    def contract(self):
        return {"ready": True, "script": "scripts/build_windows_portable.py", "command": "python scripts/build_windows_portable.py --profile internal", "requires_tests_passed": True, "requires_smoke_test": True, "requires_artifact_registration": True, "does_not_enable_real_execution": True}
windows_portable_build_script_contract = WindowsPortableBuildScriptContract()
