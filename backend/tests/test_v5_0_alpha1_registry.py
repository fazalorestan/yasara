from app.platform_core.indicators.v5_expansion.multi_registry import MultiIndicatorRegistryV5

def test_v500_alpha1_registry():
 r=MultiIndicatorRegistryV5().seed_defaults(); assert 'yasara' in r and 'future_indicator_template' in r
