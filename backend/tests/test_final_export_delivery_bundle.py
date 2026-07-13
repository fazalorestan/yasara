from app.final_export_v1.delivery_bundle import DeliveryBundleBuilderV1

def test_delivery_bundle():
    bundle = DeliveryBundleBuilderV1().build()
    assert bundle.bundle_name == "YaSara_Professional_v1.0_Delivery"
    assert "README.md" in bundle.files
