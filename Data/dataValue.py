import boto3


class dataValue:
    def retTable(self, tableName):
        dynamodb = boto3.resource('dynamodb', 
                                    aws_access_key_id="anything",
                                    aws_secret_access_key="anything",
                                    region_name='us-west-2', 
                                    endpoint_url="http://localhost:8000")

        table = dynamodb.Table(tableName)

        return table