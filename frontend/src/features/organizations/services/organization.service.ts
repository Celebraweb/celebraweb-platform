import api from "@/services/api";

import type { Organization } from "../types/organization";

export interface CreateOrganizationRequest {
  code: string;
  name: string;
  legal_name?: string;
  country: string;
  timezone: string;
  language: string;
}

export interface UpdateOrganizationRequest {
  code: string;
  name: string;
  legal_name?: string;
  country: string;
  timezone: string;
  language: string;
}

export async function getOrganizations(): Promise<Organization[]> {

  const response = await api.get<Organization[]>(
    "/organizations"
  );

  return response.data;
}

export async function createOrganization(
  data: CreateOrganizationRequest
): Promise<Organization> {

  const response = await api.post<Organization>(
    "/organizations",
    data
  );

  return response.data;
}

export async function updateOrganization(
  organizationId: string,
  data: UpdateOrganizationRequest
): Promise<Organization> {

  const response = await api.put<Organization>(
    `/organizations/${organizationId}`,
    data
  );

  return response.data;
}

export async function deleteOrganization(
  organizationId: string
): Promise<void> {

  await api.delete(
    `/organizations/${organizationId}`
  );
}