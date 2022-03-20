"""
DSC 20 Homework 03
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def assert_playground(num, lst, *args, **kwargs):
    """
    This function filters out inputs not of the expected types.
    Requirements for all parameters:
    1) "num" must be a positive float
    2) "lst" must be a list of numeric values summing to no less than 10
    3) "args" must be a float between -5.0 and -1.0 (inclusive)
    4) "kwargs" must be a string having the second character be an "S" and
    be  of length greater than 1

    >>> assert_playground(1.5, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    1.5
    >>> assert_playground(15, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(1.5, [0, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(1.22, [10, 1], -1.12, -9.17,s1="sS", s2="DsC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(3.0, [11, 1], 3, 2,s1="aSsert", s2="DSC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(3.0, [11, 1], -1.3, 22.2,s1="aSsert")
    3.0
    """
    # check if num is a positive float
    assert isinstance(num, float) and (num > 0)
    # check if lst is a list
    assert isinstance(lst, list)
    # check if the elements of lst are either int/ float & sum to be > 10
    assert (all(isinstance(element, (int, float)) for element in lst) and
            (sum(lst) > 10))
    # check if the args are all float
    assert all(isinstance(element, float) for element in args)
    # check if at least one arg > - 5.0 & < -1.0
    assert any(-5.0 < element and element < -1.0 for element in args)
    # check if all values in kwargs are strings with len > 1 & has a second
    # character of capital 'S'
    assert all(isinstance(element, str) and (len(element) > 1) and
               (element[1] == 'S') for element in kwargs.values())
    #return num if all assert tests pass
    return num

# Question 2
def various_types(lst):
    """
    This function takes in a list and performs operations on the elements in
    them depending on the type of element. Elements that are booleans will be
    changed to the opposite boolean, strings will be reversed, integers will
    be squared, and the length will be returned if the element is a list.
    Any other type will be replaced with "None".

    >>> various_types(['Hello', 4, ['A', 'B', 'C'], True])
    ['olleH', 16, 3, False]
    >>> various_types([])
    []
    >>> various_types([False, 0, 1, [], 'olleH', ('a', 'b')])
    [True, 0, 1, 0, 'Hello', None]
    >>> various_types([2, (2,2,2), [2,0]])
    [4, None, 2]
    >>> various_types(['', [2], True, False])
    ['', 1, False, True]
    >>> various_types([['','','','','']])
    [5]
    """
    # checks if input is a list
    assert isinstance(lst, list)

            # returns the opposite if boolean
    return [not element if isinstance(element, bool) \
            # reverses element if string
            else element[::-1] if isinstance(element, str) \
            # sqaures element if integer
            else element**2 if isinstance(element, int) \
            # gets length of element if list
            else len(element) if isinstance(element, list) \
            # otherwise "None" for elements not of the above types
            else None for element in lst]

# Question 3
def find_greatest_divisor(lower, upper):
    """
    This function returns the greatest single digit divisor for every number
    in the range of inputs from lower to upper (inclusive) in a dictionary.
    The keys of the dictionary are each number from lower to upper and the
    corresponding values are their highest single digit divisor.

    >>> find_greatest_divisor(20, 27)
    {20: 5, 21: 7, 22: 2, 23: 1, 24: 8, 25: 5, 26: 2, 27: 9}
    >>> find_greatest_divisor(1, 10)
    {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 5}
    >>> find_greatest_divisor(11, 19)
    {11: 1, 12: 6, 13: 1, 14: 7, 15: 5, 16: 8, 17: 1, 18: 9, 19: 1}
    >>> find_greatest_divisor(98, 25)
    Traceback (most recent call last):
    AssertionError
    >>> find_greatest_divisor(0, 10)
    {0: 9, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 5}
    >>> find_greatest_divisor(-2,2)
    {-2: 2, -1: 1, 0: 9, 1: 1, 2: 2}
    >>> find_greatest_divisor(1.3, 5)
    Traceback (most recent call last):
    AssertionError
    """
    # checks that lower and upper are both integers
    assert isinstance(lower, int)
    assert isinstance(upper, int)
    # checks that lower is less than or equal to upper input
    assert lower <= upper
    # constant for first double digit number
    double_digit = 10
    # numbers given the inclusive bounds
    numbers = [number for number in range(lower, upper + 1)]
    return {number: divisor for number in numbers \
    for divisor in range(1, double_digit) if number % divisor == 0}

# Question 4
def best_player(**player_scores):
    """
    This function gets the truncated mean, which drops the highest and lowest
    score in a given player's list of scores. The result is the name of the
    player with the highest score after truncating the mean.

    >>> best_player(marina=[9.6, 9, 9.8, 9.9], yuxuan=[9.0, 9.5, 9.9],
    ... elvy=[10.0, 9.8, 10.0, 9.5, 9.6])
    'elvy'
    >>> best_player(sean=[100, 99.99, 100])
    'sean'
    >>> best_player(james=[3.8, 3.5, 3.2], simon=[4.0, 3.6, 3.0])
    'simon'
    >>> best_player(sam = [2.0, 3.5, 2.3], sean =[2.5, 3.5, 2.0])
    'sean'
    >>> best_player(joe = [100, 100, 20], josh = [40, 90, 90])
    'joe'
    >>> best_player(jane = [2.1, 5.0, 1.3, 4.6], ann = [4.9, 100, 1.0, 1.1])
    'jane'
    """
    # check if score is numeric and not negative
    assert all(list(map(lambda score:
                        (isinstance(score, (float, int)))
                        and score >= 0, [score for player in
                                         list(player_scores.items())
                                         for score in player[1]])))

    return list(enumerate(player_scores))[[sum(list(sorted(scores)[1:-1]))/
                                           len(list(sorted(scores)[1:-1]))
                                           for player, scores in
                                           player_scores.items()].index(
                                               max([sum(list(sorted(scores)[1:-
                                                                            1])
                                                       )/
                                                    len(list(sorted(scores)
                                                             [1:-1]))
                                                    for player, scores in
                                                    player_scores.items()]))
                                         ][1]

# Question 5
def deserialize(outpath, patterns, *serialized_lines):
    """
    This function uses the arguments, serialized_lines, which contains list
    of counts that represents every line in the outpath text file. "Patterns"
    is a list of the patterns used to match with the list of counts in order
    to turn the serialized list back to the drawing file of outpath.

    >>> deserialize("outfiles/out1.txt", ["**", "Marina"],
    ... [1,1,1], [0,5], [3,3,0,3,3])
    >>> with open("outfiles/out1.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    **Marina**
    MarinaMarinaMarinaMarinaMarina
    ******MarinaMarinaMarinaMarinaMarinaMarina******

    >>> deserialize("outfiles/out2.txt", ["__", "()", "??"],
    ... [2,4,0,2], [1,2,0,2,2,0,1], [0,2,0,4,2,0], [0,1,0,6,1,0])
    >>> with open("outfiles/out2.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    ____()()()()____
    __()()____()()__
    ()()________()()
    ()____________()

    >>> deserialize("outfiles/out3.txt", ["##", "__"],
    ... [2,3,2,2,2,1,2,3,1,1], [1,1,1,1,1,3,1,5,1,1,1,1,1],
    ... [1,1,1,2,1,2,1,4,1,2,1,1,1], [1,1,1,3,1,1,1,3,1,3,1,1,1],
    ... [2,2,2,3,2,1,3,2,1,1])
    >>> with open("outfiles/out3.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    ####______####____####__####______##__
    ##__##__##______##__________##__##__##
    ##__##____##____##________##____##__##
    ##__##______##__##______##______##__##
    ####____####______####__######____##__
    >>> deserialize("outfiles/out4.txt", ["-", "A", "B","C"],
    ... [1, 1, 1, 1, 1], [0, 2, 2, 2, 2], [0, 0, 4, 0])
    >>> with open("outfiles/out4.txt", "r") as outfile4:
    ...     print(outfile4.read().strip())
    -ABC-
    AABBCC--
    BBBB
    >>> deserialize("outfiles/out5.txt", ["$$$", "HA"],
    ... [1, 2, 1], [0, 6], [3, 0], [0, 1, 0, 1, 1])
    >>> with open("outfiles/out5.txt", "r") as outfile5:
    ...     print(outfile5.read().strip())
    $$$HAHA$$$
    HAHAHAHAHAHA
    $$$$$$$$$
    HAHA$$$
    >>> deserialize("outfiles/out6.txt", [":(", "DSC"],
    ... [1, 1, 1], [0, 3], [5, 0])
    >>> with open("outfiles/out6.txt", "r") as outfile6:
    ...     print(outfile6.read().strip())
    :(DSC:(
    DSCDSCDSC
    :(:(:(:(:(
    """
    output = ""
    # get lists in serialized_lines
    for count_list in serialized_lines:
        new_string = ""
        # elements from those lists
        for index, count in enumerate(count_list):
            # pair element from pattern_list w/ element from count lists
            new_string = new_string + (
                patterns[index % len(patterns)]
                * count)
        output += (new_string + '\n')
    # write to file
    outfile = open(outpath, "w")
    outfile.write(output)
    outfile.close()

# Question 6
def sequential_apply(nums, *instructions):
    """
    This function takes a numeric list and applies operations on
    the list according to the sequence of instructions, which are
    inputted as tuples.

    Examples of all instructions:
    [1, 2, 3, 4], ('add', 1) -> [2, 3, 4, 5]
    [1, 2, 3, 4], ('multiply', 2) -> [2, 4, 6, 8]
    [1, 2, 3, 4], ('insert', 1, 100) -> [1, 100, 2, 3, 4]
    [1, 2, 3, 4], ('remove', 1) -> [1, 3, 4]
    [1, 2, 3, 4], ('mean',) -> [2.5, 2.5, 2.5, 2.5]
    [1, 2, 3, 4], ('range',) -> [3, 3, 3, 3]

    >>> sequential_apply([1, 2, 3, 4], ('add', 1))
    [2, 3, 4, 5]
    >>> sequential_apply([3.3, 6.6, 7.7],
    ... ('insert', 1, 5.5), ('insert', 1, 4.4))
    [3.3, 4.4, 5.5, 6.6, 7.7]
    >>> sequential_apply([9.9, 1.3, 8.2, 4, 10],
    ... ('remove', 0), ('mean',), ('range',), ('add', 10))
    [10.0, 10.0, 10.0, 10.0]
    >>> sequential_apply([-9,-9,18], ('mean',),
    ... ('add', 5),('insert', 2, 10))
    [5.0, 5.0, 10, 5.0]
    >>> sequential_apply([0,1,2,3,4,5,6,7,8],
    ... ('remove', 3), ('insert',3, 3))
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    third_element_index = 2
    # loop through the sequence of instructions from the input
    for sequence in instructions:
        # defining operation as the first element of the tuple
        operation = sequence[0]
        # add an amount, sequence[1], to every list element
        if operation == 'add':
            nums = [sequence[1] + element for element in nums]
        # multiply every list element by an amount, sequence[1]
        elif operation == 'multiply':
            nums = [sequence[1] * element for element in nums]
        # insert a new value to the numeric list at an index
        elif operation == 'insert':
            index = sequence[1]
            value = sequence[third_element_index]
            nums[index:index] = [value]
        # remove an element at a given index
        elif operation == 'remove':
            index = sequence[1]
            del nums[index]
        # replace all elements with the average val of the list
        elif operation == 'mean':
            list_mean = sum(nums)/len(nums)
            nums = [list_mean for element in nums]
        # replace all elements with the range of the list
        elif operation == 'range':
            list_range = max(nums) - min(nums)
            nums = [list_range for element in nums]
    return nums
