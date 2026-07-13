from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_sprint_complete(): assert PICEnterpriseFacadeV500Alpha44().package_manifest()['sprint_complete'] is True
