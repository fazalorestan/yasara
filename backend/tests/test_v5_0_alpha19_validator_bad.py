from app.platform_core.api_routing.validator import RouterImportValidator

def test_v500_alpha19_validator_bad():
    assert RouterImportValidator().validate_module_record({'module_name':'','import_path':'','has_router':False})['valid'] is False
