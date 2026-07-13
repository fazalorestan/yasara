from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_no_final_exe_yet(): assert WindowsExecutableBuilderFacadeV500Alpha48().summary().final_exe_generated is False
