class WindowsBuildOutputLayout:
    def layout(self):
        return {
            "ready": True,
            "root": "dist/windows",
            "folders": ["portable", "installer", "logs", "reports", "artifacts"],
            "requires_artifact_registry_entry": True,
            "requires_integrity_hash": True,
            "requires_changelog": True,
        }

windows_build_output_layout = WindowsBuildOutputLayout()
