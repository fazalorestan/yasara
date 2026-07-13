from app.platform_core.licensing.entitlements import entitlement_engine

class FeatureLockStateBuilder:
    def build(self, payload: dict, features: list[str]):
        return {
            "ready": True,
            "items": [
                {
                    "feature": feature,
                    "locked": not entitlement_engine.can_access(payload, feature)["enabled"],
                    "reason": entitlement_engine.can_access(payload, feature)["reason"],
                }
                for feature in features
            ],
            "execution_allowed": False,
        }

feature_lock_state_builder = FeatureLockStateBuilder()
