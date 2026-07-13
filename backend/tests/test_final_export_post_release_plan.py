from app.final_export_v1.post_release_plan import PostReleasePlanBuilderV1

def test_post_release_plan():
    plan = PostReleasePlanBuilderV1().build()
    assert any(t.target_version == "1.1.0" for t in plan.tasks)
