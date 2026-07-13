from app.platform_core.windows_packaging.output_layout import WindowsBuildOutputLayout

def test_layout(): assert 'portable' in WindowsBuildOutputLayout().layout()['folders']
