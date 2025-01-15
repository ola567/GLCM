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


def to_image(normalized_array):
    image_array = (normalized_array * 255).astype(np.uint8)
    return Image.fromarray(image_array, mode="L")


@dataclass
class Direction:
    dx: int
    dy: int


class GLCMImage:
    def __init__(
        self,
        grayscale_image,
        gray_levels: int,
        block_size: int,
        average_glcm_from: list[Direction],
    ):
        self.grayscale_image = grayscale_image // (256 // gray_levels)
        self.gray_levels = gray_levels
        self.block_size = block_size
        self.average_glcm_from = average_glcm_from

        self.blocks_in_x = self.grayscale_image.shape[1] // block_size
        self.blocks_in_y = self.grayscale_image.shape[0] // block_size

        self.average_glcm = self._get_average_glcm(self.grayscale_image)
        self.average_glcm2d = self.average_glcm[:, :, 0, 0]

    def _get_average_glcm(self, grayscale_image):
        # Initialize the summed GLCM
        summed_glcm = None
        for direction in self.average_glcm_from:
            # Calculate angle and distance for the current direction
            angle = np.arctan2(direction.dy, direction.dx)
            distance = np.hypot(direction.dx, direction.dy)
            # Compute the GLCM for this direction
            glcm = graycomatrix(
                grayscale_image,
                distances=[int(distance)],
                angles=[angle],
                levels=self.gray_levels,
            )
            # Squeeze to 2D and accumulate the result
            glcm = glcm[:, :, 0, 0]
            if summed_glcm is None:
                summed_glcm = glcm
            else:
                summed_glcm += glcm
        average_glcm_2d = np.rint(summed_glcm / len(self.average_glcm_from)).astype(
            np.uint32
        )
        average_glcm = average_glcm_2d.reshape(
            (self.gray_levels, self.gray_levels, 1, 1)
        )
        return average_glcm

    @cached_property
    def contrast(self):
        return graycoprops(self.average_glcm, "contrast")[0][0]

    @cached_property
    def dissimilarity(self):
        return graycoprops(self.average_glcm, "dissimilarity")[0][0]

    @cached_property
    def homogeneity(self):
        return graycoprops(self.average_glcm, "homogeneity")[0][0]

    @cached_property
    def energy(self):
        return graycoprops(self.average_glcm, "energy")[0][0]

    @cached_property
    def correlation(self):
        return graycoprops(self.average_glcm, "correlation")[0][0]

    def average_glcm2d_for_block(self, x, y):
        x_block = x // self.block_size
        y_block = y // self.block_size
        block = self.grayscale_image[
            y_block * self.block_size : (y_block + 1) * self.block_size,
            x_block * self.block_size : (x_block + 1) * self.block_size,
        ]
        return self._get_average_glcm(block)[:, :, 0, 0]

    def _block_graycoprops(self, grayscale_image, prop):
        h, w = self.blocks_in_y * self.block_size, self.blocks_in_x * self.block_size
        result = np.zeros((h, w), dtype=np.float32)
        for i in range(self.blocks_in_x):
            for j in range(self.blocks_in_y):
                # Extract block
                block = grayscale_image[
                    j * self.block_size : (j + 1) * self.block_size,
                    i * self.block_size : (i + 1) * self.block_size,
                ]
                # Compute GLCM for the block
                glcm = self._get_average_glcm(block)
                # Compute the property for the block
                value = graycoprops(glcm, prop)[0, 0]
                # Fill the block in the result array with the computed value
                result[
                    j * self.block_size : (j + 1) * self.block_size,
                    i * self.block_size : (i + 1) * self.block_size,
                ] = value
        return result

    @cached_property
    def contrast_block(self):
        return self._block_graycoprops(self.grayscale_image, "contrast")

    @cached_property
    def dissimilarity_block(self):
        return self._block_graycoprops(self.grayscale_image, "dissimilarity")

    @cached_property
    def homogeneity_block(self):
        return self._block_graycoprops(self.grayscale_image, "homogeneity")

    @cached_property
    def energy_block(self):
        return self._block_graycoprops(self.grayscale_image, "energy")

    @cached_property
    def correlation_block(self):
        return self._block_graycoprops(self.grayscale_image, "correlation")

    def _normalize(self, array, min_value, max_value):
        if max_value == min_value:  # Avoid division by zero
            return np.zeros_like(array) if min_value == 0 else np.ones_like(array)
        return (array - min_value) / (max_value - min_value)

    @cached_property
    def normalized_average_glcm2d(self):
        return self._normalize(
            self.average_glcm2d, min_value=0, max_value=np.max(self.average_glcm2d)
        )

    def normalized_average_glcm2d_for_block(self, x, y):
        average_glcm2d_for_block = self.average_glcm2d_for_block(x, y)
        return self._normalize(
            average_glcm2d_for_block,
            min_value=0,
            max_value=np.max(average_glcm2d_for_block),
        )

    @cached_property
    def normalized_contrast_block(self):
        return self._normalize(
            self.contrast_block, min_value=0.0, max_value=np.max(self.contrast_block)
        )

    @cached_property
    def normalized_dissimilarity_block(self):
        return self._normalize(
            self.dissimilarity_block,
            min_value=0.0,
            max_value=np.max(self.dissimilarity_block),
        )

    @cached_property
    def normalized_homogeneity_block(self):
        return self._normalize(self.homogeneity_block, min_value=0.0, max_value=1.0)

    @cached_property
    def normalized_energy_block(self):
        return self._normalize(self.energy_block, min_value=0.0, max_value=1.0)

    @cached_property
    def normalized_correlation_block(self):
        return self._normalize(self.correlation_block, min_value=-1.0, max_value=1.0)


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
