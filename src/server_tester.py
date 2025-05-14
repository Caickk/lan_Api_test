import requests
import json
#docker-compose up --build
#Acesse no navegador:
#http://localhost:8001/api/consumir/
#Você verá algo como:
#{"mensagem": "Olá do servidor2!"}


# servidor1 acessa servidor2
response = requests.get('http://localhost:8001/api/consumir/')
print(response.json())