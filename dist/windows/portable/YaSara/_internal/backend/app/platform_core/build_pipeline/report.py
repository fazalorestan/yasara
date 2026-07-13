from app.platform_core.build_pipeline.artifact_registry import build_artifact_registry
from app.platform_core.build_pipeline.build_core import build_pipeline_core_service
from app.platform_core.build_pipeline.build_dashboard_provider import build_dashboard_provider
from app.platform_core.build_pipeline.config_loader import build_configuration_loader
from app.platform_core.build_pipeline.hash_generator import build_hash_generator
from app.platform_core.build_pipeline.integrity import build_integrity_service
from app.platform_core.build_pipeline.manifest_registry import build_manifest_registry
from app.platform_core.build_pipeline.metadata_registry import build_metadata_registry
from app.platform_core.build_pipeline.package_fingerprint import package_fingerprint_service
from app.platform_core.build_pipeline.plugin_build_contract import plugin_build_contract_service
from app.platform_core.build_pipeline.profile_manager import build_profile_manager
from app.platform_core.build_pipeline.validators import build_validator_service

class BuildPipelineReportService:
    def report(self):
        return {
            "ready": True,
            "core": build_pipeline_core_service.status(),
            "manifest": build_manifest_registry.manifest(),
            "metadata": build_metadata_registry.metadata(),
            "artifacts": build_artifact_registry.artifacts(),
            "profiles": build_profile_manager.profiles(),
            "config": build_configuration_loader.config(),
            "validation": build_validator_service.validate(),
            "integrity": build_integrity_service.integrity(),
            "hash": build_hash_generator.hash(),
            "fingerprint": package_fingerprint_service.fingerprint(),
            "plugin_contract": plugin_build_contract_service.contract(),
            "dashboard": build_dashboard_provider.dashboard(),
            "packaging_enabled": False,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

build_pipeline_report_service = BuildPipelineReportService()
BuildPipelineReport = BuildPipelineReportService
build_pipeline_report = build_pipeline_report_service
