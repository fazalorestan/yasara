import pytest
from app.strategy_builder_v1.application.service import StrategyBuilderServiceV1
from app.strategy_builder_v1.domain.models import StrategyEvaluationContext
from app.strategy_builder_v1.samples import build_sample_rsi_strategy

@pytest.mark.asyncio
async def test_strategy_service_create_and_evaluate():
    service = StrategyBuilderServiceV1()
    strategy = build_sample_rsi_strategy()
    created = await service.create(strategy)
    assert created["created"] is True
    result = await service.evaluate(strategy.strategy_id, StrategyEvaluationContext(symbol="BTC/USDT", indicators={"rsi": 55}))
    assert result.entry_passed is True
