import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import MultiSelect from "@/components/ui/MultiSelect";

import type { Role } from "../types/role";
import type { Permission } from "@/features/permissions/types/permission";

import {
  getPermissions,
} from "@/features/permissions/services/permission.service";

import {
  getRolePermissions,
} from "../services/rolePermission.service";

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

  const [permissions, setPermissions] =
    useState<Permission[]>([]);

  const [selectedPermissions, setSelectedPermissions] =
    useState<string[]>([]);

  const [form, setForm] = useState({
    code: "",
    name: "",
    description: "",
  });

  useEffect(() => {

    loadPermissions();

  }, []);

  useEffect(() => {

    if (!initialData) {

      setForm({
        code: "",
        name: "",
        description: "",
      });

      setSelectedPermissions([]);

      return;

    }

    setForm({
      code: initialData.code,
      name: initialData.name,
      description:
        initialData.description ?? "",
    });

    loadRolePermissions(
      initialData.id,
    );

  }, [initialData]);

  async function loadPermissions() {

    try {

      const data =
        await getPermissions();

      setPermissions(data);

    } catch (error) {

      console.error(error);

    }

  }

  async function loadRolePermissions(
    roleId: string,
  ) {

    try {

      const data =
        await getRolePermissions(
          roleId,
        );

      setSelectedPermissions(
        data.map(
          (permission) =>
            permission.id,
        ),
      );

    } catch (error) {

      console.error(error);

    }

  }

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

    onSave({
      ...form,
      permission_ids: selectedPermissions,
    });

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

      <MultiSelect
        label="Permisos"
        options={permissions.map((permission) => ({
          value: permission.id,
          label: permission.name,
        }))}
        values={selectedPermissions}
        onChange={setSelectedPermissions}
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