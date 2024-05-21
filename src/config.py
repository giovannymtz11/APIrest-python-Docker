class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'databaseserver' 
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password' 
    MYSQL_DB = 'itl'

config = {
    'development': DevelopmentConfig
}
