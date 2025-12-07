from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def home():
    peso = None
    altura = None
    indice = None
    mensagem = None
    nome = None
    
    if request.method == 'POST':
        peso_str = request.form['formPeso']
        altura_str = request.form['formAltura']
        nome = request.form['formNome']

        peso_float = 0.0
        altura_float = 0.0

        if peso_str:
            peso_float = float(peso_str)
        else:
            mensagem = "Erro: O campo Peso não pode estar vazio."
        
        if altura_str and not mensagem:
            altura_float = float(altura_str)
        elif not mensagem:
            mensagem = "Erro: O campo Altura não pode estar vazio."

        if not mensagem:
            if altura_float > 0:
                indice = peso_float / (altura_float * altura_float)
                mensagem = "Seu IMC foi calculado com sucesso!"
            else:
                mensagem = "Erro: A altura precisa ser maior que zero."
                indice = None
        
        return render_template('index.html',peso=peso_str,altura=altura_str,indice=indice,mensagem=mensagem, nome=nome)
            
    else:
        return render_template('index.html', peso=peso, altura=altura, indice=indice, mensagem=mensagem, nome=nome)

if __name__ == '__main__':
    app.run(debug=True)