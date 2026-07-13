from app.platform_core.indicators.v5_expansion.template import FutureIndicatorTemplateService

def test_v500_alpha1_template():
 t=FutureIndicatorTemplateService().template(); assert t['ready'] and 'runtime_adapter' in t['files']
