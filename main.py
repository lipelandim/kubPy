from fastapi import FastAPI

from Model.user import user
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
