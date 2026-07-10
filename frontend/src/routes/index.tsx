import { createBrowserRouter } from "react-router-dom";

import LoginPage from "@/features/auth/LoginPage";
import DashboardPage from "@/pages/DashboardPage";

import OrganizationsPage from "@/features/organizations/pages/OrganizationsPage";
import UsersPage from "@/features/users/pages/UsersPage";

import AdminLayout from "@/layouts/AdminLayout";
import ProtectedRoute from "@/components/auth/ProtectedRoute";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage />,
  },
  {
    path: "/dashboard",
    element: (
      <ProtectedRoute>
        <AdminLayout>
          <DashboardPage />
        </AdminLayout>
      </ProtectedRoute>
    ),
  },
  {
    path: "/organizations",
    element: (
      <ProtectedRoute>
        <AdminLayout>
          <OrganizationsPage />
        </AdminLayout>
      </ProtectedRoute>
    ),
  },
  {
    path: "/users",
    element: (
      <ProtectedRoute>
        <AdminLayout>
          <UsersPage />
        </AdminLayout>
      </ProtectedRoute>
    ),
  },
]);