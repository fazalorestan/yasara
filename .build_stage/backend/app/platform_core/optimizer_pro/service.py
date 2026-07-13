from app.platform_core.optimizer_pro.genetic import genetic_optimizer_service
from app.platform_core.optimizer_pro.monte_carlo import monte_carlo_robustness_service
from app.platform_core.optimizer_pro.multi_objective import multi_objective_scoring_service
from app.platform_core.optimizer_pro.report import optimizer_pro_report_builder
from app.platform_core.optimizer_pro.robustness import robustness_grader
from app.platform_core.optimizer_pro.walk_forward import walk_forward_service

class StrategyOptimizerProService:
    def genetic(self): return genetic_optimizer_service.evolve_contract()
    def walk_forward(self): return walk_forward_service.summarize()
    def monte_carlo(self): return monte_carlo_robustness_service.simulate()
    def multi_objective(self):
        return multi_objective_scoring_service.score({"net_pnl": 120, "max_drawdown_pct": 6, "win_rate": 58, "stability": 0.7})
    def robustness(self):
        score = self.multi_objective()["score"]
        mc = self.monte_carlo()
        ratio = monte_carlo_robustness_service.robustness_ratio(mc)["ratio"]
        return robustness_grader.grade(score, ratio)
    def trials(self):
        samples = [
            {"trial_id": "pro_1", "parameters": {"lookback": 10, "risk_pct": 0.5}, "metrics": {"net_pnl": 90, "max_drawdown_pct": 5, "win_rate": 55, "stability": 0.7}},
            {"trial_id": "pro_2", "parameters": {"lookback": 20, "risk_pct": 1.0}, "metrics": {"net_pnl": 120, "max_drawdown_pct": 6, "win_rate": 58, "stability": 0.8}},
            {"trial_id": "pro_3", "parameters": {"lookback": 30, "risk_pct": 1.5}, "metrics": {"net_pnl": 70, "max_drawdown_pct": 9, "win_rate": 50, "stability": 0.4}},
        ]
        items = []
        for item in samples:
            scored = multi_objective_scoring_service.score(item["metrics"])
            mc = monte_carlo_robustness_service.simulate([{"pnl": item["metrics"]["net_pnl"]}], 50)
            ratio = monte_carlo_robustness_service.robustness_ratio(mc)["ratio"]
            grade = robustness_grader.grade(scored["score"], ratio)["grade"]
            items.append(item | {"score": scored["score"], "robustness_grade": grade})
        return {"ready": True, "items": items, "execution_allowed": False}
    def best(self):
        items = self.trials()["items"]
        return sorted(items, key=lambda x: x["score"], reverse=True)[0]
    def report(self):
        trials = self.trials()["items"]
        return optimizer_pro_report_builder.build(trials, self.best())
    def run(self):
        return {"ready": True, "report": self.report(), "execution_allowed": False}

strategy_optimizer_pro_service = StrategyOptimizerProService()
