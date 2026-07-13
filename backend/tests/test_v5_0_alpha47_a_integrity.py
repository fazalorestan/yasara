from app.platform_core.build_pipeline.integrity import BuildIntegrityService

def test_integrity(): assert BuildIntegrityService().integrity()['tamper_detected'] is False
