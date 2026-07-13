from app.platform_core.portfolio_manager.allocation import PortfolioAllocationService

def test_v500_alpha26_allocation():
    r=PortfolioAllocationService().allocation([{'symbol':'A','quantity':1,'last_price':50},{'symbol':'B','quantity':1,'last_price':50}]); assert r['items'][0]['weight_pct']==50
