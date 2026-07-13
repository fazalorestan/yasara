from app.platform_core.indicators.lifecycle.audit import indicator_lifecycle_audit_publisher
from app.platform_core.indicators.lifecycle.manager import indicator_lifecycle_state_manager
from app.platform_core.indicators.lifecycle.rollback import indicator_lifecycle_rollback_contract
from app.platform_core.indicators.lifecycle.rules import indicator_lifecycle_rules
from app.v500_alpha4_indicator_lifecycle.models import IndicatorLifecycleSummaryV500Alpha4

class IndicatorLifecycleFacadeV500Alpha4:
    def summary(self):
        return IndicatorLifecycleSummaryV500Alpha4()

    def states(self):
        return {"ready": True, "states": indicator_lifecycle_state_manager.seed_defaults()}

    def transition(self, indicator: str = "future_indicator_template", to_state: str = "validated"):
        result = indicator_lifecycle_state_manager.transition(indicator, to_state)
        if result["allowed"]:
            indicator_lifecycle_audit_publisher.publish(indicator, "transition", to_state)
        return {"ready": result["allowed"], "transition": result, "execution_allowed": False}

    def rules(self):
        return {"ready": True, "allowed": indicator_lifecycle_rules.allowed}

    def rollback_plan(self, indicator: str = "yasara"):
        return indicator_lifecycle_rollback_contract.rollback_plan(indicator)

    def audit_sample(self):
        return indicator_lifecycle_audit_publisher.publish("yasara", "snapshot", "enabled")

    def contract(self):
        return {
            "ready": True,
            "states": ["discovered", "validated", "installed", "enabled", "disabled", "uninstalled"],
            "execution_allowed": False,
            "mode": "lifecycle_contract_only",
        }
