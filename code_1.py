import boto3
from botocore.exceptions import ClientError
import logging

# function to put item to dynamodb


def put_item(table_name, item):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    try:
        response = table.put_item(Item=item)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# function to delete item from dynamodb
def delete_item(table_name, key):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    try:
        response = table.delete_item(Key=key)
    except ClientError as e:
        logging.error(e)
        return False
    return True
