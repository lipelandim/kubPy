import boto3

from Model.user import user
from Model.clients import clients
from Data.dataValue import dataValue

dt = dataValue()

class clientRepository:
    #repository getData

    def getAllClients(self):
        
        table = dt.retTable('Clients')
        response = table.scan()

        return response


    def putCLient(self, client):
        input = {
            'document': client.document,
            'name': client.name,
            'phone': client.phone,
            'email': client.email
         }
        
        table = dt.retTable('Clients')
        
        response = table.put_item(Item=input)

        return response
