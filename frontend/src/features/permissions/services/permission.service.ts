import api from "@/services/api";

import type { Permission } from "../types/permission";

export interface CreatePermissionRequest {
  code: string;
  name: string;
  description?: string;
}

export interface UpdatePermissionRequest {
  code?: string;
  name?: string;
  description?: string;
  status?: string;
}

export async function getPermissions(): Promise<Permission[]> {

  const response = await api.get<Permission[]>(
    "/permissions",
  );

  return response.data;

}

export async function getPermission(
  permissionId: string,
): Promise<Permission> {

  const response = await api.get<Permission>(
    `/permissions/${permissionId}`,
  );

  return response.data;

}

export async function createPermission(
  data: CreatePermissionRequest,
): Promise<Permission> {

  const response = await api.post<Permission>(
    "/permissions",
    data,
  );

  return response.data;

}

export async function updatePermission(
  permissionId: string,
  data: UpdatePermissionRequest,
): Promise<Permission> {

  const response = await api.put<Permission>(
    `/permissions/${permissionId}`,
    data,
  );

  return response.data;

}

export async function deletePermission(
  permissionId: string,
): Promise<void> {

  await api.delete(
    `/permissions/${permissionId}`,
  );

}