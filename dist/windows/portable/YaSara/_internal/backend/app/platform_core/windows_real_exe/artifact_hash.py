class WindowsExeArtifactHashContract:
    def hash_contract(self):
        return {
            "ready": True,
            "algorithm": "sha256",
            "artifact": "dist/windows/portable/YaSara/YaSara.exe",
            "hash_required": True,
            "hash_generated": False,
            "reason": "artifact_pending_real_build",
        }
windows_exe_artifact_hash_contract = WindowsExeArtifactHashContract()
