from app.cloud_v1.remote_notifications import RemoteNotificationPlannerV1, RemoteNotificationV1

def test_remote_notification_plan():
    plan = RemoteNotificationPlannerV1().plan(RemoteNotificationV1(target_user_id="u1", title="Hi", body="Body", channels=["in_app","email"]))
    assert len(plan) == 2
