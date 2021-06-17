import boto3

from Model.user import user
from Model.clients import clients

class clientController():

    def getAllClients():
        # criar regras de negocio
        dynamodb = boto3.resource('dynamodb', 
                                aws_access_key_id="anything",
                                aws_secret_access_key="anything",
                                region_name='us-west-2', 
                                endpoint_url="http://localhost:8000")

        table = dynamodb.Table('Clients')
        response = table.scan()

        return response
