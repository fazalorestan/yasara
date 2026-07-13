from app.platform_core.optimizer.trial_runner import OptimizerTrialRunner

def test_v500_alpha31_trial_execution_blocked(): assert OptimizerTrialRunner().run_trial({})['execution_allowed'] is False
