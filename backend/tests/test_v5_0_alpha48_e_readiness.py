from app.platform_core.windows_builder.readiness import WindowsExecutableBuilderReadinessGate

def test_readiness():
 assert WindowsExecutableBuilderReadinessGate().run()['ready'] is True
