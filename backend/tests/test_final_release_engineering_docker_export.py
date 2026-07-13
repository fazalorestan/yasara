from app.final_release_engineering_v1.docker_export_plan import DockerExportPlanBuilderV1

def test_docker_export_plan():
    plan = DockerExportPlanBuilderV1().build()
    assert plan.tag == "1.0.0"
