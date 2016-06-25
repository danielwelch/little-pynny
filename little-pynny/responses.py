"""Get responses from the stats API, only for testing/docs purposes."""
import requests

import json
import os
import re


class ParamMatchException(Exception):
    def __init__(self, endpoint, param):
        Exception.__init__(
            self,
            "{}: Failed to match param response with regex: {}".format(endpoint, param)
        )


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(THIS_DIR, "endpoints.json")

BASE_URL = 'http://stats.nba.com/stats/{endpoint}'
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}


def _load_json(path):
    with open(path) as f:
        return json.load(f)


def _write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
    return True


def _endpoint_deprecated(endpoint):
    pass


def _handle_crap_params(endpoint):
    player_scope = {"name": "PlayerScope", "required": True}
    game_scope = {"name": "GameScope", "required": True}

    endpoint["params"] = [
        param for param in endpoint["params"]
        if param["name"] != "Scope"
    ]
    endpoint["params"].extend([player_scope, game_scope])

    return endpoint


def define_required_params(endpoint, response_phrases):
    required_params = []
    for phrase in response_phrases:
        m1 = re.match("^(?P<param>(\w*)|(Game Scope)|(Player Scope)|(Stat Category)) is required.?", phrase)
        m2 = re.match("^The (?P<param>(\w*)|(Game Scope)|(Player Scope)|(Stat Category)) property is required.?", phrase)
        if m1 is None:
            if m2 is None:
                raise ParamMatchException(method, phrase)
            else:
                param = m2.group("param")
        else:
            param = m1.group("param")
        # deal with the random params nba puts a space in for no reason
        if param is "Game Scope":
            required_params.append("GameScope")
        if param is "Player Scope":
            required_params.append("PlayerScope")
        if param is "Stat Category":
            required_params.append("StatCategory")
        else:
            required_params.append(param)

    for p in endpoint["params"]:
        if p["name"] in required_params:  # TODO: deal with scope vs. playerscope vs. gamescope
            p["required"] = True

    crap = ("homepageleaders", "homepagev2", "leaderstiles")
    if endpoint["endpoint"] in crap:
        endpoint = _handle_crap_params(endpoint)
    return endpoint


def add_param_descriptions(endpoint):
    # using the server's response for bad params,
    # get the regexs that each param must match
    # and add them to the endpoint object
    r = requests.get(
        BASE_URL.format(endpoint=endpoint["endpoint"]),
        headers=HEADERS,
        params={
            param["name"]: "xxxx"
            for param in endpoint["params"]
        }
    )


if __name__ == '__main__':
    data = _load_json(JSON_PATH)
    for d in data:
        method = d["endpoint"].lower()
        # this one request will allow us to determine if an endpoint is active
        # and, if so, the required params of the endpoint
        r = requests.get(
            BASE_URL.format(endpoint=method),
            headers=HEADERS
        )

        #  determine if each endpoint is active or not (no resource in API)
        if r.text.startswith('{"Message"'):   # this works for checking endpoints
            d["active"] = False
            continue
        else:
            d["active"] = True

        #  determine which paramaters are required
        phrases = r.text.split("; ")
        d = _define_required_params(d, phrases)

    if _write_json(JSON_PATH, data):
        print('done')
