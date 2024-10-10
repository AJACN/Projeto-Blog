AMBIENTE = 'teste' #teste ou produção

if AMBIENTE == 'teste':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if AMBIENTE == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'TonyTony.mysql.pythonanywhere-services.com'
    DB_USER = 'TonyTony'
    DB_PASSWORD = 'youcankickthesword'
    DB_NAME = 'TonyTony$blog'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_PASSWORD = "youcankickthesword"
MASTER_EMAIL = "antonio.jairo.senai@gmail.com"