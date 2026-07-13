class LicenseSettingsPageContract:
    def contract(self):
        return {
            "ready": True,
            "sections": [
                "license_status",
                "activation",
                "demo_countdown",
                "enabled_features",
                "locked_features",
                "upgrade_prompt",
                "admin_tools_placeholder",
            ],
            "actions": [
                "enter_license_key",
                "activate_offline",
                "import_license",
                "export_license",
                "refresh_status",
            ],
            "execution_allowed": False,
        }

license_settings_page_contract = LicenseSettingsPageContract()
