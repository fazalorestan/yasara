from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_no_real_broker(): assert PICEnterpriseFacadeV500Alpha44().report()['real_broker_connection_enabled'] is False
