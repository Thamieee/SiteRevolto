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
