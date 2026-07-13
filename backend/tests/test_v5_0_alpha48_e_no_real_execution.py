from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_no_real_execution(): assert WindowsExecutableBuilderFacadeV500Alpha48().report()['real_execution_enabled'] is False
