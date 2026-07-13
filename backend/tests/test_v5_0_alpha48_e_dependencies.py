from app.platform_core.windows_builder.dependency_checker import WindowsDependencyChecker

def test_dependencies():
 assert WindowsDependencyChecker().check()['dependencies_valid'] is True
