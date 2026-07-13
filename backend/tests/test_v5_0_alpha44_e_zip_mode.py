from app.v500_alpha44_pic_enterprise.service import PICEnterpriseFacadeV500Alpha44

def test_zip_mode(): assert PICEnterpriseFacadeV500Alpha44().package_manifest()['one_zip_per_package'] is True
