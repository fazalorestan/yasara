from app.platform_core.patching.classifier import PatchScriptClassifier

def test_v500_alpha21_classifier_v5():
    r=PatchScriptClassifier().classify('apply_v5_0_alpha_20_launcher_api_search_patch.py'); assert r['family']=='v5'; assert r['safe'] is True
