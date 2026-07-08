import { useAuth } from "@/app/providers/AuthProvider";

export default function DashboardPage() {
  const { user } = useAuth();

  return (
    <>
      <h1>Portal del Administrador</h1>

      <p>
        Bienvenido a CelebraWeb Enterprise Experience Operations Platform.
      </p>

      <hr />

      <h2>Dashboard</h2>

      {user ? (
        <>
          <h3>
            Bienvenido, {user.first_name} {user.last_name}
          </h3>

          <table
            style={{
              borderCollapse: "collapse",
              marginTop: "20px",
              minWidth: "500px",
            }}
          >
            <tbody>
              <tr>
                <td
                  style={{
                    padding: "10px",
                    fontWeight: "bold",
                    width: "220px",
                  }}
                >
                  Correo electrónico
                </td>

                <td style={{ padding: "10px" }}>
                  {user.email}
                </td>
              </tr>

              <tr>
                <td
                  style={{
                    padding: "10px",
                    fontWeight: "bold",
                  }}
                >
                  Organización
                </td>

                <td style={{ padding: "10px" }}>
                  {user.organization_id}
                </td>
              </tr>

              <tr>
                <td
                  style={{
                    padding: "10px",
                    fontWeight: "bold",
                  }}
                >
                  Estado
                </td>

                <td style={{ padding: "10px" }}>
                  {user.status}
                </td>
              </tr>

              <tr>
                <td
                  style={{
                    padding: "10px",
                    fontWeight: "bold",
                  }}
                >
                  Perfil
                </td>

                <td style={{ padding: "10px" }}>
                  {user.is_super_admin
                    ? "Super Administrador"
                    : "Administrador"}
                </td>
              </tr>
            </tbody>
          </table>
        </>
      ) : (
        <p>Cargando información del usuario...</p>
      )}
    </>
  );
}