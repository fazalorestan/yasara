from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_commercial_no_api_key(): assert WindowsExecutableBuilderFacadeV500Alpha48().report()['commercial_api_key_required'] is False
