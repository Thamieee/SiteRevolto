from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", username = nome_usuario)

if __name__ == "__main__":
    app.run(debug = True)
