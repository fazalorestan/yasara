class WindowsRealExeBuildScriptContract:
    def contract(self):
        return {
            "ready": True,
            "script": "scripts/build_windows_exe.py",
            "command": "python scripts/build_windows_exe.py --profile internal",
            "requires_tests_passed": True,
            "requires_clean_dist": True,
            "requires_pyinstaller": True,
            "requires_artifact_hash": True,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }
windows_real_exe_build_script_contract = WindowsRealExeBuildScriptContract()
