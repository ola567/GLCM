import os
from dataclasses import dataclass
from functools import cached_property

from PIL import Image
import numpy as np
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray


def load_grayscale(image_path: str | os.PathLike):
    # Open the image file (supports JPG, PNG, BMP)
    im_frame = Image.open(image_path)

    # Convert image to numpy array
    im_array = np.array(im_frame)

    # Check the number of channels
    if len(im_array.shape) == 3:  # If the image has color channels
        if im_array.shape[2] == 4:  # 4 channels (e.g., RGBA)
            # Remove the alpha channel by extracting the first three channels (RGB)
            im_array = im_array[:, :, :3]
        # Convert to grayscale
        return (255 * rgb2gray(im_array)).astype(np.uint8)
    else:
        # If the image is already grayscale, no need to use rgb2gray
        return im_array.astype(np.uint8)


@dataclass
class Direction:
    dx: int
    dy: int


class GLCMImage:
    def __init__(self, grayscale_image: np.array, gray_levels: int, block_size: int, average_glcm_from: list[Direction]):
        grayscale_image //= (256 // gray_levels)
        self.grayscale_image = grayscale_image

        # Initialize the summed GLCM
        summed_glcm = None
        for direction in average_glcm_from:
            # Calculate angle and distance for the current direction
            angle = np.arctan2(direction.dy, direction.dx)
            distance = np.hypot(direction.dx, direction.dy)

            # Compute the GLCM for this direction
            glcm = graycomatrix(
                self.grayscale_image,
                distances=[int(distance)],
                angles=[angle],
                levels=gray_levels
            )

            # Squeeze to 2D and accumulate the result
            glcm = glcm[:, :, 0, 0]
            if summed_glcm is None:
                summed_glcm = glcm
            else:
                summed_glcm += glcm

        self.average_glcm_2d = np.rint(summed_glcm / len(average_glcm_from)).astype(np.uint32)
        self.average_glcm = self.average_glcm_2d.reshape((gray_levels, gray_levels, 1, 1))

    @cached_property
    def contrast(self):
        return graycoprops(self.average_glcm, 'contrast')[0][0]

    @cached_property
    def dissimilarity(self):
        return graycoprops(self.average_glcm, 'dissimilarity')[0][0]

    @cached_property
    def homogeneity(self):
        return graycoprops(self.average_glcm, 'homogeneity')[0][0]

    @cached_property
    def energy(self):
        return graycoprops(self.average_glcm, 'energy')[0][0]

    @cached_property
    def correlation(self):
        return graycoprops(self.average_glcm, 'correlation')[0][0]


# glcm_image = GLCMImage(
#     grayscale_image=load_grayscale("../test.bmp"),
#     gray_levels=32,
#     block_size=30,
#     average_glcm_from=[
#         Direction(dx=1, dy=0),
#         Direction(dx=0, dy=1),
#         Direction(dx=1, dy=1),
#         Direction(dx=-1, dy=1),
#     ],
# )
