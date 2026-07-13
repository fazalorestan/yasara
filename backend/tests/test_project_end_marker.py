from app.project_end_v1.end_marker import ProjectEndMarkerBuilderV1

def test_project_end_marker():
    marker = ProjectEndMarkerBuilderV1().build()
    assert marker.status == "finished"
    assert marker.confirmed_tests >= 310
    assert marker.failed_tests == 0
