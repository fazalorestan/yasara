from app.platform_core.scanner.filters import ScannerFilterPipeline

def test_v500_alpha27_filter_accept():
    r=ScannerFilterPipeline().apply([{'symbol':'A','score':80,'risk_pct':1}], {'min_score':60,'max_risk_pct':2}); assert len(r['accepted'])==1
