class WindowsExeArtifactPlan:
    def plan(self):
        return {"ready": True, "artifact_name": "YaSara_Windows_Internal_2026.50.B.001.zip", "exe_path": "dist/windows/portable/YaSara/YaSara.exe", "hash_path": "dist/windows/artifacts/YaSara.exe.sha256", "manifest_path": "dist/windows/artifacts/manifest.json", "artifact_created": False, "hash_created": False}
windows_exe_artifact_plan = WindowsExeArtifactPlan()
