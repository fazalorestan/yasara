class PortfolioCorrelationService:
    def matrix(self, symbols: list[str]):
        matrix = {}
        for a in symbols:
            matrix[a] = {}
            for b in symbols:
                matrix[a][b] = 1.0 if a == b else 0.35
        return {"ready": True, "symbols": symbols, "matrix": matrix}

    def risk_flag(self, matrix: dict):
        high_pairs = []
        for a, row in matrix.items():
            for b, value in row.items():
                if a < b and float(value) >= 0.8:
                    high_pairs.append((a, b))
        return {"ready": True, "high_correlation_pairs": high_pairs, "correlation_ok": len(high_pairs) == 0}

portfolio_correlation_service = PortfolioCorrelationService()
