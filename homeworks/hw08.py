"""
DSC 20 Homework 08
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def counter_doctests():
    """
    Doctests for Counter and AlphanumericCounter.

    >>> counter = Counter()
    >>> counter.size()
    0
    >>> counter.add_items([123, 123, "abc", (10, 10), (10, 20)])
    >>> counter.size()
    5
    >>> counter.get_count(123)
    2
    >>> counter.get_count("dsc20")
    0
    >>> counter.get_all_counts()
    {123: 2, 'abc': 1, (10, 10): 1, (10, 20): 1}

    >>> an_counter = AlphanumericCounter()
    >>> an_counter.size()
    0
    >>> len(an_counter.counts)
    62
    >>> an_counter.add_items("DSC 20 (Marina Langlois)")
    >>> an_counter.size()
    19
    >>> an_counter.get_count("a")
    3
    >>> an_counter.get_count("?")
    0
    >>> an_counter.get_all_counts()
    {'0': 1, '2': 1, 'a': 3, 'g': 1, 'i': 2, 'l': 1, 'n': 2, 'o': 1, \
'r': 1, 's': 1, 'C': 1, 'D': 1, 'L': 1, 'M': 1, 'S': 1}

    >>> my_counter = Counter()
    >>> my_counter.size()
    0
    >>> my_counter.add_items(['why', 'oh', 'why', 'is', 'this', 'so', 'hard'])
    >>> my_counter.size()
    7
    >>> my_counter.get_all_counts()
    {'why': 2, 'oh': 1, 'is': 1, 'this': 1, 'so': 1, 'hard': 1}
    >>> my_counter.get_count('why')
    2
    >>> my_counter.get_count('hehe')
    0
    >>> my_counter.add_items(['hehe'])
    >>> my_counter.get_all_counts()
    {'why': 2, 'oh': 1, 'is': 1, 'this': 1, 'so': 1, 'hard': 1, 'hehe': 1}
    >>> my_counter.size()
    8
    >>> my_counter.get_count('hehe')
    1
    >>> my_counter.add_items(['oh'])
    >>> my_counter.get_count('oh')
    2
    >>> my_counter.get_all_counts()
    {'why': 2, 'oh': 2, 'is': 1, 'this': 1, 'so': 1, 'hard': 1, 'hehe': 1}

    >>> my_alphanum = AlphanumericCounter()
    >>> my_alphanum.size()
    0
    >>> my_alphanum.add_items("I'm s0 tired!!")
    >>> my_alphanum.size()
    9
    >>> my_alphanum.get_all_counts()
    {'0': 1, 'd': 1, 'e': 1, 'i': 1, 'm': 1, 'r': 1, 's': 1, 't': 1, 'I': 1}
    >>> my_alphanum.get_index('I')
    44
    >>> my_alphanum.get_char(44)
    'I'
    >>> my_alphanum.get_index("!")
    -1
    >>> my_alphanum.get_char(0)
    '0'
    >>> my_alphanum.get_index('B')
    37
    >>> my_alphanum.get_char(-1)
    Traceback (most recent call last):
    AssertionError
    >>> my_alphanum.get_count('0')
    1
    >>> my_alphanum.get_count('!!')
    0
    >>> my_alphanum.add_items('sux 2 b u')
    >>> my_alphanum.size()
    15
    >>> my_alphanum.get_all_counts()
    {'0': 1, '2': 1, 'b': 1, 'd': 1, 'e': 1, 'i': 1, 'm': 1, 'r': 1, \
's': 2, 't': 1, 'u': 2, 'x': 1, 'I': 1}
    >>> my_alphanum.add_items('!')
    >>> my_alphanum.get_all_counts()
    {'0': 1, '2': 1, 'b': 1, 'd': 1, 'e': 1, 'i': 1, 'm': 1, 'r': 1, \
's': 2, 't': 1, 'u': 2, 'x': 1, 'I': 1}
    >>> my_alphanum.get_count('u')
    2
    """
    return


class Counter:
    """
    A class that abstracts a generalized counter for all kinds of iterable
    objects.

    """

    def __init__(self):
        """
        Constructor of Counter.

        Parameters:
            nelems (int): The total number of items stored in the counter.
            counts (dict): A dictionary that stores all item (keys) to count
                           (values) pairs.
        """
        self.nelems = 0
        self.counts = {}

    def size(self):
        """
        A method that returns the total number of items stored in the counter.

        """
        return self.nelems

    def get_count(self, item):
        """
        Returns the count of an object item.
        If the item does not exist in the counter, return 0.

        """
        if item not in self.counts:
            return 0
        else:
            return self.counts[item]

    def get_all_counts(self):
        """
        Returns a dictionary of all item to count pairs.

        """
        return self.counts

    def add_items(self, items):
        """
        Takes an iterable object (like list) of objects (items) and
        adds them to the counter. Make sure to update both counts and
        nelems attributes.

        """
        # loop through the iterable object
        for item in items:
            if item in self.counts:
                self.counts[item] += 1
                self.nelems += 1
            else:
                self.counts[item] = 1
                self.nelems += 1

class AlphanumericCounter(Counter):
    """
    A class that counts only alphabet letters and numbers in strings.
    """

    def __init__(self):
        """
        Constructor of AlphanumericCounter.

        Parameters:
            nelems (int): The total number of items stored in the counter.
            counts (list): A counter list for alhpanumeric characters

        """
        num_list_elem = 62
        self.nelems = 0
        self.counts = [0] * num_list_elem

    def get_index(self, item):
        """
        Given an item, return its corresponding index (0-9 for digits, 10-35
        for lowercase letters, 36-61 for uppercase letters).
        If the item is not an alphanumeric character, return -1.

        """
        num_numbers = 10
        num_letters = 26
        if item.isnumeric():
            return ord(item) - ord('0')
        elif item.islower():
            return ord(item) - ord('a') + num_numbers
        elif item.isupper():
            return ord(item) - ord('A') + num_letters + num_numbers
        else:
            return -1

    def get_char(self, idx):
        """
        Given an index (0-61), return the corresponding character.

        """
        # assert for valid indices
        assert 0 <= idx <= 61

        # define variables and bounds
        num_numbers = 10
        num_letters = 26
        lower_dig = 0
        upper_dig = 9
        lower_lower_case = 10
        upper_lower_case = 35
        lower_upper_case = 36
        upper_upper_case = 61

        if lower_dig <= idx <= upper_dig:
            return chr(idx + ord('0'))
        elif lower_lower_case <= idx <= upper_lower_case:
            return chr(idx + ord('a') - num_numbers)
        elif lower_upper_case <= idx <= upper_upper_case:
            return chr(idx + ord('A') - num_letters - num_numbers)

    def get_count(self, item):
        """
        Returns the count of a character item.
        If the item does not exist in the counter, return 0.

        """
        # check if the item is alphanumeric
        if self.get_index(item) == -1:
            return 0
        else:
            return self.counts[self.get_index(item)]
            # get index of item from self.counts

    def get_all_counts(self):
        """
        Returns a dictionary of all item to count pairs, where the keys are
        characters and values are counts. Only non-zero counts should be
        added.

        """
        new_dict = {}
        # where item is the counts, because it is of the count list
        for index, counts in enumerate(self.counts):
            if counts > 0:
                new_dict[self.get_char(index)] = counts
        return new_dict

    def add_items(self, items):
        """
        Takes a string items and adds each character to the counter.
        Note that you should not add non-alphanumeric characters to this
        counter. Make sure to update both counts and nelems attributes.

        """
        min_index = 0
        max_index = 61
        for char in items:
            if min_index <= self.get_index(char) <= max_index:
                self.counts[self.get_index(char)] += 1
                self.nelems += 1

# Question 2
def find_two_sums_rec(main, sub):
    """
    A recursive function that takes two sequences of numeric values
    (main and sub), and calculates two kinds of sum of the main sequence:
    1) Sum of intersection: the sum of all numbers in the main sequence that
       also appear in the sub sequence.
    2) Sum of differences: the sum of all numbers in the main sequence that
       do not appear in the sub sequence.


    >>> main_seq = [0, 1, 1, 2, 3, 3, 4, 5, 5]
    >>> find_two_sums_rec(main_seq, [])
    (0, 24)
    >>> find_two_sums_rec(main_seq, [1, 2])
    (4, 20)
    >>> find_two_sums_rec(main_seq, [3, 4, 5])
    (20, 4)

    >>> main_seq_2 = [2, 4, 6, 8, 10, 10]
    >>> find_two_sums_rec(main_seq_2, [])
    (0, 40)
    >>> find_two_sums_rec(main_seq_2, [2, 10])
    (22, 18)
    >>> find_two_sums_rec(main_seq_2, [1])
    (0, 40)
    """
    if len(main) == 0:
        return (0, 0)
    else:
        # check if val in main is in sub
        if main[0] in sub:
            #new sum of next set of values(rest of main); returns a tuple
            new_sum = find_two_sums_rec(main[1:], sub)
            # add the inter's sum index(0) to main[0] to update
            return (new_sum[0] + main[0], new_sum[1])
        elif main[0] not in sub:
            # sum of the remaining values in main to add onto old new sum
            next_new_sum = find_two_sums_rec(main[1:], sub)
            # keep the intersection sum, but add main[0] to the other element
            return (next_new_sum[0], next_new_sum[1] + main[0])


# Question 3
def compute_max_string(base, pattern):
    """
    A recursive function that takes a base string and a non-empty pattern
    string. It computes the length of the largest substring of the base that
    starts and ends with the pattern. If no match is found, return 0.

    >>> compute_max_string("jumpsjump", "jump")
    9
    >>> compute_max_string("hwhwhw", "hwh")
    5
    >>> compute_max_string("frontsdakonsakdna", "front")
    5
    >>> compute_max_string("life", "life")
    4
    >>> compute_max_string("loser", "losers")
    0
    >>> compute_max_string("bo$$", "$$")
    2
    >>> compute_max_string("", "howboutdis")
    0
    """
    #base case 1: empty string
    if base == "":
        return 0
    # base case 2: not able to find a pattern if base is shorter
    if len(base) < len(pattern):
        return 0
    # base case 3: starts and ends with the pattern
    if base[:len(pattern)] == pattern and (base[len(base)-len(pattern):]
                                           == pattern):
        return len(base)
    else:
        # prefix; base does not start with pattern
        if pattern != base[:len(pattern)]:
            return compute_max_string(base[1:], pattern)
        # suffix; base does not end with pattern
        if pattern != base[len(base)-len(pattern):]:
            return compute_max_string(base[:-1], pattern)

# Question 4 (Extra Credit)
def group_summation(nums, target):
    """
    A recursive function that takes a non-empty list of positive integers and
    a positive integer target.
    It returns True if it’s possible to pick a combination of integers from
    nums, such that their sum equals the target.
    Otherwise, it will return False.



    >>> group_summation([3, 34, 4, 12, 5, 2], 9)
    True
    >>> group_summation([1, 1, 1], 9)
    False
    >>> group_summation([1, 10, 9, 8], 17)
    True
    """

    return ...
