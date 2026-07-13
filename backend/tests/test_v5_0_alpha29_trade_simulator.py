from app.platform_core.backtest_engine.trade_simulator import TradeSimulationEngine

def test_v500_alpha29_trade_simulator():
    r=TradeSimulationEngine().simulate('BTCUSDT',[{'side':'buy','price':100},{'side':'sell','price':110}],1); assert r['trades'][0]['pnl'] == 10
