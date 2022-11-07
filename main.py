from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


from utils.logging_console import LoggingConsole
from models.user_model import User, db
from routes.user_blueprint import user_bp
from routes.auth_blueprint import auth as auth_blueprint
from routes.main_blueprint import main as main_blueprint

logger = LoggingConsole(component="Revolto Software Site Logger")
logger.log_info("Inicializando aplicação")


app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)
bcrypt = Bcrypt(app)
app.register_blueprint(user_bp, url_prefix='/usuario')
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

logger.log_info("Inicialização completa")

if __name__ == "__main__":
    app.run(debug = True)
