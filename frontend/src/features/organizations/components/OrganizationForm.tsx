import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";

import type { Organization } from "../types/organization";

export interface OrganizationFormData {
  code: string;
  name: string;
  legal_name?: string;
  country: string;
  timezone: string;
  language: string;
}

interface OrganizationFormProps {
  initialData?: Organization | null;

  onSave: (
    data: OrganizationFormData
  ) => Promise<void>;

  onCancel: () => void;
}

export default function OrganizationForm({
  initialData,
  onSave,
  onCancel,
}: OrganizationFormProps) {

  const [form, setForm] =
    useState<OrganizationFormData>({
      code: "",
      name: "",
      legal_name: "",
      country: "Colombia",
      timezone: "America/Bogota",
      language: "es",
    });

  useEffect(() => {

    if (!initialData) {

      setForm({
        code: "",
        name: "",
        legal_name: "",
        country: "Colombia",
        timezone: "America/Bogota",
        language: "es",
      });

      return;
    }

    setForm({
      code: initialData.code,
      name: initialData.name,
      legal_name:
        initialData.legal_name ?? "",
      country: initialData.country,
      timezone: initialData.timezone,
      language: initialData.language,
    });

  }, [initialData]);

  function updateField(
    field: keyof OrganizationFormData,
    value: string
  ) {

    setForm((previous) => ({
      ...previous,
      [field]: value,
    }));
  }

  async function handleSubmit(
    e: React.FormEvent
  ) {

    e.preventDefault();

    await onSave(form);
  }

  return (
    <form onSubmit={handleSubmit}>

      <Input
        label="Código"
        value={form.code}
        onChange={(e) =>
          updateField(
            "code",
            e.target.value
          )
        }
        required
      />

      <Input
        label="Nombre Comercial"
        value={form.name}
        onChange={(e) =>
          updateField(
            "name",
            e.target.value
          )
        }
        required
      />

      <Input
        label="Razón Social"
        value={form.legal_name}
        onChange={(e) =>
          updateField(
            "legal_name",
            e.target.value
          )
        }
      />

      <Input
        label="País"
        value={form.country}
        onChange={(e) =>
          updateField(
            "country",
            e.target.value
          )
        }
        required
      />

      <Input
        label="Zona Horaria"
        value={form.timezone}
        onChange={(e) =>
          updateField(
            "timezone",
            e.target.value
          )
        }
        required
      />

      <Input
        label="Idioma"
        value={form.language}
        onChange={(e) =>
          updateField(
            "language",
            e.target.value
          )
        }
        required
      />

      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          gap: "12px",
          marginTop: "24px",
        }}
      >
        <Button
          type="button"
          variant="secondary"
          onClick={onCancel}
        >
          Cancelar
        </Button>

        <Button type="submit">
          {initialData
            ? "Actualizar"
            : "Guardar"}
        </Button>

      </div>

    </form>
  );
}