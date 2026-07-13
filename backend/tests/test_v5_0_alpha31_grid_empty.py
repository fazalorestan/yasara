from app.platform_core.optimizer.parameter_grid import ParameterGridBuilder

def test_v500_alpha31_grid_empty(): assert ParameterGridBuilder().build([])['total'] == 1
