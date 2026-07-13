from app.platform_core.plugin_sdk.compat_matrix import plugin_compatibility_matrix_service
from app.platform_core.plugin_sdk.dependencies import plugin_dependency_contract_service
from app.platform_core.plugin_sdk.manifest import plugin_manifest_service
from app.platform_core.plugin_sdk.marketplace import plugin_marketplace_metadata_service
from app.platform_core.plugin_sdk.upgrade import plugin_upgrade_planner
from app.platform_core.plugin_sdk.versioning import plugin_version_service

class PluginVersioningReportService:
    def report(self):
        manifest = plugin_manifest_service.sample_manifest()
        return {"ready": True, "version": plugin_version_service.parse(manifest["version"]), "compatibility": plugin_compatibility_matrix_service.is_supported(manifest["api_version"], manifest["version"]), "dependencies": plugin_dependency_contract_service.validate(manifest), "upgrade": plugin_upgrade_planner.plan(manifest["version"], manifest["version"]), "marketplace": plugin_marketplace_metadata_service.listing(manifest), "execution_allowed": False}

plugin_versioning_report_service = PluginVersioningReportService()
