from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_readiness():
 r=WindowsExecutableBuilderFacadeV500Alpha48().readiness(); assert r is not None
