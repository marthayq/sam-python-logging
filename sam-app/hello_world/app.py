import json

# import requests


def lambda_handler(event, context):
    method = event.get('httpMethod','GET') 

    if method == 'GET':
        # Return the contents of index.html on GETs
        with open('index.html', 'r') as f:
            indexPage = f.read()
        return {
            "statusCode": 200,
            "headers": {
            'Content-Type': 'text/html',
            },
            "body": indexPage
        }
        
    if method == 'POST':
        # Todo: Configure post method to log posts
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Will log all posts"
            }),
        }
