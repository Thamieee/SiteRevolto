from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail

from utils.logging_console import LoggingConsole
from models.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    db.init_app(app)
    mail = Mail(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)

    from models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from routes.blueprints import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from routes.blueprints import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


logger = LoggingConsole(component="Revolto Software Site Logger")
logger.log_info("Inicializando aplicação")

app = create_app()

logger.log_info("Inicialização completa")

if __name__ == "__main__":
    app.run(debug = True)
