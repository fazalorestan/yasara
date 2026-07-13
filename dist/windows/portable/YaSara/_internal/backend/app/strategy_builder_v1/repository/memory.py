from datetime import datetime, timezone
from app.strategy_builder_v1.domain.models import StrategyDefinition, StrategyStatus

class InMemoryStrategyRepositoryV1:
    def __init__(self):
        self._items: dict[str, StrategyDefinition] = {}

    def save(self, strategy: StrategyDefinition) -> StrategyDefinition:
        strategy.updated_at = datetime.now(timezone.utc)
        self._items[strategy.strategy_id] = strategy
        return strategy

    def get(self, strategy_id: str) -> StrategyDefinition | None:
        return self._items.get(strategy_id)

    def list(self, include_archived: bool = False) -> list[StrategyDefinition]:
        items = list(self._items.values())
        if not include_archived:
            items = [s for s in items if s.status != StrategyStatus.ARCHIVED]
        return items

    def archive(self, strategy_id: str) -> StrategyDefinition | None:
        strategy = self.get(strategy_id)
        if strategy:
            strategy.status = StrategyStatus.ARCHIVED
            strategy.updated_at = datetime.now(timezone.utc)
        return strategy
