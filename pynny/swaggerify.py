import json
import os


OLD_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "endpoints.json")
NEW_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "stats_nba_swagger.json")


def _load_json(path):
    with open(path) as f:
        return json.load(f)


def _write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
    return None


def _method_from_endpoint(path):
    return {
        "description": path["description"],
        "produces": ["application/json", "text/html", "text/xml"],
        "responses": {
            "200": {},
            "400": {
                "description": "Bad request - bad parameters"
            },
            "404": {
                "description": "'No HTTP resource was found that matches the request URI' - possible deprecated endpoint"
            }
        }
    }


def _params_from_endpoint(params):
    return [
        {
            "name": param["name"],
            "in": "query",
            "required": param["required"],
            "type": "string"  # TODO: need to test type (integer vs. string)
        } for param in params
    ]


def _convert_path(path):
    #  convert an endpoint from old json to a swagger path object
    return {
        "get": _method_from_endpoint(path),
        "parameters": _params_from_endpoint(path["params"]),
        "deprecated": not path["active"],
        "summary": path["description"]
    }


def _swaggerify(old):
    return {
        "swagger": "2.0",
        "info": {
            "title": "NBA Stats API",
            "description": "",
            "version": "version"  # fix this
        },
        "host": "stats.nba.com",
        "basePath": "/stats",
        "paths": {
            "/" + endpoint["endpoint"]: _convert_path(endpoint)
            for endpoint in old
        },
        # "externalDocs": None,  # eventually replace with some sort of documentation
    }


if __name__ == '__main__':
    old = _load_json(OLD_PATH)
    err = _write_json(NEW_PATH, _swaggerify(old))
    if err is None:
        print("json has been swaggerified")

