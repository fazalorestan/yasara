from app.final_delivery_pack_v1.final_project_card import FinalProjectCardBuilderV1

def test_final_project_card():
    card = FinalProjectCardBuilderV1().build()
    assert card.confirmed_tests >= 291
    assert card.failed_tests == 0
