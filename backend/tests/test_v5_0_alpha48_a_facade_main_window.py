from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_main_window():
 r=WindowsAppBootstrapFacadeV500Alpha48().main_window(); assert r is not None
