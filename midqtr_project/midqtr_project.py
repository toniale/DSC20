"""
DSC 20 Mid-Quarter Project
Name: Gabriel Fara-on, Tonia Le
PID:  A15974655, A15662706
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

    def size(self):
        """
        Getter method that returns the size of the image as a tuple
        of the number of rows and number of columns
        """
        return (len(self.pixels[0]), len(self.pixels[0][1]))

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
        return RGBImage(self.get_pixels())

    def get_pixel(self, row, col):
        """
        Getter method that returns the color of the pixel at a given
        position (row, col). The color is returned as a tuple (red intensity,
        green intensity, blue intensity) at the given position.

        Requirement:
        row and col must be valid indices
        """
        assert isinstance(row, int) and isinstance(col, int)
        assert self.size()[0] > row >= 0
        assert self.size()[1] > col >= 0
        #self.pixels gives us a matrix with 3 separate arrays for R, G and B
        return (self.pixels[0][row][col], self.pixels[1][row][col],
                self.pixels[2][row][col])

    def set_pixel(self, row, col, new_color):
        """
        A setter method that updates the color of a pixel at a given position
        (row, col) to the given new color tuple (red intensity,
        green intensity, blue intensity) given. If any intensity in the tuple
        is -1, the setter does not update that intensity.

        Requirement:
        row and col must be valid indices
        """
        assert isinstance(row, int) and isinstance(col, int)
        assert self.size()[0] > row >= 0
        assert self.size()[1] > col >= 0
        if new_color[0] != -1:
            new_red_pixel = new_color[0]
            self.pixels[0][row][col] = new_red_pixel
        if new_color[1] != -1:
            new_green_pixel = new_color[1]
            self.pixels[1][row][col] = new_green_pixel
        if new_color[2] != -1:
            new_blue_pixel = new_color[2]
            self.pixels[2][row][col] = new_blue_pixel

# Part 2: Image Processing Methods #
class ImageProcessing:
    """
    A class for Image Processing
    """

    @staticmethod
    def negate(image):
        """
        Returns a negated image version of the given RGBImage Object
        """
        copy_img = image.copy()
        copy_matrix = copy_img.get_pixels()
        negate_func = lambda x: 255 - x
        new_red_plane = [list(map(negate_func, row)) for row in copy_matrix[0]]
        new_green_plane = [list(map(negate_func, row)) \
                          for row in copy_matrix[1]]
        new_blue_plane = [list(map(negate_func, row)) \
                          for row in copy_matrix[2]]
        copy_matrix[0] = new_red_plane
        copy_matrix[1] = new_green_plane
        copy_matrix[2] = new_blue_plane
        return RGBImage(copy_matrix)

    @staticmethod
    def grayscale(image):
        """
        Returns a grayscale version of the given RGBImage object
        """
        copy_img = image.copy()
        dimensions = image.size()
        rows = dimensions[0]
        cols = dimensions[1]
        grayscale_image = [[[sum(copy_img.get_pixel(row, col))//3 \
                            for col in range(cols)] \
                            for row in range(rows)] \
                            for i in range(3)]
        return RGBImage(grayscale_image)

    @staticmethod
    def scale_channel(image, channel, scale):
        """
        Returns a scaled image by the given scale.
        """
        # checks that scale is a non-negative numeric value
        assert isinstance(scale, (float, int)) and scale >= 0

        def scale_mult(value):
            """Multiplies value by given scale"""

            new_value = value * scale
            if new_value > 255:
                new_value = 255
            return new_value

        copy_img = image.copy()
        copy_matrix = copy_img.get_pixels()
        # applies scale_mult to the given channel
        new_plane = [list(map(scale_mult, row)) \
                     for row in copy_matrix[channel]]
        copy_matrix[channel] = new_plane
        return RGBImage(copy_matrix)

    @staticmethod
    def clear_channel(image, channel):
        """
        Returns an image of a cleared given channel.
        """
        # changes a value to zero
        clear_func = lambda x: 0
        # copy image
        copy_img = image.copy()
        copy_matrix = copy_img.get_pixels()
        # updates every intensity value in the channel using clear_func
        new_plane = [list(map(clear_func, row)) \
                    for row in copy_matrix[channel]]
        copy_matrix[channel] = new_plane
        return RGBImage(copy_matrix)

    @staticmethod
    def rotate_90(image, clockwise):
        """
        Returns an image rotated by 90 degrees(clockwise and counterclockwise).
        """
        copy_img = image.copy()
        copy_matrix = copy_img.get_pixels()
        # rotates matrix counter-clockwise
        rotated_matrix = [[list(row) for row in zip(*plane)] \
                          [::-1] for plane in copy_matrix]
        if clockwise is False:
            return RGBImage(rotated_matrix)
        else:
            rotated_matrix = [[row[::-1] for row in plane][::-1] \
                              for plane in rotated_matrix]
            return RGBImage(rotated_matrix)

    @staticmethod
    def crop(image, tl_row, tl_col, target_size):
        """
        Returns an image cropped to the target size.
        """
        def max_tl(image, tl_row, tl_col):
            """
            Checks if tl_row and rl_col exceed zero.
            """
            if tl_row < 0:
                tl_row = 0
            if tl_col < 0:
                tl_col = 0
            return

        def br_dims(image, tl_row, tl_col, target_size):
            """
            Checks if target_size exceeds image size, sets max to
            image max if target_size > image size
            """
            image_rows = image.size()[0]
            image_cols = image.size()[1]
            br_rows = target_size[0] + tl_row
            br_cols = target_size[1] + tl_col
            if br_rows > image_rows:
                br_rows = image_rows
            if br_cols > image_cols:
                br_cols = image_cols
            return[br_rows, br_cols]

        max_tl(image, tl_row, tl_col)
        copy_img = image.copy()
        copy_matrix = copy_img.get_pixels()

        br_row = br_dims(copy_img, tl_row, tl_col, target_size)[0]
        br_col = br_dims(copy_img, tl_row, tl_col, target_size)[1]

        cropped_matrix = [[[(plane[row][col]) \
                            for col in range(tl_col, br_col)] \
                            for row in range(tl_row, br_row)] \
                            for plane in copy_matrix]
        return RGBImage(cropped_matrix)

    @staticmethod
    def chroma_key(chroma_image, background_image, color):
        """
        Returns an image where the pixels of given a color are replaced by a
        given background image's pixels in the same positions.
        """
        assert isinstance(chroma_image, RGBImage)
        assert isinstance(background_image, RGBImage)
        assert chroma_image.size() == background_image.size()

        chroma_copy = chroma_image.copy()
        bg_copy = background_image.copy()
        rows = chroma_copy.size()[0]
        cols = chroma_copy.size()[1]
        for row in range(rows):
            for col in range(cols):
                #tuple of the colors of chroma image at that pixel
                chroma_color = chroma_copy.get_pixel(row, col)
                #if chroma pixel color is the same as the given color
                if chroma_color == color:
                    #set chroma pixel color to background pixel color
                    bg_color = bg_copy.get_pixel(row, col)
                    chroma_copy.set_pixel(row, col, bg_color)
        return chroma_copy


# Part 3: Image KNN Classifier #
class ImageKNNClassifier:
    """
    A class that applies the training data to its own algorithm to predict a
    label.  (?)
    """

    def __init__(self, n_neighbors):
        """
        Constructor that initializes a ImageKNNClassifier instance and
        necessary instance variables.
        Parameters:
            n_neighbors = size of the nearest neighborhood
        """
        self.n_neighbors = n_neighbors

    def fit(self, data):
        """
        Fits the classifier by storing all training data(list of tuples(image,
        label), where image is a RGBImage instance and label is a string.
        """
        #assert len(self.data) == 0
        self.data = data
        assert len(self.data) > self.n_neighbors

    @staticmethod
    def distance(image1, image2):
        """
        Calculates the Euclidean distance between RGB image image1 and image2.
        """
        assert image1.size() == image2.size()
        rows = image1.size()[0]
        cols = image2.size()[1]
        sq_diff = sum([(image1.get_pixels()[i][row][col] - \
                       image2.get_pixels()[i][row][col])**2 for i in range(3)\
                       for row in range(rows) for col in range(cols)])
        dist = (sq_diff)**(1/2)
        return dist

    @staticmethod
    def vote(candidates):
        """
        Finds the most popular label from a list of candidates labels.
        """
        return mode(candidates)

    def predict(self, image):
        """
        Predicts the label of the given image using the KNN classification
        algorithm.
        """
        k = self.n_neighbors
        assert self.data
        #Take list of tuples (Image, Label)
        training_data = self.data
        #Function calculates distance from test image to training image
        dist_func = lambda x: ImageKNNClassifier.distance(image, x[0])
        #Take distance of test image and every training image
        #Make that a list
        distance_list = [[dist_func(candidate), candidate[1]] \
                          for candidate in training_data]
        distance_key = lambda candidate: candidate[0]
        distance_list.sort(key=distance_key)
        closest_k_neighbors = distance_list[-k:]
        closest_labels = [candidate[1] for candidate in closest_k_neighbors]
        return vote(closest_labels)
