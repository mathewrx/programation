from flask import Flask,render_template,request
app= Flask(__name__)


@app.route("/")
def carai():
    return render_template("inicio.html")

@app.route("/listagem_receitas")
def listagem():
    return render_template("listagem_receitas.html")

@app.route("/cadastrar_receitas")
def cadastro():
    return render_template("cadastrar_receitas.html")






app.run(debug=True)
