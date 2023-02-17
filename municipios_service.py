from municipios_repository import MunicipiosRepository

class MunicipiosService:
    def __init__(self):
        self.municipios_repository = MunicipiosRepository()

    def get_all_municipios(self):
        municipios = self.municipios_repository.get_all_municipios()
        return municipios

    def get_municipio_by_codigo(self, codigo):
        municipio = self.municipios_repository.get_municipio_by_codigo(codigo)
        return municipio
