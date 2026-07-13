class RefactorGuardService:
    def policy(self):
        return {
            "ready": True,
            "api_breaking_changes_allowed": False,
            "import_breaking_changes_allowed": False,
            "router_breaking_changes_allowed": False,
            "backward_compatibility_required": True,
            "alias_required_for_renames": True,
            "adds_new_feature": False,
        }

refactor_guard_service = RefactorGuardService()
