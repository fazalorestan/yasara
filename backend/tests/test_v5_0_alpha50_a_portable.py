from app.platform_core.windows_real_exe.portable_builder import WindowsRealPortableBuilder

def test_portable(): assert WindowsRealPortableBuilder().builder()['final_exe_expected'] is True
