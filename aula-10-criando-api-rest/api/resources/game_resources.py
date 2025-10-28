from flask_restful import Resource
from api import api

#respostas da  api
class GameList(Resource):
    def get(self):
        return "Bem vindo a API The Games!!!"
    
    #criando o endpoint (rota principal da api)
api.add_resource(GameList, '/games')