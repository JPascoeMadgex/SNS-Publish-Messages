import boto3
import json
from icecream import ic
from FormatMessage import MessageFormatter

# Format the messages
formatter = MessageFormatter()
formatter.format_messages()

# Read the JSON file
with open('message_data.json', 'r') as file:
    data = json.load(file)

# Create a session using the specified profile

# Initialize the SNS client with the session
sns_client = boto3.client(
    'sns', 
    region_name='eu-west-1', 
    endpoint_url='http://localhost:4566'
    )

# Iterate over each message in the JSON data
for message in data['Messages']:
    topic_arn = message['TopicArn']
    subject = message['Subject']
    message_content = message['MessageContent']
    message_attributes = message['MessageAttributes']

    # Publish the message to the SNS topic
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message_content),
        Subject=subject,
        MessageAttributes={
            key: {
                'DataType': attr['Type'],
                'StringValue': attr['Value']
            } for key, attr in message_attributes.items()
        }
    )
    ic(response)