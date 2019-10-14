import json
import time
import requests
import os
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

def save_log(logData):
    firebaseProject = "https://awesome-56c60.firebaseio.com/"
    url = firebaseProject+"/logs.json"
        
    response = requests.post(url=url, 
                            data=json.dumps(logData))
    result = json.loads(response.text)
    return result
    
def save_dynamodb_log(logData):
    timestamp = str(datetime.utcnow().timestamp())

    table = dynamodb.Table('loggingTable')
    
    item = {
        'itemId': str(uuid.uuid1()),
        'text': "Just testing",
        'createdAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)


def lambda_handler(event, context):
    method = event.get('httpMethod','GET') 

    if method == 'GET':
        # Look for the path on GETs
        path = event.get('path','/hello/index.html')
        # Return the contents of local files on GETs
        if path == "/hello/" or path == "/hello": 
            path = "/hello/index.html"
        file = path.replace("/hello/","")
        with open(file, 'r') as f:
            page = f.read()
        return {
            "statusCode": 200,
            "headers": {
            'Content-Type': 'text/html',
            },
            "body": page
        }
        
    if method == 'POST':
        body = json.loads(event.get('body','{}'))
 
        result = save_log(body)
        save_dynamodb_log(body)
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "loggedData":body,
                "result":result # "os": str(list(os.environ.keys()))
            }),
        }
