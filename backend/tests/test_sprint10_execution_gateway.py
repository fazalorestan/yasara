import pytest
from app.decision_v1.domain.models import DecisionDirection
from app.execution_v1.domain.models import ExecutionIntent, ExecutionIntentStatus, ExecutionMode, ExecutionSide
from app.execution_v1.engine.execution_gateway import ExecutionGatewayV1

@pytest.mark.asyncio
async def test_execution_gateway_dry_run_executes():
    gateway = ExecutionGatewayV1()
    intent = ExecutionIntent(symbol="BTC/USDT", direction=DecisionDirection.LONG, side=ExecutionSide.BUY, quantity=0.01, price=60000, mode=ExecutionMode.DRY_RUN)
    result = await gateway.execute(intent)
    assert result.status == ExecutionIntentStatus.EXECUTED
    assert result.exchange_order_id.startswith("dryrun_")
    assert len(gateway.audit.list_entries()) == 2

@pytest.mark.asyncio
async def test_execution_gateway_live_disabled_rejected():
    gateway = ExecutionGatewayV1()
    intent = ExecutionIntent(symbol="BTC/USDT", direction=DecisionDirection.LONG, side=ExecutionSide.BUY, quantity=0.01, mode=ExecutionMode.LIVE_DISABLED)
    result = await gateway.execute(intent)
    assert result.status == ExecutionIntentStatus.REJECTED
