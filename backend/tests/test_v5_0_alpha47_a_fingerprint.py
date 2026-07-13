from app.platform_core.build_pipeline.package_fingerprint import PackageFingerprintService

def test_fingerprint(): assert PackageFingerprintService().fingerprint()['stable'] is True
