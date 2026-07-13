from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_resources():
 r=WindowsExecutableBuilderFacadeV500Alpha48().resources(); assert r is not None
