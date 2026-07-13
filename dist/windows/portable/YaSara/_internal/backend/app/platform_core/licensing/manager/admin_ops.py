class AdminLicenseOperationsContract:
    def operations(self):
        return {
            "ready": True,
            "operations": [
                "create_license",
                "renew_license",
                "revoke_license",
                "inspect_license",
                "export_license",
                "import_license",
                "assign_features",
                "change_device_limit",
            ],
            "requires_internal_license": True,
            "requires_admin_permission": True,
            "execution_allowed": False,
            "mode": "contract_only",
        }

admin_license_operations_contract = AdminLicenseOperationsContract()
