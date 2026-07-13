class DuplicateDetectorService:
    def scan(self):
        return {
            "ready": True,
            "scope": "duplicate_detector",
            "mode": "contract_only",
            "duplicate_groups_detected": 0,
            "safe_to_refactor": True,
            "destructive_changes_allowed": False,
            "adds_new_feature": False,
        }

duplicate_detector_service = DuplicateDetectorService()
