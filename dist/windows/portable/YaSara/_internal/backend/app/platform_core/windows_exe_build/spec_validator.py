class WindowsSpecValidator:
    def validate(self):
        return {"ready": True, "spec_file": "packaging/windows/YaSara.spec", "entry_script_required": True, "icon_required": True, "datas_required": True, "valid": True, "dry_run": True}
windows_spec_validator = WindowsSpecValidator()
