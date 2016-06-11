import json
import os


OLD_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "endpoints.json")
NEW_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "stats_nba_swagger.json")


def _method_from_endpoint(path):
    return {
        "description": "",
        "produces": ["application/json", "text/html", "text/xml"],
        "responses": {
            "200": {
                "description": "200 OK"
            },
            "400": {
                "description": "Bad request - bad parameters"
            },
            "404": {
                "description": "'No HTTP resource was found that matches the request URI' - possible deprecated endpoint"
            }
        },
        "deprecated": not path["active"],
        "summary": "",
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
    }


def swaggerify(old):
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
    err = _write_json(NEW_PATH, swaggerify(old))
    if err is None:
        print("json has been swaggerified")
