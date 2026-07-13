from app.platform_core.optimizer.backtest_link import optimizer_backtest_link_service
from app.platform_core.optimizer.config import optimizer_config_service
from app.platform_core.optimizer.parameter_grid import parameter_grid_builder
from app.platform_core.optimizer.ranking import optimizer_ranking_service
from app.platform_core.optimizer.trial_runner import optimizer_trial_runner

class OptimizerFoundationService:
    def config(self): return optimizer_config_service.default()
    def ranges(self):
        return {"ready": True, "ranges": [{"name": "lookback", "values": [10, 20, 30]}, {"name": "risk_pct", "values": [0.5, 1.0, 2.0]}]}
    def grid(self):
        return parameter_grid_builder.build(self.ranges()["ranges"])
    def trials(self):
        grid = self.grid()["items"]
        trials = []
        for idx, params in enumerate(grid):
            result = optimizer_trial_runner.run_trial(params)
            trials.append({"trial_id": f"trial_{idx+1}", "parameters": params, "score": result["score"], "metrics": result["metrics"]})
        return {"ready": True, "total": len(trials), "items": trials, "execution_allowed": False}
    def ranking(self):
        return optimizer_ranking_service.rank(self.trials()["items"])
    def best(self):
        return self.ranking()["best"]
    def backtest_link(self):
        return optimizer_backtest_link_service.link()
    def run(self):
        ranking = self.ranking()
        return {"ready": True, "best": ranking["best"], "total_trials": len(ranking["items"]), "execution_allowed": False}

optimizer_foundation_service = OptimizerFoundationService()
