"""
Parse the stats.nba.com-Endpoint-Documentation markdown file.

Parse into JSON file.
https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation
"""

import json


class Endpoint():

    def __init__(self, endpoint):
        self.method = endpoint["method"]
        self.params = endpoint["params"]
        self.description = endpoint["description"]


def parse_endpoint(block):
    name = block[0][3:-1]
    params = [line[4:] for line in block[2:]
              if line[4:] is not '']
    return {"endpoint": name, "params": params, "description": None}


def get_endpoints():
    with open('../nba_py.wiki/stats.nba.com-Endpoint-Documentation.md', 'r') as f:
        md = ''.join(f.read())

    endpoints = [parse_endpoint(block)
                 for block in map(lambda s: s.split("\n"), md.split("\n\n"))
                 if block[0].startswith("##")]

    return endpoints


if __name__ == '__main__':
    #  create JSON in form
    #  {"endpoint": string, "params": [param1, param2], "description": string}
    data = get_endpoints()

    with open('endpoints.json', 'w') as f:
        json.dump(data, f)