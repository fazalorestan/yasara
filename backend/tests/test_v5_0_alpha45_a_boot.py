from app.platform_core.production_runtime.boot_contract import RuntimeBootContractService

def test_boot(): assert RuntimeBootContractService().dry_boot()['booted'] is True
