from app.platform_core.windows_builder.build_coordinator import WindowsBuildCoordinator

def test_coordinator():
 assert WindowsBuildCoordinator().coordinate()['ready'] is True
