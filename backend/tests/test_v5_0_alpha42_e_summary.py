from app.v500_alpha42_execution_enterprise.models import ExecutionEnterpriseSummaryV500Alpha42

def test_v500_alpha42_e_summary():
 s=ExecutionEnterpriseSummaryV500Alpha42(); assert s.ready and s.test_pack_size==65
