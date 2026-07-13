from app.platform_core.windows_packaging.portable_contract import WindowsPortableAppContract

def test_portable(): assert WindowsPortableAppContract().contract()['requires_installer'] is False
