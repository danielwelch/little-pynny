"""A python client for the stats.nba.com API."""

import requests


#  Constants - Taken from https://github.com/seemethere/nba_py/
BASE_URL = 'http://stats.nba.com/stats/{endpoint}'
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}


class Client():

    def _get_json(self, endpoint, params):

        res = requests.get(
            BASE_URL.format(endpoint=endpoint),
            params=params,
            headers=HEADERS
        )
        res.raise_for_status()
        return res.json()
    {% for item in endpoints %}
    def {{ item.endpoint.lower() }}(
        self,{% for param in item.params %}
        {{ param.lower() }},{% endfor %}
    ):
        """{{item.description}}."""
        params = { {% for param in item.params %}
            "{{ param }}": {{ param.lower() }},{% endfor %}
        }
        return self._get_json("{{ item.endpoint }}", params)
    {% endfor %}
