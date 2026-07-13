from app.platform_core.scanner.filters import ScannerFilterPipeline

def test_v500_alpha27_filter_reject_risk():
    r=ScannerFilterPipeline().apply([{'symbol':'A','score':80,'risk_pct':3}], {'min_score':60,'max_risk_pct':2}); assert 'risk_exceeded' in r['rejected'][0]['reject_reasons']
