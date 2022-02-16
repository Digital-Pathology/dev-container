from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import logging


def upload_file_to_s3(file_name, s3_client):
    """Upload a file to an S3 bucket

    :param file_name: file name of image to upload
    :param s3_client: a low-level client representing Amazon Simple Storage Service (S3)
    :return: True if file was uploaded, else False
    """

    folder = 'Preprocessing'

    # Upload the file
    try:
        s3_client.upload_file(
            Filename=f'local_images/{file_name}', Bucket='digpath-data', Key=f'{folder}/{file_name}')
        print(file_name, "uploaded successfully")
    except ClientError as e:
        logging.error(e)
        return False
    except NoCredentialsError:
        print("Credentials not available or expired")
        return False

    return True
