"""
Parse the stats.nba.com-Endpoint-Documentation markdown file.

Parse into JSON file.
https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation
"""


def parse_endpoint(block):
    name = block[0][3:-1]
    param_names = [line[4:] for line in block[2:]
                   if line[4:] is not '']
    params = [
        {"name": p, "required": False}
        for p in param_names
    ]
    return {"endpoint": name, "params": params, "description": None}


def get_endpoints(path):
    with open(path, 'r') as f:
        md = ''.join(f.read())

    endpoints = [parse_endpoint(block)
                 for block in map(lambda s: s.split("\n"), md.split("\n\n"))
                 if block[0].startswith("##")]

    return endpoints
