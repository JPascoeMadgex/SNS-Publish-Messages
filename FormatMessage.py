import json

class MessageFormatter:
    def __init__(self, input_file='raw_messages.json', output_file='message_data.json'):
        self.input_file = input_file
        self.output_file = output_file

    def format_messages(self):
        # Read the JSON file containing multiple raw messages
        with open(self.input_file, 'r') as file:
            raw_messages = json.load(file)

        formatted_messages = {"Messages": []}

        # Iterate over each raw message
        for sqs_message in raw_messages['RawMessages']:
            # Extract relevant fields
            topic_arn = sqs_message['TopicArn']
            subject = sqs_message['Subject']
            message_content = sqs_message['Message']
            message_attributes = sqs_message['MessageAttributes']

            # Format the data to match message_data.json structure
            formatted_message = {
                "TopicArn": topic_arn,
                "Subject": subject,
                "MessageContent": message_content,
                "MessageAttributes": {
                    key: { 
                        "Type": attr['Type'],
                        "Value": attr['Value']
                    } for key, attr in message_attributes.items()
                }
            }

            # Add the formatted message to the list
            formatted_messages["Messages"].append(formatted_message)

        # Save the formatted data to a new JSON file
        with open(self.output_file, 'w') as file:
            json.dump(formatted_messages, file, indent=2)

        print(f"Formatted message data saved to {self.output_file}")