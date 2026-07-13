from app.platform_core.ai_decision.metrics import AIDecisionMetricsService

def test_v500_alpha33_a_metrics_blocked(): assert AIDecisionMetricsService().summarize([{'confidence':80,'execution_allowed':False}])['blocked_decisions']==1
