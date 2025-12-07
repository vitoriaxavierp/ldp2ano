from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    usuario = request.cookies.get('nome_usuario')
    return render_template('index.html', usuario=usuario)

@app.route('/set-cookie')
def definir_cookie():
    resposta = make_response(redirect(url_for('index')))
    resposta.set_cookie('nome_usuario', 'Aluno_IFSP')
    return resposta

@app.route('/delete-cookie')
def deletar_cookie():
    resposta = make_response(redirect(url_for('index')))
    resposta.set_cookie('nome_usuario', '', expires=0)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)