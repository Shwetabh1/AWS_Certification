# lambda function blueprint
"""
import json

def sampleLambda(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
)
"""
import boto3  # pip install boto3 just like aws-sdk in node
# https://pypi.org/project/boto3/

client = boto3.client('lambda')

# consider we have a lambda function called sampleLambda, written above
# I will send some payload

response = client.invoke(
    FunctionName='sampleLambda',
    # InvocationType='RequestResponse' is by default
    LogType='Tail',
    Payload='Some Payload' # This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type
)
print(response)

"""
Invocation type event is used for asynchronus execution. 
An asynchronously executed AWS Lambda function doesn't return the result of execution
https://stackoverflow.com/questions/39456309/using-boto-to-invoke-lambda-functions-how-do-i-do-so-asynchronously
"""
