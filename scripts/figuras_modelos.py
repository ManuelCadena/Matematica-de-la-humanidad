#!/usr/bin/env python3.11
"""Genera las 7 figuras de los modelos matemáticos explicados."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent.parent
MEDIA = BASE / "media" / "modelos"
APP = BASE / "app"
DATOS = BASE / "datos"
DOCS = BASE / "docs"

sys.path.insert(0, str(DOCS))
import referencia_modelos as ref

D = ("politico", "historico", "religioso", "cientifico", "cultural", "social")


def cargar():
    conos = json.loads((DATOS / "civilizaciones_fibras.json").read_text())
    nodos = [json.loads(l) for l in (DATOS / "ontologia_nodos.jsonl").read_text().splitlines() if l.strip()]
    nodos_dict = {n["id"]: n for n in nodos}
    acoples = json.loads((DATOS / "acoples_multicapa.json").read_text())
    centros = json.loads((DATOS / "centros_conos.json").read_text())["centros"]
    return conos, nodos_dict, acoples, centros


def conos_con_centros(conos, centros):
    """Convierte el diccionario de civilizaciones a la lista de conos con xy y t0/t1."""
    out = []
    for cid, c in conos["civilizaciones"].items():
        if cid not in centros:
            continue
        lon, lat = centros[cid]
        t0 = c["support"]["t0"]
        t1 = c["support"]["t1"]
        n = c.get("n_nodes", 50)
        peak = min(1.0, np.log1p(n) / 5.0)
        out.append({"id": cid, "t0": t0, "t1": t1, "peak": peak, "xy": [lon, lat]})
    return out


def nodos_por_lente_ano(nodos_dict, year):
    cnt = Counter()
    for n in nodos_dict.values():
        if n.get("start") is None or n.get("end") is None:
            continue
        if n["start"] <= year <= n["end"]:
            for d in ref.assign_dims(n):
                cnt[d] += 1
    return cnt


def fig_01_envelope():
    years = np.arange(-250, 800, 5)
    env = [ref.envelope(t, -100, 650) for t in years]
    amp = [1.0 * e for e in env]

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120, facecolor="white")
    ax.plot(years, env, color="#8a6a12", lw=2.5, label="env(t; −100, 650)")
    ax.plot(years, amp, color="#1f5c58", lw=1.5, ls="--", label="amp(t) = peak·env")
    ax.axvline(-100, color="#9a4a2a", ls=":", alpha=0.7)
    ax.axvline(650, color="#9a4a2a", ls=":", alpha=0.7)
    ax.set_xlabel("año")
    ax.set_ylabel("encendido (0…1)")
    ax.set_title("Ecuación 1: envelope de Teotihuacan [−100, 650] · rampa 40 años")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(MEDIA / "01_envelope.png", facecolor="white")
    plt.close(fig)


def fig_02_cono():
    t = 200
    clon, clat = -98.84, 19.69
    amp = 1.0 * ref.envelope(t, -100, 650)
    H = amp * 16.0
    k = np.tan(np.radians(52.0))
    R = max(5.5, H * k)
    lons = np.linspace(clon - 35, clon + 35, 400)
    z = [ref.cone_z(lon, 0, 0, 0, H, R) for lon in lons]  # perfil a lo largo del meridiano

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120, facecolor="white")
    ax.fill_between(lons, 0, z, color="#1f5c58", alpha=0.3)
    ax.plot(lons, z, color="#1f5c58", lw=2)
    ax.axvline(clon, color="#8a6a12", ls=":")
    ax.set_xlabel("longitud (°)")
    ax.set_ylabel("z_C (luz)")
    ax.set_title(f"Ecuación 2: cono de Teotihuacan en t={t} · H={H:.1f} · R={R:.1f}° · α=52°")
    ax.text(clon - 30, H * 0.85, f"H = amp×H_max\nR = H·tan(52°)", fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(MEDIA / "02_cono.png", facecolor="white")
    plt.close(fig)


def fig_03_distancia():
    teo = {"start": -100, "end": 650, "region": "meso", "lentes": ["politico", "historico", "cultural"]}
    otros = [
        ("Tikal", {"start": 200, "end": 900, "region": "meso", "lenses": ["politico", "historico", "cultural"]}),
        ("Tenochtitlan", {"start": 1325, "end": 1521, "region": "meso", "lentes": ["politico", "historico"]}),
        ("Roma", {"start": -50, "end": 476, "region": "eu-west", "lentes": ["politico", "historico", "cultural"]}),
    ]
    nombres = ["Teotihuacan"] + [o[0] for o in otros]
    dt, dr, dd = [0], [0], [0]
    for _, v in otros:
        vec = ref.dist_vector(teo, v)
        dt.append(vec[0])
        dr.append(vec[1])
        dd.append(vec[2])

    x = np.arange(len(nombres))
    w = 0.25
    fig, ax = plt.subplots(figsize=(10, 5), dpi=120, facecolor="white")
    ax.bar(x - w, dt, w, label="d_T (años)", color="#8a6a12")
    ax.bar(x, dr, w, label="d_R (saltos)", color="#1f5c58")
    ax.bar(x + w, dd, w, label="d_D (lente)", color="#9a4a2a")
    ax.set_xticks(x)
    ax.set_xticklabels(nombres, rotation=15, ha="right")
    ax.set_ylabel("magnitud")
    ax.set_title("Ecuación 3: vector distancia (d_T, d_R, d_D) desde Teotihuacan")
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(MEDIA / "03_distancia.png", facecolor="white")
    plt.close(fig)


def fig_04_At(conos, acoples):
    # civs con centro georreferenciado
    civs = sorted(c for c in conos["civilizaciones"] if c in json.loads((DATOS / "centros_conos.json").read_text())["centros"])
    idx = {c: i for i, c in enumerate(civs)}
    t = 100
    A = np.zeros((len(civs), len(civs)))
    for e in acoples["acoples"]:
        if e["from"] not in idx or e["to"] not in idx:
            continue
        if e["interval"]["t0"] <= t <= e["interval"]["t1"]:
            i, j = idx[e["from"]], idx[e["to"]]
            A[i, j] += 1
            if e.get("symmetric"):
                A[j, i] += 1
    ev = np.linalg.eigvals(A)
    rho = max(abs(ev)) if len(ev) else 0.0

    fig, ax = plt.subplots(figsize=(11, 9), dpi=120, facecolor="white")
    im = ax.imshow(A, cmap="YlOrRd", aspect="auto", vmin=0)
    ax.set_xticks(range(len(civs)))
    ax.set_yticks(range(len(civs)))
    ax.set_xticklabels(civs, rotation=90, fontsize=7)
    ax.set_yticklabels(civs, fontsize=7)
    ax.set_title(f"Ecuación 4: matriz A_t en t={t} · ρ(A) = {rho:.3f}")
    fig.colorbar(im, ax=ax, label="acoples")
    fig.tight_layout()
    fig.savefig(MEDIA / "04_At.png", facecolor="white")
    plt.close(fig)


def fig_05_W1(nodos_dict):
    years = list(range(-1000, 1950, 50))
    vals = []
    for y in years:
        a = nodos_por_lente_ano(nodos_dict, y)
        b = nodos_por_lente_ano(nodos_dict, y + 50)
        ta = sum(a.values())
        tb = sum(b.values())
        if ta == 0 and tb == 0:
            vals.append(0.0)
            continue
        tv = 0.0
        for d in D:
            va = a.get(d, 0) / ta if ta else 0.0
            vb = b.get(d, 0) / tb if tb else 0.0
            tv += abs(va - vb)
        vals.append(0.5 * tv)

    fig, ax = plt.subplots(figsize=(12, 5), dpi=120, facecolor="white")
    ax.plot(years, vals, color="#7a2f56", lw=2, marker="o", markersize=3)
    ax.set_xlabel("año")
    ax.set_ylabel("W₁ / Δt")
    ax.set_title("Ecuación 5: velocidad de Wasserstein aproximada (Δt = 50 años)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(MEDIA / "05_W1.png", facecolor="white")
    plt.close(fig)


def fig_06_allen(nodos_dict):
    ids = ["san-lorenzo", "la-venta", "cuicuilco", "el-mirador", "teotihuacan", "tula", "tenochtitlan"]
    found = [i for i in ids if i in nodos_dict]
    rels = Counter()
    for i in range(len(found)):
        for j in range(i + 1, len(found)):
            a = (nodos_dict[found[i]].get("start"), nodos_dict[found[i]].get("end"))
            b = (nodos_dict[found[j]].get("start"), nodos_dict[found[j]].get("end"))
            rels[ref.allen(a, b)] += 1

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120, facecolor="white")
    bars = ax.bar(rels.keys(), rels.values(), color="#6b4c7a")
    ax.set_xlabel("relación de Allen")
    ax.set_ylabel("pares")
    ax.set_title("Ecuación 6: relaciones de Allen entre polidades mesoamericanas")
    ax.tick_params(axis="x", rotation=30)
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h, int(h), ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    fig.savefig(MEDIA / "06_allen.png", facecolor="white")
    plt.close(fig)


def fig_07_fibrado(nodos_dict):
    regions = [k for k in ref.ADJ if k != "humanidad"]
    bins = list(range(-3000, 2026, 200))
    Z = np.zeros((len(regions), len(bins)))
    for i, r in enumerate(regions):
        for j, b0 in enumerate(bins):
            b1 = b0 + 200
            cnt = 0
            for n in nodos_dict.values():
                if n.get("region") == r and ref.overlaps((b0, b1), (n.get("start"), n.get("end"))):
                    cnt += 1
            Z[i, j] = cnt

    fig, ax = plt.subplots(figsize=(14, 6), dpi=120, facecolor="white")
    im = ax.imshow(Z, cmap="magma", aspect="auto", origin="lower")
    ax.set_yticks(range(len(regions)))
    ax.set_yticklabels(regions)
    ax.set_xticks(range(0, len(bins), 3))
    ax.set_xticklabels([bins[i] for i in range(0, len(bins), 3)], rotation=45)
    ax.set_xlabel("bin de 200 años")
    ax.set_ylabel("región")
    ax.set_title("Ecuación 7: fibrado R×T (incidencias de nodos por región y bin)")
    fig.colorbar(im, ax=ax, label="nodos activos")
    fig.tight_layout()
    fig.savefig(MEDIA / "07_fibrado.png", facecolor="white")
    plt.close(fig)


def generar_html():
    out_dir = APP / "modelos_matematicos.html"
    css = """:root{--bg:#f6f1e4;--ink:#1a140e;--gold:#8a6a12;--teal:#1f5c58;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Georgia,serif;line-height:1.6}
.wrap{max-width:1000px;margin:0 auto;padding:2rem}
h1,h2,h3{color:var(--gold)}
figure{margin:1.5rem 0;background:#fff;padding:1rem;border:1px solid #d9cbb0}
figcaption{font-size:.9rem;color:#5c5346}
img{width:100%;display:block}
.eq{background:#fff;border-left:4px solid var(--teal);padding:1rem;margin:1rem 0;font-family:monospace}
"""
    figs = [
        ("01_envelope.png", "Ecuación 1 — envelope", "env(t; t₀, t₁) apaga y enciende cada cono con una rampa de 40 años. Teotihuacan se apaga en 700."),
        ("02_cono.png", "Ecuación 2 — cono", "z_C(x,t) = H·max(0, 1 − dist/R). La luz cae linealmente hasta el radio R = H·tan(52°)."),
        ("03_distancia.png", "Ecuación 3 — distancia", "(d_T, d_R, d_D) mide años de separación, saltos de región y lentes compartidos."),
        ("04_At.png", "Ecuación 4 — acoplos A_t", "A_t es la matriz de tinta entre conos en una ventana; ρ(A) mide si la copia crece sola."),
        ("05_W1.png", "Ecuación 5 — Wasserstein W₁", "W₁/Δt es la velocidad con que la sábana de lentes se reacomoda entre dos años."),
        ("06_allen.png", "Ecuación 6 — relaciones de Allen", "Allen(a,b) clasifica cómo se tocan dos intervalos temporales."),
        ("07_fibrado.png", "Ecuación 7 — fibrado R×T", "R×T organiza los nodos del corpus en regiones y bins de tiempo."),
    ]
    body = [
        '<div class="wrap">',
        '<h1>Modelos matemáticos de la humanidad</h1>',
        '<p class="eq">Cada figura es una instantánea del mismo corpus: 2336 nodos, 22 fibras, 81 conos. No se inventan datos.</p>',
    ]
    for fn, title, cap in figs:
        body.append(f'<h2>{title}</h2>')
        body.append(f'<p>{cap}</p>')
        body.append(f'<figure><img src="../media/modelos/{fn}" alt="{title}"><figcaption>{title}</figcaption></figure>')
    body.append('<p><a href="indice_documental.html" style="color:var(--teal)">Volver al índice documental</a></p>')
    body.append('</div>')
    html = f"<!doctype html><html lang='es'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Modelos matemáticos · MMH</title><style>{css}</style></head><body>{''.join(body)}</body></html>"
    out_dir.write_text(html, encoding="utf-8")


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    conos, nodos_dict, acoples, _ = cargar()
    fig_01_envelope()
    fig_02_cono()
    fig_03_distancia()
    fig_04_At(conos, acoples)
    fig_05_W1(nodos_dict)
    fig_06_allen(nodos_dict)
    fig_07_fibrado(nodos_dict)
    generar_html()
    print("modelos generados en", MEDIA)


if __name__ == "__main__":
    main()
