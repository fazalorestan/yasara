class PluginVersionService:
    def parse(self, version: str):
        parts = [int(x) for x in version.split(".") if x.isdigit()]
        while len(parts) < 3:
            parts.append(0)
        return {"ready": True, "major": parts[0], "minor": parts[1], "patch": parts[2]}

    def compare(self, a: str, b: str):
        av = self.parse(a)
        bv = self.parse(b)
        at = (av["major"], av["minor"], av["patch"])
        bt = (bv["major"], bv["minor"], bv["patch"])
        return {"ready": True, "a": a, "b": b, "result": 0 if at == bt else 1 if at > bt else -1}

plugin_version_service = PluginVersionService()
