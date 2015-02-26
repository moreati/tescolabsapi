import requests

API_URL = 'https://secure.techfortesco.com/tescolabsapi/restservice.aspx'


class TescoLabsApi(object):
    def __init__(self, url, developerkey, applicationkey):
        self.url = url
        self.developerkey = developerkey
        self.applicationkey = applicationkey
        res = requests.get(self.url,
                           params={'command': 'login',
                                   'email': '', 'password': '',
                                   'developerkey': self.developerkey,
                                   'applicationkey': self.applicationkey,
                                   })
        self.sessionkey = res.json()['SessionKey']

    def _command(self, command, **kwargs):
        params = kwargs
        params.update({'command': command, 'sessionkey': self.sessionkey})
        res = requests.get(self.url, params=params)
        return res

    def listproductcategories(self):
        return self._command('listproductcategories')

    def listproductsincategory(self, category):
        return self._command('listproductsincategory', category=category)

    def listproductoffers(self):
        return self._command('listproductoffers')

    def productsearch(self, searchtext, page=1, extendedinfo=False):
        return self._command('productsearch', searchtext=searchtext,
                             page=page, extendedinfo=extendedinfo)

