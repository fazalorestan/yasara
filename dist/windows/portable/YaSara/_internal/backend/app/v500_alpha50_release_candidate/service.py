from app.platform_core.release_candidate.manual_trading_toggle import manual_auto_trading_toggle_contract
from app.platform_core.release_candidate.rc_manifest import internal_rc_manifest
from app.platform_core.release_candidate.readiness import internal_rc_readiness_gate
from app.platform_core.release_candidate.release_health import internal_rc_release_health
from app.platform_core.release_candidate.report import internal_rc_preparation_report_service
from app.platform_core.release_candidate.safety_toggle_policy import safety_toggle_policy
from app.platform_core.release_candidate.toggle_dashboard_contract import auto_trading_toggle_dashboard_contract
from app.platform_core.release_candidate.trading_control_state import trading_control_state_contract
from app.v500_alpha50_release_candidate.models import InternalRCPreparationSummaryV500Alpha50

class InternalRCPreparationFacadeV500Alpha50:
    def summary(self): return InternalRCPreparationSummaryV500Alpha50()
    def manifest(self): return internal_rc_manifest.manifest()
    def manual_toggle(self): return manual_auto_trading_toggle_contract.contract()
    def dashboard_toggle(self): return auto_trading_toggle_dashboard_contract.dashboard()
    def trading_state(self, auto_trading_enabled=False, disabled_by_safety=False): return trading_control_state_contract.state(auto_trading_enabled, disabled_by_safety)
    def safety_disable(self, failed_module='exchange'): return safety_toggle_policy.apply_failure(failed_module)
    def health(self): return internal_rc_release_health.health()
    def report(self): return internal_rc_preparation_report_service.report()
    def readiness(self): return internal_rc_readiness_gate.run()
    def contract(self): return {'ready': True, 'release_candidate': 'package_e_internal_rc', 'build_id': '2026.50.E.001'}
internal_rc_preparation_facade_v500_alpha50 = InternalRCPreparationFacadeV500Alpha50()
