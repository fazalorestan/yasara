from __future__ import annotations

import pytest

from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.router_engine import ExchangeRouterEngineV1
from app.multi_exchange_v1.symbol_registry import symbol_registry_v1


def test_sprint49_preserves_existing_preferred_route_contract():
    decision = ExchangeRouterEngineV1().choose(
        "BTC/USDT",
        SupportedExchange.TOOBIT,
    )
    assert decision.selected_exchange == SupportedExchange.TOOBIT
    assert decision.reason == "preferred_exchange_available"
    assert decision.fallback_used is False


def test_sprint49_dry_run_order_uses_preferred_when_eligible():
    decision = ExchangeRouterEngineV1().choose_for_order(
        "BTC/USDT",
        SupportedExchange.BITUNIX,
        dry_run=True,
    )
    assert decision.selected_exchange == SupportedExchange.BITUNIX
    assert decision.reason == "preferred_exchange_eligible"
    assert decision.routing_mode == "dry_run_order"


def test_sprint49_falls_back_when_preferred_exchange_lacks_manual_symbol():
    symbol = "S49TEST/USDT"
    symbol_registry_v1.register(SupportedExchange.TOOBIT, symbol)

    decision = ExchangeRouterEngineV1().choose_for_order(
        symbol,
        SupportedExchange.BITUNIX,
        dry_run=True,
        priority=[SupportedExchange.BITUNIX, SupportedExchange.TOOBIT],
    )

    assert decision.selected_exchange == SupportedExchange.TOOBIT
    assert decision.fallback_used is True
    assert decision.reason == "preferred_exchange_ineligible_fallback"
    assert "symbol_not_available" in decision.rejected_exchanges["bitunix"]


def test_sprint49_live_route_is_blocked_until_adapter_enables_live_trading():
    with pytest.raises(ValueError, match="No eligible exchange"):
        ExchangeRouterEngineV1().choose_for_order(
            "BTC/USDT",
            SupportedExchange.BITUNIX,
            dry_run=False,
        )
