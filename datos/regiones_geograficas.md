# Regiones geográficas

**Aviso metodológico**: `R` es el grafo de adyacencia historiográfico de 16 regiones
definido en `modelo_espacio_tiempo.json` y `docs/referencia_modelos.py`.
Los centroides y polígonos de este archivo son una proyección de investigación
para anclar visualizaciones geográficas. No son una constante del modelo formal.

## am-north
- Centroide: `lon=-100.0, lat=45.0`
- Adyacencias: ['meso']
- Polígono aproximado: 5 vértices

## meso
- Centroide: `lon=-92.0, lat=18.0`
- Adyacencias: ['am-north', 'andes']
- Polígono aproximado: 5 vértices

## andes
- Centroide: `lon=-72.0, lat=-15.0`
- Adyacencias: ['meso']
- Polígono aproximado: 5 vértices

## af-west
- Centroide: `lon=-5.0, lat=12.0`
- Adyacencias: ['maghreb', 'af-nile', 'af-cs']
- Polígono aproximado: 5 vértices

## af-nile
- Centroide: `lon=35.0, lat=20.0`
- Adyacencias: ['af-west', 'af-cs', 'maghreb', 'near-east']
- Polígono aproximado: 5 vértices

## af-cs
- Centroide: `lon=25.0, lat=-18.0`
- Adyacencias: ['af-west', 'af-nile']
- Polígono aproximado: 5 vértices

## maghreb
- Centroide: `lon=5.0, lat=32.0`
- Adyacencias: ['af-west', 'af-nile', 'eu-west', 'near-east']
- Polígono aproximado: 5 vértices

## eu-west
- Centroide: `lon=2.0, lat=47.0`
- Adyacencias: ['eu-east', 'maghreb', 'near-east']
- Polígono aproximado: 5 vértices

## eu-east
- Centroide: `lon=28.0, lat=50.0`
- Adyacencias: ['eu-west', 'near-east', 'iran-steppe']
- Polígono aproximado: 5 vértices

## near-east
- Centroide: `lon=42.0, lat=34.0`
- Adyacencias: ['eu-west', 'eu-east', 'maghreb', 'af-nile', 'iran-steppe']
- Polígono aproximado: 5 vértices

## iran-steppe
- Centroide: `lon=62.0, lat=36.0`
- Adyacencias: ['near-east', 'eu-east', 'sasia', 'easia']
- Polígono aproximado: 5 vértices

## sasia
- Centroide: `lon=78.0, lat=22.0`
- Adyacencias: ['iran-steppe', 'easia', 'seasia']
- Polígono aproximado: 5 vértices

## easia
- Centroide: `lon=108.0, lat=35.0`
- Adyacencias: ['sasia', 'iran-steppe', 'seasia']
- Polígono aproximado: 5 vértices

## seasia
- Centroide: `lon=115.0, lat=12.0`
- Adyacencias: ['sasia', 'easia', 'oceania']
- Polígono aproximado: 5 vértices

## oceania
- Centroide: `lon=140.0, lat=-25.0`
- Adyacencias: ['seasia']
- Polígono aproximado: 5 vértices

## humanidad
- Centroide: `lon=0.0, lat=0.0`
- Adyacencias: []
- Polígono aproximado: 5 vértices
