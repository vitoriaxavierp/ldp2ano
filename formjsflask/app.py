from flask import Flask, render_template, redirect, url_for, request, flash, make_response


app = Flask(__name__)
app.secret_key = 'sao_paulo_maior_time'


@app.route('/', methods=['GET', 'POST'])
def form():
   username = ''
   password = ''
   email = ''


   if request.method == 'POST':
       username = request.form['usernameForm']
       password = request.form['passwordForm']
       email = request.form['emailForm']
       flash(f'{username}, seu cadastro foi concluido com sucesso!')
      
   return render_template('formulario.html', password=password, username=username, email=email)


@app.route('/dados')
def dados():
   return render_template('dados.html')


if __name__ == '__main__':
   app.run(debug=True)
