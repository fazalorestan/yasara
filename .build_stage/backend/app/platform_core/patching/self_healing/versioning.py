import re
class PatchVersionParser:
    def parse(self, script_name: str):
        m = re.search(r"apply_v(\d+)_(\d+)_alpha_(\d+)", script_name.lower())
        if m:
            return {"family":"v","major":int(m.group(1)),"minor":int(m.group(2)),"alpha":int(m.group(3)),"sort_key":(int(m.group(1)),int(m.group(2)),int(m.group(3)),script_name)}
        return {"family":"legacy","major":0,"minor":0,"alpha":-1,"sort_key":(0,0,-1,script_name)}
patch_version_parser = PatchVersionParser()
