from app.platform_core.alert_engine.evaluator import AlertRuleEvaluator

def test_v500_alpha28_eval_risk_trigger(): assert AlertRuleEvaluator().evaluate_risk_result({'allowed':False,'reason':'x'})['severity']=='critical'
