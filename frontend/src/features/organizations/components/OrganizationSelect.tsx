import { useEffect, useState } from "react";

import {
  getOrganizations,
} from "../services/organization.service";

import type { Organization } from "../types/organization";

interface OrganizationSelectProps {
  value: string;
  onChange: (value: string) => void;
  required?: boolean;
}

export default function OrganizationSelect({
  value,
  onChange,
  required = false,
}: OrganizationSelectProps) {

  const [organizations, setOrganizations] = useState<
    Organization[]
  >([]);

  useEffect(() => {

    async function loadOrganizations() {

      try {

        const data =
          await getOrganizations();

        setOrganizations(data);

      } catch (error) {

        console.error(
          "No fue posible cargar las organizaciones.",
          error
        );

      }

    }

    loadOrganizations();

  }, []);

  return (
    <div
      style={{
        marginBottom: "16px",
      }}
    >
      <label
        style={{
          display: "block",
          marginBottom: "6px",
          fontWeight: 600,
        }}
      >
        Organización
      </label>

      <select
        value={value}
        required={required}
        onChange={(event) =>
          onChange(event.target.value)
        }
        style={{
          width: "100%",
          padding: "10px",
          borderRadius: "6px",
          border: "1px solid #cccccc",
          fontSize: "14px",
        }}
      >
        <option value="">
          Seleccione una organización
        </option>

        {organizations.map((organization) => (
          <option
            key={organization.id}
            value={organization.id}
          >
            {organization.name}
          </option>
        ))}
      </select>
    </div>
  );
}