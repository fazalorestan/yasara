class FeatureFlagCenter:
    def __init__(self):
        self._global = {}
        self._user = {}
        self._license = {}
        self._environment = {}
    def set_global(self, name, enabled):
        self._global[name] = bool(enabled)
    def is_enabled(self, name, user_id=None, license_key=None, environment=None):
        if user_id and name in self._user.get(user_id, {}): return self._user[user_id][name]
        if license_key and name in self._license.get(license_key, {}): return self._license[license_key][name]
        if environment and name in self._environment.get(environment, {}): return self._environment[environment][name]
        return self._global.get(name, False)
    def list_global(self):
        return dict(self._global)

feature_flag_center = FeatureFlagCenter()
