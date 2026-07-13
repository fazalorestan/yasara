class PermissionManager:
    def __init__(self):
        self._role_permissions = {}
    def grant(self, role, permission):
        self._role_permissions.setdefault(role, set()).add(permission)
    def has_permission(self, role, permission):
        return permission in self._role_permissions.get(role, set())
    def list(self):
        return {k: sorted(v) for k, v in self._role_permissions.items()}

permission_manager = PermissionManager()
