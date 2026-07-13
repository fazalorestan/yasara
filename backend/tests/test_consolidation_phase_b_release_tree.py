from app.consolidation_v1.release_tree import ReleaseTreePlanBuilderV1

def test_phase_b_release_tree():
    tree = ReleaseTreePlanBuilderV1().build()
    assert any(node.path == "YaSara/backend" for node in tree.nodes)
