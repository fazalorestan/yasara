class WindowsBuildLogContract:
    def log(self):
        return {"ready": True, "log_file": "dist/windows/reports/build_2026.50.B.001.log", "captures_stdout": True, "captures_stderr": True, "captures_return_code": True, "captures_duration": True, "write_enabled": False}
windows_build_log_contract = WindowsBuildLogContract()
