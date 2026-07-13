from app.platform_core.release_candidate.report import internal_rc_preparation_report_service

class InternalRCReadinessGate:
    def run(self):
        r = internal_rc_preparation_report_service.report()
        ready = (
            r['ready']
            and r['manual_toggle']['user_can_enable']
            and r['manual_toggle']['safety_can_disable']
            and r['manual_toggle']['system_can_enable_automatically'] is False
            and r['dashboard_toggle']['requires_manual_reenable_after_safety']
            and r['health']['system_auto_reenable_blocked']
            and r['real_execution_enabled'] is False
            and r['real_broker_connection_enabled'] is False
        )
        return {
            'ready': ready,
            'checks': {
                'manual_toggle_ready': r['manual_toggle']['ready'],
                'safety_can_disable': r['manual_toggle']['safety_can_disable'],
                'system_auto_reenable_blocked': r['manual_toggle']['system_can_enable_automatically'] is False,
                'requires_manual_reenable': r['dashboard_toggle']['requires_manual_reenable_after_safety'],
                'signal_only_default': r['manifest']['signal_only_default'],
                'auto_trading_default': r['manifest']['auto_trading_default']
            }
        }
internal_rc_readiness_gate = InternalRCReadinessGate()
