from pprint import pprint
from fastapi import FastAPI
import boto3

from Model.user import user
from Model.clients import clients
from Controller.clientController import clientController

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Hello": "World"}

# Criar base de dados

base_de_dados = [
    user(id=1, email="felipe@landim.com.br", password="landim123"),
    user(id=2, email="teste@teste.com.br", password="teste123")
]

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for user in base_de_dados:
        if(user.id == id_usuario):
            return user
    
    return {"Status": 404, "Mensagem": "Não encontrou usuario"}

# Rota Insere
@app.post("/usuarios")
def insere_usuario(user: user):
    # criar regras de negocio
    base_de_dados.append(user)
    return user


# Rota Insere
@app.post("/clients")
def insere_usuario(clients: clients):
    # criar regras de negocio
    cliContr = clientController()
    response = cliContr.putClient(clients)
    
    return response



# Rota Insere
@app.get("/clients")
def search_all_clients():
    # criar regras de negocio
    cliContr = clientController()
    response = cliContr.getAllClients()
    return response




#add new client 
def put_client(document, name, email, phone, dynamodb=None):
    
    cliContr = clientController()
    
    response = table.put_item(Item=input)
    return response




#criar tabela clients

 

'''

# Rota Insere
@app.post("/createtableclients")
def insere_usuario():
    # criar tabela
    return create_clients_table()
    

def create_clients_table(dynamodb=None):
    if not dynamodb:
           dynamodb = boto3.resource('dynamodb', 
                                  aws_access_key_id="anything",
                                  aws_secret_access_key="anything",
                                  region_name='us-west-2', 
                                  endpoint_url="http://localhost:8000")


    table = dynamodb.create_table(
        TableName='Clients',
        KeySchema=[
            {
                'AttributeName': 'document',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'name',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'document',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


'''