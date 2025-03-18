from flask import render_template, request, redirect, url_for
#lista de npcs
npcs =['Abigail', 'Seah', 'Sebastian', 'Harley', 'Alex,', 'Harvey', 'Emily', 'Maru', 'Eliot', 'Shane']

#Aret de objetos - Lista de games
gamelist = [{
            'Titulo' : 'Stardew Valley',
            'Ano' : 2016,
            'Categoria': 'Simulação',
        }]
consolelist = [{
    'Nome' : 'Playstation 5',
    'Fabricante' : 'Sony',
    'Ano' : '2020',
    'Preco' : '500',
}
]
        
def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no python
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]

        
        #Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            #Verificar se o campo jofador existe
            if request.form.get('npc'):
                #
                npcs.append(request.form.get('npc'))
            return redirect(url_for('games'))
                
        
        jogos = ['Rinworld', 'Roblox', 'Minecraft', 'Terraria', 'TickTowers', 'Infinity Nikki']
        return render_template('games.html', 
                               game=game, 
                               npcs=npcs, 
                               jogos=jogos)
        
        
    #Rota de cadastro de jogos (em dicionario)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            #existe valor para um input de nome titulo?
            if request.form.get('titulo') and request.form.get ('ano') and request.form.get('categoria'):
                gamelist.append({'Titulo' : request.form.get('titulo'), 
                                 'Ano' : request.form.get('ano'), 
                                 'Categoria' : request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)
        
        
        
        
    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get ('fabricante') and request.form.get('ano') and request.form.get('preco'):
                consolelist.append({'Nome' : request.form.get('nome'),
                                 'Fabricante' : request.form.get('fabricante'),  
                                 'Ano' : request.form.get('ano'), 
                                 'Preco' : request.form.get('preco')})
                return redirect(url_for('consoles'))
        return render_template('consoles.html',
                                   consolelist=consolelist)
            