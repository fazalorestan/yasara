def max_drawdown(equity_curve):
    if not equity_curve:
        return 0
    peak = equity_curve[0]
    max_dd = 0
    for v in equity_curve:
        peak = max(peak, v)
        dd = (peak - v) / peak * 100 if peak else 0
        max_dd = max(max_dd, dd)
    return round(max_dd, 4)


def profit_factor(trades):
    gross_profit = sum(t["pnl"] for t in trades if t["pnl"] > 0)
    gross_loss = abs(sum(t["pnl"] for t in trades if t["pnl"] < 0))
    if gross_loss == 0:
        return round(gross_profit, 4) if gross_profit else 0
    return round(gross_profit / gross_loss, 4)


def win_rate(trades):
    if not trades:
        return 0
    wins = sum(1 for t in trades if t["pnl"] > 0)
    return round(wins / len(trades) * 100, 4)


def expectancy(trades):
    if not trades:
        return 0
    return round(sum(t["pnl"] for t in trades) / len(trades), 6)


def sharpe_proxy(trades):
    if len(trades) < 2:
        return 0
    values = [t["pnl_percent"] for t in trades]
    mean = sum(values) / len(values)
    var = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    std = var ** 0.5
    return round(mean / std, 4) if std else 0


def stats(trades, equity_curve, initial_equity, final_equity):
    return {
        "trades": len(trades),
        "win_rate": win_rate(trades),
        "profit_factor": profit_factor(trades),
        "expectancy": expectancy(trades),
        "max_drawdown_percent": max_drawdown(equity_curve),
        "sharpe_proxy": sharpe_proxy(trades),
        "net_profit": round(final_equity - initial_equity, 6),
        "net_profit_percent": round((final_equity - initial_equity) / initial_equity * 100, 4) if initial_equity else 0,
    }
