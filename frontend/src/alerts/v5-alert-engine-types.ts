export type YaSaraAlertSeverity = "info" | "warning" | "critical";
export type YaSaraAlertRule = { ruleId: string; name: string; condition: string; severity: YaSaraAlertSeverity; enabled: boolean; };
export type YaSaraAlertEvent = { ruleId: string; symbol: string; message: string; severity: YaSaraAlertSeverity; acknowledged: boolean; };
export type YaSaraNotificationContract = { channel: string; enabled: boolean; dryRun: boolean; };
