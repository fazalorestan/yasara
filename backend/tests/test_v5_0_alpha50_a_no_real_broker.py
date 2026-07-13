from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_no_real_broker(): assert WindowsRealExeBuildPipelineFacadeV500Alpha50().report()['real_broker_connection_enabled'] is False
