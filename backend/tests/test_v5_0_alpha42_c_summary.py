from app.v500_alpha42_execution_lifecycle.models import ExecutionLifecycleSummaryV500Alpha42

def test_v500_alpha42_c_summary():
 s=ExecutionLifecycleSummaryV500Alpha42(); assert s.ready and s.test_pack_size==60
