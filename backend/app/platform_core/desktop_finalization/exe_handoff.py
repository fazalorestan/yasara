class FirstRealExeHandoffContract:
    def contract(self):
        return {
            "ready": True,
            "handoff_to": "v5.0-alpha.50",
            "target": "first_real_windows_exe_build",
            "requires_pyinstaller_or_equivalent": True,
            "requires_portable_output": True,
            "requires_smoke_test_on_real_exe": True,
            "requires_artifact_hash": True,
            "final_exe_generated_now": False,
        }
first_real_exe_handoff_contract = FirstRealExeHandoffContract()
