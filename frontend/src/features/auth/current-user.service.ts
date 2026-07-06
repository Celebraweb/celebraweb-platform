import api from "@/services/api";

export interface CurrentUser {
  user_id: string;
  organization_id: string;
  email: string;
  first_name: string;
  last_name: string;
  is_super_admin: boolean;
  status: string;
}

export async function getCurrentUser(): Promise<CurrentUser> {
  const response = await api.get<CurrentUser>("/auth/me");

  return response.data;
}