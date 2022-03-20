"""
DSC 20 Mid-Quarter Project
Name:
PID:  TODO
"""

# Part 1: RGB Image #
class RGBImage:
    """
    Template for image objects in RGB color spaces
    """

    def __init__(self, pixels):
        """
        Constructor that initializes the RGGImage instance
        and the instance's pixels attribute.
        """
        self.pixels = pixels
        print(self.pixels)

    def size(self):
        """
        Getter method that returns the size of the image as a tuple
        of the number of rows and number of columns
        """
        return((len(self.pixels[0]), len(self.pixels[0][1])))

    def get_pixels(self):
        """
        Getter method that returns a COPY of the pixels matrix of the image
        (3 dimensional list). The returned matrix is exactly the same as the
        passed pixels matrix
        """
        copy_matrix = []
        for plane in self.pixels:
            plane_list = []
            for row in plane:
                row_list = []
                for col in row:
                    row_list.append(col)
                plane_list.append(row_list)
            copy_matrix.append(plane_list)
        return copy_matrix

    def copy(self):
        """
        Method that returns a COPY of the RGBImage instance. This method
        returns a new RGBImage instance with a copy of the pixels matrix.
        """
        copy_image = RGBImage(self.get_pixels())
        return copy_image

    def get_pixel(self, row, col):
        """
        Getter method that returns the color of the pixel at a given
        position (row, col). The color is returned as a tuple (red intensity,
        green intensity, blue intensity) at the given position.

        Requirement:
        row and col must be valid indices
        """
        assert self.size()[0] >= row >= 0
        assert self.size()[1] >= col >= 0
        #self.pixels gives us a matrix with 3 separate arrays for R, G and B
        return (self.pixels[0][row][col], self.pixels[1][row][col], self.pixels[2][row][col])

    def set_pixel(self, row, col, new_color):
        """
        A setter method that updates the color of a pixel at a given position
        (row, col) to the given new color tuple (red intensity,
        green intensity, blue intensity) given. If any intensity in the tuple
        is -1, the setter does not update that intensity.

        Requirement:
        row and col must be valid indices
        """
        assert self.size()[0] >= row >= 0
        assert self.size()[1] >= col >= 0
        if new_color[0] != -1:
            new_red_pixel = new_color[0]
        if new_color[1] != -1:
            new_green_pixel = new_color[1]
        if new_color[2] != -1:
            new_blue_pixel = new_color[2]
        #set new red
        self.pixels[0][row][col] = new_red_pixel
        self.pixels[1][row][col] = new_green_pixel
        self.pixels[2][row][col] = new_blue_pixel

# Part 2: Image Processing Methods #
class ImageProcessing:
    """
    A class that includes several image processing methods.
    """

    @staticmethod
    def negate(image):
        """
        A method that return the negative image of the given image.

        """
        copy_matrix = image.get_pixels()
        negate_func = lambda x: 255 - x
        new_red_plane = [list(map(negate_func, row)) for row in copy_matrix[0]]
        new_green_plane = [list(map(negate_func, row)) for row in copy_matrix[1]]
        new_blue_plane = [list(map(negate_func, row)) for row in copy_matrix[2]]
        copy_matrix[0] = new_red_plane
        copy_matrix[1] = new_green_plane
        copy_matrix[2] = new_blue_plane
        return RGBImage(copy_matrix)

    @staticmethod
    def grayscale(image):
        """
        A method that converts the given image to grayscale.
        """
        copy_image = image.copy()
        dimensions = image.size()
        rows = dimensions[0]
        cols = dimensions[1]

        grayscale_image = [[[sum(copy_image.get_pixel(row, col))//3 for col in range(cols)] for row in range(rows)]for i in range(3)]
        return RGBImage(grayscale_image)


    @staticmethod
    def scale_channel(image, channel, scale):
        """
        A method that scales the given channel of the image by the given
        scale.

        The channel argument will be one of 0 (R), 1 (G) or 2 (B).
        The scale argument is a non-negative numeric value.
        For each intensity value val in the specified channel, update it with
        int(val * scale).
        However, if the scaled value exceeds the maximum pixel value 255, you
        need to cap the value to 255.

        """
        # replace one channel with scaled value, for each value in the channel, pick main value between minimium val and max(255)
        copy_image = image.copy
        def scaled_func(pixels, scale):
            new_value = value * scale
            if new_value > 255:
                new_value = 255
            return new_value

    copy_matrix = image.get_pixels()
    new_plane = [list(map(scaled_func, row)) for row in copy_matrix[channel]]
    copy_matrix[channel] = new_plane
    return RGBImage(copy_matrix)

    @staticmethod
    def clear_channel(image, channel):
        """
        A method that clears the given channel of the image.
        """
    clear_func
    copy_matrix = image.get_pixels()
    new_plane = [list(map(clear_func, row)) for row in copy_matrix[channel]]
    copy_matrix[channel] = new_plane
    return RGBImage(copy_matrix)

    @staticmethod
    def rotate_90(image, clockwise):
        """
        A method that rotates the image for 90 degrees.
        """
        copy_img =
    @staticmethod
    def crop(image, tl_row, tl_col, target_size):
        """
        A method that crops the image.
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def chroma_key(chroma_image, background_image, color):
        """
        A method that performs the chroma key algorithm on the chroma_image
        by replacing all pixels with the specified color in the chroma_image
        to the pixels at the same places in the background_image.
        """
        # YOUR CODE GOES HERE #


# Part 3: Image KNN Classifier #
class ImageKNNClassifier:
    """
    TODO: add description
    """

    def __init__(self, n_neighbors):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def fit(self, data):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def distance(image1, image2):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    @staticmethod
    def vote(candidates):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #

    def predict(self, image):
        """
        TODO: add description
        """
        # YOUR CODE GOES HERE #
