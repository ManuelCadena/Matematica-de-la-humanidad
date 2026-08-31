# Sesión `2026-08-31-higiene-taladro-40`

```
id:          2026-08-31-higiene-taladro-40
agent:       Claude Fable 5
started:     2026-08-31T18:00:00Z
ended:       2026-08-31T19:10:00Z
activity:    add-node
protocol:    heartbeat.v1.1
```

## Intent

Ejecutar la higiene del corpus (precision fuera de enum, conos sin src trazable, divergencias cono-nodo) y taladrar handbook las cinco regiones subrepresentadas del pending #1.

## Chain

```
prev_session_id: 2026-08-31-repo-corpus-push
prev_sha256:     e7e4cfa0b3bede053624a13811912cd9f8eb1fdca0f8208895f1f08c5b6e6ec2
```

## Used (prov:used)

```
- role: protocol
  path: LLM.md
  why:  contrato de alta §6; invariantes §3
- role: corpus-meta
  path: datos/cronologia_mundial_arbol.json
  why:  inventario pre-inserción 2296; ids existentes por región
- role: corpus-meta
  path: datos/historia_ontologia.json
  why:  semántica de indices (por_siglo cap 40 buckets, lentes por kind)
- role: cone
  path: datos/sim_meta.json
  why:  16 conos con src no-id; 10+ divergencias de ventana
- role: skill
  path: skills/heartbeat-human-history/SKILL.md
  why:  protocolo de cierre v1.1
```

## Generated (prov:generated)

```
- role: corpus-meta
  path: datos/cronologia_mundial_arbol.json
  change: alta (+40 nodos, 2296→2336; fix precision poverty-point/shield-archaic/old-copper; v6.4.0-taladro)
- role: corpus-meta
  path: datos/cronologia_mundial_flat.jsonl
  change: alta (reconstruido por preorden desde trees)
- role: corpus-meta
  path: datos/historia_ontologia.json
  change: alta (+40 nodos con lentes, 2522→2562; indices incrementales; v7.3.0-taladro)
- role: corpus-meta
  path: datos/ontologia_nodos.jsonl
  change: alta (regenerado desde nodos)
- role: cone
  path: datos/sim_meta.json
  change: correccion (16 conos con src_ids verificados contra el árbol; src_note conserva descriptor; 20 conos con note capital≠polidad)
- role: derived-artefact
  path: heartbeat_human_history/HEARTBEAT.json
  change: pulse
```

## Evidence

```
- source: Ortmann & Kidder 2013, Geoarchaeology
  supports: poverty-point precision→century
- source: Wright 1972 (Shield Archaic); Pompeani et al. 2021, Radiocarbon (Old Copper)
  supports: shield-archaic / old-copper precision→millenium
- source: Belich 1986, The New Zealand Wars
  supports: nz-wars 1845–1872
- source: O'Malley 2016; Te Ara Encyclopedia of New Zealand
  supports: kingitanga desde 1858
- source: Kuykendall 1938, The Hawaiian Kingdom I
  supports: ai-noa-1819 (abolición del kapu, nov. 1819)
- source: Lātūkefu 1974, Church and State in Tonga
  supports: tonga-tupou 1845 (constitución 1875)
- source: Scarr 1984, Fiji: A Short History
  supports: fiji-cession-1874
- source: Garanger 1972; UNESCO WHC 2008 (Chief Roi Mata's Domain)
  supports: roy-mata 1250–1650 precision debated (C14 s. XIII vs revisión ~1600)
- source: Fischer 2005, Island at the End of the World; Routledge 1919
  supports: huri-moai 1722–1868; tangata-manu (última competencia ~1866–67)
- source: Saunders et al. 1997, Science 277
  supports: watson-brake −3500…−2800 (~5400–5000 cal BP)
- source: Tuck 1976 (Maritime Archaic); Kidder 1927 (clasificación de Pecos)
  supports: maritime-archaic; basketmaker
- source: Birmingham & Eisenberg 2000, Indian Mounds of Wisconsin
  supports: effigy-mounds 650–1200
- source: Seaver 1996; Kuitems et al. 2021, Nature 601 (AD 1021)
  supports: norse-greenland 985–1450; lanse-aux-meadows 1000–1030
- source: Rasmussen et al. 2010, Nature 463; Knuth 1954
  supports: saqqaq; independence-i
- source: Pauketat 2004, Ancient Cahokia; Williams 1990; Cobb & Butler 2002, American Antiquity
  supports: cahokia-lohmann; cahokia-moorehead; vacant-quarter (debated)
- source: Denbow 1986; Fagan 1969 (Ingombe Ilede); Posnansky 1969 (Bigo)
  supports: toutswe; ingombe-ilede; bigo-cwezi (asociación Bachwezi émica, debated)
- source: Omer-Cooper 1966; Hamilton 1998; Cobbing 1988, J. African History
  supports: mthethwa; ndwandwe; mfecane 1815–1840 (debate historiográfico en notes)
- source: Kent 1970, Early Kingdoms in Madagascar
  supports: sakalava 1650–1896
- source: Abun-Nasr 1987, A History of the Maghrib; al-Bakri
  supports: wattasid 1472–1554; barghawata 744–1058; nekor 710–1019
- source: Frend 1952, The Donatist Church
  supports: donatism 311–650 (lentes religioso+historico)
- source: Fredegario IV.48; Curta 2006; Golden 1992; Róna-Tas 1999
  supports: samo-realm; pechenegs; cumania; magyar-conquest
- source: Herrmann 1985 (obodritas); Carter 1972 (Ragusa); Šmahel / Fudge 2002 (husitas)
  supports: obodrites; ragusa 1358–1808; hussite-wars 1419–1436
- source: Bethell, Cambridge History of Latin America; Fausto 1999
  supports: brazil-empire 1822–1889; brazil-rep 1889–2026 (trazabilidad del cono rio)
```

## Complements

Taladro extiende la capa 1 (fibrado) en cinco regiones sin tocar la capa 0.5 ni los 81 conos existentes (no se creó cono nuevo; species/site nuevos —watson-brake, roy-mata, etc.— NO entran a sim_meta). `src_ids` en sim_meta restaura la trazabilidad cono→árbol exigida por LLM.md §6 sin cambiar ninguna ventana [t0,t1].

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
- [x] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok
- [x] conteos del pulso = `meta` atestado, no memoria del agente

## Counts (solo si tocaste corpus)

```
cronologia n_nodes: 2336
ontologia n_nodos: 2562
sim_meta n_conos: 81
origenes species/sites/migrations/admixture/anclas: 37/41/14/7/9
```

## Pending left for the next agent

- brazil-empire / brazil-rep alojados en árbol andes por ausencia de árbol atlántico sudamericano: decidir si se crea árbol/región propia (afecta enum R y adyacencia).
- Acople kush→egypt (conquest, Dinastía XXV, Piye ~−744) detectado como hueco bien documentado: no se dio de alta en esta sesión (fuera de alcance); primero de la cola de los 197 pares vacíos.
- Divergencias cono-nodo ahora anotadas genéricamente; refinar nota por cono (p. ej. meroe: cono = fase meroítica, nodo = Kush completo).
- paris-mod: src_ids cubren 1589–1815; rama de la Francia posterior a 1815 sin nodo dedicado en el árbol (hueco declarado en src_note).
- Taladro pendiente aún: Sahul profundo en árbol oceania (la capa 0.5 lo cubre), Norteamérica subártica, África centro-sur pre-900.

## Notes

40 altas: oceania 8, am-north 11, af-cs 7, maghreb 4, eu-east 8, andes-atlántico 2. Ningún señorío inventado: cada nodo cita handbook o paper en `notes`. Tres nodos con `precision: debated` donde la disputa es real (roy-mata, tangata-manu, vacant-quarter, bigo-cwezi). Índices actualizados incrementalmente replicando semántica observada (por_siglo: cubos de siglo, tope 40 por nodo). Re-auditoría post-cambio: 0 duplicados, 0 start>end, 0 precision fuera de enum, 0 conos huérfanos, 0 src_ids inválidos.
