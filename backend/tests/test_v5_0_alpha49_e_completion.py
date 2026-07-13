from app.platform_core.desktop_finalization.sprint_completion import Sprint49CompletionContract

def test_completion(): assert Sprint49CompletionContract().completion()['sprint_complete'] is True
