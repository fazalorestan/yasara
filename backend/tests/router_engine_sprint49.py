from __future__ import annotations

from collections.abc import Iterable

from pydantic import BaseModel, Field

from app.multi_exchange_v1.domain.models import (
    ExchangeAdapterStatus,
    ExchangeCapability,
    SupportedExchange,
)
from app.multi_exchange_v1.registry import exchange_registry_v1
from app.multi_exchange_v1.symbol_registry import symbol_registry_v1


class ExchangeRouteDecisionV1(BaseModel):
    selected_exchange: SupportedExchange
    symbol: str
    reason: str
    available_exchanges: list[SupportedExchange]
    requested_exchange: SupportedExchange | None = None
    fallback_used: bool = False
    routing_mode: str = "market_data"
    rejected_exchanges: dict[str, list[str]] = Field(default_factory=dict)


class ExchangeRouterEngineV1:
    def available_for_symbol(self, symbol: str) -> list[SupportedExchange]:
        exchanges: list[SupportedExchange] = []
        for descriptor in exchange_registry_v1.descriptors():
            item = symbol_registry_v1.get(descriptor.exchange, symbol)
            if item is not None and item.enabled:
                exchanges.append(descriptor.exchange)
        return exchanges

    def choose(
        self,
        symbol: str,
        preferred: SupportedExchange | None = None,
    ) -> ExchangeRouteDecisionV1:
        available = self.available_for_symbol(symbol)
        if not available:
            available = [d.exchange for d in exchange_registry_v1.descriptors()]

        if preferred and preferred in available:
            return ExchangeRouteDecisionV1(
                selected_exchange=preferred,
                symbol=symbol,
                reason="preferred_exchange_available",
                available_exchanges=available,
                requested_exchange=preferred,
            )

        selected = available[0]
        return ExchangeRouteDecisionV1(
            selected_exchange=selected,
            symbol=symbol,
            reason=(
                "preferred_exchange_unavailable_fallback"
                if preferred is not None
                else "default_first_available"
            ),
            available_exchanges=available,
            requested_exchange=preferred,
            fallback_used=preferred is not None and selected != preferred,
        )

    def choose_for_order(
        self,
        symbol: str,
        preferred: SupportedExchange | None = None,
        *,
        dry_run: bool = True,
        priority: Iterable[SupportedExchange] | None = None,
    ) -> ExchangeRouteDecisionV1:
        descriptors = {
            descriptor.exchange: descriptor
            for descriptor in exchange_registry_v1.descriptors()
        }

        ordered: list[SupportedExchange] = []
        if preferred is not None:
            ordered.append(preferred)
        for exchange in priority or descriptors.keys():
            if exchange not in ordered:
                ordered.append(exchange)

        required_capability = (
            ExchangeCapability.DRY_RUN_PRIVATE
            if dry_run
            else ExchangeCapability.LIVE_TRADING
        )

        eligible: list[SupportedExchange] = []
        rejected: dict[str, list[str]] = {}

        for exchange in ordered:
            reasons: list[str] = []
            descriptor = descriptors.get(exchange)
            symbol_info = symbol_registry_v1.get(exchange, symbol)

            if descriptor is None:
                reasons.append("adapter_not_registered")
            else:
                if descriptor.status == ExchangeAdapterStatus.DISABLED:
                    reasons.append("adapter_disabled")
                if required_capability not in descriptor.capabilities:
                    reasons.append(f"missing_capability:{required_capability.value}")
                if not dry_run and not descriptor.live_trading_enabled:
                    reasons.append("live_trading_disabled")

            if symbol_info is None:
                reasons.append("symbol_not_available")
            elif not symbol_info.enabled:
                reasons.append("symbol_disabled")

            if reasons:
                rejected[exchange.value] = reasons
                continue

            eligible.append(exchange)

        if not eligible:
            mode = "dry_run" if dry_run else "live"
            raise ValueError(
                f"No eligible exchange found for {symbol} in {mode} mode."
            )

        selected = eligible[0]
        fallback_used = preferred is not None and selected != preferred
        if preferred is None:
            reason = "first_eligible_exchange"
        elif fallback_used:
            reason = "preferred_exchange_ineligible_fallback"
        else:
            reason = "preferred_exchange_eligible"

        return ExchangeRouteDecisionV1(
            selected_exchange=selected,
            symbol=symbol,
            reason=reason,
            available_exchanges=eligible,
            requested_exchange=preferred,
            fallback_used=fallback_used,
            routing_mode="dry_run_order" if dry_run else "live_order",
            rejected_exchanges=rejected,
        )
