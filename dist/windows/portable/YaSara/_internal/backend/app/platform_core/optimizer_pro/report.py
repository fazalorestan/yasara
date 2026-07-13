class OptimizerProReportBuilder:
    def build(self, trials: list[dict], best: dict | None):
        return {
            "ready": True,
            "trial_count": len(trials),
            "best": best,
            "research_only": True,
            "execution_allowed": False,
            "auto_trading": False,
        }

optimizer_pro_report_builder = OptimizerProReportBuilder()
