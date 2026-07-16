---
id: CW-144
code: CW-144
title: Technical Debt
version: 1.0.0
status: APPROVED
classification: INTERNAL

owner: PMO

created: 2026-07-16
updated: 2026-07-16

repository: docs/00-Governance/CW-144-Technical-Debt.md

references:
  - PROJECT.yaml
  - CW-130
  - CW-131
  - CW-500
---

# CW-144 – Technical Debt

# Propósito

Registrar de forma centralizada la deuda técnica identificada durante la evolución del proyecto CelebraWeb.

La deuda técnica representa implementaciones funcionales que requieren refactorización, optimización o mejora futura, sin impedir la operación actual del producto.

Es un documento vivo administrado por el CW PMO.

---

# Objetivos

- Centralizar la deuda técnica del proyecto.
- Priorizar actividades de mejora.
- Mantener la calidad arquitectónica.
- Facilitar la planificación de futuros Sprint.
- Servir como entrada del comando `review`.

---

# Prioridades

| Prioridad | Descripción |
|------------|-------------|
| Critical | Debe resolverse inmediatamente |
| High | Resolver en los próximos Sprint |
| Medium | Resolver cuando exista capacidad |
| Low | Mejora deseable |

---

# Estados

| Estado | Descripción |
|---------|-------------|
| OPEN | Pendiente |
| IN PROGRESS | En ejecución |
| RESOLVED | Implementada |
| CANCELLED | Descartada |

---

# Registro de Technical Debt

| ID | Fecha | Componente | Descripción | Prioridad | Sprint objetivo | Estado | Observaciones |
|----|-------|------------|-------------|-----------|-----------------|--------|---------------|

---

# Reglas

- Toda deuda técnica deberá registrarse.
- Ningún registro será eliminado; únicamente cambiará su estado.
- La resolución de una deuda técnica deberá quedar registrada en el Sprint correspondiente.

---

# Integración con el PMO

Este documento es utilizado por:

- review
- start
- close

para identificar la deuda técnica vigente antes del inicio de cada Sprint.