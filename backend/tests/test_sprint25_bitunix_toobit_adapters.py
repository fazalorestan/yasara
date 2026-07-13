import pytest
from app.multi_exchange_v1.adapters.bitunix import BitunixAdapterV1
from app.multi_exchange_v1.application.service import MultiExchangeServiceV1
from app.multi_exchange_v1.domain.models import SupportedExchange, UnifiedPrivateOrderRequest
from tests.helpers.fake_exchange_client import FakeExchangePublicClient

@pytest.mark.asyncio
async def test_bitunix_ticker_scaffold_offline():
    fake = FakeExchangePublicClient()
    result = await BitunixAdapterV1(client=fake).ticker("BTC/USDT")
    assert result.exchange == "bitunix"
    assert result.symbol == "BTC/USDT"
    assert result.price == 100
    assert fake.calls[0][1]["symbol"] == "BTCUSDT"

@pytest.mark.asyncio
async def test_toobit_dry_run_order():
    request = UnifiedPrivateOrderRequest(exchange=SupportedExchange.TOOBIT, symbol="BTC/USDT", side="BUY", quantity=0.01)
    result = await MultiExchangeServiceV1().dry_run_order(request)
    assert result.accepted is True
    assert result.exchange_order_id.startswith("toobit_dryrun_")

@pytest.mark.asyncio
async def test_bitunix_live_order_rejected():
    request = UnifiedPrivateOrderRequest(exchange=SupportedExchange.BITUNIX, symbol="BTC/USDT", side="BUY", quantity=0.01, dry_run=False)
    result = await MultiExchangeServiceV1().dry_run_order(request)
    assert result.accepted is False
    assert "disabled" in result.message.lower()
