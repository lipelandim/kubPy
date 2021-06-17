from pydantic import BaseModel

# Criar model
class clients(BaseModel):
    name: str
    email: str
    phone: str
    document: str