from app.platform_core.windows_packaging.report import windows_packaging_report_service

class WindowsPackagingReadinessGate:
    def run(self):
        report = windows_packaging_report_service.report()
        ready = (
            report["ready"]
            and report["profile"]["ready"]
            and report["portable"]["ready"]
            and report["installer"]["ready"]
            and report["metadata"]["ready"]
            and report["layout"]["ready"]
            and report["validation"]["profile_valid"]
            and report["exe_packaging_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "profile_ready": report["profile"]["ready"],
                "portable_ready": report["portable"]["ready"],
                "installer_ready": report["installer"]["ready"],
                "metadata_ready": report["metadata"]["ready"],
                "layout_ready": report["layout"]["ready"],
                "validation_ready": report["validation"]["ready"],
                "exe_packaging_enabled": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

windows_packaging_readiness_gate = WindowsPackagingReadinessGate()
