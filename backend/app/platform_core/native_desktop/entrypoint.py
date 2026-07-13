class NativeDesktopEntrypoint:
    def specification(self):
        return {
            "ready": True,
            "module": "yasara_desktop",
            "callable": "main",
            "build_id": "2026.49.A.001",
            "platform": "windows-x64",
            "launch_backend": True,
            "launch_main_window": True,
            "final_exe_generated": False,
        }

native_desktop_entrypoint = NativeDesktopEntrypoint()
