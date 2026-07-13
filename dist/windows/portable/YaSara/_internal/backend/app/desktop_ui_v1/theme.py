from pydantic import BaseModel

class ThemeTokensV1(BaseModel):
    mode: str = "dark"
    primary: str = "#4F46E5"
    background: str = "#0F172A"
    surface: str = "#111827"

class ThemeServiceV1:
    def get(self, mode: str = "dark") -> ThemeTokensV1:
        if mode == "light":
            return ThemeTokensV1(mode="light", background="#FFFFFF", surface="#F8FAFC")
        return ThemeTokensV1()
