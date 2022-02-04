from matplotlib import pyplot as plt
import numpy as np
import os
from RegionFilter import doesPassFilter


def split_image(ds, file_name) -> None:
    """Split a tiff image dataset into tiles (512 x 512) and save it locally

    :param ds: dataset of the image
    :param file_name: name of the file (image)
    :return: void
    """

    x_size, y_size = ds.RasterXSize, ds.RasterYSize
    xoff, yoff, xcount, ycount = (0, 0, 512, 512)
    local_imgs_dir = f'local_images/{file_name}'

    if not os.path.exists(local_imgs_dir):
        print("creating dir", local_imgs_dir)
        os.makedirs(local_imgs_dir)

    while xoff + xcount < x_size:
        while yoff + ycount < y_size:
            # produces a (3, x, y) matrix
            img_region = ds.ReadAsArray(xoff, yoff, xcount, ycount)

            # transforms (3, x, y) matrix to (x, y, 3)
            img_region = np.moveaxis(img_region, 0, -1)

            if doesPassFilter(img_region):
                save_path = os.path.join(
                    'local_images', file_name, f'{file_name}_{xoff}_{yoff}.png')
                plt.imsave(save_path, img_region)

            yoff += ycount

        xoff += xcount
        yoff = 0
