import { useNavigate } from "react-router-dom";

import { useAuth } from "@/app/providers/AuthProvider";

export default function Header() {
  const navigate = useNavigate();
  const { user } = useAuth();

  function handleLogout() {
    localStorage.removeItem("access_token");

    navigate("/", {
      replace: true,
    });
  }

  return (
    <header
      style={{
        background: "#ffffff",
        borderBottom: "1px solid #dfe3e8",
        padding: "16px 32px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        height: "72px",
      }}
    >
      <div>
        <div
          style={{
            fontSize: "22px",
            fontWeight: "bold",
          }}
        >
          XOP Platform
        </div>

        <div
          style={{
            fontSize: "13px",
            color: "#666",
          }}
        >
          Producto activo: CelebraWeb Platform
        </div>
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "24px",
        }}
      >
        <span
          style={{
            cursor: "pointer",
            fontSize: "20px",
          }}
          title="Notificaciones"
        >
          🔔
        </span>

        <span
          style={{
            cursor: "pointer",
            fontSize: "20px",
          }}
          title="Configuración"
        >
          ⚙️
        </span>

        <div
          style={{
            textAlign: "right",
          }}
        >
          <div
            style={{
              fontWeight: "bold",
            }}
          >
            {user
              ? `${user.first_name} ${user.last_name}`
              : "Usuario"}
          </div>

          <div
            style={{
              fontSize: "12px",
              color: "#666",
            }}
          >
            {user?.is_super_admin
              ? "Super Administrator"
              : "Administrator"}
          </div>
        </div>

        <button
          onClick={handleLogout}
          style={{
            padding: "8px 16px",
            cursor: "pointer",
            borderRadius: "6px",
            border: "1px solid #d0d7de",
            background: "#ffffff",
          }}
        >
          Cerrar sesión
        </button>
      </div>
    </header>
  );
}