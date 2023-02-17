from flask import Flask, jsonify
from flask_cors import CORS
from municipios import Municipios

app = Flask(__name__)
CORS(app)

@app.route('/municipios')
def get_municipios():
    municipios = Municipios().get_all()
    return jsonify(municipios)

@app.route('/municipios/<codigo>')
def get_municipio(codigo):
    municipio = Municipios().get_by_codigo(codigo)
    return jsonify(municipio)

if __name__ == '__main__':
    app.run()
