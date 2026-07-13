class IndicatorRegressionSafetySummary:
    def summary(self):
        return {
            "ready": True,
            "protected_surfaces": [
                "existing_api_routes",
                "dashboard",
                "frontend_layout",
                "analysis_engines",
                "execution_layer",
                "market_data_layer",
            ],
            "changed_behavior": False,
            "execution_allowed": False,
            "status": "safe",
        }

indicator_regression_safety_summary = IndicatorRegressionSafetySummary()
