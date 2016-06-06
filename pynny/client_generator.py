"""Generates the nba stats client."""

from jinja2 import Environment, FileSystemLoader
import os
import json


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(THIS_DIR, "endpoints.json")
OUT_PATH = os.path.join(THIS_DIR, "client.py")


def _load_json(path):
    with open(path) as f:
        return json.load(f)


def _generate_client(dir, templ, json):
    env = Environment(loader=FileSystemLoader(dir))
    return env.get_template(templ).render(endpoints=json)

if __name__ == '__main__':
    output = _generate_client(
        THIS_DIR, "endpoint_template.py", _load_json(JSON_PATH)
    )
    with open(OUT_PATH, 'w') as f:
        f.write(output)
