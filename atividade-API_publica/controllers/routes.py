from flask import render_template, request, url_for, redirect
from models.database import db, Game, Console
import urllib # Permite ler a url de uma API
import json # Faz a conversão de dados para JSON em um dicionário de dados

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

 

    # Rota de catálogo de jogos (Consumo da API)
    @app.route("/apidnd", methods=['GET', 'POST'])
    @app.route('/apidnd/<int:id>', methods=['GET', 'POST'])
    def apidnd(id=None):       
        BASE_URL = "https://www.dnd5eapi.co/api/2014"
        response = urllib.request.urlopen(BASE_URL + "/races") 
        apiData = response.read() # lê a resposta da API
        raceList = json.loads(apiData) # converte JSON para dicionário
        
        if id:
            raceInfo = []
            for race in raceList:
               if race['id'] == id:
                   raceInfo = race
                   break
                
        #     if raceInfo:
        #         return render_template("raceInfo.html", raceInfo=raceInfo)
        #     else:
        #         return f'Não foi possível encontrar uma raça com esse ID: {id}!'
                
        return render_template("apidnd.html", raceList=raceList)
        