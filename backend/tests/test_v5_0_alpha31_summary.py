from app.v500_alpha31_optimizer.models import OptimizerSummaryV500Alpha31

def test_v500_alpha31_summary():
    s=OptimizerSummaryV500Alpha31(); assert s.ready is True; assert s.test_pack_size == 30
