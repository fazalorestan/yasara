from app.platform_core.optimizer.parameter_grid import ParameterGridBuilder

def test_v500_alpha31_grid_total(): assert ParameterGridBuilder().build([{'name':'a','values':[1,2]},{'name':'b','values':[3,4]}])['total'] == 4
