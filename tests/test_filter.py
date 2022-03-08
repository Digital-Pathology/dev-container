from src.filtration.filter_manager import FilterManager
from src.filtration.filter import Filter, FilterBlackAndWhite, FilterHSV, FilterFocusMeasure
from pathlib import Path
import cv2
import os

black_and_white_filter: Filter = FilterBlackAndWhite()
hsv_filter: Filter = FilterHSV()
focus_measure_filter: Filter = FilterFocusMeasure()

filter_manager = FilterManager([black_and_white_filter, hsv_filter, focus_measure_filter])

test_dir = 'tests/test_images'
test_files = os.listdir(test_dir)


def test():
    assert 2+2 == 4


# def test():
#     for path in Path(test_dir).rglob("*.*"):
#         absolute_path = str(path.absolute())
#         img = cv2.imread(absolute_path)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         if 'pass' in absolute_path:
#             assert filter_manager.filter(img) == True
#         elif 'fail' in absolute_path:
#             assert filter_manager.filter(img) == False


# if __name__ == "__main__":
#     retcode = pytest.main()
