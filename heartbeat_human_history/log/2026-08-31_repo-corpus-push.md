# Session `2026-08-31-repo-corpus-push`

```
id:          2026-08-31-repo-corpus-push
agent:       Grok 4.6
started:     2026-08-31T01:34:00Z
ended:       2026-08-31T01:42:00Z
activity:    repo-push
protocol:    heartbeat.v1.1
```

## Intent

Subir a github.com/ManuelCadena/Matematica-de-la-humanidad absolutamente todo lo que el proyecto usa.

## Chain

```
prev_session_id: 2026-08-31-gaps-v7
prev_sha256:     3586fbe8a5b98f5929532692ba6080e81c2c7ee7a918688a316d492e7b3104c2
```

## Used (prov:used)

```
- role: corpus-meta
  path: datos/cronologia_mundial_arbol.json
- role: protocol
  path: LLM.md
```

## Generated (prov:generated)

```
- role: other
  path: datos/schemas/nodo.schema.json
  change: docs
- role: other
  path: scripts/pack_ontologia.py
  change: docs
- role: protocol
  path: docs/SPEC_03_FIBRAS_ACOPLES.md
  change: docs
```

## Evidence

```
```

## Complements

Remote main @ 99297a35. No se tocó Teotihuacan ni sim_meta.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] `flat` reconstruido si se tocó el árbol
- [x] `python docs/referencia_modelos.py` → selftest ok
- [ ] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok
- [x] conteos del pulso = `meta` atestado, no memoria del agente

## Counts

```
cronologia n_nodes: 2296
ontologia n_nodos: 2522
sim_meta n_conos: 81
origenes species/sites/migrations/admixture/anclas: 37/41/14/7/9
```

## Pending left for the next agent

- Empujar JSON canónicos a GitHub (árbol compacto 852 KB sí cabe; ontología pretty 1.82 MB no — usar compacta sin índices 722 KB o jsonl+packer).
- Reemplazar stubs SPEC_04 (438 B) y SPEC_05 (497 B) por textos locales (5.1 KB / 8.3 KB).
- Subir origenes/, sim_meta, fibras, acoples, app/, modelo/, heartbeat actual, media.
- video_cgi_globo_conos.mp4 = 4.2 MB: Contents API no lo acepta; Release asset o git local.
- Connector GitHub quedó en lock «another agent already completed» tras SPEC_03.

## Notes

No afirmar que el repo está completo. Workspace local sigue siendo la fuente de verdad.
