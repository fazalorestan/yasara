from app.platform_core.windows_packaging.packaging_profile import WindowsPackagingProfileService

def test_profile(): assert WindowsPackagingProfileService().profile()['portable_supported'] is True
