class GenericIndicatorContractService:
    def contract(self):
        return {
            "ready": True,
            "plugin_type": "indicator",
            "required_contracts": ["manifest","runtime_adapter","chart_overlay_contract","engine_bridge","scanner_contract","alert_contract","settings_presets","readiness_gate"],
            "optional_contracts": ["pine_source_archive","custom_renderer","multi_timeframe_adapter","market_specific_settings"],
            "forbidden": ["direct_live_execution","direct_exchange_order","direct_dashboard_mutation","plugin_to_plugin_direct_import"],
            "communication": ["event_bus","platform_services","public_contracts"],
            "mode": "contract_only",
        }
generic_indicator_contract_service = GenericIndicatorContractService()
