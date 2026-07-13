import { apiGet } from "./client";

export interface AlertHistoryItem {
  id?: string | number;
  time?: string;
  timestamp?: string;
  title?: string;
  type?: string;
  detail?: string;
  symbol?: string;
  severity?: "high" | "medium" | "low" | string;
}

export interface AlertHistoryResponse {
  alerts?: AlertHistoryItem[];
}

export interface NotificationChannelsResponse {
  [key: string]: unknown;
}

export interface NotificationAlertsSummary {
  [key: string]: unknown;
}

export const getNotificationAlertsSummary = <T = NotificationAlertsSummary>() =>
  apiGet<T>("/v4-7/notifications/summary");

export const getNotificationChannels = <T = NotificationChannelsResponse>() =>
  apiGet<T>("/v4-7/notifications/channels");

export const getAlertHistory = <T = AlertHistoryResponse>() =>
  apiGet<T>("/v4-7/notifications/alerts");
