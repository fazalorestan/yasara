from app.platform_core.live_data_pipeline.event_dispatcher import LiveStreamEventDispatcher

def test_v500_alpha39_c_dispatch(): assert LiveStreamEventDispatcher().dispatch_preview()['dispatched'] is True
