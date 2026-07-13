from app.v410_market_structure_sprint2.models import MarketStructureSprint2RequestV410
from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410

def test_v410_analyze():
    data=MarketStructureSprint2ServiceV410().analyze(MarketStructureSprint2RequestV410(timeframes=['1m','5m'],limit=100)); assert data['ready'] is True; assert 'multi_timeframe_structure' in data; assert data['real_order_execution_enabled'] is False
