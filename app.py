from flask import Flask, render_template, request, render_template_string, send_file
from controllers.importar import importar

app = Flask(__name__)

# Adicionar rota para importar arquivo
@app.route("/", methods=["GET"])
def get_importar():
    return render_template("importar.html")

@app.route("/importar", methods=["POST"])
def post_importar():
    arquivo = request.files.get("arquivocsv")
    if arquivo:
        importar(arquivo)
        return render_template_string("<h1>Funcionou</h1>")
    else:
        return render_template_string("<h1>erro</h1>")

# from flask import send_file
@app.route("/download")
def baixar_relatorio():
    return send_file(
        "relatorio.pdf"
    )

app.run(debug=True)