from app.final_export_scripts_v1.export_status import OneClickExportStatusBuilderV1

def test_one_click_final_export_status():
    status = OneClickExportStatusBuilderV1().build()
    assert status.ready is True
    assert status.confirmed_tests >= 312
    assert status.final_archive_name == "yasara_professional_v1_0_stable.zip"
