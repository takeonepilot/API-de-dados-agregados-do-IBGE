from repositories.municipios_repository import MunicipiosRepository

class MunicipiosService:
    def __init__(self):
        self.repository = MunicipiosRepository()

    def listar_municipios(self):
        municipios = self.repository.listar_municipios()
        return municipios

    def obter_municipio(self, codigo):
        municipio = self.repository.obter_municipio(codigo)
        return municipio
