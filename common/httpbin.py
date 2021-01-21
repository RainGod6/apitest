import requests


class HttpBin:
    url = "http://47.108.156.7:8080/"

    def get(self, params):
        rp = requests.get(self.url + 'get', params)
        return rp.json()

    def post(self, data, json=None):
        rp = requests.post(self.url + 'post', data, json)
        return rp.json()


if __name__ == '__main__':
    print(HttpBin().get({'a': 1, 'b': 2}))
