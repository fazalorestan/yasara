from app.final_integration_v1.final_release_tree import FinalReleaseTreeBuilderV1

def test_final_release_tree():
    tree = FinalReleaseTreeBuilderV1().build()
    assert tree.root == "YaSara_Professional_v1.0"
    assert any(i.path == "backend" for i in tree.items)
