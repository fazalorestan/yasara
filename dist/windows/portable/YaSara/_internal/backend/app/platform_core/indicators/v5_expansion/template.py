class FutureIndicatorTemplateService:
    def template(self):
        return {"ready":True,"folder":"frontend/src/indicators/<indicator-name>/","backend_folder":"backend/app/platform_core/indicators/<indicator-name>/","files":["manifest","runtime_adapter","chart_overlay_contract","engine_bridge","scanner_contract","alert_contract","settings_presets","readiness_gate","docs","tests"],"mode":"template_only"}
future_indicator_template_service = FutureIndicatorTemplateService()
