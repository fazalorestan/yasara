from app.platform_core.release_registry.artifact_store import artifact_store_contract
from app.platform_core.release_registry.artifact_integrity import artifact_integrity_contract

class ArtifactSignalProvider:
    def signal(self):
        store = artifact_store_contract.store()
        integrity = artifact_integrity_contract.integrity()
        return {
            "ready": True,
            "artifact_count": store["artifact_count"],
            "integrity_required": store["integrity_required"],
            "tamper_detected": integrity["tamper_detected"],
            "artifact_consistency_required": integrity["artifact_consistency_required"],
            "signal": "green" if integrity["tamper_detected"] is False else "red",
            "hardcoded_dashboard": False,
        }

artifact_signal_provider = ArtifactSignalProvider()
