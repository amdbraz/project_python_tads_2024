from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Variáveis globais para o jogo
jogador = {
    "nome": "",
    "nivel": 1,
    "exp": 0,
    "moedas": 0,
    "atributo": 100
}

def exp_para_subir_nivel(nivel):
    """Calcula a experiência necessária para subir de nível."""
    return 100 * (1.4 ** (nivel - 1))

def subir_de_nivel():
    """Lógica para subir de nível."""
    jogador["nivel"] += 1
    jogador["atributo"] = int(jogador["atributo"] * 1.5)
    jogador["moedas"] += 10  # Recompensa ao subir de nível

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    jogador["nome"] = request.form['nome']
    jogador["nivel"] = 1
    jogador["exp"] = 0
    jogador["moedas"] = 0
    jogador["atributo"] = 100
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    mensagem = None
    if request.method == 'POST':
        acao = request.form.get('acao')

        if acao == "abrir_bau":
            jogador["moedas"] += 50
            mensagem = "Você abriu o baú e ganhou 50 moedas!"
        elif acao == "enfrentar_monstro":
            jogador["exp"] += 50
            mensagem = "Você enfrentou um monstro e ganhou 50 de experiência!"
            if jogador["exp"] >= exp_para_subir_nivel(jogador["nivel"]):
                subir_de_nivel()
                mensagem += " Parabéns! Você subiu para o nível {}!".format(jogador["nivel"])
        elif acao == "sair_caverna":  # Nova ação
            mensagem = "Você saiu da caverna. Fim da aventura por hoje!"

    return render_template('game.html', jogador=jogador, mensagem=mensagem, exp_necessaria=exp_para_subir_nivel(jogador["nivel"]))

if __name__ == '__main__':
    app.run(debug=True)
