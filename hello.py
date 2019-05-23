import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):

    # init
    name = 'World !'

    # retrieve payload
    logger.info('Event : {}'.format(event))
    if 'body' in event:
        # payload from API Gateway needs to be converted from string to json
        payload = json.loads(event['body'])
    else:
        payload = event

    # retrieve parameter
    logger.info('Payload : {}'.format(payload))
    if 'name' in payload:
        name = payload['name']

    # response
    logger.info('Name : {}'.format(name))
    headers = {'Content-type': 'application/json'}
    body = {'Message': 'Hello ' + name}
    response = {
        'statusCode': 200,
        'headers': headers,
        'body' : json.dumps(body)
    }
    return response
