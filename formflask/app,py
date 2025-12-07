from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'sao_paulo_maior_time_do_brasil'


@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        username = request.form['usernameForm']
        email = request.form['emailForm']
        password = request.form['passwordForm']

        session['ultimo_cadastro'] = {
            'username': username,
            'email': email,
            'password': password
        }
        
        flash(f'Olá, {username}! Seu cadastro foi concluído com sucesso!', 'success')
        return redirect(url_for('formulario'))

    return render_template('formulario.html')

@app.route('/dados')
def dados():

    info_ultimo_user = session.get('ultimo_cadastro')
    
    return render_template('dados.html', ultimo_usuario_sessao=info_ultimo_user)

if __name__ == '__main__':
    app.run(debug=True)