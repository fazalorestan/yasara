from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

def test_v36_registry_dependency():
    service = PhaseAMetaYKBServiceV36()
    assert "features_count" in service.registry_status()
    assert service.dependency_status()["has_commercial_execution_exclusion"] is True
