export interface Organization {
  id: string;
  name: string;
  code: string;
  email: string;
  phone?: string;
  website?: string;
  status: string;
  created_at: string;
  updated_at?: string;
}