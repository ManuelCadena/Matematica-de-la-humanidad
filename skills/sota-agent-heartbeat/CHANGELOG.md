# Changelog

All notable changes to this portable skill. Format:
[Keep a Changelog](https://keepachangelog.com/).

## [1.2.0] - 2026-08-31

### Added

- Root `README.md` so the unzipped folder is usable without reading
  `SKILL.md` first.
- `references/protocol.md` — generic contract an agent must keep.
- `validate_heartbeat.py --write-pulse` writes measured attestation
  into `HEARTBEAT.json` instead of only printing it.
- `init_heartbeat.py --copy-skill` copies this package into
  `skills/sota-agent-heartbeat/` of the target repo.
- Config `disjoint` pairs executed by the validator.
- `examples/minimal/` — tiny dataset so init+validate can be demoed
  without a real corpus.

### Changed

- Session template activities are project-agnostic
  (`add`/`fix` instead of history-only verbs).
- Schema documents `attestation` and `chain` as required on v1.1.

### Fixed

- Genesis scaffold writes both `log/INDEX.md` and `log/genesis.md`.
- Init no longer overwrites a non-empty `AGENTS.md`.

## [1.1.0] - 2026-08-31

### Added

- Protocol heartbeat.v1.1: claimed vs attested counts, sha256
  session chain, config-driven invariants, typed roles.
- `init_heartbeat.py` and `validate_heartbeat.py`.
- assets: schema, example config, session template.
