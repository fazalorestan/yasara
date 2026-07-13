from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_facade_build_hook():
 r=PICEnterpriseFacadeV500Alpha44().build_hook(); assert r is not None
