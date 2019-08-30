import json

def sampleLambda(event, context):
    #json dumps like JSON.stringify just serializes json
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
