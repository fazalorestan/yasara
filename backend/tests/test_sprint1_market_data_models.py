from app.market_data.infrastructure.utils import compact_symbol, slash_symbol, to_float, to_int

def test_symbol_helpers():
    assert compact_symbol("BTC/USDT") == "BTCUSDT"
    assert slash_symbol("BTCUSDT") == "BTC/USDT"

def test_number_helpers():
    assert to_float("1.25") == 1.25
    assert to_float(None) == 0
    assert to_int("10") == 10
