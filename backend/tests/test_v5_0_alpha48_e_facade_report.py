from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_facade_report():
 r=WindowsExecutableBuilderFacadeV500Alpha48().report(); assert r is not None
