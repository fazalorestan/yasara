from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_not_hardcoded(): assert PICEnterpriseFacadeV500Alpha44().contract()['hardcoded_dashboard'] is False
