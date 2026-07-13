from app.final_closeout_v1.project_seal import ProjectSealBuilderV1

def test_project_seal():
    seal = ProjectSealBuilderV1().build()
    assert seal.sealed is True
    assert seal.version == "1.0.0"
