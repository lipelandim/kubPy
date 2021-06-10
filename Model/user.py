from pydantic import BaseModel

# Criar model
class user(BaseModel):
    id: int
    email: str
    password: str