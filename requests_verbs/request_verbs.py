from requests import Session
import json


class RedisApiRequests:

    def __init__(self):
        self.s = Session()
        self.base_url = 'http://localhost:4201'
    
    def do_get(self, endpoint):
        url = self.build_url(endpoint)
        headers = self.get_headers()
        r = self.s.get(url=url, headers=headers)
        return r

    def do_post(self, data, endpoint):
        url = self.build_url(endpoint)
        headers = self.get_headers()
        r = self.s.post(url=url, data=json.dumps(data), headers=headers)
        return r

    def get_headers(self):
        headers = {'Content-Type': 'application/json'}
        return headers

    def build_url(self, endpoint):
        url = '{base_url}{endpoint}'.format(base_url=self.base_url, endpoint=endpoint)
        return url