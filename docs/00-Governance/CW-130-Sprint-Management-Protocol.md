---
id: CW-130
code: CW-130
title: Sprint Management Protocol
version: 1.1.0
status: APPROVED
classification: INTERNAL

owner: PMO

created: 2026-07-02
updated: 2026-07-02

repository: docs/00-Governance/CW-130-Sprint-Management-Protocol.md

references:
  - PROJECT.yaml
  - CW-110
  - CW-120
  - CW-500
---

# CW-130 - Sprint Management Protocol

## Historial de Versiones

| Versión | Fecha | Descripción |
|----------|------------|----------------------------------------------|
| 1.0.0 | 2026-07-02 | Versión inicial |
| 1.1.0 | 2026-07-02 | Se incorpora la ceremonia Generate y la automatización documental |

---

# Propósito

Definir el procedimiento oficial para la administración de los Sprint del proyecto CelebraWeb utilizando el CW PMO.

Este protocolo es de cumplimiento obligatorio durante todo el ciclo de vida del proyecto.

---

# Flujo Oficial del Sprint

REVIEW

↓

START

↓

DESARROLLO

↓

GENERATE

↓

SYNC

↓

VALIDATE

↓

CLOSE

↓

REVIEW

---


# Ceremonia 0 - Review

## Momento

Antes de iniciar oficialmente un nuevo Sprint.

## Comando

```powershell
python tools/cw_pmo/main.py review
```

## Objetivos

Reconstruir automáticamente el contexto del proyecto mediante la lectura de:

- PROJECT.yaml
- Decision Log
- Product Backlog
- Sprint Review
- Sprint Retrospective
- Open Issues
- Technical Debt
- Sprint Summary del Sprint anterior

El resultado de esta ceremonia será el contexto oficial del Sprint que inicia.

# Ceremonia 1 - Inicio del Sprint

## Momento

Antes de iniciar cualquier actividad del Sprint.

## Comando

```powershell
python tools/cw_pmo/main.py start
```

## Objetivos

- Abrir automáticamente el siguiente Sprint cuando el anterior esté cerrado.
- Reconstruir el contexto del proyecto.
- Leer PROJECT.yaml.
- Validar la documentación obligatoria.
- Mostrar el estado del proyecto.
- Autorizar oficialmente el Sprint.
- Validar que la ceremonia Review haya sido ejecutada previamente.

---

# Ceremonia 2 - Desarrollo

Durante esta fase no se ejecutan comandos del PMO.

Todo el esfuerzo se concentra en implementar funcionalidades del producto.

---

# Ceremonia 3 - Generación Documental

## Momento

Al finalizar una historia o cuando sea necesario actualizar la documentación administrativa del Sprint.

## Comando

```powershell
python tools/cw_pmo/main.py generate
```

## Objetivos

- Generar automáticamente Sprint Summary.
- Garantizar la existencia de Artifacts.md.
- Actualizar la documentación administrativa del Sprint.
- Reducir la edición manual de documentos.

---

# Ceremonia 4 - Sincronización

## Momento

Cuando exista nueva documentación oficial generada por el PMO.

## Comando

```powershell
python tools/cw_pmo/main.py sync
```

## Objetivos

- Actualizar el Engineering Handbook.
- Sincronizar la documentación administrada por el PMO.
- Mantener consistencia documental.

---

# Ceremonia 5 - Validación

## Momento

Antes del cierre del Sprint.

## Comando

```powershell
python tools/cw_pmo/main.py validate
```

## Objetivos

Verificar:

- PROJECT.yaml
- Engineering Handbook
- Sprint Summary
- Artifacts
- Product Backlog
- Sprint Review
- Sprint Retrospective
- Open Issues
- Technical Debt

Si la validación falla, el Sprint no podrá cerrarse.

---

# Ceremonia 6 - Cierre del Sprint

## Momento

Después de aprobar la validación.

## Comando

```powershell
python tools/cw_pmo/main.py close
```

## Objetivos

El PMO realiza automáticamente:

- Generación documental.
- Backup del Engineering Handbook.
- Actualización del Handbook.
- Actualización del PROJECT.yaml.
- Cambio del estado del Sprint a Closed.
- Actualización de Product Backlog.
- Actualización de Sprint Review.
- Actualización de Sprint Retrospective.
- Actualización de Open Issues.
- Actualización de Technical Debt.

---

# Reglas Oficiales

## RG-005

Nunca se inicia un Sprint sin ejecutar:

```powershell
python tools/cw_pmo/main.py start
```

---

## RG-006

Nunca se ejecuta CLOSE sin haber aprobado previamente:

```powershell
python tools/cw_pmo/main.py validate
```

---

## RG-007

El estado del Sprint será administrado exclusivamente por el CW PMO.

No se modificará manualmente PROJECT.yaml.

---

## RG-008

El CW PMO es una herramienta administrativa de apoyo.

No hace parte del producto CelebraWeb.

Las mejoras del PMO deberán planificarse como backlog independiente.

---

## RG-009

La documentación administrativa del Sprint deberá generarse mediante:

```powershell
python tools/cw_pmo/main.py generate
```

antes de ejecutar la sincronización, validación y cierre del Sprint.

---

## RG-010

Nunca se inicia un Sprint sin ejecutar previamente:

```powershell
python tools/cw_pmo/main.py review
```

---

## RG-011

Los documentos Product Backlog, Sprint Review, Sprint Retrospective, Open Issues y Technical Debt constituyen la memoria viva del proyecto y deberán mantenerse actualizados durante todo el ciclo de vida de CelebraWeb.