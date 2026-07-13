from app.platform_core.pydantic_settings_runtime_gate.report import pydantic_settings_runtime_gate_report_service
class PydanticSettingsRuntimeGateReadinessGate:
    def run(self):
        r = pydantic_settings_runtime_gate_report_service.report()
        return {'ready': r['ready'] and r['pydantic_settings_gate'] and not r['auto_trading_enabled'], 'checks': r}
pydantic_settings_runtime_gate_readiness_gate = PydanticSettingsRuntimeGateReadinessGate()
