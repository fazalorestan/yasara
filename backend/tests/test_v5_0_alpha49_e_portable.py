from app.platform_core.desktop_finalization.portable_readiness import InternalPortableReadinessSummary

def test_portable(): assert InternalPortableReadinessSummary().summary()['requires_real_binary_builder_next'] is True
