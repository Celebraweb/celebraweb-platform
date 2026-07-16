import api from "@/services/api";

import type { Role } from "@/features/roles/types/role";

export interface UserRoleAssignmentRequest {
  role_ids: string[];
}

export async function getUserRoles(
  userId: string
): Promise<Role[]> {

  const response = await api.get<Role[]>(
    `/users/${userId}/roles`
  );

  return response.data;

}

export async function replaceUserRoles(
  userId: string,
  roleIds: string[],
): Promise<Role[]> {

  const response = await api.put<Role[]>(
    `/users/${userId}/roles`,
    {
      role_ids: roleIds,
    } satisfies UserRoleAssignmentRequest,
  );

  return response.data;

}