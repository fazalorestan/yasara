class LicenseCompatibilityMatrix:
    def matrix(self):
        return {
            "ready": True,
            "subsystem": "licensing",
            "v5_compatible": True,
            "offline_mode": True,
            "online_future_ready": True,
            "plugin_ready": True,
            "feature_flag_ready": True,
            "admin_ui_future_ready": True,
            "demo_supported": True,
            "trial_14_days_supported": True,
            "trial_30_days_supported": True,
            "dashboard_unchanged": True,
            "execution_allowed": False,
        }

license_compatibility_matrix = LicenseCompatibilityMatrix()
