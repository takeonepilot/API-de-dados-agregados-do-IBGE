from flask import Flask
from controllers.municipios_controller import municipios_controller

app = Flask(__name__)
app.register_blueprint(municipios_controller)

if __name__ == '__main__':
    app.run()
