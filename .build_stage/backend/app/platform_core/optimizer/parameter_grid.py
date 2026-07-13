class ParameterGridBuilder:
    def build(self, ranges: list[dict]):
        grid = [{}]
        for item in ranges:
            name = item["name"]
            values = item["values"]
            grid = [base | {name: value} for base in grid for value in values]
        return {"ready": True, "total": len(grid), "items": grid}

parameter_grid_builder = ParameterGridBuilder()
