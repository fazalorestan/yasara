from app.platform_core.windows_packaging.validation import WindowsPackagingValidationService

def test_validation(): assert WindowsPackagingValidationService().validate()['profile_valid'] is True
