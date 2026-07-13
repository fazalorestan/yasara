from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_facade_test_hook():
 r=PICEnterpriseFacadeV500Alpha44().test_hook(); assert r is not None
