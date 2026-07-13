from app.platform_core.api_routing.validator import RouterImportValidator

def test_v500_alpha19_validator_ok():
    assert RouterImportValidator().validate_module_record({'module_name':'x','import_path':'a.b','has_router':True})['valid'] is True
