import { apiGet } from "./client";

export const getConstitutionAuditSummary = () =>
  apiGet("/v3-5-1/constitution-audit/summary");

export const getConstitutionAuditHealth = () =>
  apiGet("/v3-5-1/constitution-audit/health");

export const getConstitutionAuditRecommendations = () =>
  apiGet("/v3-5-1/constitution-audit/recommendations");
