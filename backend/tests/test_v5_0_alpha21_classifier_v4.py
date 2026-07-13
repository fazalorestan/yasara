from app.platform_core.patching.classifier import PatchScriptClassifier

def test_v500_alpha21_classifier_v4(): assert PatchScriptClassifier().classify('apply_v4_18_launcher_router_patch.py')['family']=='v4'
