class LicenseTypes:
    DEMO = "demo"
    PERSONAL = "personal"
    PRO = "pro"
    ELITE = "elite"
    ENTERPRISE = "enterprise"
    LIFETIME = "lifetime"
    INTERNAL = "internal"

    def all(self):
        return [self.DEMO, self.PERSONAL, self.PRO, self.ELITE, self.ENTERPRISE, self.LIFETIME, self.INTERNAL]

license_types = LicenseTypes()
