from flask import Flask

#Rutas
from  .routes import dashboar_MEDRoute, IndexRoute, login_route

app = Flask(__name__)


def init_app (config):
    #configuracion basica
    app.config.from_object(config)

    #blueprints
    app.register_blueprint(IndexRoute.main, url_prefix='/')
    app.register_blueprint(dashboar_MEDRoute, url_prefix='/auth')
    app.register_blueprint(login_route, url_prefix='/login')
    return app