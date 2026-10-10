"""Persistent local registry, independent of the analysis gate."""
import json
import os
from pathlib import Path
from research.engine import validate_case

def load_catalog(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(data, list):
        raise ValueError('Catalogue must be a JSON list')
    seen = set()
    for case in data:
        validate_case(case)
        if case['incident_id'] in seen:
            raise ValueError('Duplicate incident ID in catalogue')
        seen.add(case['incident_id'])
    return data

def save_registration(path, case):
    validate_case(case)
    path = Path(path)
    data = load_catalog(path)
    for i, current in enumerate(data):
        if current['incident_id'] == case['incident_id']:
            data[i] = case
            break
    else:
        data.append(case)
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    os.replace(temporary, path)
    return data
