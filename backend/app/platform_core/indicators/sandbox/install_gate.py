from app.platform_core.indicators.sandbox.isolation_check import indicator_isolation_checker
from app.platform_core.indicators.sandbox.manifest_validator import indicator_manifest_validator
from app.platform_core.indicators.sandbox.runtime_validator import indicator_runtime_output_validator
from app.platform_core.indicators.sandbox.security_validator import indicator_security_policy_validator

class IndicatorInstallSafetyGate:
    def evaluate(self, manifest: dict, runtime_output: dict | None = None, security_request: dict | None = None):
        manifest_result = indicator_manifest_validator.validate(manifest)
        runtime_result = indicator_runtime_output_validator.validate(runtime_output or {
            "indicator": manifest.get("name", "unknown"),
            "version": manifest.get("version", "v0"),
            "overlays": [],
            "signals": [{"execution_allowed": False}],
            "mode": "analysis_only",
        })
        security_result = indicator_security_policy_validator.validate(security_request or {})
        isolation_result = indicator_isolation_checker.check(manifest.get("metadata", {}))

        ready = all([
            manifest_result["valid"],
            runtime_result["valid"],
            security_result["valid"],
            isolation_result["ready"],
        ])

        return {
            "ready": ready,
            "manifest": manifest_result,
            "runtime": runtime_result,
            "security": security_result,
            "isolation": isolation_result,
            "install_allowed": ready,
            "execution_allowed": False,
            "mode": "safety_gate_only",
        }

indicator_install_safety_gate = IndicatorInstallSafetyGate()
