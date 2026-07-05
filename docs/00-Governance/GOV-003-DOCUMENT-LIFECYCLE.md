---
id: GOV-003
code: GOV-003
title: Document Lifecycle
version: 1.0.0
status: APPROVED
classification: INTERNAL

owner: Product Owner
architect: Enterprise Architect

created: 2026-06-30
updated: 2026-06-30

parent: GOV-001

domain: Governance

repository: docs/00-Governance/GOV-003-DOCUMENT-LIFECYCLE.md

tags:
  - governance
  - documentation
  - lifecycle

references:
  - GOV-001
  - GOV-002
  - CW-000
---

# GOV-003 — Document Lifecycle

---

# Propósito

Este documento define el ciclo de vida oficial de todos los documentos pertenecientes al Enterprise Knowledge System (EKS) de CelebraWeb.

Su objetivo es garantizar que cada documento siga un proceso uniforme de creación, revisión, aprobación, publicación, mantenimiento y retiro.

---

# Objetivos

- Estandarizar el ciclo de vida documental.
- Garantizar la trazabilidad.
- Facilitar el gobierno documental.
- Mantener la calidad de la documentación.
- Evitar documentos huérfanos u obsoletos.

---

# Ciclo de Vida

Todo documento del Enterprise Knowledge System deberá atravesar las siguientes etapas.

## 1. Propuesta

El documento ha sido identificado como necesario.

Características:

- Código reservado.
- Sin contenido definitivo.
- No hace parte del EKS oficial.

Estado:

```text
PROPOSED
```

---

## 2. Borrador

Se desarrolla el contenido inicial.

Características:

- Puede modificarse libremente.
- Aún no posee aprobación formal.

Estado:

```text
DRAFT
```

---

## 3. Revisión

El documento entra en revisión técnica y funcional.

Actividades:

- Validación de estructura.
- Revisión arquitectónica.
- Revisión funcional.
- Revisión documental.

Estado:

```text
IN REVIEW
```

---

## 4. Aprobación

El documento recibe aprobación oficial.

Requiere:

- Enterprise Architect.
- Product Owner.

Estado:

```text
APPROVED
```

---

## 5. Publicación

El documento se incorpora oficialmente al repositorio.

Debe cumplir:

- Versionado.
- Metadata completa.
- Registro en DOCUMENT-INDEX.
- Commit en Git.

Estado:

```text
PUBLISHED
```

---

## 6. Mantenimiento

El documento continúa vigente.

Podrá recibir:

- Correcciones.
- Mejoras.
- Nuevas versiones.

Toda modificación deberá conservar la trazabilidad.

Estado:

```text
ACTIVE
```

---

## 7. Obsolescencia

El documento deja de utilizarse.

No podrá eliminarse.

Será marcado como:

```text
DEPRECATED
```

Mantendrá su historial completo.

---

## 8. Archivo

El documento se conserva únicamente con fines históricos.

Estado:

```text
ARCHIVED
```

---

# Estados Oficiales

| Estado | Significado |
|---------|-------------|
| PROPOSED | Propuesto |
| DRAFT | En elaboración |
| IN REVIEW | En revisión |
| APPROVED | Aprobado |
| PUBLISHED | Publicado |
| ACTIVE | Vigente |
| DEPRECATED | Obsoleto |
| ARCHIVED | Archivado |

---

# Reglas

Todo documento deberá:

- tener un código único;
- tener un propietario;
- indicar versión;
- indicar estado;
- estar registrado en DOCUMENT-INDEX;
- mantenerse bajo control de versiones.

---

# Transiciones Permitidas

```text
PROPOSED
      │
      ▼
DRAFT
      │
      ▼
IN REVIEW
      │
      ▼
APPROVED
      │
      ▼
PUBLISHED
      │
      ▼
ACTIVE
      │
      ├──────────────┐
      ▼              │
DEPRECATED           │
      │              │
      ▼              │
ARCHIVED ◄───────────┘
```

---

# Gobierno

Toda transición de estado deberá quedar registrada mediante:

- Git.
- Historial documental.
- DOCUMENT-INDEX.
- PROJECT-STATUS (cuando aplique).

---

# Definition of Done

Un documento solo podrá considerarse **terminado** cuando:

- Está aprobado.
- Existe físicamente en el repositorio.
- Está registrado en DOCUMENT-INDEX.
- Tiene versión.
- Tiene metadata completa.
- Se encuentra bajo control de versiones.
- Ha sido publicado mediante Git.

---

# Conclusión

El ciclo de vida documental garantiza que el Enterprise Knowledge System evolucione de manera disciplinada, manteniendo la trazabilidad, la calidad y la gobernanza de todos los activos documentales de CelebraWeb.