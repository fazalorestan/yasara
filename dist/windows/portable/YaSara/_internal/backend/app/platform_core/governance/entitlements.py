class EntitlementManager:
    def __init__(self):
        self._requirements = {}
    def require(self, feature, entitlements):
        self._requirements[feature] = entitlements
    def allowed(self, feature, user_entitlements):
        return all(x in user_entitlements for x in self._requirements.get(feature, []))
    def list_requirements(self):
        return self._requirements

entitlement_manager = EntitlementManager()
