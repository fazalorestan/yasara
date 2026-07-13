from app.platform_core.build_pipeline.validators import build_validator_service
from app.platform_core.build_pipeline.integrity import build_integrity_service
from app.platform_core.ci_pipeline.test_result_registry import test_result_registry

class BuildQualitySignalProvider:
    def signal(self):
        validation = build_validator_service.validate()
        integrity = build_integrity_service.integrity()
        tests = test_result_registry.results()
        green = validation["build_valid"] and integrity["integrity_valid"] and tests["tests_failed"] == 0 and tests["tests_errors"] == 0
        return {
            "ready": True,
            "build_valid": validation["build_valid"],
            "integrity_valid": integrity["integrity_valid"],
            "tests_failed": tests["tests_failed"],
            "tests_errors": tests["tests_errors"],
            "signal": "green" if green else "red",
            "hardcoded_dashboard": False,
        }

build_quality_signal_provider = BuildQualitySignalProvider()
