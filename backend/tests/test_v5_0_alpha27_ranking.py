from app.platform_core.scanner.ranking import ScannerRankingService

def test_v500_alpha27_ranking():
    r=ScannerRankingService().rank([{'symbol':'A','score':70,'risk_pct':1},{'symbol':'B','score':90,'risk_pct':1}]); assert r['items'][0]['symbol']=='B'
