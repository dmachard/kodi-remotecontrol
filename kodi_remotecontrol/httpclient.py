
import requests
import json

class HttpClient:
    def __init__(self, api_host,
                       api_port=8080, 
                       api_username="",
                       api_password="",):
        """authenticator class"""
        self.api_host = api_host
        self.api_port = api_port
        self.api_username = api_username
        self.api_password = api_password
        
        self.api_url = "http://%s:%s/jsonrpc" % (api_host, api_port)
    
    def post(self, method, params={}):
        """post request"""
        payload = { "method": method, 
                    "id": 1, "jsonrpc": "2.0",
                    "params": params}
        r = requests.post(url=self.api_url, json=payload)
        if r.status_code != 200:
            raise Exception("[error] post: %s - %s" % (r.status_code,
                                                       r.text))
        return r.json()