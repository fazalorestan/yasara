from app.market_tools_v1.batch_analysis import BatchMarketAnalyzerV1, BatchSymbolAnalysisInputV1

def test_batch_market_analyzer():
    result = BatchMarketAnalyzerV1().analyze([BatchSymbolAnalysisInputV1(symbol="BTC/USDT", closes=[100, 103])])
    assert result[0].symbol == "BTC/USDT"
    assert result[0].regime == "trending_up"
