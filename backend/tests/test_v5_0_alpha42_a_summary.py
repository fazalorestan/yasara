from app.v500_alpha42_execution_core.models import ExecutionCoreSummaryV500Alpha42

def test_v500_alpha42_a_summary():
 s=ExecutionCoreSummaryV500Alpha42(); assert s.ready and s.test_pack_size==60
