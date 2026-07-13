class RouterRegistrationAuditContract:
    def audit_text(self, router_text: str, module_name: str):
        return {
            "ready": module_name in router_text and f"{module_name}.router" in router_text,
            "import_present": module_name in router_text,
            "include_present": f"{module_name}.router" in router_text,
        }

    def missing_from_text(self, router_text: str, module_names: list[str]):
        missing = [name for name in module_names if name not in router_text or f"{name}.router" not in router_text]
        return {"ready": len(missing) == 0, "missing": missing, "checked": len(module_names)}

router_registration_audit_contract = RouterRegistrationAuditContract()
