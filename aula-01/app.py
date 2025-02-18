# Importando o Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views') 


# Criando a primeira rota do site
@app.route('/')
# Criando função no python
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    titulo = 'Stardew Valley'
    ano = 2016
    categoria = 'Simulação'
    npcs =['Abigail', 'Seah', 'Sebastian', 'Harley', 'Alex,', 'Harvey', 'Emily', 'Maru', 'Eliot', 'Shane']
    jogos = ['Rinworld', 'Roblox', 'Minecraft', 'Terraria', 'TickTowers', 'Infinity Nikki']
    return render_template('games.html', titulo=titulo, ano=ano, categoria=categoria, npcs=npcs, jogos=jogos)

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado.
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    