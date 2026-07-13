from app.platform_core.licensing.manager.admin_ops import admin_license_operations_contract
from app.platform_core.licensing.manager.demo_renewal import demo_renewal_policy
from app.platform_core.licensing.manager.export_import import license_export_import_contract
from app.platform_core.licensing.manager.health import license_health_check
from app.platform_core.licensing.manager.plans import license_plan_builder
from app.platform_core.licensing.manager.status import license_status_reporter

class LicenseManagerService:
    def status(self, payload: dict):
        return license_status_reporter.status(payload)

    def plan(self, license_type: str = "demo", days: int | str = 30):
        return license_plan_builder.build(license_type, days)

    def admin_operations(self):
        return admin_license_operations_contract.operations()

    def demo_renewal_policy(self):
        return demo_renewal_policy.policy()

    def can_renew_demo(self, previous_renewals: int = 0):
        return {"ready": True, "can_renew": demo_renewal_policy.can_renew(previous_renewals), "execution_allowed": False}

    def health(self):
        return license_health_check.check()

    def export_license(self, payload: dict):
        return license_export_import_contract.export_license(payload)

    def import_license(self, blob: dict):
        return license_export_import_contract.import_license(blob)

license_manager_service = LicenseManagerService()
