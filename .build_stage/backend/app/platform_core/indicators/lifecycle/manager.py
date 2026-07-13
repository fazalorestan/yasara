from app.platform_core.indicators.lifecycle.models import IndicatorLifecycleState, IndicatorLifecycleTransition
from app.platform_core.indicators.lifecycle.rules import indicator_lifecycle_rules

class IndicatorLifecycleStateManager:
    def __init__(self):
        self._states = {}

    def seed_defaults(self):
        if "yasara" not in self._states:
            self._states["yasara"] = IndicatorLifecycleState(indicator="yasara", state="enabled", version="v1.0")
        return self.snapshot()

    def get(self, indicator: str):
        return self._states.get(indicator)

    def set_state(self, indicator: str, state: str, version: str = "v1.0"):
        self._states[indicator] = IndicatorLifecycleState(indicator=indicator, state=state, version=version)
        return self._states[indicator]

    def transition(self, indicator: str, to_state: str):
        current = self._states.get(indicator) or self.set_state(indicator, "discovered")
        allowed = indicator_lifecycle_rules.can_transition(current.state, to_state)
        transition = IndicatorLifecycleTransition(
            indicator=indicator,
            from_state=current.state,
            to_state=to_state,
            allowed=allowed,
            reason="allowed" if allowed else "transition_not_allowed",
        )
        if allowed:
            self.set_state(indicator, to_state, current.version)
        return transition.__dict__

    def snapshot(self):
        return {k: v.__dict__ for k, v in self._states.items()}

indicator_lifecycle_state_manager = IndicatorLifecycleStateManager()
