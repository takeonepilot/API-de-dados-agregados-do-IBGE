from flask import jsonify
from municipios_service import MunicipiosService

class MunicipiosController:
    def __init__(self):
        self.municipios_service = MunicipiosService()

    def get_all_municipios(self):
        municipios = self.municipios_service.get_all_municipios()
        return jsonify(municipios)

    def get_municipio_by_codigo(self, codigo):
        municipio = self.municipios_service.get_municipio_by_codigo(codigo)
        return jsonify(municipio)
