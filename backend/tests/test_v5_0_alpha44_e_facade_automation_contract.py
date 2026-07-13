from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_facade_automation_contract():
 r=PICEnterpriseFacadeV500Alpha44().automation_contract(); assert r is not None
