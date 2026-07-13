from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_report():
 r=WindowsAppBootstrapFacadeV500Alpha48().report(); assert r is not None
