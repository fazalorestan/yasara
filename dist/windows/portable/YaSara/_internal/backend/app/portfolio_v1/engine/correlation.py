import math
from app.portfolio_v1.domain.models import CorrelationMatrix, CorrelationPair, PortfolioSnapshot

class CorrelationEngineV1:
    def calculate(self, snapshot: PortfolioSnapshot, price_returns: dict[str, list[float]] | None = None) -> CorrelationMatrix:
        symbols = sorted({p.symbol for p in snapshot.positions})
        returns = price_returns or self._default_returns(symbols)
        pairs: list[CorrelationPair] = []
        for i, a in enumerate(symbols):
            for b in symbols[i + 1:]:
                corr = self._pearson(returns.get(a, []), returns.get(b, []))
                pairs.append(CorrelationPair(symbol_a=a, symbol_b=b, correlation=corr))
        avg = sum(abs(p.correlation) for p in pairs) / len(pairs) if pairs else 0
        high = sum(1 for p in pairs if abs(p.correlation) >= 0.75)
        return CorrelationMatrix(pairs=pairs, average_abs_correlation=avg, high_correlation_count=high)

    def _default_returns(self, symbols: list[str]) -> dict[str, list[float]]:
        return {symbol: [0.01, -0.005, 0.004, 0.002, -0.003] for symbol in symbols}

    def _pearson(self, a: list[float], b: list[float]) -> float:
        n = min(len(a), len(b))
        if n < 2: return 0.0
        x, y = a[-n:], b[-n:]
        mx, my = sum(x)/n, sum(y)/n
        numerator = sum((xi-mx)*(yi-my) for xi, yi in zip(x,y))
        dx = math.sqrt(sum((xi-mx)**2 for xi in x))
        dy = math.sqrt(sum((yi-my)**2 for yi in y))
        if dx == 0 or dy == 0: return 1.0 if x == y else 0.0
        return max(-1.0, min(1.0, numerator/(dx*dy)))
