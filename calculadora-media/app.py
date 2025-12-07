from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():

    return render_template('formulario.html')

@app.route('/calcular', methods=['POST'])
def calcular_media():

    nome_aluno = request.form['nome']
    nota1 = float(request.form['n1'])
    nota2 = float(request.form['n2'])

    media_final = (nota1 + nota2) / 2


    situacao = "Aprovado" if media_final >= 6 else "Reprovado"

    return render_template('resultado.html', nome=nome_aluno, media=media_final, status=situacao)

if __name__ == '__main__':
    app.run(debug=True)