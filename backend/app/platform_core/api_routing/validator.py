class RouterImportValidator:
    def validate_module_record(self, record: dict):
        errors = []
        if not record.get("module_name"):
            errors.append("missing_module_name")
        if not record.get("import_path"):
            errors.append("missing_import_path")
        if record.get("has_router") is not True:
            errors.append("missing_router")
        return {"valid": len(errors) == 0, "errors": errors, "record": record}

router_import_validator = RouterImportValidator()
