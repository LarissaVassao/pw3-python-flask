from flask import Flask
from models.database import db
import mysql.connector
from mysql.connector import errorcode
 
app = Flask(__name__, template_folder='views')
 
DB_NAME = 'galeria'  # Corrija o nome aqui
app.config['DATABASE_NAME'] = DB_NAME
 
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database=DB_NAME
    )
    return connection
 
def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"O banco de dados {DB_NAME} está criado!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar o banco de dados: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
 
if __name__ == "__main__":
    create_database()  # Cria banco, se necessário
 
    # Inicializa SQLAlchemy com o app
    db.init_app(app)
 
    # Cria as tabelas a partir dos models (se ainda não existirem)
    with app.app_context():
        db.create_all()
 
    # Inicia o servidor Flask
    app.run(host='localhost', port=5000, debug=True)
 