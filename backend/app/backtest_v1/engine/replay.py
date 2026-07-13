import uuid
from app.backtest_v1.domain.models import BacktestConfig, BacktestTrade, CostModel, EquityPoint, ExitReason, TradeStatus
from app.backtest_v1.engine.costs import CostEngineV1
from app.decision_v1.domain.models import DecisionDirection
from app.market_data.domain.models import Candle

class CandleReplayEngineV1:
    def __init__(self):
        self.costs = CostEngineV1()

    def run_simple_breakout(self, config: BacktestConfig, candles: list[Candle]) -> tuple[list[BacktestTrade], list[EquityPoint]]:
        equity = config.initial_capital
        peak = equity
        trades: list[BacktestTrade] = []
        equity_curve: list[EquityPoint] = []
        open_trade: BacktestTrade | None = None

        for i in range(20, len(candles)):
            candle = candles[i]
            previous = candles[i-20:i]
            high = max(c.high for c in previous)
            low = min(c.low for c in previous)

            if open_trade:
                closed = self._maybe_close(open_trade, candle, config)
                if closed:
                    equity += open_trade.net_pnl
                    open_trade = None

            if open_trade is None and len([t for t in trades if t.status == TradeStatus.OPEN]) < config.max_open_trades:
                if candle.close > high:
                    open_trade = self._open_trade(config, candle, DecisionDirection.LONG)
                    trades.append(open_trade)
                elif candle.close < low:
                    open_trade = self._open_trade(config, candle, DecisionDirection.SHORT)
                    trades.append(open_trade)

            peak = max(peak, equity)
            dd = (peak - equity) / peak * 100 if peak else 0
            equity_curve.append(EquityPoint(time=candle.close_time, equity=equity, drawdown_pct=dd))

        if open_trade:
            last = candles[-1]
            self._close_trade(open_trade, last.close_time, last.close, ExitReason.END_OF_TEST, config)
            equity += open_trade.net_pnl
            peak = max(peak, equity)
            dd = (peak - equity) / peak * 100 if peak else 0
            equity_curve.append(EquityPoint(time=last.close_time, equity=equity, drawdown_pct=dd))

        return trades, equity_curve

    def _open_trade(self, config: BacktestConfig, candle: Candle, direction: DecisionDirection) -> BacktestTrade:
        entry = candle.close * (1 + config.cost_model.slippage_rate if direction == DecisionDirection.LONG else 1 - config.cost_model.slippage_rate)
        risk_amount = config.initial_capital * config.risk_per_trade_pct / 100
        stop_distance = candle.close * 0.01
        quantity = risk_amount / stop_distance if stop_distance else 0
        if direction == DecisionDirection.LONG:
            sl = entry - stop_distance
            tp = entry + stop_distance * 2
        else:
            sl = entry + stop_distance
            tp = entry - stop_distance * 2
        return BacktestTrade(
            id=uuid.uuid4().hex,
            symbol=config.symbol,
            direction=direction,
            entry_time=candle.close_time,
            entry_price=entry,
            quantity=quantity,
            stop_loss=sl,
            take_profit=tp,
            fees=self.costs.commission(entry * quantity, config.cost_model),
            slippage=self.costs.slippage(entry * quantity, config.cost_model),
        )

    def _maybe_close(self, trade: BacktestTrade, candle: Candle, config: BacktestConfig) -> bool:
        if trade.direction == DecisionDirection.LONG:
            if candle.low <= trade.stop_loss:
                self._close_trade(trade, candle.close_time, trade.stop_loss, ExitReason.STOP_LOSS, config)
                return True
            if candle.high >= trade.take_profit:
                self._close_trade(trade, candle.close_time, trade.take_profit, ExitReason.TAKE_PROFIT, config)
                return True
        else:
            if candle.high >= trade.stop_loss:
                self._close_trade(trade, candle.close_time, trade.stop_loss, ExitReason.STOP_LOSS, config)
                return True
            if candle.low <= trade.take_profit:
                self._close_trade(trade, candle.close_time, trade.take_profit, ExitReason.TAKE_PROFIT, config)
                return True
        return False

    def _close_trade(self, trade: BacktestTrade, exit_time, exit_price: float, reason: ExitReason, config: BacktestConfig) -> None:
        trade.exit_time = exit_time
        trade.exit_price = exit_price
        trade.status = TradeStatus.CLOSED
        trade.exit_reason = reason
        if trade.direction == DecisionDirection.LONG:
            trade.gross_pnl = (exit_price - trade.entry_price) * trade.quantity
        else:
            trade.gross_pnl = (trade.entry_price - exit_price) * trade.quantity
        exit_notional = abs(exit_price * trade.quantity)
        trade.fees += self.costs.commission(exit_notional, config.cost_model)
        trade.slippage += self.costs.slippage(exit_notional, config.cost_model)
        trade.funding = self.costs.funding(exit_notional, trade.entry_time, exit_time, config.cost_model)
        trade.net_pnl = trade.gross_pnl - trade.fees - trade.slippage - trade.funding
        trade.return_pct = trade.net_pnl / config.initial_capital * 100 if config.initial_capital else 0
