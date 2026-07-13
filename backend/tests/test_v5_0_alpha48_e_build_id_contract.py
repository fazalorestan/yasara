from app.v500_alpha48_windows_builder.service import WindowsExecutableBuilderFacadeV500Alpha48

def test_build_id_contract(): assert WindowsExecutableBuilderFacadeV500Alpha48().contract()['build_id']=='2026.48.E.001'
