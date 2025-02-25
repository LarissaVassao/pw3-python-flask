from flask import render_template, request

npcs =['Abigail', 'Seah', 'Sebastian', 'Harley', 'Alex,', 'Harvey', 'Emily', 'Maru', 'Eliot', 'Shane']
        
def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no python
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        #dicionario em python (objeto)
        game = {
            'Titulo' : 'Stardew Valley',
            'Ano' : 2016,
            'Categoria': 'Simulação',
        }
        
        
        #Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            #Verificar se o campo jofador existe
            if request.form.get('npc'):
                npcs.append(request.form.get('npc'))
                
        
        jogos = ['Rinworld', 'Roblox', 'Minecraft', 'Terraria', 'TickTowers', 'Infinity Nikki']
        return render_template('games.html', game=game, npcs=npcs, jogos=jogos)