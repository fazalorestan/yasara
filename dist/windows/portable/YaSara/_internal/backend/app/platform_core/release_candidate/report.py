from app.platform_core.release_candidate.manual_trading_toggle import manual_auto_trading_toggle_contract
from app.platform_core.release_candidate.rc_manifest import internal_rc_manifest
from app.platform_core.release_candidate.release_health import internal_rc_release_health
from app.platform_core.release_candidate.safety_toggle_policy import safety_toggle_policy
from app.platform_core.release_candidate.toggle_dashboard_contract import auto_trading_toggle_dashboard_contract
from app.platform_core.release_candidate.trading_control_state import trading_control_state_contract

class InternalRCPreparationReportService:
    def report(self):
        return {
            'ready': True,
            'build_id': '2026.50.E.001',
            'manifest': internal_rc_manifest.manifest(),
            'manual_toggle': manual_auto_trading_toggle_contract.contract(),
            'dashboard_toggle': auto_trading_toggle_dashboard_contract.dashboard(),
            'default_state': trading_control_state_contract.state(False, False),
            'safety_state_example': safety_toggle_policy.apply_failure('exchange'),
            'health': internal_rc_release_health.health(),
            'final_exe_generated': False,
            'real_execution_enabled': False,
            'real_broker_connection_enabled': False,
            'commercial_execution_engine_enabled': False,
            'commercial_api_key_required': False
        }
internal_rc_preparation_report_service = InternalRCPreparationReportService()
InternalRCPreparationReport = InternalRCPreparationReportService
internal_rc_preparation_report = internal_rc_preparation_report_service
