# SNS-Publish-Messages

This project formats and publishes messages to AWS SNS (Simple Notification Service) using Python.

## Prerequisites

- Python 3.x
- AWS CLI configured with your credentials
- LocalStack (for local AWS services testing)

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd SNS-Publish-Messages
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Publish the formatted messages to SNS:
   ```sh
   python PublishMessage.py
   ```

## Files

- `FormatMessage.py`: Contains the `MessageFormatter` class to format raw messages.
- `PublishMessage.py`: Publishes the formatted messages to SNS.
- `raw_messages.json`: Input file containing raw messages.
- `message_data.json`: Output file containing formatted messages.
- `requirements.txt`: Lists the required Python packages.

## Example

1. Add your raw messages to `raw_messages.json` in the following format:

   ```json
   {
     "RawMessages": [
       {
         "TopicArn": "arn:aws:sns:region:account-id:topic-name",
         "Subject": "Subject of the message",
         "Message": "Content of the message",
         "MessageAttributes": {
           "AttributeKey": {
             "Type": "String",
             "Value": "AttributeValue"
           }
         }
       }
     ]
   }
   ```

2. Run the publisher script as described in the Usage section.
