class LicenseKeyParser:
    def parse_visual_format(self, license_key: str):
        key = (license_key or "").strip().upper()
        parts = key.split("-")
        return {
            "ready": bool(key),
            "raw": key,
            "length": len(key.replace("-", "")),
            "prefix": parts[0] if parts else "",
            "parts": parts,
            "format_only": True,
        }

license_key_parser = LicenseKeyParser()
