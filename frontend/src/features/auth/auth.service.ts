import api from "@/services/api";

export interface LoginRequest {
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
}

export async function login(
  credentials: LoginRequest
): Promise<TokenResponse> {

  const response = await api.post<TokenResponse>(
    "/auth/login",
    credentials
  );

  return response.data;
}