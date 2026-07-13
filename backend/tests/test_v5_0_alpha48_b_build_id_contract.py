from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_build_id_contract(): assert WindowsPackagingFacadeV500Alpha48().contract()['build_id']=='2026.48.B.001'
