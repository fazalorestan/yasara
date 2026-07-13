import { apiGet } from "./client";

export const getProjectCliSummary = () =>
  apiGet("/v3-6-2/project-cli/summary");

export const getProjectCliStatus = () =>
  apiGet("/v3-6-2/project-cli/status");

export const getProjectCliUsage = () =>
  apiGet("/v3-6-2/project-cli/usage");
