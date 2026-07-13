from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_facade_package_manifest():
 r=PICEnterpriseFacadeV500Alpha44().package_manifest(); assert r is not None
