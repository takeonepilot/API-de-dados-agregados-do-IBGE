from flask import Blueprint, jsonify, request
from services.municipios_service import MunicipiosService

municipios_controller = Blueprint('municipios_controller', __name__)
municipios_service = MunicipiosService()

@municipios_controller.route('/municipios')
def listar_municipios():
    municipios = municipios_service.listar_municipios()
    return jsonify(municipios)

@municipios_controller.route('/municipios/<codigo>')
def obter_municipio(codigo):
    municipio = municipios_service.obter_municipio(codigo)
    return jsonify(municipio)
