class DeprecationPolicy:
    def __init__(self):
        self.policy = {
            "mode": "report_only",
            "remove_without_notice": False,
            "minimum_deprecation_window": "one_major_version",
            "allowed_states": [
                "active",
                "deprecated",
                "supported_legacy",
                "migration_available",
                "disabled_in_major_version",
            ],
        }

    def report(self):
        return {
            "ready": True,
            "policy": self.policy,
        }

deprecation_policy = DeprecationPolicy()
