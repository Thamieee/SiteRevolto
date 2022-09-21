from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_migrate import Migrate

from utils.logging_console import LoggingConsole
from models.user import db
from routes.user_blueprint import user_bp

logger = LoggingConsole(component="Revolto Software Site Logger")
logger.log_info("Inicializando aplicação")


app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)
app.register_blueprint(user_bp, url_prefix='/usuario')

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("homepage.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        msg = Message("Teste", recipients = ["noreply.revoltosoftware@gmail.com"])
        msg.body = "Testando envio de e-mail pelo Flask"
        mail.send(msg)
        return "Message sent!"
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/jogos")
def jogos():
    return render_template("jogos.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/jogos/oniriko")
def oniriko():
    return render_template("oniriko.html")


logger.log_info("Inicialização completa")

if __name__ == "__main__":
    app.run(debug = True)
