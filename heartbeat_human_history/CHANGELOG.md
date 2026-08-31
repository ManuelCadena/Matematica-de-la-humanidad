# Changelog

Cambios notables del corpus y del protocolo. Formato [Keep a Changelog](https://keepachangelog.com/).
Versiones del árbol/ontología viven en `meta.version` de cada JSON.

## [Unreleased]

### Added

- Protocolo `heartbeat.v1.1`: `attestation` (conteos medidos + sha256
  de 9 JSON), `chain` (sesión previa + sha256), invariantes
  ejecutables (Teotihuacan `[-100,650]`, origin-kind ∩ conos = ∅).
- `validate_heartbeat.py --write-attestation`.
- Plantilla de sesión con roles tipados y evidencia obligatoria
  en `add-node|add-origin|fix-date|add-cone`.
- `heartbeat_human_history/` — pulso, schema, log de sesiones, protocolo.
- `AGENTS.md` — ToC para agentes (estándar AAIF).
- Skill `heartbeat-human-history` (agentskills.io).

### Fixed

- Pulso: `sim_meta.n_conos` 42 → 81 (archivo real, years −4000…2026).
- Pulso y nota de capa 0.5: homininos 31 → 37, yacimientos 57 → 38,
  migraciones 13 → 14 (leídos de `datos/origenes/*.json` `meta.n`).
- Sesión `2026-08-30-consensus-verify` audita el diseño contra
  literatura Consensus 2025–2026.

## [6.2.1-origenes / 7.1.1-origenes] - 2026-08-30

### Added

- Capa 0.5: `datos/origenes/{homininos,migraciones,yacimientos,introgresion}.json`.
- SPEC_05. 37 homininos, 38 yacimientos, 14 pulsos, 7 introgresiones
  (counts del pulso inicial 31/57/13 eran cache obsoleto; corregido
  2026-08-30-consensus-verify).
- Dimensión constitutiva `hominina`.
- `LLM.md` contrato de máquina.

### Changed

- Árbol 2182 → 2259 nodos. Ontología 2403 → 2485.
- `hominina.end` extendido a 2026 (incluye *Homo*).
- Habilís y rudolfensis separados; Paranthropus partido en tres.

### Fixed

- Hijos de sapiens / afarensis / erectus que un upsert vacío había borrado.
- IDs duplicados yangshao, longshan, erlitou, lapita-spread, polynesian-triangle.
