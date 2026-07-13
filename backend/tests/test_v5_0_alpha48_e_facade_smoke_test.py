from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_smoke_test():
 r=WindowsExecutableBuilderFacadeV500Alpha48().smoke_test(); assert r is not None
