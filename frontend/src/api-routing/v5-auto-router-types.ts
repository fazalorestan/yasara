export type YaSaraAutoRouterModule = { moduleName: string; importPath: string; hasRouter: boolean; safeToRegister: boolean; };
export type YaSaraAutoRouterPlan = { ready: boolean; totalModules: number; safeModules: number; unsafeModules: number; };
export type YaSaraSwaggerVisibility = { docsUrl: string; openapiUrl: string; apiPrefix: string; };
