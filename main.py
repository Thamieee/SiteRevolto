from flask import Flask, render_template

revolto = Flask(__name__)

@revolto.route("/")
def homepage():
    return render_template("homepage.html")

@revolto.route("/contato")
def contato():
    return render_template("contato.html")

@revolto.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", username=nome_usuario)

if __name__ == "__main__":
    revolto.run(debug = True)
