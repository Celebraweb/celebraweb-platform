import api from "@/services/api";

import type { Role } from "../types/role";

export interface CreateRoleRequest {
  code: string;
  name: string;
  description?: string;
}

export interface UpdateRoleRequest {
  code?: string;
  name?: string;
  description?: string;
  status?: string;
}

export async function getRoles(): Promise<Role[]> {
  const response = await api.get<Role[]>("/roles");

  return response.data;
}

export async function getRole(
  roleId: string
): Promise<Role> {
  const response = await api.get<Role>(
    `/roles/${roleId}`
  );

  return response.data;
}

export async function createRole(
  data: CreateRoleRequest
): Promise<Role> {
  const response = await api.post<Role>(
    "/roles",
    data
  );

  return response.data;
}

export async function updateRole(
  roleId: string,
  data: UpdateRoleRequest
): Promise<Role> {
  const response = await api.put<Role>(
    `/roles/${roleId}`,
    data
  );

  return response.data;
}

export async function deleteRole(
  roleId: string
): Promise<void> {
  await api.delete(
    `/roles/${roleId}`
  );
}