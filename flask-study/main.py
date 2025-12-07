from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vitoria')
def vitoria():
    dados = {'nome':'vitoria', 'idade': '16', 'curso':'ds', 'escola':'ifsp'}
    idade_int = int(dados['idade'])
    habilidades = ['comunicação', 'inglês', 'liderança']

    return render_template('vitoria.html', dados=dados, idade=idade_int, habilidades=habilidades)

@app.route('/ola/<user>')
def ola(user):
    return f'olá,{user} '

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method=='POST':
        nome = request.form['nomeForm']
        email = request.form['emailForm']
        print(f" Nome: {nome}")
        print(f" Email: {email}")
        return render_template('formulario.html', nome=nome, email=email)
    else:
        return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)