from app.v500_alpha42_execution_analytics.models import ExecutionAnalyticsSummaryV500Alpha42

def test_v500_alpha42_d_summary():
 s=ExecutionAnalyticsSummaryV500Alpha42(); assert s.ready and s.test_pack_size==60
