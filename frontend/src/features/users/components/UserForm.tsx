import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import MultiSelect from "@/components/ui/MultiSelect";

import OrganizationSelect from "@/features/organizations/components/OrganizationSelect";

import {
  getRoles,
} from "@/features/roles/services/role.service";

import {
  getUserRoles,
} from "../services/userRole.service";

import type { Role } from "@/features/roles/types/role";
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

  const [roles, setRoles] = useState<Role[]>([]);

  const [selectedRoles, setSelectedRoles] =
    useState<string[]>([]);

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

    loadRoles();

  }, []);

  useEffect(() => {

    if (!initialData) {

      setForm({
        organization_id: "",
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        is_super_admin: false,
        email_verified: false,
      });

      setSelectedRoles([]);

      return;

    }

    setForm({
      organization_id: initialData.organization_id,
      first_name: initialData.first_name,
      last_name: initialData.last_name,
      email: initialData.email,
      password: "",
      is_super_admin: initialData.is_super_admin,
      email_verified: initialData.email_verified,
    });

    loadUserRoles(
      initialData.id,
    );

  }, [initialData]);

  async function loadRoles() {

    try {

      const data = await getRoles();

      setRoles(data);

    } catch (error) {

      console.error(error);

    }

  }

  async function loadUserRoles(
    userId: string,
  ) {

    try {

      const data =
        await getUserRoles(
          userId,
        );

      setSelectedRoles(
        data.map(
          (role) => role.id,
        ),
      );

    } catch (error) {

      console.error(error);

    }

  }

  function handleInputChange(
    event: React.ChangeEvent<HTMLInputElement>,
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
    organizationId: string,
  ) {

    setForm((previous) => ({
      ...previous,
      organization_id: organizationId,
    }));

  }
    function handleSubmit(
    event: React.FormEvent,
  ) {

    event.preventDefault();

    onSave({
      ...form,
      role_ids: selectedRoles,
    });

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

          {" "}
          Super Admin

        </label>

        <br />

        <label>

          <input
            type="checkbox"
            name="email_verified"
            checked={form.email_verified}
            onChange={handleInputChange}
          />

          {" "}
          Email Verificado

        </label>

      </div>

      <MultiSelect
        label="Roles"
        options={roles.map((role) => ({
          value: role.id,
          label: role.name,
        }))}
        values={selectedRoles}
        onChange={setSelectedRoles}
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