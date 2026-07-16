import api from "@/services/api";

import type { Permission } from "@/features/permissions/types/permission";

export interface RolePermissionAssignmentRequest {
  permission_ids: string[];
}

export async function getRolePermissions(
  roleId: string,
): Promise<Permission[]> {

  const response = await api.get<Permission[]>(
    `/roles/${roleId}/permissions`,
  );

  return response.data;

}

export async function replaceRolePermissions(
  roleId: string,
  permissionIds: string[],
): Promise<Permission[]> {

  const response = await api.put<Permission[]>(
    `/roles/${roleId}/permissions`,
    {
      permission_ids: permissionIds,
    } satisfies RolePermissionAssignmentRequest,
  );

  return response.data;

}