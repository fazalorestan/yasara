from app.platform_core.alert_engine.evaluator import AlertRuleEvaluator

def test_v500_alpha28_eval_scanner_not_trigger(): assert AlertRuleEvaluator().evaluate_scanner_candidate({'symbol':'BTCUSDT','score':50})['triggered'] is False
