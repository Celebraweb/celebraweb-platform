import Button from "@/components/ui/Button";

import type { Organization } from "../types/organization";

interface OrganizationsTableProps {
  organizations: Organization[];
  onEdit: (organization: Organization) => void;
  onDelete: (organization: Organization) => void;
}

export default function OrganizationsTable({
  organizations,
  onEdit,
  onDelete,
}: OrganizationsTableProps) {
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
            Código
          </th>

          <th style={{ padding: "12px", textAlign: "left" }}>
            País
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
        {organizations.map((organization) => (
          <tr key={organization.id}>
            <td style={{ padding: "12px" }}>
              {organization.name}
            </td>

            <td style={{ padding: "12px" }}>
              {organization.code}
            </td>

            <td style={{ padding: "12px" }}>
              {organization.country}
            </td>

            <td style={{ padding: "12px" }}>
              {organization.status}
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
                onClick={() => onEdit(organization)}
              >
                Editar
              </Button>

              <Button
                variant="danger"
                onClick={() => onDelete(organization)}
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