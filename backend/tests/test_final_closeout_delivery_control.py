from app.final_closeout_v1.delivery_control import DeliveryControlBuilderV1

def test_delivery_control():
    control = DeliveryControlBuilderV1().build()
    assert control.ready is True
