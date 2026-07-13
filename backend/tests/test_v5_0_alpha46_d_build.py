from app.platform_core.desktop_app.build_information_provider import DesktopBuildInformationProvider

def test_build(): assert DesktopBuildInformationProvider().build_info()['ready'] is True
