from app.v500_alpha45_runtime_enterprise.models import RuntimeEnterpriseSummaryV500Alpha45

def test_summary():
 s=RuntimeEnterpriseSummaryV500Alpha45(); assert s.ready and s.test_pack_size==85 and s.commercial_execution_engine_enabled is False
