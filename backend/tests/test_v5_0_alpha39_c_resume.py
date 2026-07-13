from app.platform_core.live_data_pipeline.subscriptions import LiveStreamSubscriptionManager

def test_v500_alpha39_c_resume(): assert LiveStreamSubscriptionManager().resume()['state']=='active'
