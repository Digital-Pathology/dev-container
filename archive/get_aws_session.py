import boto3
# from osgeo import gdal
import os
import re
import sys


def aws_session(aws_access_key_id, aws_secret_access_key, aws_session_token):

    region_name = 'us-east-1'

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=region_name)

    s3_client = boto3.client('s3',
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key,
                             aws_session_token=aws_session_token)

    # gdal.SetConfigOption("AWS_ACCESS_KEY_ID", aws_access_key_id)
    # gdal.SetConfigOption("AWS_SECRET_ACCESS_KEY", aws_secret_access_key)
    # gdal.SetConfigOption("AWS_SESSION_TOKEN", aws_session_token)
    # gdal.SetConfigOption('AWS_REGION', region_name)

    return session, s3_client


def get_s3_resource(aws_credentials_path):

    # aws_config_path = os.path.abspath('AWSConfig')
    # aws_credentials_path = os.path.join(aws_config_path, 'credentials')

    if not os.path.isfile(aws_credentials_path):
        raise FileNotFoundError

    if aws_credentials_path not in sys.path:
        sys.path.append(aws_credentials_path)

    with open(aws_credentials_path, 'r') as f:
        match = re.split('\n', f.read())
        tokens = list(filter(lambda x: 'aws' in x, match))
        for token in tokens:
            split = token.split('=')
            if split[0] == "aws_access_key_id":
                aws_access_key_id = split[1]
            elif split[0] == "aws_secret_access_key":
                aws_secret_access_key = split[1]
            elif split[0] == "aws_session_token":
                aws_session_token = split[1]

    return aws_session(aws_access_key_id, aws_secret_access_key, aws_session_token)
