import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Modal from "@/components/ui/Modal";

import type { Role } from "../types/role";

import {
  getRoles,
  createRole,
  updateRole,
  deleteRole,
} from "../services/role.service";

import {
  replaceRolePermissions,
} from "../services/rolePermission.service";

import RolesTable from "../components/RolesTable";
import RoleForm from "../components/RoleForm";

export default function RolesPage() {

  const [roles, setRoles] = useState<Role[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [open, setOpen] = useState(false);

  const [selectedRole, setSelectedRole] =
    useState<Role | null>(null);

  async function loadRoles() {

    try {

      const data = await getRoles();

      setRoles(data);

      setError("");

    } catch (error) {

      console.error(error);

      setError(
        "No fue posible consultar los roles."
      );

    } finally {

      setLoading(false);

    }

  }

  useEffect(() => {

    loadRoles();

  }, []);

  function handleCreate() {

    setSelectedRole(null);

    setOpen(true);

  }

  function handleEdit(
    role: Role
  ) {

    setSelectedRole(role);

    setOpen(true);

  }

  async function handleSave(
    data: any
  ) {

    try {

      const {
        permission_ids,
        ...roleData
      } = data;

      let savedRole: Role;

      if (selectedRole) {

        savedRole = await updateRole(
          selectedRole.id,
          roleData,
        );

      } else {

        savedRole = await createRole(
          roleData,
        );

      }

      await replaceRolePermissions(
        savedRole.id,
        permission_ids ?? [],
      );
            setOpen(false);

      setSelectedRole(null);

      await loadRoles();

    } catch (error) {

      console.error(error);

      alert(
        "No fue posible guardar el rol."
      );

    }

  }

  async function handleDelete(
    role: Role
  ) {

    const confirmed = window.confirm(
      `¿Desea eliminar el rol "${role.name}"?`
    );

    if (!confirmed) {
      return;
    }

    try {

      await deleteRole(role.id);

      await loadRoles();

    } catch (error) {

      console.error(error);

      alert(
        "No fue posible eliminar el rol."
      );

    }

  }

  return (
    <>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "20px",
        }}
      >
        <div>

          <h1>Roles</h1>

          <p>
            Administración de roles.
          </p>

        </div>

        <Button onClick={handleCreate}>

          + Nuevo Rol

        </Button>

      </div>

      <hr />

      {loading && (
        <p>Cargando roles...</p>
      )}

      {!loading && error && (

        <p style={{ color: "red" }}>
          {error}
        </p>

      )}

      {!loading && !error && (

        <RolesTable
          roles={roles}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />

      )}

      <Modal
        open={open}
        title={
          selectedRole
            ? "Editar Rol"
            : "Nuevo Rol"
        }
        onClose={() => {

          setOpen(false);

          setSelectedRole(null);

        }}
      >

        <RoleForm
          initialData={selectedRole}
          onSave={handleSave}
          onCancel={() => {

            setOpen(false);

            setSelectedRole(null);

          }}
        />

      </Modal>

    </>
  );

}