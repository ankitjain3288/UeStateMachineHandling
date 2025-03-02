import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UEStateTable')

def lambda_handler(event, context):
    ue_id = event['ue_id']
    new_state = event['state']

    table.put_item(
        Item={
            'UE_ID': ue_id,
            'CurrentState': new_state,
            'LastUpdated': datetime.utcnow().isoformat()
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'UE_ID': ue_id, 'NewState': new_state})
    }
