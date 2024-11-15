import traceback


main = Blueprint('index_blueprint',__name__)

@main.route('/')
def index():
    return "Hola Insectos..."