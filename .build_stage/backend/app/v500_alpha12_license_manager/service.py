from app.platform_core.licensing.manager.service import license_manager_service
from app.v500_alpha12_license_manager.models import LicenseManagerSummaryV500Alpha12

class LicenseManagerFacadeV500Alpha12:
    def summary(self):
        return LicenseManagerSummaryV500Alpha12()

    def sample_payload(self, license_type: str = "demo"):
        return {"license_key": "LOCAL-SAMPLE", "license_type": license_type}

    def status(self, license_type: str = "demo"):
        return license_manager_service.status(self.sample_payload(license_type))

    def plan(self, license_type: str = "demo", days: int = 30):
        return license_manager_service.plan(license_type, days)

    def admin_operations(self):
        return license_manager_service.admin_operations()

    def demo_renewal_policy(self):
        return license_manager_service.demo_renewal_policy()

    def can_renew_demo(self, previous_renewals: int = 0):
        return license_manager_service.can_renew_demo(previous_renewals)

    def health(self):
        return license_manager_service.health()

    def export_sample(self, license_type: str = "demo"):
        return license_manager_service.export_license(self.sample_payload(license_type))

    def import_sample(self):
        exported = self.export_sample("demo")
        return license_manager_service.import_license(exported["export"])

    def contract(self):
        return {
            "ready": True,
            "manager": ["status", "plan", "admin_operations", "demo_renewal", "health", "export", "import"],
            "admin_ui_future_ready": True,
            "execution_allowed": False,
        }
