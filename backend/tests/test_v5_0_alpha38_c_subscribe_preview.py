from app.platform_core.exchange_layer.streams import ExchangeStreamContractService

def test_v500_alpha38_c_subscribe_preview(): assert ExchangeStreamContractService().subscribe_preview()['dry_run'] is True