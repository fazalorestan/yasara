class IndicatorV5PluginContract:
    def contract(self):
        return {
            "ready": True,
            "plugin_type": "indicator",
            "required_files": [
                "manifest",
                "runtime_adapter",
                "chart_overlay_contract",
                "engine_bridge",
                "scanner_contract",
                "alert_contract",
                "settings_presets",
                "readiness_gate",
            ],
            "required_properties": [
                "name",
                "version",
                "enabled_by_default",
                "overlay",
                "capabilities",
                "execution_allowed_false",
            ],
            "communication": ["event_bus", "platform_services", "public_contracts"],
            "forbidden": ["direct_live_execution", "direct_exchange_order", "dashboard_coupling"],
            "mode": "contract_only",
        }

indicator_v5_plugin_contract = IndicatorV5PluginContract()
