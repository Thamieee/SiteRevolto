from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from utils.logging_console import LoggingConsole
from utils.enforcement_functions import *

from datetime import date

logger = LoggingConsole(component="Revolto Software Site Logger")
logger.log_info("Inicializando aplicação")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/revolto_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app.config["SECRET_KEY"] = os.environ["SECRET_KEY"] (required to use flash())
app.config["SECRET_KEY"] = "23eae2cc4fc2aea77a2bd85baadcb755c21973d931466f95"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
# app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_USERNAME"] = "noreply.revoltosoftware@gmail.com"
app.config["MAIL_PASSWORD"] = "uyimtytcszuwqcjg"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_DEFAULT_SENDER"] = ("Revolto Software", "noreply.revoltosoftware@gmail.com")
mail = Mail(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    date_added = db.Column(db.Date())

    def __init__(self, email: str, username: str, password: str,
                 is_admin: bool = False, date_added: date = None):
        self.email = email
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.date_added = date_added

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"


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

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        data = request.form
        test = check_user_form(data)
        if test:
            new_user = User(
                email=data["email"],
                username=data["username"],
                password=data["password"],
                date_added=(date.today())
            )
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.username} has been created successfully."}
    return render_template("cadastro.html")

@app.route("/usuario/<username>", methods=['GET', 'PUT', 'DELETE'])
def usuario(username):
    user = User.query.get_or_404(username)

    if request.method == "GET":
        return render_template("usuario.html", username=username)

    elif request.method == "PUT":
        data = request.form
        user.email = data["email"]
        user.username = data["username"]
        user.password = data["password"]
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {user.username} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.username} successfully deleted."}

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
