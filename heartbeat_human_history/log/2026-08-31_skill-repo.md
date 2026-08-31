# Session `2026-08-31-skill-repo`

```
id:          2026-08-31-skill-repo
agent:       Grok 4.6
started:     2026-08-31T00:42:00Z
ended:       2026-08-31T00:50:00Z
activity:    repo-push
protocol:    heartbeat.v1.1
```

## Intent

Crear un repositorio GitHub dedicado solo al skill portable `sota-agent-heartbeat`.

## Chain

```
prev_session_id: 2026-08-31-github-skill-zip
prev_sha256:     5928ce641c95065e48cf671c0f45f532ea2a0f38fff21b296dee281629859e39
```

## Used (prov:used)

```
- role: skill
  path: skills/sota-agent-heartbeat/
  why:  fuente genérica v1.2.0, sin invariantes de Historia
- role: protocol
  path: heartbeat_human_history/HEARTBEAT.json
  why:  pulso previo y cadena
```

## Generated (prov:generated)

```
- role: skill
  path: https://github.com/ManuelCadena/sota-agent-heartbeat
  change: add
- role: skill
  path: https://github.com/ManuelCadena/sota-agent-heartbeat/issues/1
  change: docs
```

## Evidence

Vacío. Sesión de repo-push / docs, no muta el corpus.

## Complements

El skill portable vive ahora en su propio repo. El corpus sigue en Matematica-de-la-humanidad. No se sustituyen.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] `flat` reconstruido si se tocó el árbol
- [ ] `python docs/referencia_modelos.py` → selftest ok (si aplica)
- [ ] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok
- [x] conteos del pulso = `meta` atestado, no memoria del agente

## Counts (solo si tocaste corpus)

No se tocó el corpus.

```
cronologia n_nodes: 2259
ontologia n_nodos: 2485
sim_meta n_conos: 81
origenes species/sites/migrations/admixture/anclas: 37/38/14/7/9
```

## Pending left for the next agent

- Subir `scripts/init_heartbeat.py` y `scripts/validate_heartbeat.py` a ManuelCadena/sota-agent-heartbeat (lock de escritura del conector tras el commit de docs).
- Tag `v1.2.0` cuando los scripts estén en main.
- Push restante del corpus a Matematica-de-la-humanidad (SPEC_03-05 íntegros, JSON grandes).
- Taladro dinástico restante por región (no inventar nodos).

## Notes

Repo público creado: https://github.com/ManuelCadena/sota-agent-heartbeat (id 1351849691).
main en d083a4be: SKILL.md, README, LICENSE, CHANGELOG, assets/, references/, examples/, .gitignore.
No se subió HEARTBEAT.json al skill repo (correcto: el pulso nace en el destino).
Issue #1 documenta los scripts pendientes.
Zip local intacto: artifacts/sota-agent-heartbeat.zip sha256 b0abb98b1c1cb17f9dde0738463c404e98e87099f243fe85587e7d17635e14a7.
Status del pulso de Historia permanece `degraded` (GitHub del corpus sigue atrasado).
