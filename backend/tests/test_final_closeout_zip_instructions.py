from app.final_closeout_v1.final_zip_instructions import FinalZipInstructionsBuilderV1

def test_zip_instructions():
    instructions = FinalZipInstructionsBuilderV1().build()
    assert instructions.archive_name == "yasara_professional_v1_0_stable.zip"
    assert len(instructions.steps) >= 3
