from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_output():
 r=WindowsExecutableBuilderFacadeV500Alpha48().output(); assert r is not None
