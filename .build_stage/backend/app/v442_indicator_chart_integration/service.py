from app.v442_indicator_chart_integration.models import IndicatorChartIntegrationSummaryV442

class IndicatorChartIntegrationServiceV442:
    def summary(self):
        return IndicatorChartIntegrationSummaryV442()

    def chart_binding(self):
        return {
            "ready": True,
            "chart": "market_workspace_chart",
            "default_indicator": "yasara",
            "enabled_by_default": True,
            "script_slot": "frontend/src/indicators/yasara/yasara-script.ts",
            "manager": "frontend/src/indicators/chart-indicator-manager.ts",
            "renderer": "frontend/src/indicators/yasara/yasara-renderer-contract.ts",
            "mode": "contract_only",
        }

    def visibility(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "default_visible": True,
            "overlays": {
                "ema": True,
                "sma": True,
                "smc": True,
                "fvg": True,
                "entry_sl_tp": True,
                "dynamic_sl": True,
                "fibonacci": False,
            },
            "panels": {
                "ai_decision": True,
                "risk_panel": True,
                "engine_scores": True,
                "status_bar": True,
            },
        }

    def update_contract(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "update_strategy": "replace_script_slot_only",
            "stable_files": [
                "frontend/src/indicators/chart-indicator-manager.ts",
                "frontend/src/indicators/chart-overlay-contract.ts",
                "frontend/src/indicators/yasara/yasara-renderer-contract.ts",
            ],
            "editable_file": "frontend/src/indicators/yasara/yasara-script.ts",
            "backward_compatible": True,
        }
