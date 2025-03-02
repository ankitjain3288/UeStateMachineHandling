import boto3
import json

eventbridge = boto3.client('events')

def lambda_handler(event, context):
    ue_id = event['ue_id']
    event_type = event['eventType']

    response = eventbridge.put_events(
        Entries=[
            {
                'Source': '5GCore',
                'DetailType': event_type,
                'Detail': json.dumps({'ue_id': ue_id})
            }
        ]
    )
    return response
