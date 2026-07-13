from app.platform_core.scanner.filters import ScannerFilterPipeline

def test_v500_alpha27_filter_reject_score():
    r=ScannerFilterPipeline().apply([{'symbol':'A','score':40,'risk_pct':1}], {'min_score':60,'max_risk_pct':2}); assert r['rejected'][0]['reject_reasons'][0]=='below_min_score'
