from flask import Blueprint, render_template, request
from flask_mail import Message

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def homepage():
    return render_template("homepage.html")

@main.route("/contato", methods=["GET", "POST"])
def contato():
    from main import mail
    if request.method == "POST":
        msg = Message("Teste", recipients = ["noreply.revoltosoftware@gmail.com"])
        msg.body = "Testando envio de e-mail pelo Flask"
        mail.send(msg)
        return "Message sent!"
    return render_template("contato.html")

@main.route("/sobre")
def sobre():
    return render_template("sobre.html")

@main.route("/jogos")
def jogos():
    return render_template("jogos.html")

@main.route("/blog")
def blog():
    return render_template("blog.html")

@main.route("/jogos/oniriko")
def oniriko():
    return render_template("oniriko.html")

