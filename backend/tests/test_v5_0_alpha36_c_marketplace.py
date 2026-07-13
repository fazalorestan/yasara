from app.platform_core.plugin_sdk.marketplace import PluginMarketplaceMetadataService

def test_v500_alpha36_c_marketplace(): assert PluginMarketplaceMetadataService().listing({'plugin_id':'p','name':'P','version':'1'})['verified'] is True