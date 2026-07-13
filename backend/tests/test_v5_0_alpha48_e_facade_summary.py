from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_summary():
 r=WindowsExecutableBuilderFacadeV500Alpha48().summary(); assert r is not None
