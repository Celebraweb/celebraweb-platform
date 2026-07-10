import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";

import OrganizationSelect from "@/features/organizations/components/OrganizationSelect";

import type { User } from "../types/user";

interface UserFormProps {
  initialData?: User | null;
  onSave: (data: any) => void;
  onCancel: () => void;
}

export default function UserForm({
  initialData,
  onSave,
  onCancel,
}: UserFormProps) {

  const [form, setForm] = useState({
    organization_id: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    is_super_admin: false,
    email_verified: false,
  });

  useEffect(() => {

    if (initialData) {

      setForm({
        organization_id: initialData.organization_id,
        first_name: initialData.first_name,
        last_name: initialData.last_name,
        email: initialData.email,
        password: "",
        is_super_admin: initialData.is_super_admin,
        email_verified: initialData.email_verified,
      });

    }

  }, [initialData]);

  function handleInputChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {

    const {
      name,
      value,
      type,
      checked,
    } = event.target;

    setForm((previous) => ({
      ...previous,
      [name]:
        type === "checkbox"
          ? checked
          : value,
    }));

  }

  function handleOrganizationChange(
    organizationId: string
  ) {

    setForm((previous) => ({
      ...previous,
      organization_id: organizationId,
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

      <OrganizationSelect
        value={form.organization_id}
        onChange={handleOrganizationChange}
        required
      />

      <Input
        label="First Name"
        name="first_name"
        value={form.first_name}
        onChange={handleInputChange}
        required
      />

      <Input
        label="Last Name"
        name="last_name"
        value={form.last_name}
        onChange={handleInputChange}
        required
      />

      <Input
        label="Email"
        type="email"
        name="email"
        value={form.email}
        onChange={handleInputChange}
        required
      />

      <Input
        label="Password"
        type="password"
        name="password"
        value={form.password}
        onChange={handleInputChange}
        required={!initialData}
      />

      <div
        style={{
          marginTop: "16px",
          marginBottom: "16px",
        }}
      >
        <label>
          <input
            type="checkbox"
            name="is_super_admin"
            checked={form.is_super_admin}
            onChange={handleInputChange}
          />
          {" "}Super Admin
        </label>

        <br />

        <label>
          <input
            type="checkbox"
            name="email_verified"
            checked={form.email_verified}
            onChange={handleInputChange}
          />
          {" "}Email Verificado
        </label>
      </div>

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