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
    #dicionario em python (objeto)
    game = {
        'Titulo' : 'Stardew Valley',
        'Ano' : 2016,
        'Categoria': 'Simulação',
    }
    
    npcs =['Abigail', 'Seah', 'Sebastian', 'Harley', 'Alex,', 'Harvey', 'Emily', 'Maru', 'Eliot', 'Shane']
    jogos = ['Rinworld', 'Roblox', 'Minecraft', 'Terraria', 'TickTowers', 'Infinity Nikki']
    return render_template('games.html', game=game, npcs=npcs, jogos=jogos)



# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado.
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    