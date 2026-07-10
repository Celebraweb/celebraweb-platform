import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Modal from "@/components/ui/Modal";

import type { User } from "../types/user";

import {
  getUsers,
  createUser,
  updateUser,
  deleteUser,
} from "../services/user.service";

import UsersTable from "../components/UsersTable";
import UserForm from "../components/UserForm";

export default function UsersPage() {

  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [open, setOpen] = useState(false);

  const [selectedUser, setSelectedUser] =
    useState<User | null>(null);

  async function loadUsers() {

    try {

      const data = await getUsers();

      setUsers(data);

      setError("");

    } catch (error) {

      console.error(error);

      setError(
        "No fue posible consultar los usuarios."
      );

    } finally {

      setLoading(false);

    }

  }

  useEffect(() => {

    loadUsers();

  }, []);

  function handleCreate() {

    setSelectedUser(null);

    setOpen(true);

  }

  function handleEdit(
    user: User
  ) {

    setSelectedUser(user);

    setOpen(true);

  }

  async function handleSave(
    data: any
  ) {

    try {

      if (selectedUser) {

        await updateUser(
          selectedUser.id,
          data
        );

      } else {

        await createUser(data);

      }

      setOpen(false);

      setSelectedUser(null);

      await loadUsers();

    } catch (error) {

      console.error(error);

      alert(
        "No fue posible guardar el usuario."
      );

    }

  }

  async function handleDelete(
    user: User
  ) {

    const confirmed = window.confirm(
      `¿Desea eliminar el usuario "${user.first_name} ${user.last_name}"?`
    );

    if (!confirmed) {
      return;
    }

    try {

      await deleteUser(user.id);

      await loadUsers();

    } catch (error) {

      console.error(error);

      alert(
        "No fue posible eliminar el usuario."
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

          <h1>Users</h1>

          <p>
            Administración de usuarios.
          </p>

        </div>

        <Button onClick={handleCreate}>

          + Nuevo Usuario

        </Button>

      </div>

      <hr />

      {loading && (
        <p>Cargando usuarios...</p>
      )}

      {!loading && error && (

        <p style={{ color: "red" }}>
          {error}
        </p>

      )}

      {!loading && !error && (

        <UsersTable
          users={users}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />

      )}

      <Modal
        open={open}
        title={
          selectedUser
            ? "Editar Usuario"
            : "Nuevo Usuario"
        }
        onClose={() => {

          setOpen(false);

          setSelectedUser(null);

        }}
      >

        <UserForm
          initialData={selectedUser}
          onSave={handleSave}
          onCancel={() => {

            setOpen(false);

            setSelectedUser(null);

          }}
        />

      </Modal>

    </>
  );

}