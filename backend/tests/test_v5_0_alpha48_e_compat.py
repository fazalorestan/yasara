from app.platform_core.windows_builder.report import WindowsExecutableBuilderReport, windows_executable_builder_report

def test_compat(): assert WindowsExecutableBuilderReport().report()['ready'] and windows_executable_builder_report.report()['ready']
