from wiki_parser import get_endpoints
from responses import define_required_params, add_param_descriptions
from swaggerify import swaggerify

import requests

import json
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(THIS_DIR, 'stats.nba.com-Endpoint-Documentation.md')
SWAGGER_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "swagger.json")

BASE_URL = 'http://stats.nba.com/stats/{endpoint}'
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}


def _write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
    return True


def main():
    """Generate OpenAPI compliant JSON from stats.nba.com-Endpoint-Documentation.md."""
    data = get_endpoints(DOC_PATH)

    for d in data:
        method = d["endpoint"].lower()
        # this one request will allow us to determine if an endpoint is active
        # and, if so, the required params of the endpoint
        r = requests.get(
            BASE_URL.format(endpoint=method),
            headers=HEADERS
        )
        #  determine if each endpoint is active or not (no resource in API)
        if r.text.startswith('{"Message"'):
            d["active"] = False
            continue
        else:
            d["active"] = True
        #  determine which paramaters are required
        phrases = r.text.split("; ")
        d = define_required_params(d, phrases)

    swag = swaggerify(data)
    if _write_json(SWAGGER_PATH, swag):
        print("docs have been swaggerified")


if __name__ == '__main__':
    main()
