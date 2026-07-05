export default function Sidebar() {
  return (
    <aside
      style={{
        background: "#20232a",
        color: "white",
        padding: "20px",
        minHeight: "100vh",
      }}
    >
      <h2>CelebraWeb XOP</h2>

      <hr />

      <p>🏠 Dashboard</p>
      <p>🏢 Organizaciones</p>
      <p>👥 Usuarios</p>
      <p>🛡 Roles</p>
      <p>📋 Auditoría</p>
      <p>⚙ Configuración</p>
    </aside>
  );
}