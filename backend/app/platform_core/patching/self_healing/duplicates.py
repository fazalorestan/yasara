class PatchDuplicateDetector:
    def detect(self, scripts: list[dict]):
        seen, duplicates = {}, []
        for item in scripts:
            key = item["version"]["sort_key"][:3]
            if key in seen:
                duplicates.append({"first": seen[key], "second": item["script"]})
            else:
                seen[key] = item["script"]
        return {"ready": len(duplicates) == 0, "duplicates": duplicates}
patch_duplicate_detector = PatchDuplicateDetector()
