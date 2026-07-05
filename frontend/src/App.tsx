import AdminLayout from "./layouts/AdminLayout";
import LoginPage from "./features/auth/LoginPage";

function App() {
  return (
    <AdminLayout>
      <LoginPage />
    </AdminLayout>
  );
}

export default App;