from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_commercial_no_execution(): assert WindowsExecutableBuilderFacadeV500Alpha48().report()['commercial_execution_engine_enabled'] is False
