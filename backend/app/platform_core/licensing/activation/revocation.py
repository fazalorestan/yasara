class LicenseRevocationContract:
    def revoke_plan(self, license_key: str):
        return {
            "ready": True,
            "license_key": license_key,
            "steps": [
                "mark_activation_revoked",
                "clear_entitlement_cache",
                "disable_protected_features",
                "emit_activation_audit_event",
            ],
            "destructive": False,
            "execution_allowed": False,
            "mode": "contract_only",
        }

license_revocation_contract = LicenseRevocationContract()
