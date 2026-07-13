from app.platform_core.optimizer.trial_runner import OptimizerTrialRunner

def test_v500_alpha31_trial(): assert OptimizerTrialRunner().run_trial({'lookback':20,'risk_pct':1})['ready'] is True
