from app.platform_core.windows_exe_build.spec_validator import WindowsSpecValidator

def test_spec(): assert WindowsSpecValidator().validate()['valid'] is True
