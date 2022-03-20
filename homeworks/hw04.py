"""
DSC 20 Homework 04
Name: Tonia Le
PID:  A15662706
"""

# Utility Function
def is_iterable(obj):
    """
    A function that checks if `obj` is a iterable (can be iterated over
    in a for-loop).

    DO NOT MODIFY THIS FUNCTION. You don't need to add new doctests
    for this function.

    >>> is_iterable(1)
    False
    >>> is_iterable("DSC 20")
    True
    >>> is_iterable(["Fall", 2020])
    True
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Question 1
def ucsd_spam_quarantine(emails, allowlist, blocklist):
    """
    This function filters undesired email addresses from a list of emails.
    An undesired, malicious, email address is in the blocklist, or it doesn't
    end with "ucsd.edu". An exception for what is considered a malicious
    email address is that it is in the allow list, which then it will be
    returned in list alongside non-malicious email addresses.

    >>> emails = ["mlanglois@ucsd.edu", "istudents@ucsd.edu", \
    "jsmith@eng.ucsd.edu", "hello@gmail.com", "python@yahoo.com", \
    "phish@ucsd.edu"]
    >>> allowlist = ["hello@gmail.com"]
    >>> blocklist = ["phish@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['mlanglois@ucsd.edu', 'istudents@ucsd.edu', \
'jsmith@eng.ucsd.edu', 'hello@gmail.com']

    >>> emails = ["sean@ucsd.edu", "jojo@ucsd.edu", "dsc@ucsd.edu.us", \
    "tritons@outlook.com", "spam@ucsd.edu", "bad@ucsd.edu"]
    >>> allowlist = ["tritons@outlook.com", "no-reply@piazza.com"]
    >>> blocklist = ["spam@ucsd.edu", "bad@ucsd.edu", "phish@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['sean@ucsd.edu', 'jojo@ucsd.edu', 'tritons@outlook.com']

    >>> emails = ["scam@ucsd.edu", "econdept@ucsc.edu", "LAKERS@yahoo.com", \
    "scam-diego@ucsd.edu"]
    >>> allowlist = ["LAKERS@yahoo.com"]
    >>> blocklist = ["scam@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['LAKERS@yahoo.com', 'scam-diego@ucsd.edu']

    >>> emails = ("tle@gmail.com", "tle@aol.com", "tle@yahoo.com")
    >>> allowlist = []
    >>> blocklist = []
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    Traceback (most recent call last):
    AssertionError

    >>> emails = ["scam-diego@ucsd.edu", "SSC@ucsd.edu", "finaid@ucsd.edu", \
     "tle@gmail.com", "tritons4neva@aol.com"]
    >>> allowlist = ["tle@gmail.com"]
    >>> blocklist = ["finaid@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['scam-diego@ucsd.edu', 'SSC@ucsd.edu', 'tle@gmail.com']
    """
    # check if email addresses are in a list
    assert isinstance(emails, list)
    # check if addresses are strings
    assert all(isinstance(addresses, str) for addresses in emails)
    # check if allowlist is a list
    assert isinstance(allowlist, list)
    # check if items in allowlist are strings
    assert all(isinstance(allowed, str) for allowed in allowlist)
    # check if blocklist is a list
    assert isinstance(blocklist, list)
    # check if items in blocklist are strings
    assert all(isinstance(blocked, str) for blocked in blocklist)

    return  list(filter(lambda x: (x not in blocklist) and
                        (x.endswith('ucsd.edu')) or
                        (x in allowlist), emails))

# Question 2
def create_dsc_email(students, years):
    """
    Given a tuple containing a student's full name, class year, college name,
    major code in parameter "students", this function creates an email for
    data science major students in desired class years(presented as a list
    of years in the "years" parameter).
    It first filters the list of tuples of student information and then uses
    the "years" parameter to check for students of desired class years.
    After filtering out by the correct major and desired class years, emails
    are created and put into a dictionary where the keys are students'
    full names and values are the corresponding emails.

    >>> students = [ \
        ("First Middle Last", 2022, "revelle", "DS25"), \
        ("hi HELLO", 2022, "seventh", "DS25"), \
        ("Computer Science", 2021, "Warren", "CS25"), \
        ("longfirstname longlastname", 1990, "Marshall", "DS25") \
    ]
    >>> create_dsc_email(students, [2022])
    {'First Middle Last': 'firlast22rc@dsc.ucsd.edu', \
'hi HELLO': 'hihello22sv@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [1990, 2021])
    {'longfirstname longlastname': 'lonlongla90tm@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [])
    {}

    >>> students = [ \
        ("Sammy Jones", 2023, "SIXth", "DS25"), \
        ("First Middle Last", 2021, "seventh", "DS25"), \
        ("Abby Ko", 2021, "revelle", "EN28"), \
        ("Shawn Wu", 2022, "Sixth", "EN26"), \
        ("jake jay monste", 2022, "sixth", "DS25") \
    ]
    >>> create_dsc_email(students, [2021])
    {'First Middle Last': 'firlast21sv@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [2022])
    {'jake jay monste': 'jakmonste22sx@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [2022, 2023])
    {'Sammy Jones': 'samjones23sx@dsc.ucsd.edu', \
'jake jay monste': 'jakmonste22sx@dsc.ucsd.edu'}
    """
    # filter for only DS25 students
    by_major = filter(lambda x: x[-1] == 'DS25', students)
    #filter for correct years from the DS25 students
    by_maj_and_year = filter(lambda x: x[1] in years, by_major)

    def info(student):
        """
        This inner function creates the emails for the DS25 students
        with class years as per the input parameter, years, based on
        their names and college.
        """
        third_position = 2
        fourth_position = 3
        fifth_position = 6
        # split name to easily identify the first & last names
        name = student[0].split()
        first_name = name[0][:fourth_position]
        last_name = name[-1][:fifth_position]
        # turn class year into a string
        class_year = str(student[1])[third_position:]
        # indexing for college names from student info
        college = student[third_position]
        # .lower() to ignore cases
        if college.lower() == 'revelle':
            college = 'RC'
        elif college.lower() == 'muir':
            college = 'MC'
        elif college.lower() == 'marshall':
            college = 'TM'
        elif college.lower() == 'warren':
            college = 'WC'
        elif college.lower() == 'roosevelt':
            college = 'ER'
        elif college.lower() == 'sixth':
            college = 'SX'
        elif college.lower() == 'seventh':
            college = 'SV'
        return (first_name + last_name + class_year + college
                + '@dsc.ucsd.edu').lower()
    # taking names(x[0]) from the list of student info filtered by DS25 & year
    emails = list(map(lambda x: (x[0], info(x)), by_maj_and_year))
    # dictionary where the keys are the names from filtered list and values
    # are the actual emails created by the functiono, info.
    return dict(emails)

# Question 3
def base_converter(target_base):
    """
    This function takes in an integer between and including 2 and 36 as the
    "target base".
    It'll return a function that takes a non-negative integer in decimal
    (base-10) and converts it to the target base as a string.
    If the base is greater than 10, those digits(up to 36) will be expressed
    by the letters of the alphabet. These will be returned as a string.

    >>> binary_converter = base_converter(2)
    >>> [binary_converter(i) for i in range(10)]
    ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']
    >>> base_converter(16)(8200)
    '2008'
    >>> base_converter(36)(8200)
    '6BS'

    >>> binary_converter = base_converter(4)
    >>> [binary_converter(i) for i in range(6)]
    ['0', '1', '2', '3', '10', '11']
    >>> base_converter(-1)(400)
    Traceback (most recent call last):
    AssertionError
    >>> base_converter(24)(400)
    'GG'
    """
    # target base and is an integer
    assert isinstance(target_base, int) and target_base >= 0
    # check if target base is in the correct bounds
    assert 2 <= target_base <= 36

    # dictionary to store the values and digits
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    values = dict(enumerate(digits))

    def converter(current_number):
        """
        This function yields for the remainder by performing modulo and
        integer division operations on the number to convert. It also gets
        the digits (provided as the values of our defined dictionary).
        Ultimately returning the result as a string.
        """
        # non-negative target base and is an integer
        assert isinstance(current_number, int) and current_number >= 0

        output = []
        if current_number == 0:
            output.append('0')
        # loop through as long as the current # isn't zero
        while current_number != 0:
            # get the remainder
            remainder = current_number % target_base
            current_number = current_number // target_base
            digis = values[remainder]
            output.append(str(digis))
        output.reverse()
        output = ('').join(output)
        return output
    return converter

# Question 4
def magic_sequence_generator(start0, start1, start2):
    """
    This generator takes three arguments: start0, start1, start2 and creates
    an infinite sequence of non-negative integers. To create a new value, it
    stores the values of the arguments from three previous rounds and resuses
    them for this new absolute value.

    >>> gen = magic_sequence_generator(10, 20, 30)
    >>> [next(gen) for _ in range(3)]
    [10, 20, 30]
    >>> next(gen)
    0
    >>> [next(gen) for _ in range(10)]
    [50, 20, 30, 40, 10, 60, 10, 60, 10, 60]

    >>> gen = magic_sequence_generator(-1, 2, 3)
    >>> [next(gen) for _ in range(2)]
    Traceback (most recent call last):
    AssertionError

    >>> gen = magic_sequence_generator(15, 20, 25)
    >>> [next(gen) for _ in range(3)]
    [15, 20, 25]
    >>> [next(gen) for _ in range(6)]
    [10, 35, 0, 45, 10, 35]
    >>> [next(gen)]
    [20]
    """
    assert isinstance(start0, int) and start0 >= 0
    assert isinstance(start1, int) and start1 >= 0
    assert isinstance(start2, int) and start2 >= 0

    while True:
        # first three of the sequence are the original arguments
        yield start0
        yield start1
        yield start2
        # calculating the following intergers
        start0 = abs(start0 + start1 - start2)
        start1 = abs(start1 + start2 - start0)
        start2 = abs(start2 + start0 - start1)

# Question 5
def round_robin_generator(k, arg1, arg2, arg3):
    """
    This function creates three generators, one for each of the iterable
    arguments: arg1, arg2, and arg3. These generators will yield the next
    "k" elements in order from each iterable object. It will yield "None"
    for objects that can no longer be iterated on.

    >>> arg1 = "abcdefgh"
    >>> arg2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> arg3 = (True, False, True, False, True, False)
    >>> gen = round_robin_generator(2, arg1, arg2, arg3)
    >>> [next(gen, None) for _ in range(14)]
    ['a', 'b', 1, 2, True, False, 'c', 'd', 3, 4, True, False, 'e', 'f']

    >>> gen = round_robin_generator(3, arg1, arg2, arg3)
    >>> [next(gen, None) for _ in range(14)]
    ['a', 'b', 'c', 1, 2, 3, True, False, True, 'd', 'e', 'f', 4, 5]

    >>> arg4 = "dsc"
    >>> arg5 = [2, 0]
    >>> arg6 = "fall"
    >>> gen = round_robin_generator(4, arg4, arg5, arg6)
    >>> [next(gen, None) for _ in range(10)]
    ['d', 's', 'c', None, 2, 0, None, None, 'f', 'a']

    >>> arg7 = "midterm szn"
    >>> arg8 = (False, False, False, False)
    >>> arg9 = [0, 1, 0, 1, 0, 1]
    >>> gen = round_robin_generator(3, arg7, arg8, arg9)
    >>> [next(gen, None) for _ in range(9)]
    ['m', 'i', 'd', False, False, False, 0, 1, 0]

    >>> gen = round_robin_generator(5, arg7, arg8, arg9)
    >>> [next(gen, None) for _ in range(10)]
    ['m', 'i', 'd', 't', 'e', False, False, False, False, None]

    >>> arg10 = [2, 4, 6, 8, 10]
    >>> arg11 = "crying"
    >>> arg12 = "hehehehe"
    >>> gen = round_robin_generator(3, arg10, arg11, arg12)
    >>> [next(gen, None) for _ in range(6)]
    [2, 4, 6, 'c', 'r', 'y']
    """
    #generators created to yield later
    gen_1 = (arg for arg in arg1)
    gen_2 = (arg for arg in arg2)
    gen_3 = (arg for arg in arg3)

    #iterations until 'k' with default value of 'None'
    while True:
        for element in range(k):
            yield next(gen_1, None)
        for element in range(k):
            yield next(gen_2, None)
        for element in range(k):
            yield next(gen_3, None)

# Question 6
def make_generator(*args):
    """
    Previously defined generators will be called back if the inputs meet
    certain conditions:
        1. If three non-negative integers are passed as arguments, then
            "magic_sequence_generator" will be returned.
        2. If three iterables are passed as arguments, "round_robin_generator"
            will be returned, where "k" is 2.
    Otherwise, a new generator that yield arguments at even indices first and
    then all arguments at odd indices will be returned.

    >>> gen1 = make_generator(10, 20, 30)
    >>> [next(gen1, None) for _ in range(10)]
    [10, 20, 30, 0, 50, 20, 30, 40, 10, 60]
    >>> gen2 = make_generator([10, 20], "Sean", [True, False])
    >>> [next(gen2, None) for _ in range(10)]
    [10, 20, 'S', 'e', True, False, None, None, 'a', 'n']
    >>> gen3 = make_generator("Ev", 0, ["en"], ("DD",))
    >>> [next(gen3, None) for _ in range(10)]
    ['Ev', ['en'], 0, ('DD',), None, None, None, None, None, None]
    >>> gen4 = make_generator(1, 2, 3, 4, 5)
    >>> [next(gen4, None) for _ in range(5)]
    [1, 3, 5, 2, 4]
    >>> gen5 = make_generator(["What", "Is", "Happening", "?"], 2, 4, 6)
    >>> [next(gen5, None) for _ in range(4)]
    [['What', 'Is', 'Happening', '?'], 4, 2, 6]
    >>> gen6 = make_generator([2,4,6,8], ["two"], ["four"], ["six"], \
    ["eight"])
    >>> [next(gen6, None) for _ in range(4)]
    [[2, 4, 6, 8], ['four'], ['eight'], ['two']]
    """
    number_of_arguments = 3
    #Case 1: if 3 non-negative integers pass into magic_sequence_generator
    if (all(list(map(lambda x: isinstance(x, int) and x >= 0, args))) and
            len(args) == number_of_arguments):
        return magic_sequence_generator(*args)
    # Case 2: if 3 iterables, pass into round_robin_generator
    elif (all(list(map(lambda x: is_iterable(x), args))) and
          len(args) == number_of_arguments):
        k = 2
        return round_robin_generator(k, *args)
    # Case 3: if above conditions not met
    else:
        def other_gen():
            """
            This generator yields all of the arguments at even indices first
            and then all of those at odd indices.
            """
            skip_an_element = 2
            for elements in args[::skip_an_element] + args[1::skip_an_element]:
                yield elements
        return other_gen()

# Question 7
def skip_increasing(iterable, k):
    """
    Taking in an iterable and an intger, k, this function returns a list of
    values starting with the 0 index item and then skipping values in between
    in increments of 1.
    The output values will be returned when the iterable runs out of items or
    we reach k amount of elements in the output list.

    >>> skip_increasing(iter([1,2,3,4,5,6,7,8,9,10,11]), 5)
    [1, 2, 4, 7, 11]
    >>> skip_increasing(iter('ABcDefGhijKlmnoPqrs'), 10)
    ['A', 'B', 'D', 'G', 'K', 'P']
    >>> skip_increasing(iter((1, None, 3, 4, 5, 6, 7, 8)), 3)
    [1, None, 4]
    >>> skip_increasing(iter(['I', 'am', 20, 'very', 40, 50,'tired']), 4)
    ['I', 'am', 'very', 'tired']
    >>> skip_increasing(iter((5, 10, 15, 20, 25, 30)), 5)
    [5, 10, 20]
    >>> skip_increasing(iter([None, False, True, True, False, True]), 30)
    [None, False, True]
    """
    # defining skip as zero to not skip second element
    skip = 0
    output = []
    # iterate through iterable
    for element in iterable:
        if len(output) >= k:
            break
        output.append(element)
        # second loop to skip over increasing increments
        # skip is stored and keeps +1 until k or iterable is out of items
        for position in range(skip):
            next(iterable, None)
        skip += 1
    return output
