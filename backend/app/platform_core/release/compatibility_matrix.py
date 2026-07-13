class CompatibilityMatrix:
    def matrix(self):
        return {
            "ready": True,
            "core": "v4.31",
            "compatible_with": [
                "v4.22 platform_core",
                "v4.23 plugin_catalog",
                "v4.24 registry_sync",
                "v4.25 policy_gate",
                "v4.26 contracts_sdk",
                "v4.27 extension_host",
                "v4.28 state_snapshot",
                "v4.29 timezone_runtime",
                "v4.30 diagnostics",
            ],
            "breaking_changes": [],
            "mode": "report_only",
        }
