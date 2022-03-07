import os
import cv2
from filter import *

test_dir = 'test_images'
test_files = os.listdir(test_dir)

labels = None


def test_filter(img):
    black_and_white_filter: Filter = FilterBlackAndWhite()
    hsv_filter: Filter = FilterHSV()
    focus_measure_filter: Filter = FilterFocusMeasure()
    return black_and_white_filter(img) and hsv_filter(img) and focus_measure_filter(img)[0]


def test_lens_filter(img):
    focus_measure_filter: Filter = FilterFocusMeasure()
    return focus_measure_filter(img)[1]


if __name__ == "__main__":
    for image in os.listdir(test_dir):
        path = f'{test_dir}/{image}'
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if '/x' in path and test_filter(img):
            print(image, "passes")
        elif '/o' in path and not test_filter(img):
            print(image, "does not pass")
        else:
            print(image, test_lens_filter(img))
