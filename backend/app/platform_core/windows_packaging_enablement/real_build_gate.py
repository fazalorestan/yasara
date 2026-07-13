class WindowsRealBuildGate:
    def gate(self):
        return {'ready': True,'can_attempt_real_build':True,'requires_execute_flag':True,'requires_pyinstaller_available':True,'requires_clean_tests':True,'requires_signal_only_default':True,'blocks_trading_execution':True,'blocks_broker_connection':True}
windows_real_build_gate=WindowsRealBuildGate()
