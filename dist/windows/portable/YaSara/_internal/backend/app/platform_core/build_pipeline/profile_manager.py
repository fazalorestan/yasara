class BuildProfileManager:
    def profiles(self):
        return {
            "ready": True,
            "profiles": ["development", "test", "release_candidate", "stable"],
            "active_profile": "development",
            "windows_profile_ready": True,
            "android_profile_ready": False,
            "ios_profile_ready": False,
            "web_profile_ready": False,
        }

build_profile_manager = BuildProfileManager()
