from app.rc1_v1.docker_validation import DockerValidationPlannerV1

def test_rc1_docker_validation():
    plan = DockerValidationPlannerV1().build()
    assert "yasara-backend" in plan.services
