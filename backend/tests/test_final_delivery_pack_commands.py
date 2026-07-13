from app.final_delivery_pack_v1.final_commands import FinalCommandsBuilderV1

def test_final_commands():
    commands = FinalCommandsBuilderV1().build()
    assert any("pytest" in c.command for c in commands.commands)
