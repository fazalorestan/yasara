from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_no_real_execution(): assert PICEnterpriseFacadeV500Alpha44().report()['real_execution_enabled'] is False
