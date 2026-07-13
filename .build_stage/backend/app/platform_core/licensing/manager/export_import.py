from app.platform_core.licensing.offline import offline_license_contract

class LicenseExportImportContract:
    def export_license(self, payload: dict):
        packed = offline_license_contract.pack(payload)
        return {
            "ready": True,
            "export": packed,
            "format": "offline_signed_blob",
            "execution_allowed": False,
        }

    def import_license(self, blob: dict):
        result = offline_license_contract.verify(blob)
        return {
            "ready": result["ready"],
            "verification": result,
            "execution_allowed": False,
        }

license_export_import_contract = LicenseExportImportContract()
