from app.platform_core.ai_decision.metrics import AIDecisionMetricsService

def test_v500_alpha33_a_metrics_empty(): assert AIDecisionMetricsService().summarize([])['total_decisions']==0
