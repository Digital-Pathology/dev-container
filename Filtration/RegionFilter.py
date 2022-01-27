
import abc

class RegionFilter(abc.ABC):

    def __call__(self, region) -> bool:
        return self.filter(region)

    @abc.abstractmethod
    def filter(self, region) -> bool:
        raise NotImplementedError()

class RegionFilterBlackAndWhite(RegionFilter):

    def __init__(self, threshold):
        self.threshold = threshold

    def filter(self, region) -> bool:
        raise NotImplementedError()

class RegionFilterHSV(RegionFilter):

    def __init__(self, **kwargs):
        raise NotImplementedError()

    def filter(self, region) -> bool:
        raise NotImplementedError()
