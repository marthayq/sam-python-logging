import json
import time
import requests
import os
import boto3
from datetime import datetime
##import uuid

dynamodb = boto3.resource('dynamodb')

def save_log(logData):
    # Comment out one or both of these
    result = save_firebase_log(logData)
    result = save_dynamodb_log(logData)

    return result
    
def save_firebase_log(logData):
    firebaseProject = "https://awesome-56c60.firebaseio.com/"
    url = firebaseProject+"/logs.json"
    
    timestamp = str(datetime.utcnow().timestamp())
    
    log = logData.copy() # A shallow copy
    log['createdAt'] = timestamp

    response = requests.post(url=url,
                            data=json.dumps(log))
                            
    result = json.loads(response.text)
    return result
    
def save_dynamodb_log(logData):
    timestamp = str(datetime.utcnow().timestamp())

    table = dynamodb.Table('loggingTable')
    
    log = logData.copy() # A shallow copy
    log['itemId'] = str(timestamp) #str(uuid.uuid1()) for more granular keys
    log['createdAt'] = timestamp
    

    # write logData to dynamoDB
    table.put_item(Item=log)
    return logData

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

        return {
            "statusCode": 200,
            "body": json.dumps({
                "loggedData":body,
                "result":result
            }),
        }
