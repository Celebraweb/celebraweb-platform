import { createBrowserRouter } from "react-router-dom";

import LoginPage from "@/features/auth/LoginPage";
import DashboardPage from "@/pages/DashboardPage";
import AdminLayout from "@/layouts/AdminLayout";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage />,
  },
  {
    path: "/dashboard",
    element: (
      <AdminLayout>
        <DashboardPage />
      </AdminLayout>
    ),
  },
]);