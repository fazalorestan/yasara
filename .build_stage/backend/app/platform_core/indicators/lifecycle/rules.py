class IndicatorLifecycleRules:
    allowed = {
        "discovered": ["validated", "disabled"],
        "validated": ["installed", "disabled"],
        "installed": ["enabled", "disabled", "uninstalled"],
        "enabled": ["disabled"],
        "disabled": ["enabled", "uninstalled"],
        "uninstalled": ["discovered"],
    }

    def can_transition(self, from_state: str, to_state: str):
        return to_state in self.allowed.get(from_state, [])

indicator_lifecycle_rules = IndicatorLifecycleRules()
