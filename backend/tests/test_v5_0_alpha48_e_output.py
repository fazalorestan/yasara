from app.platform_core.windows_builder.output_manager import WindowsBuildOutputManager

def test_output():
 assert WindowsBuildOutputManager().output()['integrity_hash_required'] is True
