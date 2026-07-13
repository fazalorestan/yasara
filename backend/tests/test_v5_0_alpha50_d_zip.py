from app.platform_core.windows_artifact_registration.portable_zip_plan import LocalPortableZipPlan

def test_zip(): assert LocalPortableZipPlan().plan()['requires_hash'] is True
