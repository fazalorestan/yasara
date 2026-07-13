from app.enterprise_v1.logging_framework import LoggingFrameworkV1

def test_logging_framework_info():
    entry = LoggingFrameworkV1().info("started")
    assert entry.level == "info"
