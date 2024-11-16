from flask import Flask
from config import config
from source.models.modelo_usuario import modelo_usuario

app = Flask(__name__)

if __name__ == '__main__':
    modelo_usuario.get_usuario_list()
    app.config.from_object(config['development'])
    app.run()