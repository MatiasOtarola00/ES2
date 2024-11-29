import json
import requests
 
class Mindicador:
 
    def __init__(self, indicador, year):
        self.indicador = indicador
        self.year = year
    
    def Info_Api(self):
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        pretty_json = json.dumps(data, indent=2)
        return pretty_json