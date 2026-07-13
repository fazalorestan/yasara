from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_portable():
 r=WindowsExecutableBuilderFacadeV500Alpha48().portable(); assert r is not None
