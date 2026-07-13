import { apiGet } from "./client";
export const getLauncherSummary = () => apiGet("/v4-18/launcher/summary");
