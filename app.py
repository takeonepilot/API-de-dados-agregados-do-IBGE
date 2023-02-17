from flask import Flask
from municipios_controller import MunicipiosController

app = Flask(__name__)
municipios_controller = MunicipiosController()

app.add_url_rule('/municipios', view_func=municipios_controller.get_all_municipios, methods=['GET'])
app.add_url_rule('/municipios/<codigo>', view_func=municipios_controller.get_municipio_by_codigo, methods=['GET'])

if __name__ == '__main__':
    app.run()
