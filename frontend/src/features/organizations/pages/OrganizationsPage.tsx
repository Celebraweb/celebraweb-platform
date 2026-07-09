import { useEffect, useState } from "react";

import Button from "@/components/ui/Button";
import Modal from "@/components/ui/Modal";

import type { Organization } from "../types/organization";

import {
  getOrganizations,
  createOrganization,
  updateOrganization,
  deleteOrganization,
} from "../services/organization.service";

import OrganizationsTable from "../components/OrganizationsTable";
import OrganizationForm from "../components/OrganizationForm";

export default function OrganizationsPage() {
  const [organizations, setOrganizations] = useState<Organization[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [open, setOpen] = useState(false);

  const [selectedOrganization, setSelectedOrganization] =
    useState<Organization | null>(null);

  async function loadOrganizations() {
    try {
      const data = await getOrganizations();

      setOrganizations(data);

      setError("");
    } catch (err) {
      console.error(err);

      setError(
        "No fue posible consultar las organizaciones."
      );
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadOrganizations();
  }, []);

  function handleCreate() {
    setSelectedOrganization(null);
    setOpen(true);
  }

  function handleEdit(
    organization: Organization
  ) {
    setSelectedOrganization(organization);
    setOpen(true);
  }

  async function handleSave(data: any) {
    try {

      if (selectedOrganization) {

        await updateOrganization(
          selectedOrganization.id,
          data
        );

      } else {

        await createOrganization(data);

      }

      setOpen(false);
      setSelectedOrganization(null);

      await loadOrganizations();

    } catch (err) {

      console.error(err);

      alert(
        "No fue posible guardar la organización."
      );
    }
  }

  async function handleDelete(
    organization: Organization
  ) {

    const confirmed = window.confirm(
      `¿Desea eliminar la organización "${organization.name}"?`
    );

    if (!confirmed) {
      return;
    }

    try {

      await deleteOrganization(
        organization.id
      );

      await loadOrganizations();

    } catch (err) {

      console.error(err);

      alert(
        "No fue posible eliminar la organización."
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
          <h1>Organizations</h1>

          <p>
            Administración de organizaciones de la plataforma.
          </p>
        </div>

        <Button
          onClick={handleCreate}
        >
          + Nueva Organización
        </Button>
      </div>

      <hr />

      {loading && (
        <p>Cargando organizaciones...</p>
      )}

      {!loading && error && (
        <p
          style={{
            color: "red",
          }}
        >
          {error}
        </p>
      )}

      {!loading && !error && (
        <OrganizationsTable
          organizations={organizations}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      )}

      <Modal
        open={open}
        title={
          selectedOrganization
            ? "Editar Organización"
            : "Nueva Organización"
        }
        onClose={() => {
          setOpen(false);
          setSelectedOrganization(null);
        }}
      >
        <OrganizationForm
          initialData={selectedOrganization}
          onSave={handleSave}
          onCancel={() => {
            setOpen(false);
            setSelectedOrganization(null);
          }}
        />
      </Modal>
    </>
  );
}