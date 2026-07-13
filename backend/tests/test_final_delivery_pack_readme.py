from app.final_delivery_pack_v1.delivery_readme import DeliveryReadmeBuilderV1

def test_delivery_readme():
    readme = DeliveryReadmeBuilderV1().build()
    assert readme.title == "YaSara Professional v1.0"
    assert len(readme.sections) >= 3
