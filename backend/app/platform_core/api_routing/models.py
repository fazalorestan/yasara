from dataclasses import dataclass

@dataclass
class DiscoveredRouterModule:
    module_name: str
    import_path: str
    has_router: bool = True
    safe_to_register: bool = True

@dataclass
class RouterRegistrationPlan:
    ready: bool
    total_modules: int
    safe_modules: int
    unsafe_modules: int
