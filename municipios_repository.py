import requests

class MunicipiosRepository:
    def __init__(self):
        self.url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'

    def listar_municipios(self):
        response = requests.get(self.url)
        municipios = response.json()
        return municipios

    def obter_municipio(self, codigo):
        url_municipio = f'{self.url}/{codigo}'
        response = requests.get(url_municipio)
        municipio = response.json()
        return municipio
