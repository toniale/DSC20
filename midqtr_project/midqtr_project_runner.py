"""
DSC 20 Mid-Quarter Project Runner
"""
# pylint: disable = E1101

import cv2
import numpy as np
from midqtr_project import (
    RGBImage,
    ImageProcessing as IP,
    ImageKNNClassifier,
)

"""
>>> large_img = img_read('img/testmac.png')
>>> gray_background = IP.grayscale(large_img)
>>> img_save('img/large_negate.png', gray_background)

>>> image_processing_test_examples()
>>> large_img = img_read('img/testmac.png')
>>> large_scaled = IP.scale_channel(large_img, 2, 0.63)
>>> img_save('img/large_scaled.png', large_scaled)
"""

def doctest_func():
    """
    Test Size:
    >>> test_size_img = RGBImage(pixels_example())
    >>> test_size_img.size()
    (5, 10)

    Test Get pixel:
    >>> test_size_img.get_pixel(4, 9)
    (223, 127, 202)

    Test Copy pixel:
    >>> copy_pixels_matrix = test_size_img.get_pixels()
    >>> copy_pixels_matrix == test_size_img.get_pixels()
    True
    >>> copy_pixels_matrix is test_size_img.get_pixels()
    False
    >>> copy_pixel_img = RGBImage(copy_pixels_matrix)
    >>> copy_pixel_img.get_pixels() == test_size_img.get_pixels()
    True
    >>> copy_pixel_img.get_pixels() is test_size_img.get_pixels()
    False
    >>> copy_pixel_img = test_size_img.copy()
    >>> copy_pixel_img == test_size_img
    False
    >>> copy_pixel_img.get_pixels() == test_size_img.get_pixels()
    True
    >>> copy_pixel_img.get_pixels() is test_size_img.get_pixels()
    False
    >>> copy_pixel_img is test_size_img
    False

    Test Copy Image:
    >>> heart_img = img_read('img/dsc20.png')
    >>> heart_copy = heart_img.copy()
    >>> heart_img is heart_copy
    False

    Test Negate:
    >>> negate_heart = IP.negate(heart_copy)
    >>> img_save('img/neg_heart.png', negate_heart)

    Test Grayscale:
    >>> gray_heart = IP.grayscale(heart_img)
    >>> img_save('img/gray_heart.png', gray_heart)

    Test Scale:
    >>> heart_copy = heart_img.copy()
    >>> scaled_heart = IP.scale_channel(heart_copy, 2, 0.63)
    >>> img_save('img/scaled_heart1.png', scaled_heart)
    >>> scaled_heart = IP.scale_channel(heart_copy, 2, 2.25)
    >>> img_save('img/scaled_heart2.png', scaled_heart)

    Test Clear:
    >>> heart_copy = heart_img.copy()
    >>> clear_heart = IP.clear_channel(heart_copy, 0)
    >>> img_save('img/clear_heart1.png', clear_heart)
    >>> clear_heart = IP.clear_channel(heart_copy, 2)
    >>> img_save('img/clear_heart2.png', clear_heart)

    Test rotate_90:
    >>> rotated_heart_left = IP.rotate_90(heart_copy, False)
    >>> img_save('img/rotated_heart_left.png', rotated_heart_left)
    >>> rotated_heart_right = IP.rotate_90(heart_copy, True)
    >>> img_save('img/rotated_heart_right.png', rotated_heart_right)

    Test crop:
    >>> heart_copy = heart_img.copy()
    >>> cropped_heart1 = IP.crop(heart_copy, 50, 75, (75,50))
    >>> img_save('img/cropped1.png', cropped_heart1)
    >>> cropped_heart2 = IP.crop(heart_copy, 100, 50, (100, 150))
    >>> img_save('img/cropped2.png', cropped_heart2)

    Test Chroma:
    >>> heart_copy = heart_img.copy()
    >>> test_size_img = RGBImage(pixels_example())
    >>> wrong_size = IP.chroma_key(heart_copy, test_size_img, (0, 0, 0))
    Traceback (most recent call last):
    AssertionError
    >>> not_RGB = IP.chroma_key(pixels_example(), test_size_img, (0, 0, 0))
    Traceback (most recent call last):
    AssertionError
    >>> background_img = img_read('img/blue_gradient.png')
    >>> chroma_img = IP.chroma_key(heart_copy, background_img, (255, 255, 255))
    >>> img_save('img/chroma_img.png', chroma_img)

    #
    # Test KNN?:
    # >>> knn_test_examples()

    """

def img_read(path):
    """
    Read the image with given `path` to a RGBImage instance.
    """
    mat = cv2.imread(path).transpose(2, 0, 1).tolist()
    mat.reverse()  # convert BGR (cv2 default behavior) to RGB
    return RGBImage(mat)


def img_save(path, image):
    """
    Save a RGBImage instance (`image`) as a image file with given `path`.
    """
    mat = np.stack(list(reversed(image.get_pixels()))).transpose(1, 2, 0)
    cv2.imwrite(path, mat)


def create_random_pixels(low, high, nrows, ncols):
    """
    Create a random pixels matrix with dimensions of
    3 (channels) x `nrows` x `ncols`, and fill in integer
    values between `low` and `high` (both exclusive).
    """
    return np.random.randint(low, high + 1, (3, nrows, ncols)).tolist()


def pixels_example():
    """
    An example of the 3-dimensional pixels matrix (3 x 5 x 10).
    """
    return [
        [
            # channel 0: red (5 rows x 10 columns)
            #[list(map(negate_func, row)) for row in copy_matrix[0][row]]
            [206, 138, 253, 211, 102, 194, 188, 188, 120, 231],
            [204, 208, 220, 214, 203, 165, 249, 225, 198, 185],
            [113, 196, 133, 235, 173, 179, 252, 105, 214, 238],
            [152, 156, 143, 114, 166, 132, 106, 115, 116, 177],
            [231, 193, 123, 154, 184, 242, 226, 155, 222, 223],
        ],
        [
            # channel 1: green (5 rows x 10 columns)
            [214, 190, 173, 141, 248, 189, 105, 193, 125, 122],
            [209, 136, 131, 187, 177, 186, 239, 222, 175, 152],
            [239, 236, 177, 243, 183, 192, 114, 211, 147, 192],
            [168, 119, 120, 182, 190, 108, 181, 219, 198, 127],
            [251, 222, 205, 102, 104, 217, 234, 196, 131, 127],
        ],
        [
            # channel 2: blue (5 rows x 10 columns)
            [233, 188, 214, 175, 152, 174, 235, 174, 234, 149],
            [163, 169, 131, 209, 232, 180, 238, 224, 152, 214],
            [137, 135, 181, 146, 243, 210, 236, 107, 193, 200],
            [230, 233, 206, 227, 150, 131, 177, 187, 143, 150],
            [117, 188, 127, 166, 134, 219, 241, 108, 217, 202],
        ],
    ]

def pixels_example_white():
    """
    An example of the 3-dimensional pixels matrix (3 x 5 x 10).
    """
    return [
        [
            # channel 0: red (5 rows x 10 columns)
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [204, 208, 220, 214, 203, 165, 249, 225, 198, 185],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [152, 156, 143, 114, 166, 132, 106, 115, 116, 177],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
        ],
        [
            # channel 1: green (5 rows x 10 columns)
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [209, 136, 131, 187, 177, 186, 239, 222, 175, 152],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [168, 119, 120, 182, 190, 108, 181, 219, 198, 127],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
        ],
        [
            # channel 2: blue (5 rows x 10 columns)
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [163, 169, 131, 209, 232, 180, 238, 224, 152, 214],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            [230, 233, 206, 227, 150, 131, 177, 187, 143, 150],
            [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
        ],
    ]


def image_processing_test_examples():
    """
    Examples of image processing methods tests using real images.
    """
    # read image
    dsc20_img = img_read("img/dsc20.png")

    # negate and save
    negative_dsc20_img = IP.negate(dsc20_img)
    img_save("img/out/dsc20_negate.png", negative_dsc20_img)

    # chroma key with a background image and save
    bg_img = img_read("img/blue_gradient.png")
    chroma_white_dsc20_img = IP.chroma_key(dsc20_img, bg_img, (255, 255, 255))
    img_save("img/out/dsc20_chroma_white.png", chroma_white_dsc20_img)


#def knn_test_examples():
    """
    Examples of KNN classifier tests.
    """
    # make random training data (type: List[Tuple[RGBImage, str]])
    train = []
    # create training images with low intensity values
    train.extend(
        (RGBImage(create_random_pixels(0, 75, 300, 300)), "low")
        for _ in range(20)
    )
    # create training images with high intensity values
    train.extend(
        (RGBImage(create_random_pixels(180, 255, 300, 300)), "high")
        for _ in range(20)
    )

    # initialize and fit the classifier
    knn = ImageKNNClassifier(5)
    knn.fit(train)

    # should be "low"
    print(knn.predict(RGBImage(create_random_pixels(0, 75, 300, 300))))
    # can be either "low" or "high"
    print(knn.predict(RGBImage(create_random_pixels(75, 180, 300, 300))))
    # should be "high"
    print(knn.predict(RGBImage(create_random_pixels(180, 255, 300, 300))))
