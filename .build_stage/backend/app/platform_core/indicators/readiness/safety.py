class YaSaraIndicatorSafetyReport:
    def report(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "live_execution_enabled": False,
            "auto_trade_enabled": False,
            "analysis_only": True,
            "external_data_connection_added": False,
            "dashboard_changed": False,
            "safe_for_v5_plugin_expansion": True,
        }

yasara_indicator_safety_report = YaSaraIndicatorSafetyReport()
