from app.platform_core.portfolio_manager.models import PortfolioHolding

def test_v500_alpha26_models_holding():
    h=PortfolioHolding('BTCUSDT',1,100,110); assert h.symbol=='BTCUSDT'
