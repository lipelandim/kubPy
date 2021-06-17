import boto3

from Model.clients import clients
from Repository.clientRepository import clientRepository

class clientController():
    def getAllClients(self):
        cliRep = clientRepository()
        response = cliRep.getAllClients()
        return response

    def putClient(self, clients):
        cliRep = clientRepository()
        response = cliRep.putCLient(clients)
        return response

