from flask import render_template, request, url_for, redirect
from models.database import db, Game, Console
import urllib
import json 

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

 

    @app.route("/apidnd", methods=['GET', 'POST'])
    @app.route('/apidnd/<id>', methods=['GET', 'POST'])
    def apidnd(id=None):       
        BASE_URL = "https://www.dnd5eapi.co"
        response = urllib.request.urlopen(BASE_URL + "/api/2014/races") 
        apiData = response.read() 
        data = json.loads(apiData)
        raceList = data["results"] 
        
        if id:
            raceInfo = []
            for race in raceList:
               if race['index'] == id:
                    response = urllib.request.urlopen(BASE_URL + race["url"])
                    apiData = response.read() 
                    raceInfo = json.loads(apiData)
                    print(raceInfo)
                    break
                
            if raceInfo:
                
                return render_template("raceInfo.html", raceInfo=raceInfo)
            else:
               return f'Não foi possível encontrar uma raça com esse ID: {id}!'
             
                
        return render_template("apidnd.html", raceList=raceList)
        