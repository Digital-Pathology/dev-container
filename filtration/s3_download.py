import re
import os


def download_file_from_s3(image_folder, bucket, s3_client):
    """Download a file from a folder in an S3 bucket
    :param image_folder: folder containing preprocessed images for a whole image
    :param bucket: bucket from which to download file(s)
    :param s3_client: a low-level client representing Amazon Simple Storage Service (S3)
    :return: void
    """
    images = []
    image_dir = f'local_images/{image_folder}'

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for x in bucket.objects.all():
        if f'Preprocessing/{image_folder}' in x.key:
            images.append(x.key)

    images.sort(key=lambda x: x[1])

    for image in images:
        file_name = re.search('([^\/]+$)', image).group()
        save_path = os.path.join('local_images', image_folder, f'{file_name}')
        s3_client.download_file('digpath-data', image, save_path)
