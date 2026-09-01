#!/usr/bin/env python3
"""Genera los entregables del documental matemático de la humanidad.

Lee el corpus actual del repositorio, georreferencia las 16 regiones,
produce por capítulo datos medidos, figuras, un video 1080p60 y
un HTML consolidado final.
"""
from __future__ import annotations

import json
import math
import os
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

BASE = Path(__file__).resolve().parent.parent
MEDIA = BASE / "media"
APP = BASE / "app"
DATOS = BASE / "datos"
DOCS = BASE / "docs"

sys.path.insert(0, str(DOCS))
import referencia_modelos as ref  # noqa

D = ref.D
REGION_IDS = [
    "am-north",
    "meso",
    "andes",
    "af-west",
    "af-nile",
    "af-cs",
    "maghreb",
    "eu-west",
    "eu-east",
    "near-east",
    "iran-steppe",
    "sasia",
    "easia",
    "seasia",
    "oceania",
    "humanidad",
]

# ============================================================
# 1. Georreferenciación aproximada (proyección de investigación)
# ============================================================
REGIONES = {
    "am-north": {
        "centroide": [-100.0, 45.0],
        "poligono": [[-130, 25], [-80, 25], [-60, 55], [-130, 55], [-130, 25]],
    },
    "meso": {
        "centroide": [-92.0, 18.0],
        "poligono": [[-105, 14], [-85, 14], [-80, 22], [-100, 22], [-105, 14]],
    },
    "andes": {
        "centroide": [-72.0, -15.0],
        "poligono": [[-80, -35], [-60, -35], [-60, 5], [-80, 5], [-80, -35]],
    },
    "af-west": {
        "centroide": [-5.0, 12.0],
        "poligono": [[-17, 4], [7, 4], [7, 20], [-17, 20], [-17, 4]],
    },
    "af-nile": {
        "centroide": [35.0, 20.0],
        "poligono": [[25, 10], [45, 10], [45, 30], [25, 30], [25, 10]],
    },
    "af-cs": {
        "centroide": [25.0, -18.0],
        "poligono": [[10, -35], [40, -35], [40, -5], [10, -5], [10, -35]],
    },
    "maghreb": {
        "centroide": [5.0, 32.0],
        "poligono": [[-10, 25], [20, 25], [20, 40], [-10, 40], [-10, 25]],
    },
    "eu-west": {
        "centroide": [2.0, 47.0],
        "poligono": [[-10, 36], [15, 36], [15, 60], [-10, 60], [-10, 36]],
    },
    "eu-east": {
        "centroide": [28.0, 50.0],
        "poligono": [[18, 42], [40, 42], [40, 60], [18, 60], [18, 42]],
    },
    "near-east": {
        "centroide": [42.0, 34.0],
        "poligono": [[35, 28], [50, 28], [50, 42], [35, 42], [35, 28]],
    },
    "iran-steppe": {
        "centroide": [62.0, 36.0],
        "poligono": [[45, 25], [80, 25], [80, 48], [45, 48], [45, 25]],
    },
    "sasia": {
        "centroide": [78.0, 22.0],
        "poligono": [[68, 8], [90, 8], [90, 35], [68, 35], [68, 8]],
    },
    "easia": {
        "centroide": [108.0, 35.0],
        "poligono": [[95, 20], [125, 20], [125, 45], [95, 45], [95, 20]],
    },
    "seasia": {
        "centroide": [115.0, 12.0],
        "poligono": [[95, -10], [135, -10], [135, 25], [95, 25], [95, -10]],
    },
    "oceania": {
        "centroide": [140.0, -25.0],
        "poligono": [[110, -45], [170, -45], [170, -5], [110, -5], [110, -45]],
    },
    "humanidad": {
        "centroide": [0.0, 0.0],
        "poligono": [[-180, -90], [180, -90], [180, 90], [-180, 90], [-180, -90]],
    },
}

for rid in REGION_IDS:
    REGIONES[rid]["adyacencias"] = ref.ADJ.get(rid, [])

CENTROS_CONOS = json.loads((DATOS / "centros_conos.json").read_text())["centros"]

COLOR_POR_REGION = {
    "am-north": "#ff6b6b", "meso": "#ff9f43", "andes": "#feca57",
    "af-west": "#54a0ff", "af-nile": "#5f27cd", "af-cs": "#00d2d3",
    "maghreb": "#1dd1a1", "eu-west": "#48dbfb", "eu-east": "#0abde3",
    "near-east": "#ee5a24", "iran-steppe": "#f368e0", "sasia": "#ff9ff3",
    "easia": "#54a0ff", "seasia": "#5f27cd", "oceania": "#1dd1a1",
    "humanidad": "#ffffff",
}


def guardar_regiones():
    out = {"meta": {"tipo": "proyeccion_investigacion", "aviso": "R es un grafo historiografico; estas coordenadas son un anclaje cartografico opcional, no constante del modelo."}, "regiones": REGIONES}
    (DATOS / "regiones_geograficas.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

    md = [
        "# Regiones geográficas",
        "",
        "**Aviso metodológico**: `R` es el grafo de adyacencia historiográfico de 16 regiones",
        "definido en `modelo_espacio_tiempo.json` y `docs/referencia_modelos.py`.",
        "Los centroides y polígonos de este archivo son una proyección de investigación",
        "para anclar visualizaciones geográficas. No son una constante del modelo formal.",
        "",
    ]
    for rid in REGION_IDS:
        r = REGIONES[rid]
        md.append(f"## {rid}")
        md.append(f"- Centroide: `lon={r['centroide'][0]}, lat={r['centroide'][1]}`")
        md.append(f"- Adyacencias: {r['adyacencias']}")
        md.append(f"- Polígono aproximado: {len(r['poligono'])} vértices")
        md.append("")
    (DATOS / "regiones_geograficas.md").write_text("\n".join(md))


# ============================================================
# 2. Carga del corpus
# ============================================================
def cargar_datos():
    conos = json.loads((DATOS / "civilizaciones_fibras.json").read_text())
    nodos = [json.loads(l) for l in (DATOS / "ontologia_nodos.jsonl").read_text().splitlines() if l.strip()]
    nodos_dict = {n["id"]: n for n in nodos}
    acoples = json.loads((DATOS / "acoples_multicapa.json").read_text())
    return conos, nodos, nodos_dict, acoples


# ============================================================
# 3. Definición de capítulos
# ============================================================
SEGMENTOS = [
    {"cap": 0, "t0": -7000000, "t1": 2026, "title": "Introducción y metodología", "tagline": "Cómo leer la historia como fibrado espaciotemporal."},
    {"cap": "0.5", "t0": -2500000, "t1": -10000, "title": "Origen del ser humano", "tagline": "Homininos, sapiens, pulsos Out-of-Africa y la capa de especie."},
    {"cap": 1, "t0": -10000, "t1": -3000, "title": "Primeras lámparas", "tagline": "Neolítico, agricultura y las primeras sociedades asentadas."},
    {"cap": 2, "t0": -3000, "t1": 500, "title": "Ejes antiguos", "tagline": "Egipto, Mesopotamia, Valle del Indo, Shang, Olmeca/Maya Preclásico."},
    {"cap": 3, "t0": 500, "t1": 1500, "title": "Encuentros y solapes", "tagline": "Calzada de la Seda, Islam, imperios mongoles, Mesoamérica clásica."},
    {"cap": 4, "t0": 1500, "t1": 1900, "title": "Aceleración global", "tagline": "Conquistas, colonias, revolución industrial y demografía."},
    {"cap": 5, "t0": 1900, "t1": 1950, "title": "Guerras y revoluciones", "tagline": "Dos guerras mundiales y reconfiguración del sistema de conos."},
    {"cap": 6, "t0": 1950, "t1": 2000, "title": "Guerra Fría y globalización", "tagline": "Descolonización, tecnología, conectividad y densidad de archivo."},
    {"cap": 7, "t0": 2000, "t1": 2026, "title": "Presente y horizonte", "tagline": "Digitalización, sesgo de tinta y lo que el modelo no puede decir."},
]


def sample_years(seg):
    t0, t1 = seg["t0"], seg["t1"]
    if t0 == -7000000:
        return [-100000, -10000, 0, 1000, 2026]
    step = max(1, (t1 - t0) // 5)
    return sorted({int(round(t0 + i * step)) for i in range(6)} & set(range(t0, t1 + 1)))


def n_active_nodes_in_window(nodos, t0, t1):
    return sum(1 for n in nodos if ref.overlaps((t0, t1), (n.get("start"), n.get("end"))))


def conos_activos_en_ventana(conos, t0, t1):
    return [cid for cid, c in conos["civilizaciones"].items() if ref.overlaps((t0, t1), (c["support"]["t0"], c["support"]["t1"]))]


def nodos_activos_por_lente(nodos, t0, t1):
    cnt = Counter()
    for n in nodos:
        if not ref.overlaps((t0, t1), (n.get("start"), n.get("end"))):
            continue
        for d in ref.assign_dims(n):
            cnt[d] += 1
    return {d: cnt.get(d, 0) for d in D}


def nodos_por_lente_ano(nodos_dict, year):
    sliced = ref.slice_t(nodos_dict, year)
    cnt = Counter()
    for n in sliced:
        for d in ref.assign_dims(n):
            cnt[d] += 1
    return {d: cnt.get(d, 0) for d in D}


def top_nodos_por_lente(nodos, t0, t1, n=10):
    por_lente = {d: [] for d in D}
    for nd in nodos:
        if not ref.overlaps((t0, t1), (nd.get("start"), nd.get("end"))):
            continue
        span = (nd.get("end") or 0) - (nd.get("start") or 0)
        dims = ref.assign_dims(nd)
        for d in dims:
            por_lente[d].append((span, nd.get("name") or nd["id"], nd.get("start"), nd.get("end"), nd.get("region"), nd["id"]))
    out = {}
    for d in D:
        sel = sorted(por_lente[d], key=lambda x: -x[0])[:n]
        out[d] = [{"name": s[1], "start": s[2], "end": s[3], "region": s[4], "id": s[5]} for s in sel]
    return out


def A_t_para_ano(acoples, civs_index, year):
    n = len(civs_index)
    A = np.zeros((n, n))
    for e in acoples["acoples"]:
        i = e["from"]
        j = e["to"]
        if i not in civs_index or j not in civs_index:
            continue
        if e["interval"]["t0"] <= year <= e["interval"]["t1"]:
            A[civs_index[i], civs_index[j]] += 1
    return A


def rho_de_A(A):
    if A.size == 0 or np.all(A == 0):
        return 0.0
    try:
        ev = np.linalg.eigvals(A)
        return float(max(abs(ev)))
    except Exception:
        return 0.0


def W1_aproximado(nodos, t0, t1, year_a, year_b):
    a = nodos_por_lente_ano(nodos, year_a)
    b = nodos_por_lente_ano(nodos, year_b)
    total_a = sum(a.values())
    total_b = sum(b.values())
    if total_a == 0 and total_b == 0:
        return 0.0
    tv = 0.0
    for d in D:
        va = a.get(d, 0) / total_a if total_a else 0.0
        vb = b.get(d, 0) / total_b if total_b else 0.0
        tv += abs(va - vb)
    return 0.5 * tv


def meso_overlap(nodos_dict):
    ids = ["san-lorenzo", "la-venta", "cuicuilco", "el-mirador", "teotihuacan", "tula", "tenochtitlan"]
    found = [i for i in ids if i in nodos_dict]
    out = []
    for i in range(len(found)):
        for j in range(i + 1, len(found)):
            a = (nodos_dict[found[i]].get("start"), nodos_dict[found[i]].get("end"))
            b = (nodos_dict[found[j]].get("start"), nodos_dict[found[j]].get("end"))
            out.append({
                "a": found[i],
                "b": found[j],
                "allen": ref.allen(a, b),
            })
    return out


# ============================================================
# 4. Computo de datos por capítulo
# ============================================================
def conos_para_phi(year, conos, nodos_dict):
    """Construye la lista de conos activos en year con sus centros geográficos."""
    lista = []
    for cid, c in conos["civilizaciones"].items():
        amp = ref.envelope(year, c["support"]["t0"], c["support"]["t1"])
        if amp < 0.04:
            continue
        if cid in CENTROS_CONOS:
            lon, lat = CENTROS_CONOS[cid]
            regs = c["support"]["regions"]
        else:
            regs = [r for r in c["support"]["regions"] if r in REGIONES]
            if not regs:
                continue
            lon, lat = REGIONES[regs[0]]["centroide"]
        n_nodes = c.get("n_nodes", 50)
        peak = min(1.0, math.log1p(n_nodes) / 5.0)
        lista.append({"id": cid, "t0": c["support"]["t0"], "t1": c["support"]["t1"], "peak": peak, "xy": [lon, lat], "region": regs[0]})
    return lista


def calcular_todo():
    conos, nodos, nodos_dict, acoples = cargar_datos()
    civs = sorted(conos["civilizaciones"].keys())
    civs_index = {c: i for i, c in enumerate(civs)}

    for seg in SEGMENTOS:
        t0, t1 = seg["t0"], seg["t1"]
        cap = str(seg["cap"])
        out_dir = MEDIA / "segmentos" / cap
        out_dir.mkdir(parents=True, exist_ok=True)

        n_conos = len(conos_activos_en_ventana(conos, t0, t1))
        n_nodos = n_active_nodes_in_window(nodos, t0, t1)
        n_por_lente = nodos_activos_por_lente(nodos, t0, t1)
        top = top_nodos_por_lente(nodos, t0, t1)

        mid = (t0 + t1) // 2
        A_mid = A_t_para_ano(acoples, civs_index, mid)
        rho = rho_de_A(A_mid)

        s_a, s_b = sample_years(seg)[:2] if sample_years(seg) else (t0, t1)
        w1 = W1_aproximado(nodos_dict, t0, t1, s_a, s_b)

        data = {
            "cap": seg["cap"],
            "title": seg["title"],
            "t0": t0,
            "t1": t1,
            "n_conos_activos": n_conos,
            "n_nodos_activos": n_nodos,
            "n_por_lente": n_por_lente,
            "top_10_por_lente": top,
            "sample_years": sample_years(seg),
            "A_t_rho": round(rho, 4),
            "W1_aproximado": round(w1, 4),
            "civs_index": {c: i for i, c in enumerate(civs)},
            "meso_overlap": meso_overlap(nodos_dict) if seg["cap"] in (2, 3, "2", "3") else [],
        }
        (out_dir / "data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))

    return conos, nodos, nodos_dict, acoples, civs, civs_index


# ============================================================
# 5. Figuras
# ============================================================
def generar_mapa_conos(conos, nodos_dict, seg, year, out_path, video=False):
    clist = conos_para_phi(year, conos, nodos_dict)

    figsize = (19.2, 10.8) if video else (12.8, 7.2)
    fig = plt.figure(figsize=figsize, dpi=100, facecolor="#0f1115")
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_facecolor("#0f1115")
    ax.set_extent([-180, 180, -60, 80], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor="#1a1d24", edgecolor="none")
    ax.add_feature(cfeature.OCEAN, facecolor="#0f1115", edgecolor="none")
    ax.add_feature(cfeature.COASTLINE, linewidth=0.6, color="#5c6370")
    ax.add_feature(cfeature.BORDERS, linestyle=":", linewidth=0.4, color="#3a404a")

    if not video:
        lons = np.linspace(-180, 180, 96)
        lats = np.linspace(-60, 70, 54)
        Z = np.zeros((len(lats), len(lons)))
        for i, lat in enumerate(lats):
            for j, lon in enumerate(lons):
                total, _ = ref.phi_at(year, clist, lon, lat)
                Z[i, j] = total

        if Z.max() > 0:
            ax.imshow(Z, extent=(-180, 180, -60, 70), origin="lower", cmap="magma", aspect="auto", vmin=0, vmax=max(1.0, Z.max()), transform=ccrs.PlateCarree())

    for c in clist:
        lon, lat = c["xy"]
        # amplitud del cono en este año
        amp = ref.envelope(year, c["t0"], c["t1"])
        if amp < 0.01:
            continue
        reg = c.get("region", "humanidad")
        color = COLOR_POR_REGION.get(reg, "#ffffff")
        size = 40 + 160 * c["peak"] * amp
        ax.plot(lon, lat, "o", color=color, markersize=np.sqrt(size), alpha=0.5 + 0.4 * amp, transform=ccrs.PlateCarree())
        ax.plot(lon, lat, "+", color="white", markersize=4, alpha=0.8, transform=ccrs.PlateCarree())

    ax.text(0.02, 0.02, f"t = {year}", transform=ax.transAxes, color="white", fontsize=16, fontweight="bold", ha="left", va="bottom")
    ax.set_title(f"Conos activos sobre el mundo · {year}", color="white")
    fig.tight_layout()
    fig.savefig(out_path, facecolor="#0f1115", edgecolor="none")
    plt.close(fig)


def generar_densidad_archivo(nodos_dict, seg, out_path):
    years = sample_years(seg)
    series = {d: [] for d in D}
    for y in years:
        cnt = nodos_por_lente_ano(nodos_dict, y)
        for d in D:
            series[d].append(cnt.get(d, 0))

    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100)
    for d in D:
        ax.plot(years, series[d], marker="o", label=d)
    ax.set_title(f"Densidad de archivo por lente: capítulo {seg['cap']}")
    ax.set_xlabel("Año")
    ax.set_ylabel("Nodos activos")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, facecolor="white")
    plt.close(fig)


def generar_acoples(acoples, conos, seg, out_path):
    t0, t1 = seg["t0"], seg["t1"]
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100, facecolor="#0f1115")
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_facecolor("#0f1115")
    ax.set_extent([-180, 180, -60, 80], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5, color="#5c6370")
    ax.add_feature(cfeature.BORDERS, linestyle=":", linewidth=0.4, color="#3a404a")

    colores_civ = {}
    for i, cid in enumerate(conos["civilizaciones"]):
        if cid not in CENTROS_CONOS:
            continue
        lon, lat = CENTROS_CONOS[cid]
        colores_civ[cid] = COLOR_POR_REGION.get(conos["civilizaciones"][cid]["support"]["regions"][0], "#ffffff")
        ax.plot(lon, lat, "o", markersize=5, color=colores_civ[cid], alpha=0.6, transform=ccrs.PlateCarree())
        ax.text(lon + 2, lat, cid, fontsize=6, color="white", transform=ccrs.PlateCarree())

    n = 0
    for e in acoples["acoples"]:
        if not ref.overlaps((t0, t1), (e["interval"]["t0"], e["interval"]["t1"])):
            continue
        i, j = e["from"], e["to"]
        if i not in CENTROS_CONOS or j not in CENTROS_CONOS:
            continue
        x1, y1 = CENTROS_CONOS[i]
        x2, y2 = CENTROS_CONOS[j]
        color = {"war": "#ff6b6b", "trade": "#1dd1a1", "conquest": "#ee5a24", "exchange": "#54a0ff", "fusion": "#f368e0", "treaty": "#5f27cd"}.get(e["type"], "#aaaaaa")
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=color, alpha=0.55, lw=1.2), transform=ccrs.PlateCarree())
        n += 1

    if n == 0:
        ax.text(0.5, 0.5, f"Sin acoples documentados en [{t0}, {t1}]", transform=ax.transAxes, color="white", ha="center", va="center", fontsize=12)

    ax.set_title(f"Acoples activos: capítulo {seg['cap']} (n={n})", color="white")
    fig.tight_layout()
    fig.savefig(out_path, facecolor="#0f1115", edgecolor="none")
    plt.close(fig)


def generar_figuras():
    conos, nodos, nodos_dict, acoples, _, _ = calcular_todo()
    for seg in SEGMENTOS:
        cap = str(seg["cap"])
        out_dir = MEDIA / "segmentos" / cap
        out_dir.mkdir(parents=True, exist_ok=True)
        años = sample_years(seg)
        mid = años[len(años) // 2] if años else (seg["t0"] + seg["t1"]) // 2

        generar_densidad_archivo(nodos_dict, seg, out_dir / "densidad_archivo.png")
        generar_mapa_conos(conos, nodos_dict, seg, mid, out_dir / f"mapa_conos_{cap}.png")
        generar_acoples(acoples, conos, seg, out_dir / f"acoples_{cap}.png")


def generar_video():
    conos, _, nodos_dict, _ = cargar_datos()
    frames_dir = MEDIA / "global" / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    años = list(range(-3000, 2027, 5))
    for i, year in enumerate(años):
        generar_mapa_conos(conos, nodos_dict, None, year, frames_dir / f"frame_{i:04d}.png", video=True)

    video_path = MEDIA / "global" / "video_mapa_conos_1080p60.mp4"
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", "60",
        "-i", str(frames_dir / "frame_%04d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        str(video_path),
    ]
    subprocess.run(cmd, check=True)
    # Limpieza de frames intermedios opcional
    for f in frames_dir.glob("*.png"):
        f.unlink()


# ============================================================
# 6. HTML
# ============================================================
CSS = """
:root{--bg:#0f1115;--fg:#e8e6e3;--accent:#2ec4b6;--muted:#9aa0a6;--danger:#ff6b6b;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;line-height:1.65}
header,footer{padding:2rem;background:#151821;border-bottom:1px solid #252a35}
h1,h2,h3{color:var(--accent);font-weight:400}
.container{max-width:920px;margin:0 auto;padding:2rem}
.eq{background:#11141a;border-left:4px solid var(--accent);padding:1rem;font-family:"Courier New",monospace;margin:1rem 0;overflow-x:auto}
.warning{border-left:4px solid var(--danger);background:#1f1717;padding:1rem;margin:1rem 0}
figure{margin:1.5rem 0;text-align:center}
figcaption{color:var(--muted);font-size:.9rem}
img{max-width:100%;height:auto;border:1px solid #2a2f3a}
table{width:100%;border-collapse:collapse;margin:1rem 0}
th,td{border:1px solid #2a2f3a;padding:.4rem .6rem;text-align:left}
th{background:#181c24}
.toc{list-style:none;padding:0}
.toc li{margin:.25rem 0}
.toc a{color:var(--accent);text-decoration:none}
.section{border-top:1px solid #252a35;padding:3rem 0}
"""

INDEX_HTML = """<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Matemática de la Humanidad — Índice</title><style>@@css@@</style></head>
<body>
<header><div class="container"><h1>Matemática de la Humanidad</h1><p>Documental matemático-geográfico: del origen del sapiens a 2026.</p></div></header>
<div class="container">
<h2>Figuras del modelo</h2>
<p><a href="modelos_matematicos.html" style="color:var(--accent)">Siete modelos matemáticos explicados con gráficas</a></p>
<h2>Índice de capítulos</h2>
<ul class="toc">
  <li><a href="documental_consolidado.html#cap-0">0. Introducción y metodología</a></li>
  <li><a href="documental_consolidado.html#cap-0-5">0.5. Origen del ser humano</a></li>
  <li><a href="documental_consolidado.html#cap-1">1. Primeras lámparas</a></li>
  <li><a href="documental_consolidado.html#cap-2">2. Ejes antiguos</a></li>
  <li><a href="documental_consolidado.html#cap-3">3. Encuentros y solapes</a></li>
  <li><a href="documental_consolidado.html#cap-4">4. Aceleración global</a></li>
  <li><a href="documental_consolidado.html#cap-5">5. Guerras y revoluciones</a></li>
  <li><a href="documental_consolidado.html#cap-6">6. Guerra Fría y globalización</a></li>
  <li><a href="documental_consolidado.html#cap-7">7. Presente y horizonte</a></li>
</ul>
<p><a href="documental_consolidado.html" style="color:var(--accent)">Ver documental consolidado (HTML final)</a></p>
</div>
</body>
</html>"""

SECTION_HTML = """
<section class="section" id="cap-@@cap_id@@">
<h2>@@cap_title@@ (@@years@@)</h2>
<p class="tagline">@@tagline@@</p>
<p>@@narrative@@</p>

<h3>Ecuaciones aplicadas</h3>
<div class="eq">C = (W_C, F_C)<br>z_C(x,t) = H · max(0, 1 − dist/R)<br>Φ(x,t) = Σ_C z_C(x,t)</div>
<p>La sábana <code>Φ</code> se calcula con los conos activos y sus intervalos datados. En este segmento hay <strong>@@n_conos_activos@@</strong> conos activos y <strong>@@n_nodos_activos@@</strong> nodos en la ventana.</p>

<h3>Conteos por lente</h3>
<table><tr><th>Lente</th>@@th_lente@@</tr><tr><td>Nodos</td>@@td_lente@@</tr></table>

<h3>Top nodos por lente</h3>
@@top_nodes_html@@

<h3>Red de acoples</h3>
<p>Radio espectral aproximado de A_t en el año medio: <code>ρ(A) ≈ @@A_t_rho@@</code>.<br>
Variación Wasserstein aproximada entre inicio y fin del segmento: <code>W₁ ≈ @@W1_aproximado@@</code>.</p>

<h3>Mesoamérica solapada</h3>
@@meso_html@@

<figure>
  <img src="../media/segmentos/@@cap_str@@/mapa_conos_@@cap_str@@.png" alt="Mapa de conos"/>
  <figcaption>Mapa georreferenciado de Φ en el año medio del segmento.</figcaption>
</figure>

<figure>
  <img src="../media/segmentos/@@cap_str@@/densidad_archivo.png" alt="Densidad de archivo"/>
  <figcaption>Densidad de nodos por lente a lo largo de años muestra.</figcaption>
</figure>

<figure>
  <img src="../media/segmentos/@@cap_str@@/acoples_@@cap_str@@.png" alt="Acoples"/>
  <figcaption>Acoples activos en la ventana temporal.</figcaption>
</figure>

<div class="warning">
  <strong>Lo que el modelo no deja decir</strong>: el corpus mide densidad de archivo, no intensidad histórica real. La georreferenciación es una proyección de investigación, no una constante del modelo. <code>A^n u</code> es un escenario, nunca una predicción.
</div>
</section>
"""

INTRO_HTML = """
<section class="section" id="cap-0">
<h2>Capítulo 0 — Introducción y metodología</h2>
<div class="eq">G = (V, D, E_intra, E_inter, I, σ, φ)<br>B = R × T, |D| = 6<br>v ↦ (I(v)=[t₀,t₁], σ(v)⊆R, φ(v)⊆D)</div>
@@narrative@@
<div class="warning">
  El corpus contiene <strong>@@n_total_nodos@@</strong> nodos, <strong>@@n_total_conos@@</strong> civilizaciones/fibras y <strong>@@n_total_acoples@@</strong> acoples documentados. Estas cifras son densidad de archivo, no población ni poder histórico.
</div>
</section>
"""

CONSOLIDATED_HTML = """<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Matemática de la Humanidad — Documental Consolidado</title><style>@@css@@</style></head>
<body>
<header><div class="container"><h1>Matemática de la Humanidad</h1><p>Del origen del ser humano a 2026, narrado a través del modelo espaciotemporal.</p></div></header>
<div class="container">
<h2>Índice</h2>
<ul class="toc">@@toc@@</ul>

<figure>
  <video width="100%" controls poster="../media/segmentos/2/mapa_conos_2.png">
    <source src="../media/global/video_mapa_conos_1080p60.mp4" type="video/mp4">
  </video>
  <figcaption>Secuencia 1080p60 de conos simultáneos sobre mapa georreferenciado, 1920×1080, 60 fps, ~16.7 s. Los conos son polidades datadas; los centroides provienen del corpus georreferenciado.</figcaption>
</figure>

<p><a href="modelos_matematicos.html" style="color:var(--accent)">Ver las siete figuras del modelo matemático</a></p>

@@intro@@
@@sections@@

</div>
<footer><div class="container"><p>Generado el @@timestamp@@ · <a href="indice_documental.html">Índice</a> · <a href="https://github.com/ManuelCadena/Matematica-de-la-humanidad">Repositorio</a></p></div></footer>
</body>
</html>"""


def build_data_rows(n_por_lente):
    th = "".join(f"<th>{d}</th>" for d in D)
    td = "".join(f"<td>{n_por_lente.get(d, 0)}</td>" for d in D)
    return th, td


def build_top_html(top):
    parts = []
    for d in D:
        items = top.get(d, [])
        if not items:
            continue
        ul = "<ul>" + "".join(f"<li>{h['name']} ({h['start']}–{h['end']}, {h['region']})</li>" for h in items) + "</ul>"
        parts.append(f"<h4>{d}</h4>{ul}")
    return "\n".join(parts) if parts else "<p>No hay nodos destacados en este segmento.</p>"


def build_meso_html(meso, cap):
    if not meso:
        return "<p>Este segmento no incluye el análisis de solapes mesoamericanos.</p>"
    rows = "<ul>" + "".join(f"<li>{m['a']} ↔ {m['b']}: <code>{m['allen']}</code></li>" for m in meso) + "</ul>"
    return f"<p>Relaciones de Allen entre polidades mesoamericanas:</p>{rows}"


NARRATIVAS = json.loads((DATOS / "narrativas_capitulos.json").read_text())


def generar_htmls():
    _, nodos, _, acoples = cargar_datos()
    conos = json.loads((DATOS / "civilizaciones_fibras.json").read_text())
    n_total_nodos = len(nodos)
    n_total_conos = len(conos["civilizaciones"])
    n_total_acoples = len(acoples["acoples"])

    css = CSS
    toc = "".join(f'<li><a href="#cap-{str(s["cap"]).replace(".", "-")}">{s["cap"]} — {s["title"]}</a></li>' for s in SEGMENTOS)

    intro = (INTRO_HTML
        .replace("@@narrative@@", NARRATIVAS.get("0", ""))
        .replace("@@n_total_nodos@@", str(n_total_nodos))
        .replace("@@n_total_conos@@", str(n_total_conos))
        .replace("@@n_total_acoples@@", str(n_total_acoples)))

    sections = []
    for seg in SEGMENTOS[1:]:
        cap = str(seg["cap"])
        data = json.loads((MEDIA / "segmentos" / cap / "data.json").read_text())
        th, td = build_data_rows(data["n_por_lente"])
        section = (SECTION_HTML
            .replace("@@cap_id@@", cap.replace(".", "-"))
            .replace("@@cap_title@@", seg["title"])
            .replace("@@years@@", f"{data['t0']} a {data['t1']}")
            .replace("@@tagline@@", seg["tagline"])
            .replace("@@narrative@@", NARRATIVAS.get(cap, "Segmento documentado con datos del corpus."))
            .replace("@@n_conos_activos@@", str(data["n_conos_activos"]))
            .replace("@@n_nodos_activos@@", str(data["n_nodos_activos"]))
            .replace("@@th_lente@@", th)
            .replace("@@td_lente@@", td)
            .replace("@@top_nodes_html@@", build_top_html(data["top_10_por_lente"]))
            .replace("@@A_t_rho@@", str(data["A_t_rho"]))
            .replace("@@W1_aproximado@@", str(data["W1_aproximado"]))
            .replace("@@meso_html@@", build_meso_html(data["meso_overlap"], seg["cap"]))
            .replace("@@cap_str@@", cap))
        sections.append(section)

        # Crea capítulo individual ligero
        (APP / f"capitulo_{cap}.html").write_text(
            CONSOLIDATED_HTML
            .replace("@@css@@", css)
            .replace("@@toc@@", "")
            .replace("@@intro@@", "")
            .replace("@@sections@@", section)
            .replace("@@timestamp@@", datetime.now(timezone.utc).isoformat()),
        )

    consolidated = (CONSOLIDATED_HTML
        .replace("@@css@@", css)
        .replace("@@toc@@", toc)
        .replace("@@intro@@", intro)
        .replace("@@sections@@", "\n".join(sections))
        .replace("@@timestamp@@", datetime.now(timezone.utc).isoformat()))

    (APP / "documental_consolidado.html").write_text(consolidated)
    (APP / "indice_documental.html").write_text(INDEX_HTML.replace("@@css@@", css))


def generar_estilo():
    text = """# Estilo documental

## Voz
- Español académico, accesible, sin simplificaciones civilizacionistas.
- Años enteros astronómicos, intervalos cerrados [t₀,t₁].

## Metáforas permitidas
- "lámparas" = concentración de nodos.
- "sábana" = Φ(x,t).
- "conos" = polidades datadas.
- "tinta" = sesgo del archivo.

## Ecuaciones
- Usar bloque `div.eq` con LaTeX textual.
- Nunca escalar `dist_vector` sin declarar (α,β,γ).

## Advertencias
- Cada capítulo incluye "Lo que el modelo no deja decir".
- Distinguir evidencia medida, inferencia, hipótesis y escenario.

## Figuras
- Pie con año, proyección, lente y fuente de datos.
- Leyenda para medido, derivado, ilustrativo e hipotético.
- Resolución 1080p60 para videos.
"""
    (DOCS / "estilo_documental.md").write_text(text)


def main():
    APP.mkdir(exist_ok=True)
    MEDIA.mkdir(exist_ok=True)
    guardar_regiones()
    calcular_todo()
    generar_figuras()
    generar_video()
    generar_htmls()
    generar_estilo()
    print("Documental generado en app/documental_consolidado.html")


if __name__ == "__main__":
    main()
