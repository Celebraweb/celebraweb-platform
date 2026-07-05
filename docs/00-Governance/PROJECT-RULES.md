---
id: CW-110
code: CW-110
title: Project Rules
version: 1.1.0
status: APPROVED
classification: INTERNAL

owner: Enterprise Architecture

created: 2026-07-01
updated: 2026-07-03

repository: docs/00-Governance/PROJECT-RULES.md

references:
  - PROJECT.yaml
  - CW-500
  - CW-120
---

# CW-110 - Project Rules

**Proyecto:** CelebraWeb Platform

## Propósito

Este documento contiene las reglas oficiales aprobadas para la gestión y desarrollo del proyecto CelebraWeb.

---

# RG-001

## El chat no es la memoria del proyecto

**Estado:** Aprobada

**Fecha:** 2026-07-01

### Regla

Toda decisión aprobada por el Product Owner debe registrarse inmediatamente en la documentación oficial correspondiente antes de continuar con el desarrollo.

El chat es un espacio de trabajo.

La documentación del repositorio es la memoria oficial del proyecto.

### Implicaciones

- Ninguna decisión aprobada permanecerá únicamente en el chat.
- El PMO deberá identificar el documento que debe actualizar.
- Solo después del registro podrá continuar el desarrollo.

---

# RG-002

## El PMO es una herramienta de apoyo

**Estado:** Aprobada

**Fecha:** 2026-07-01

### Regla

El CW PMO es una herramienta de apoyo para la gestión y documentación del proyecto.

No hace parte del producto CelebraWeb.

Su objetivo es automatizar tareas administrativas y preservar el conocimiento del proyecto.

---

# RG-003

## Inicio obligatorio del Sprint

**Estado:** Aprobada

**Fecha:** 2026-07-01

### Regla

Antes de iniciar cualquier Sprint, el PMO deberá leer y validar la documentación oficial del proyecto.

Como mínimo:

- PROJECT.yaml
- Engineering Handbook
- Sprint Summary anterior
- Artifacts
- Project Rules
- Decision Log

Si encuentra inconsistencias deberá informar al Product Owner antes de continuar.

---

# RG-004

## Metodología de implementación

**Estado:** Aprobada

**Fecha:** 2026-07-02

### Regla

Cuando el Product Owner solicite modificaciones de archivos, el Arquitecto entregará siempre archivos completos con su ruta exacta.

No se utilizarán fragmentos de código, instrucciones parciales, referencias del tipo "agrega", "inserta", "busca" o "...".

### Implicaciones

- Cada modificación corresponderá a un archivo completo.
- Se indicará siempre la ruta completa del archivo.
- El procedimiento será: reemplazar, guardar y probar.
- Esta metodología busca reducir el riesgo de errores durante la implementación.

---

# RG-005

## La Constitución gobierna el producto

**Estado:** Aprobada

**Fecha:** 2026-07-03

### Regla

La Constitución Empresarial (CW-000) constituye la máxima autoridad funcional y arquitectónica del producto CelebraWeb.

Toda decisión de diseño, implementación o evolución del producto deberá mantener trazabilidad con la Constitución.

### Implicaciones

- Ninguna funcionalidad podrá contradecir la Constitución.
- La Arquitectura Empresarial deberá alinearse con la visión definida en CW-000.
- En caso de conflicto prevalecerá la Constitución.

---

# RG-006

## El Enterprise Knowledge System es la única fuente oficial de conocimiento

**Estado:** Aprobada

**Fecha:** 2026-07-03

### Regla

El Enterprise Knowledge System (EKS) constituye la única fuente oficial de conocimiento permanente del proyecto.

Las decisiones aprobadas deberán preservarse en el EKS y no depender del historial de conversaciones.

### Implicaciones

- Las conversaciones son espacios de trabajo.
- La documentación oficial constituye la memoria del proyecto.
- El PMO garantizará la sincronización del conocimiento.

---

# RG-007

## Desarrollo guiado por Arquitectura Empresarial

**Estado:** Aprobada

**Fecha:** 2026-07-03

### Regla

Toda funcionalidad implementada deberá derivarse de una Business Capability identificada dentro de la Arquitectura Empresarial.

No se desarrollarán funcionalidades aisladas sin una capacidad empresarial que las justifique.

### Implicaciones

Toda historia de usuario deberá mantener trazabilidad con:

- Constitución Empresarial.
- Dominio Empresarial.
- Business Capability.
- Proceso de Negocio.

---

# RG-008

## El diseño empresarial precede al diseño técnico

**Estado:** Aprobada

**Fecha:** 2026-07-03

### Regla

Antes de iniciar el diseño técnico de cualquier funcionalidad deberán identificarse como mínimo:

- Dominio Empresarial.
- Business Capability.
- Proceso de Negocio relacionado.

La arquitectura de software será consecuencia del diseño empresarial.

### Implicaciones

- No se iniciará el desarrollo por pantallas o tablas.
- El software implementará capacidades de negocio.
- La trazabilidad deberá mantenerse durante todo el ciclo de vida del producto.

---

# RG-009

## Decisiones Arquitectónicas

**Estado:** Aprobada

**Fecha:** 2026-07-03

### Regla

Las decisiones arquitectónicas permanentes deberán preservarse mediante el mecanismo oficial definido por el Enterprise Knowledge System.

Hasta la implementación del repositorio de Architecture Decision Records (ADR), dichas decisiones deberán registrarse en la documentación oficial aprobada por el Product Owner.

### Implicaciones

- Ninguna decisión arquitectónica importante permanecerá únicamente en el chat.
- El Enterprise Architect será responsable de identificar el documento oficial donde debe preservarse la decisión.