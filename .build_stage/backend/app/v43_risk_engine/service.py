from app.v42_signal_engine.models import SignalRequestV42
from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42
from app.v43_risk_engine import calculations as calc
from app.v43_risk_engine.models import RiskEngineSummaryV43, RiskRequestV43


class AdvancedRiskEngineServiceV43:
    def __init__(self):
        self.signal_engine = MultiLayerSignalEngineServiceV42()

    def summary(self):
        return RiskEngineSummaryV43()

    def evaluate(self, request: RiskRequestV43):
        profile = request.profile
        state = request.state
        breaker = calc.circuit_breaker(profile, state)
        recovery = calc.recovery_mode(profile, state)

        effective_risk_percent = profile.risk_per_trade_percent * recovery["risk_multiplier"]
        size = calc.position_size(profile.equity, effective_risk_percent, request.entry_price, request.stop_loss_price)
        notional_value = calc.notional(size, request.entry_price)
        leverage = calc.leverage_required(notional_value, profile.equity)
        rr = calc.reward_risk(request.entry_price, request.stop_loss_price, request.take_profit_price)
        kelly = calc.kelly_fraction(request.win_rate, rr or request.reward_risk)

        leverage_ok = leverage <= profile.max_leverage
        portfolio_heat_ok = state.portfolio_heat_percent + effective_risk_percent <= profile.daily_risk_limit_percent
        allowed = (not breaker["active"]) and leverage_ok and portfolio_heat_ok and size > 0

        reasons = []
        if breaker["active"]:
            reasons.extend(breaker["reasons"])
        if not leverage_ok:
            reasons.append("leverage_limit_exceeded")
        if not portfolio_heat_ok:
            reasons.append("portfolio_heat_limit_exceeded")
        if size <= 0:
            reasons.append("invalid_position_size")

        risk_label = "low" if allowed and effective_risk_percent <= 1 else "medium" if allowed else "high"

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "position": {
                "size": size,
                "notional": notional_value,
                "leverage_required": leverage,
                "effective_risk_percent": round(effective_risk_percent, 4),
                "risk_amount": calc.risk_amount(profile.equity, effective_risk_percent),
            },
            "trade_math": {
                "entry": request.entry_price,
                "stop_loss": request.stop_loss_price,
                "take_profit": request.take_profit_price,
                "reward_risk": rr,
                "kelly_fraction": kelly,
            },
            "guards": {
                "allowed": allowed,
                "risk_label": risk_label,
                "circuit_breaker": breaker,
                "recovery_mode": recovery,
                "leverage_ok": leverage_ok,
                "portfolio_heat_ok": portfolio_heat_ok,
                "reasons": reasons if reasons else ["risk_gate_passed"],
            },
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def signal_risk(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        signal = self.signal_engine.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
        entry = 50000
        stop = 49000 if signal["signal"]["direction"] != "bearish" else 51000
        tp = 53000 if signal["signal"]["direction"] != "bearish" else 47000
        risk = self.evaluate(RiskRequestV43(symbol=symbol, exchange=exchange, entry_price=entry, stop_loss_price=stop, take_profit_price=tp))
        return {
            "ready": True,
            "signal": signal["signal"],
            "risk": risk,
            "execution_allowed": signal["signal"]["execution_allowed"] and risk["guards"]["allowed"],
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }
