export interface User {
  id: string;
  organization_id: string;
  first_name: string;
  last_name: string;
  email: string;
  is_super_admin: boolean;
  email_verified: boolean;
  status: string;
  created_at: string;
  updated_at?: string;
}