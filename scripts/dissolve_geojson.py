"""
Dissolves GeoJSON wilderness/WSA files so each named area is a single feature,
using a proper polygon union (not just grouping).

Usage:
    python3 scripts/dissolve_geojson.py
"""

import json
from collections import defaultdict
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

def dissolve(input_path, output_path, name_key):
    with open(input_path) as f:
        data = json.load(f)

    by_name = defaultdict(list)
    for feat in data['features']:
        name = feat['properties'].get(name_key, '')
        by_name[name].append(feat)

    dissolved = []
    for name, feats in by_name.items():
        geoms = [shape(f['geometry']).buffer(0) for f in feats]
        merged = unary_union(geoms)
        dissolved.append({
            'type': 'Feature',
            'geometry': mapping(merged),
            'properties': feats[0]['properties']
        })

    result = {'type': 'FeatureCollection', 'features': dissolved}
    with open(output_path, 'w') as f:
        json.dump(result, f, separators=(',', ':'))

    print(f'{input_path}: {len(data["features"])} features → {len(dissolved)} dissolved')

dissolve(
    'static/data/wy_wilderness.geojson',
    'static/data/wy_wilderness.geojson',
    'WILDERNESSNAME'
)
dissolve(
    'static/data/wy_wsa.geojson',
    'static/data/wy_wsa.geojson',
    'NLCS_NAME'
)
