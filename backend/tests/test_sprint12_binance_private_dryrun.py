import pytest
from app.exchange_private_v1.application.service import PrivateExchangeServiceV1
from app.exchange_private_v1.domain.models import ExchangeCredentialRef, PrivateOrderRequest, PrivateOrderSide
from app.secrets_v1.application.service import secrets_vault_service_v1
from app.secrets_v1.domain.models import SecretCreateRequest, SecretScope

@pytest.mark.asyncio
async def test_binance_private_order_dryrun():
    await secrets_vault_service_v1.create_secret(SecretCreateRequest(scope=SecretScope.EXCHANGE, name="binance_key", value="abcd1234key"))
    await secrets_vault_service_v1.create_secret(SecretCreateRequest(scope=SecretScope.EXCHANGE, name="binance_secret", value="secret123"))
    request = PrivateOrderRequest(
        symbol="BTC/USDT",
        side=PrivateOrderSide.BUY,
        quantity=0.01,
        credential_ref=ExchangeCredentialRef(api_key_secret_name="binance_key", api_secret_secret_name="binance_secret"),
    )
    result = await PrivateExchangeServiceV1().place_order(request)
    assert result.accepted is True
    assert result.status == "accepted_dry_run"
    assert result.exchange_order_id.startswith("binance_dryrun_")
    assert result.signed_payload_preview["signature"] == "***redacted***"

@pytest.mark.asyncio
async def test_binance_private_order_live_disabled():
    request = PrivateOrderRequest(symbol="BTC/USDT", side=PrivateOrderSide.BUY, quantity=0.01, dry_run=False)
    result = await PrivateExchangeServiceV1().place_order(request)
    assert result.accepted is False
    assert "Live private exchange order placement is disabled" in result.message
