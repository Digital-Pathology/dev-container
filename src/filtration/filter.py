
import abc
import cv2
from numbers import Number
import numpy as np
import random

# TODO: Add docstrings to all classes, methods, and top of each file

class Filter(abc.ABC):

    def __call__(self, region) -> bool:
        return self.filter(region)

    def __str__(self):
        return f"<{self.__class__.__name__}: {vars(self)}>"

    @abc.abstractmethod
    def filter(self, region) -> bool:
        pass


class FilterBlackAndWhite(Filter):

    def __init__(self, filter_threshold=0.5, binarization_threshold=0.85, rgb_weights=[0.2989, 0.5870, 0.1140]):
        """
            Initialize FilterBlackAndWhite Object
            Parameters:
                filter_threshold: Threshold at which image region passes black and white filter
                binarization_threshold: Threshold to determine will be converted to either black or white
                rgb_weights: Weighting used for RGB to greyscale conversion

        """
        self.filter_threshold = filter_threshold
        self.binarization_threshold = binarization_threshold
        self.rgb_weights = rgb_weights

    def filter(self, region) -> bool:
        """
            Perform filtration to a region
            Parameters:
                region (np.ndarray): numpy array representing the region
            Returns:
                True if the average of the binary region is less than x% white (x is the filter_threshold*100), else False
        """
        greyscale_image = self.convert_rgb_to_greyscale(region)
        # if pixel is > 85% white, set value to 1 else 0
        binary_image = np.where(
            greyscale_image > self.binarization_threshold*255, 1, 0)
        return np.mean(binary_image) < self.filter_threshold

    def convert_rgb_to_greyscale(self, region):
        """
            Convert an RGB region of image to greyscale
            Parameters:
                region (np.ndarray): numpy array representing the region, region consists of RGB values
            Returns:
                np.ndarray: a numpy array representing the region, region is in greyscale
        """
        return np.uint8(np.dot(region[..., :3], self.rgb_weights))


class FilterHSV(Filter):

    def __init__(self, threshold=100) -> None:
        """
            Initialize FilterHSV Object
            Parameters:
                threshold: Threshold at which image region passes HSV filter
        """
        self.threshold = threshold

    def filter(self, region) -> bool:
        """
            Perform filtration to a region
            Parameters:
                region (np.ndarray): numpy array representing the region
            Returns:
                True if the mean of the hues in the hsv region is greather than the threshold, else False
        """
        hsv_img = self.convert_rgb_to_hsv(region)
        hue = hsv_img[:, :, 0]
        return np.mean(hue) > self.threshold

    def convert_rgb_to_hsv(self, region):
        """
            Converts RGB region of image to HSV
            Parameters:
                region (np.ndarray): numpy array representing the region, region consists of RGB values
            Returns:
                np.ndarray: a numpy array representing the region, region consists of HSV values
        """
        return cv2.cvtColor(region, cv2.COLOR_RGB2HSV)


class FilterRandom(Filter):
    
    def __init__(self, p: Number = 0.5) -> None:
        self.p = p
    
    def filter(self, region) -> bool:
        return random.random() > self.p
