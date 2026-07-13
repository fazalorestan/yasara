from app.platform_core.startup.backend_contract import BackendLauncherContract

def test_v500_alpha20_backend_contract():
    c=BackendLauncherContract().contract(); assert c['backend_module']=='app.main:app'; assert c['single_source_of_truth'] is True
