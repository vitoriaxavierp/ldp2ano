from flask import Flask, redirect, render_template, url_for, make_response, request
from db import db
from models import Login


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db.init_app(app)




usuario_cadastrado = 'admin'
senha_cadastrada = '123'


@app.route('/', methods=('GET', 'POST'))
def login():


   mensagem = 'Logado com sucesso'
   if request.method == 'POST':
       usuario = request.form['userForm']
       senha = request.form['senhaForm']


       usuario_cadastrado = 'admin'
       senha_cadastrada = '123'
       mensagem = 'Não'


       new_login = Login(usuario=usuario, senha=senha)


       if usuario == usuario_cadastrado and senha == senha_cadastrada:
           resposta =  make_response(redirect(url_for('bemvindo')))
           resposta.set_cookie('username', usuario, max_age=60*10)


           return resposta
       else:
           mensagem = 'Usuário ou senha inválido'


           return render_template('home.html', error=mensagem)
      
   else:
       return render_template('home.html', error=mensagem)


@app.route('/bemvindo')
def bemvindo():
   username = request.cookies.get('username')


   if not username:
       return redirect(url_for('login'))
  
   return render_template('bemvindo.html', user=username)


@app.route('/logout')
def logout():
   resposta = make_response(redirect(url_for('login')))


   resposta.set_cookie('username', '', expires=0)


   return resposta


  


if __name__ == '__main__':
   with app.app_context():
       db.create_all()


   app.run(debug=True)




