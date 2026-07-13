from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_exe_contract():
 r=WindowsExecutableBuilderFacadeV500Alpha48().exe_contract(); assert r is not None
