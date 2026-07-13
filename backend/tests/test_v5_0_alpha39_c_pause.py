from app.platform_core.live_data_pipeline.subscriptions import LiveStreamSubscriptionManager

def test_v500_alpha39_c_pause(): assert LiveStreamSubscriptionManager().pause()['state']=='paused'
