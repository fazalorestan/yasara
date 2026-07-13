import uuid
from app.strategy_builder_v1.domain.models import StrategyDefinition, StrategyEvaluationContext
from app.strategy_builder_v1.engine.evaluator import StrategyEvaluatorV1
from app.strategy_builder_v1.engine.validator import StrategyValidatorV1
from app.strategy_builder_v1.repository.memory import InMemoryStrategyRepositoryV1

class StrategyBuilderServiceV1:
    def __init__(self):
        self.repository = InMemoryStrategyRepositoryV1()
        self.validator = StrategyValidatorV1()
        self.evaluator = StrategyEvaluatorV1()

    async def create(self, strategy: StrategyDefinition):
        if not strategy.strategy_id:
            strategy.strategy_id = uuid.uuid4().hex
        validation = self.validator.validate(strategy)
        if not validation.valid:
            return {"created": False, "validation": validation, "strategy": strategy}
        saved = self.repository.save(strategy)
        return {"created": True, "validation": validation, "strategy": saved}

    async def list(self):
        return self.repository.list()

    async def get(self, strategy_id: str):
        return self.repository.get(strategy_id)

    async def evaluate(self, strategy_id: str, context: StrategyEvaluationContext):
        strategy = self.repository.get(strategy_id)
        if strategy is None:
            return None
        return self.evaluator.evaluate(strategy, context)

    async def archive(self, strategy_id: str):
        return self.repository.archive(strategy_id)

strategy_builder_service_v1 = StrategyBuilderServiceV1()
