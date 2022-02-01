from cgi import test
import os
import cv2
from RegionFilter import *

test_dir = 'test_images'
test_files = os.listdir(test_dir)

labels = None


def test_filter(img):
    black_and_white_filter: RegionFilter = RegionFilterBlackAndWhite()
    hsv_filter: RegionFilter = RegionFilterHSV()
    return black_and_white_filter(img) and hsv_filter(img)


if __name__ == "__main__":
    for image in os.listdir(test_dir):
        path = f'{test_dir}/{image}'
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if '/x' in path and not test_filter(img):
            print('filter works for x')
        elif '/o' in path and test_filter(img):
            print('filter works for o')
        else:
            print(path, test_filter(img))
