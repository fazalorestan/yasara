export type YaSaraPluginManifest = { pluginId: string; name: string; version: string; apiVersion: string; enabled: boolean; capabilities: string[]; };
export type YaSaraPluginSDKStatus = { ready: boolean; compatible: boolean; safe: boolean; executionAllowed: false; };
