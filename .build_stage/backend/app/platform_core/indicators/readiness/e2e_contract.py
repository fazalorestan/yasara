class YaSaraIndicatorE2EContract:
    def contract(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "pipeline": [
                "pine_source_archive",
                "settings_presets",
                "runtime_adapter",
                "chart_overlay_contract",
                "engine_bridge",
                "scanner_watchlist",
                "alert_notification",
                "readiness_gate",
            ],
            "outputs": [
                "chart_overlays",
                "signals",
                "ai_decision",
                "risk_panel",
                "scanner_items",
                "alerts",
            ],
            "execution_allowed": False,
            "mode": "analysis_only",
        }

yasara_indicator_e2e_contract = YaSaraIndicatorE2EContract()
