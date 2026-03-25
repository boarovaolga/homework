import requests


class ApiClient:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

    def post(self, path, json=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.post(url, json=json)

    def put(self, path, json=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.put(url, json=json)

    def get(self, path):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url)
