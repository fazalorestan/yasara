class InProcessBackendRunnerReportService:
    def report(self):
        return {'ready':True,'build_id':'2026.52.G.001','backend_runner':'in_process_thread','fixes_recursive_frozen_exe_launch':True,'health_candidates':['/api/v1/health','/health','/docs','/openapi.json'],'signal_only_default':True,'auto_trading_enabled':False}
in_process_backend_runner_report_service=InProcessBackendRunnerReportService()
