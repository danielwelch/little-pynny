
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
