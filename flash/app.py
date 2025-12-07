from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'amo_spfc'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem', methods=['POST'])
def enviar_mensagem():
    flash('Mensagem para aprender flash!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)