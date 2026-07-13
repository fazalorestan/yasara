from app.desktop_ui_v1.chart_models import ChartSeriesBuilderV1

def test_chart_series_builder():
    series = ChartSeriesBuilderV1().from_ohlcv_rows("BTC/USDT", "1h", [{"open":1,"high":2,"low":0.5,"close":1.5,"volume":10}])
    assert series.symbol == "BTC/USDT"
    assert series.candles[0].close == 1.5
