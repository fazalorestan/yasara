from app.v500_alpha47_production_readiness.models import ProductionReadinessSummaryV500Alpha47

def test_summary():
 s=ProductionReadinessSummaryV500Alpha47(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.47.E.001'
