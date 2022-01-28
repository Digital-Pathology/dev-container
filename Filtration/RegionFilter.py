
import abc
import numpy as np
import numpy.typing as npt
import cv2

def black_and_white_filter(region: npt.ArrayLike):
    filter_threshold=0.5
    binarization_threshold=0.85
    rgb_weights=[0.2989, 0.5870, 0.1140]
    
    gray_scale_img = np.uint8(np.dot(region[...,:3], rgb_weights))
    binary_image = np.where(gray_scale_img > binarization_threshold*255, 1, 0)
    return np.mean(binary_image) < filter_threshold

def hsv_filter(rgb_img):
    hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)
    h = hsv_img[:,:,0]
    return np.mean(h) > 100


def doesPassFilter(img):
    return black_and_white_filter(img) and hsv_filter(img)
    
# class RegionFilter(abc.ABC):

#     def __call__(self, region) -> bool:
#         return self.filter(region)

#     @abc.abstractmethod
#     def filter(self, region) -> bool:
#         filter_black_and_white = RegionFilterBlackAndWhite()
#         return filter_black_and_white.filter(region)

# class RegionFilterBlackAndWhite(RegionFilter):

#     # binarization_threshold - percentage 
#     def __init__(self, filter_threshold=0.5, binarization_threshold=0.85, rgb_weights=[0.2989, 0.5870, 0.1140]):
#         self.filter_threshold = filter_threshold
#         self.binarization_threshold = binarization_threshold
#         self.rgb_weights = rgb_weights

#     def filter(self, region) -> bool:
#         greyscale_image = self.convert_to_greyscale(region)
#         binary_image = np.where(greyscale_image > self.binarization_threshold*255, 1, 0)
#         return np.mean(binary_image) < self.filter_threshold

#     def convert_to_greyscale(self, region):
#         return np.uint8(np.dot(region[...,:3], self.rgb_weights))


# class RegionFilterHSV(RegionFilter):

#     def __init__(self, **kwargs):
#         raise NotImplementedError()

#     def filter(self, region) -> bool:
#         raise NotImplementedError()
