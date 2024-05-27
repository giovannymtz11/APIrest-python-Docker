<<<<<<< HEAD
class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'databaseserver' 
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password' 
    MYSQL_DB = 'itl'

config = {
    'development': DevelopmentConfig
=======
import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'itl')

config = {
    'default': Config,
    'development': Config
>>>>>>> bba1099 (Dockerizacion exitosa)
}
