export interface Role {
  id: string;
  code: string;
  name: string;
  description?: string;
  status: string;
  created_at: string;
  updated_at: string;
}

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