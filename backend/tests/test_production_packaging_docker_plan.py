from app.production_packaging_v1.docker_plan import DockerPlanBuilderV1

def test_docker_plan_has_backend():
    plan = DockerPlanBuilderV1().build()
    assert any(s.name == "yasara-backend" for s in plan.services)
