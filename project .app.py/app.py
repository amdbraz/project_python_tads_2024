from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo para armazenar o jogador
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    level = db.Column(db.Integer, default=1)
    exp = db.Column(db.Integer, default=0)
    attribute = db.Column(db.Integer, default=100)

# Requisitos de EXP por nível
def exp_para_subir_nivel(nivel):
    if nivel == 1:
        return 100
    else:
        return int(100 * (1.4 ** (nivel - 1)))

# Função para subir de nível
def subir_de_nivel(player):
    player.level += 1
    player.attribute = int(player.attribute * 1.5)
    db.session.commit()

# Rota inicial
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        player = Player(name=name)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for("game", player_id=player.id))
    return render_template("index.html")

# Rota do jogo
@app.route("/game/<int:player_id>", methods=["GET", "POST"])
def game(player_id):
    player = Player.query.get_or_404(player_id)
    mensagem = None

    if request.method == "POST":
        action = request.form["action"]

        if action == "explore":
            tipo_monstro = random.choice(["fraco", "medio", "dificil", "chefe"])
            exp_ganha = {"fraco": 50, "medio": 100, "dificil": 200, "chefe": 500}[tipo_monstro]
            mensagem = f"Você enfrentou um monstro {tipo_monstro} e ganhou {exp_ganha} de experiência!"
            player.exp += exp_ganha
            exp_necessaria = exp_para_subir_nivel(player.level)

            if player.exp >= exp_necessaria:
                subir_de_nivel(player)
                mensagem += f" Parabéns! Você subiu para o nível {player.level}."

            db.session.commit()

    return render_template("game.html", player=player, mensagem=mensagem)

# Inicialização do banco de dados
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
