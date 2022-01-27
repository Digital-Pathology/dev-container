
import os
import cv2
from RegionFilter import *

from RegionFilter import RegionFilter

test_dir = 'test_images'
test_files = os.listdir(test_dir)

labels = None

def test_filter(filter: RegionFilter):

    for image in os.listdir(test_dir):
        path = f'{test_dir}/{image}'
        img = cv2.imread(path)

        # ds = gdal.Open()
        # fn = ""
        # split_image(ds, fn)
    ### TODO
    pass
