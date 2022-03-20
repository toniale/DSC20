"""
DSC 20 Homework 06
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def hate_f(word):
    """
    This function recursively removes any capital and lowercase
    letter "f"s from an inputted string, word.
    A string without letters "F" and "f" will be returned.

    >>> hate_f('FabFxx')
    'abxx'
    >>> hate_f('FfFf')
    ''
    >>> hate_f('ABCde')
    'ABCde'
    >>> hate_f('FFofofpsFF')
    'oops'
    >>> hate_f('')
    ''
    >>> hate_f('24f_4ever')
    '24_4ever'
    """
    letter_f = 'Ff'
    if word == "":
        return word
    elif word[0] in letter_f:
        return hate_f(word[1:])
    return word[0] + hate_f(word[1:])

# Question 2
def encode(mapping, plaintext):
    """
    This recursive function matches the characters in a string, plaintext,
    to keys in mapping. It then replaces the plaintext with the string value
    corresponding to the key.

    >>> mapping = {'z': 'not', 'r': 'ece', 't': 'dsc'}
    >>> encode(mapping, 'zzr')
    'notnotece'
    >>> encode(mapping, 'zzt')
    'notnotdsc'
    >>> encode(mapping, 'ttzrr')
    'dscdscnoteceece'
    >>> mapping = {'d': 'dog', 'r': 'bee', 'q': 'qts', 'b': 'bye', \
    'p': 'pls', 'h': 'hah'}
    >>> encode(mapping, 'pdqh')
    'plsdogqtshah'
    >>> encode(mapping, 'bbr')
    'byebyebee'
    >>> encode(mapping, 'hhbhh')
    'hahhahbyehahhah'
    >>> encode(mapping, '')
    ''
    """
    if plaintext == "":
        return ""
    # if first character in keys, return the value of the key + recursion
    if plaintext[0] in mapping.keys():
        return mapping[plaintext[0]] + encode(mapping, plaintext[1:])
    return plaintext[0] + encode(mapping, plaintext[1:])

# Question 3
def climb_stair(n_steps):
    """
    This function recursively returns the number of sum combinations of a
    positive integer, n_steps, where the only addends are the numbers 1
    and 2.

    >>> climb_stair(2)
    2
    >>> climb_stair(5)
    8
    >>> climb_stair(8)
    34
    >>> climb_stair(1)
    1
    >>> climb_stair(10)
    89
    >>> climb_stair(3)
    3
    """
    two_steps = 2
    if n_steps == 1:
        return 1
    if n_steps == two_steps:
        return two_steps
    else:
        return climb_stair(n_steps - 1) + climb_stair(n_steps - two_steps)

# Question 4
def add_all_digits(num):
    """
    Taking in a non-negative integer, num, this function recursively adds
    the digits of the integer until it becomes single digit. If num is already
    a single digit number, it returns itself.

    >>> add_all_digits(41)
    5
    >>> add_all_digits(567)
    9
    >>> add_all_digits(999777)
    3
    >>> add_all_digits(10)
    1
    >>> add_all_digits(3)
    3
    >>> add_all_digits(0)
    0
    """
    double_digit = 10
    # base case: returns itself if is a single digit
    if num < double_digit:
        return num
    else:
        # last digit of the sum
        last_digit = num // double_digit
        # sum of the rest of the digits
        all_else = num % double_digit
        # adding the last digit and sum all digits that's not the last
        return  add_all_digits(all_else + last_digit)

# Question 5
def find_max_recursive(lst):
    """
    This function finds the maximum value element in an input list, lst. It
    does so recursively by comparing the first element of the list with the
    rest of the list and returns the max.

    >>> find_max_recursive([1, 2, 3, 4, 5])
    5
    >>> find_max_recursive([10, 11, 5, 0, -10, 1])
    11
    >>> find_max_recursive(['b', 'c', 'z', 'y', 'a', 'e'])
    'z'
    >>> find_max_recursive([1, 32, 0.7, 2.1, 23.1])
    32
    >>> find_max_recursive(['T'])
    'T'
    >>> find_max_recursive([4, 4, 4])
    4
    """
    # max of one element is itself
    if len(lst) == 1:
        return lst[0]
    else:
        maximum = lst[0]
        max_num = find_max_recursive(lst[1:])
        # if list w/o element > the first element, where max is the largest
        # and max_num is the largest in the rest of the list excluding
        # first element
        if max_num > maximum:
            maximum = max_num
        return maximum

# Question 6
def skip_then_swap(string, n_skip, n_swap):
    """
    This function recursively swaps and skips characters in a string by pairs.
    It first skips n_skip amount of pairs and then swaps by n_swaps.
    A pair is one of the first character and one of the last. Multiple pairs
    continue with this pattern of pairing a character from the beginning
    and one at the end. A string would be returned after all operations.

    >>> skip_then_swap('kkkABXXXXCDkkk', 3, 2)
    'kkkDCXXXXBAkkk'
    >>> skip_then_swap('DSC20', 1, 2)
    'D2CS0'
    >>> skip_then_swap('skip_then_swap', 4, 3)
    'skip_neht_swap'
    >>> skip_then_swap('T', 2, 2)
    'T'
    >>> skip_then_swap('happyholidaze', 2, 1)
    'haapyholidpze'
    >>> skip_then_swap('skskNOTURKEYsksk', 0, 0)
    'skskNOTURKEYsksk'
    """
    if string == "":
        return ""
    if len(string) == 1:
        return string
    if n_swap == 0:
        return string
    else:
        # reduce n_skip to zero
        if n_skip > 0:
            return string[0] + \
                    skip_then_swap(string[1:-1], n_skip - 1, n_swap) + \
                    string[-1]
        # reduce n_swap to zero
        if n_skip == 0:
            return string[-1] + \
                    skip_then_swap(string[1:-1], 0, n_swap - 1) + \
                    string[0]

# Question 7
def flatten_dict(nested_dict):
    """
    This function takes in a dictionary, nested_dict, which may or may not
    have dictionaries in the values. If the value of nested_dict is a
    dictionary, then it will be "flattened", meaning the keys of the value's
    dictionary will be added to the key of the value.

    >>> flatten_dict({'A': 1, 'B': 2})
    {'A': 1, 'B': 2}
    >>> flatten_dict({'Hi': True, 'Hello': {'World': 'Java',
    ... 'Kitty': 'Python'}})
    {'Hi': True, 'HelloWorld': 'Java', 'HelloKitty': 'Python'}
    >>> flatten_dict({'A': {'B': 1, 'C': 2, 'D': {'E': 3, 'F': 4}},
    ... 'G': 5, 'H': 6})
    {'AB': 1, 'AC': 2, 'ADE': 3, 'ADF': 4, 'G': 5, 'H': 6}
    >>> flatten_dict({'NO':'NESTED', 'DICT': 'HERE', 'OR': 'HERE'})
    {'NO': 'NESTED', 'DICT': 'HERE', 'OR': 'HERE'}
    >>> flatten_dict({'Water': {'Gate': 'Scandal', 'Bottle': 'Filter',
    ... 'Bill': 'Due'}})
    {'WaterGate': 'Scandal', 'WaterBottle': 'Filter', 'WaterBill': 'Due'}
    >>> flatten_dict({})
    {}
    """
    result = {}
    for key, value in nested_dict.items():
        # check if value is a dictionary
        if isinstance(value, dict):
            # loop through the value dictionary
            # and concatenate its keys to outer key
            sub_dict = flatten_dict(value)
            for sub_key, sub_value in sub_dict.items():
                result[key + sub_key] = sub_value
        else:
            result[key] = value
    return result
