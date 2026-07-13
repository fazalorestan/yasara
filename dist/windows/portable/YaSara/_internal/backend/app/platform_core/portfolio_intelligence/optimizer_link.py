from app.platform_core.optimizer_pro.service import strategy_optimizer_pro_service

class PortfolioOptimizerLinkService:
    def optimizer_best(self):
        return {"ready": True, "best_trial": strategy_optimizer_pro_service.best(), "source": "optimizer_pro", "execution_allowed": False}

    def allocation_bias(self):
        grade = self.optimizer_best()["best_trial"].get("robustness_grade", "D")
        return {"ready": True, "bias": "increase" if grade in ["A", "B"] else "hold", "robustness_grade": grade, "execution_allowed": False}

portfolio_optimizer_link_service = PortfolioOptimizerLinkService()
