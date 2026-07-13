from app.platform_core.indicators.sandbox.install_gate import indicator_install_safety_gate
from app.platform_core.indicators.sandbox.manifest_validator import indicator_manifest_validator
from app.platform_core.indicators.sandbox.runtime_validator import indicator_runtime_output_validator
from app.platform_core.indicators.sandbox.security_validator import indicator_security_policy_validator
from app.v500_alpha3_indicator_sandbox.models import IndicatorSandboxSummaryV500Alpha3

class IndicatorSandboxFacadeV500Alpha3:
    def summary(self):
        return IndicatorSandboxSummaryV500Alpha3()

    def policy(self):
        return {"ready": True, "policy": indicator_security_policy_validator.policy()}

    def validate_manifest(self):
        manifest = {"name": "yasara", "version": "v1.0", "display_name": "YaSara", "capabilities": ["runtime"]}
        return {"ready": True, "validation": indicator_manifest_validator.validate(manifest)}

    def validate_runtime(self):
        output = {"indicator": "yasara", "version": "v1.0", "overlays": [], "signals": [{"execution_allowed": False}], "mode": "analysis_only"}
        return {"ready": True, "validation": indicator_runtime_output_validator.validate(output)}

    def install_gate(self):
        manifest = {"name": "yasara", "version": "v1.0", "display_name": "YaSara", "capabilities": ["runtime"], "metadata": {"imports": []}}
        return indicator_install_safety_gate.evaluate(manifest)

    def contract(self):
        return {
            "ready": True,
            "validators": ["manifest", "runtime_output", "security_policy", "isolation", "install_gate"],
            "execution_allowed": False,
            "mode": "validation_only",
        }
