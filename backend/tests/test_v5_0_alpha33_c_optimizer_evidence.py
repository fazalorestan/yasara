from app.platform_core.ai_decision.integration.optimizer_link import AIDecisionOptimizerLink

def test_v500_alpha33_c_optimizer_evidence(): assert AIDecisionOptimizerLink().evidence()['execution_allowed'] is False