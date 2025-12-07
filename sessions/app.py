from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'eu_amo_muito_o_spfc' 

@app.route('/')
def index():
    if 'usuario' in session:
        return render_template('painel.html', nome=session['usuario'])
    
    return render_template('login.html')

@app.route('/fazer-login', methods=['POST'])
def login():
    nome_digitado = request.form['nome_usuario']
    
    session['usuario'] = nome_digitado
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)