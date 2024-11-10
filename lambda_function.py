import business.webhook
import json

def lambda_handler(event, context):
    print(str(event), str(context))

    business.webhook.create_event(json.loads(event["body"]))

    return {
        'statusCode': 200
    }
