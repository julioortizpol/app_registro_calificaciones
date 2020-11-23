import requests
import json

class Services:

    def __init__(self, cedula):
        self._url='https://api.adamix.net/apec/cedula/'
        self._cedula = cedula
        self.set_datos()
    #end method

    def set_datos(self):
        self._datos = requests.get(self._url+self._cedula)
    #end method

    def get_datos(self):
        if self._datos.status_code==200:
            return self._datos.json()
        else:
            return '500'
    #end method
#end class