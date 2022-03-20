"""
DSC 20 Lab 05
Name: Tonia Le
PID:  A15662705
"""

# Question 1.1
def count_letters(inpath):
    """
    Read in a file and return a dictionary with the counts of all characters
    (including spaces and all other symbols).

    >>> count_letters("infiles/blank.txt")
    {}
    >>> count_letters("infiles/input1.txt")
    {'H': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, '.': 1, '\\n': 1, 'a': 5}
    >>> count_letters("infiles/input3.txt")
    {'a': 3}
    """
    dictionary = {}
    # open each path
    with open(inpath, 'r') as file:
        for line in file:
            # looking at each character's frequency
            for character in line:
                # if character is already in the dictionary, add to it
                if character in dictionary:
                    dictionary[character] += 1
                else:
                    # if character, the count is one
                    dictionary[character] = 1
    return dictionary

# Question 1.2
def count_letters_multiple_files(*inpaths):
    """
    Read in files and return a dictionary with the counts of all characters
    in all the files combined (including spaces and all other symbols).

    >>> count_letters_multiple_files("infiles/input1.txt",
    ... "infiles/blank.txt")
    {'H': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, '.': 1, '\\n': 1, 'a': 5}
    >>> count_letters_multiple_files("infiles/input2.txt")
    {'z': 7, '\\n': 6}
    >>> count_letters_multiple_files('infiles/blank.txt',
    ... 'infiles/input2.txt', 'infiles/input3.txt')
    {'z': 7, '\\n': 6, 'a': 3}
    """
    dictionary = {}
    # loop through each inpath in the multiple inpath files
    for inpath in inpaths:
        # update ({dictionary from count letters} to new dictionary)
          dictionary.update(count_letters(inpath))
    return dictionary

# Question 2
def find_intersection(lst1, lst2):
    """
    A function that takes two lists (lst1 and lst2), and finds all items in
    lst2 that also occur in lst1. Return all overlapping items in a list,
    whose items are in the same order as lst2 (i.e. items appear earlier in
    lst2 should also appear earlier in the returned list).

    Note that this function should preserve all intersecting values as many
    times as they occur in both lists.

    >>> find_intersection([1, 2, 3, 4], [1, 2, 1, 2])
    [1, 2]
    >>> find_intersection(['a', 'b', 'c', 'c'], ['c', 'c', 'd', 'e'])
    ['c', 'c']
    >>> find_intersection([1, 2, 3], [])
    []
    """
    output = []
    # loop through the elements in first list
    for elements in lst1:
        # put overlapping elements in a list in the same order as list 2
        if elements in lst2:
            output.append(elements)
    return output

# Question 3
def process_dict(data):
    """
    Process the input dictionary with the rules below.
    You can assume that all key-value pairs are non-negative integers.

    For each key in the dictionary:
    - if the key is odd, remove this key-value pair from the dictionary.
    - else if the square of this key exists in the dictionary, square the
        current key's corresponding value. Do not modify the key itself.
    - else if the square root of this key exists in the dictionary,
        square root the current key's corresponding value and convert it
        to int (with int()). Do not modify the key itself.
    - otherwise, don't modify this key and its corresponding value.

    >>> process_dict({1: 1, 2: 2, 3: 3, 4: 4})
    {2: 4, 4: 2}
    >>> process_dict({})
    {}
    >>> process_dict({10: 10, 100: 100, 4: 1})
    {10: 100, 100: 10, 4: 1}
    """
    # new dictionary
    new_dict = {}
    # loop through key and value
    for key, value in data.items():
        # defining the squared and square roots
        squared_key = key**2
        square_root_key = key**.5
        squared_value = value**2
        square_root_value = int(value**.5)
        # check keys and set the value = to previously defined variables
        # depending on if the condition of key meets
        if key % 2:
            del key
        elif squared_key in data.keys():
            new_dict[key] = squared_value
        elif square_root_key in data.keys():
            new_dict[key] = square_root_value
        else:
            new_dict[key] = value
    return new_dict

# Question 4
def determine_siblings(str1, str2):
    """
    A function that checks if two string arguments are siblings.

    We define two strings as siblings if we can rearrange one string to form
    another. For instance, we can rearrange "aabbcde" to form "abedcba" since
    they have the same occurrences of characters, but we cannot rearrange
    "abcdefg" to "xyzabcd".

    >>> determine_siblings("abc", "cba")
    True
    >>> determine_siblings("friend", "aba")
    False
    >>> determine_siblings("ccc", "aba")
    False
    """
    # sort letters so if they're siblings, they'll have the same amount of
    # letters
    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False
    else:
        return False

# Question 5
def create_piecewise_function(*cases):
    """
    Given a list of cases as (lower_bound, upper_bound, subfunction) tuples,
    return a piecewise function that takes a numeric argument and apply the
    correct subfunction to the input.

    >>> f_x = create_piecewise_function( \
        (-float('inf'), -1, lambda num: -3 - num), \
        (1, float('inf'), lambda num: num * 3 + 1))
    >>> f_x(-2)
    -1
    >>> f_x(-1)
    -1
    >>> f_x(1)
    4
    """
    # inner function goes through the cases
    def piecewise_function(num):
        for case in cases:
            lower_bound = case[0]
            upper_bound = case[1]
            subfunction = case[2]
            if num >= lower_bound and num < upper_bound:
                return subfunction(num)
        return num
    return piecewise_function
