import Button from "@/components/ui/Button";

import type { User } from "../types/user";

interface UsersTableProps {
  users: User[];
  onEdit: (user: User) => void;
  onDelete: (user: User) => void;
}

export default function UsersTable({
  users,
  onEdit,
  onDelete,
}: UsersTableProps) {
  return (
    <table
      style={{
        width: "100%",
        borderCollapse: "collapse",
        marginTop: "20px",
      }}
    >
      <thead>
        <tr
          style={{
            background: "#f5f5f5",
          }}
        >
          <th style={{ padding: "12px", textAlign: "left" }}>
            Nombre
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            Apellido
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            Correo
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            Super Admin
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            Estado
          </th>

          <th
            style={{
              padding: "12px",
              textAlign: "center",
              width: "220px",
            }}
          >
            Acciones
          </th>
        </tr>
      </thead>

      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td style={{ padding: "12px" }}>
              {user.first_name}
            </td>

            <td style={{ padding: "12px" }}>
              {user.last_name}
            </td>

            <td style={{ padding: "12px" }}>
              {user.email}
            </td>

            <td style={{ padding: "12px" }}>
              {user.is_super_admin ? "Sí" : "No"}
            </td>

            <td style={{ padding: "12px" }}>
              {user.status}
            </td>

            <td
              style={{
                padding: "12px",
                display: "flex",
                justifyContent: "center",
                gap: "10px",
              }}
            >
              <Button
                variant="secondary"
                onClick={() => onEdit(user)}
              >
                Editar
              </Button>

              <Button
                variant="danger"
                onClick={() => onDelete(user)}
              >
                Eliminar
              </Button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}