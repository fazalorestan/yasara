from app.platform_core.windows_packaging.app_metadata import WindowsAppMetadataService

def test_metadata(): assert WindowsAppMetadataService().metadata()['app_name']=='YaSara OS'
