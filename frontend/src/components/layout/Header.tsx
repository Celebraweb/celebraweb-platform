import { useNavigate } from "react-router-dom";

export default function Header() {
  const navigate = useNavigate();

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
        padding: "20px 30px",
        borderBottom: "1px solid #ddd",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <div>
        <strong>CelebraWeb XOP</strong>
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "20px",
        }}
      >
        <span>Administrador</span>

        <button
          onClick={handleLogout}
          style={{
            padding: "8px 16px",
            cursor: "pointer",
          }}
        >
          Cerrar sesión
        </button>
      </div>
    </header>
  );
}