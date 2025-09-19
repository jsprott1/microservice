import requests

class MicroserviceClient:
    def __init__(self, url):
        self.url = url
    def __getattr__(self,name):
        if name[0] == "_":
            return object.__getattr__(self, name)
        else:
            def _(*args, **kwargs):
                return requests.post(self.url, json={"function":name, "args":args,  "kwargs":kwargs})
            return _
