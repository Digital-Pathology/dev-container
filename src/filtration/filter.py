
import abc
import numpy as np
import cv2

# TODO: Add docstrings to all classes, methods, and top of each file

class Filter(abc.ABC):

    def __call__(self, region) -> bool:
        return self.filter(region)

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def filter(self, region) -> bool:
        pass


class FilterBlackAndWhite(Filter):

    def __init__(self, filter_threshold=0.5, binarization_threshold=0.85, rgb_weights=[0.2989, 0.5870, 0.1140]):
        self.filter_threshold = filter_threshold
        self.binarization_threshold = binarization_threshold
        self.rgb_weights = rgb_weights
    
    def __str__(self):
        s = "FilterBlackAndWhite: {"
        s += f"filter_threshold:{self.filter_threshold}"
        s += " "
        s += f"binarization_threshold:{self.binarization_threshold}"
        s += " "
        s += f"rgb_weights:{self.rgb_weights}"
        s += "}"
        return s

    def filter(self, region) -> bool:
        greyscale_image = self.convert_rgb_to_greyscale(region)
        # if pixel is > 85% white, set value to 1 else 0
        binary_image = np.where(
            greyscale_image > self.binarization_threshold*255, 1, 0)
        # return True if average of binary image is less than 50% white
        return np.mean(binary_image) < self.filter_threshold

    def convert_rgb_to_greyscale(self, region):
        return np.uint8(np.dot(region[..., :3], self.rgb_weights))


class FilterHSV(Filter):

    def __init__(self, threshold=100) -> None:
        self.threshold = threshold
    
    def __str__(self):
        s = "FilterBlackAndWhite: {"
        s += f"threshold:{self.threshold}"
        s += "}"
        return s

    def filter(self, region) -> bool:
        hsv_img = self.convert_rgb_to_hsv(region)
        hue = hsv_img[:, :, 0]
        return np.mean(hue) > self.threshold

    def convert_rgb_to_hsv(self, region):
        return cv2.cvtColor(region, cv2.COLOR_RGB2HSV)
