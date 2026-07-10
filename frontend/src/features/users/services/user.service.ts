import api from "@/services/api";

import type { User } from "../types/user";

export interface CreateUserRequest {
  organization_id: string;
  first_name: string;
  last_name: string;
  email: string;
  password: string;
  is_super_admin?: boolean;
  email_verified?: boolean;
}

export interface UpdateUserRequest {
  first_name?: string;
  last_name?: string;
  email?: string;
  password?: string;
  is_super_admin?: boolean;
  email_verified?: boolean;
  status?: string;
}

export async function getUsers(): Promise<User[]> {
  const response = await api.get<User[]>("/users");

  return response.data;
}

export async function getUser(
  userId: string
): Promise<User> {
  const response = await api.get<User>(
    `/users/${userId}`
  );

  return response.data;
}

export async function createUser(
  data: CreateUserRequest
): Promise<User> {
  const response = await api.post<User>(
    "/users",
    data
  );

  return response.data;
}

export async function updateUser(
  userId: string,
  data: UpdateUserRequest
): Promise<User> {
  const response = await api.put<User>(
    `/users/${userId}`,
    data
  );

  return response.data;
}

export async function deleteUser(
  userId: string
): Promise<void> {
  await api.delete(
    `/users/${userId}`
  );
}
