import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";

import type { Role } from "../types/role";

interface RoleFormProps {
  initialData?: Role | null;
  onSave: (data: any) => void;
  onCancel: () => void;
}

export default function RoleForm({
  initialData,
  onSave,
  onCancel,
}: RoleFormProps) {

  const [form, setForm] = useState({
    code: "",
    name: "",
    description: "",
  });

  useEffect(() => {

    if (initialData) {

      setForm({
        code: initialData.code,
        name: initialData.name,
        description: initialData.description ?? "",
      });

    }

  }, [initialData]);

  function handleInputChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {

    const {
      name,
      value,
    } = event.target;

    setForm((previous) => ({
      ...previous,
      [name]: value,
    }));

  }

  function handleSubmit(
    event: React.FormEvent
  ) {

    event.preventDefault();

    onSave(form);

  }

  return (
    <form onSubmit={handleSubmit}>

      <Input
        label="Código"
        name="code"
        value={form.code}
        onChange={handleInputChange}
        required
      />

      <Input
        label="Nombre"
        name="name"
        value={form.name}
        onChange={handleInputChange}
        required
      />

      <Input
        label="Descripción"
        name="description"
        value={form.description}
        onChange={handleInputChange}
      />

      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          gap: "10px",
          marginTop: "20px",
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
          Guardar
        </Button>

      </div>

    </form>
  );
}