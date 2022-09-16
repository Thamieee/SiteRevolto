import os
import psycopg2
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USERNAME'] = 'noreply.revoltosoftware@gmail.com'
app.config['MAIL_PASSWORD'] = 'uyimtytcszuwqcjg'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ('Revolto Software', 'noreply.revoltosoftware@gmail.com')
mail = Mail(app)

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

# @app.route("/usuario/<nome_usuario>")
# def usuario(nome_usuario):
#     return render_template("usuario.html", username = nome_usuario)

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

if __name__ == "__main__":
    app.run(debug = True)
