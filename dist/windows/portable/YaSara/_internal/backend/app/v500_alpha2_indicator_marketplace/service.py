from app.platform_core.indicators.marketplace.catalog import indicator_catalog
from app.platform_core.indicators.marketplace.discovery import indicator_catalog_discovery
from app.platform_core.indicators.marketplace.install_contract import indicator_install_contract
from app.v500_alpha2_indicator_marketplace.models import IndicatorMarketplaceSummaryV500Alpha2
class IndicatorMarketplaceFacadeV500Alpha2:
    def summary(self): return IndicatorMarketplaceSummaryV500Alpha2()
    def catalog(self): return {"ready":True,"catalog":indicator_catalog.seed_defaults()}
    def discovery(self): return indicator_catalog_discovery.discover()
    def install_plan(self, indicator: str="yasara"): return indicator_install_contract.install_plan(indicator)
    def enable_plan(self, indicator: str="yasara"): return indicator_install_contract.enable_plan(indicator)
    def disable_plan(self, indicator: str="yasara"): return indicator_install_contract.disable_plan(indicator)
