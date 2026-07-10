import Button from "@/components/ui/Button";

import type { Role } from "../types/role";

interface RolesTableProps {
  roles: Role[];
  onEdit: (role: Role) => void;
  onDelete: (role: Role) => void;
}

export default function RolesTable({
  roles,
  onEdit,
  onDelete,
}: RolesTableProps) {
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
            Código
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            Nombre
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            Descripción
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
        {roles.map((role) => (
          <tr key={role.id}>
            <td style={{ padding: "12px" }}>
              {role.code}
            </td>

            <td style={{ padding: "12px" }}>
              {role.name}
            </td>

            <td style={{ padding: "12px" }}>
              {role.description}
            </td>

            <td style={{ padding: "12px" }}>
              {role.status}
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
                onClick={() => onEdit(role)}
              >
                Editar
              </Button>

              <Button
                variant="danger"
                onClick={() => onDelete(role)}
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