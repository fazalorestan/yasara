from app.platform_core.portfolio_manager.pnl import PortfolioPnLService

def test_v500_alpha26_pnl_summary():
    r=PortfolioPnLService().summary([{'quantity':1,'average_price':10,'last_price':12}], 1); assert r['total_pnl']==3
