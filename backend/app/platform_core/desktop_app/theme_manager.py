class DesktopThemeManager:
    def theme(self):
        return {"ready": True, "theme": "system", "supports_light": True, "supports_dark": True, "accent_color": "default"}
desktop_theme_manager = DesktopThemeManager()
