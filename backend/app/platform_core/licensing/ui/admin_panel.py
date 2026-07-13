class LicenseAdminPanelContract:
    def contract(self):
        return {
            "ready": True,
            "internal_only": True,
            "sections": [
                "create_license",
                "renew_license",
                "revoke_license",
                "assign_features",
                "device_limits",
                "export_import",
            ],
            "requires_admin_permission": True,
            "execution_allowed": False,
        }

license_admin_panel_contract = LicenseAdminPanelContract()
