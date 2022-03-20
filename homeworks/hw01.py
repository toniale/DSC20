# DSC 20 Homework 01
# Name: Tonia Le
# PID:  A15662706

# Question 1
def older_tutor(first_name, first_age, second_name, second_age):
    """
    A function that returns the name of the older tutor given their names (as
    strings) and ages (as positive integers). If they happen to be of the same
    age, return a string: 'Same Age'.

    >>> older_tutor("Aaron", 22, "James", 21)
    'Aaron'
    >>> older_tutor("Elvy", 18, "Yuxuan", 20)
    'Yuxuan'
    >>> older_tutor("Simon", 999, "Sean", 999)
    'Same Age'
    >>> older_tutor("Amy", 20, "Shia", 23)
    'Shia'
    >>> older_tutor("Ben", 30, "Jan", 30)
    'Same Age'
    >>> older_tutor("Chase", 19, "James", 21)
    'James'
    """
    if first_age > second_age:
        return first_name
    elif first_age < second_age:
        return second_name
    else:
        return 'Same Age'

# Question 2
def older_tutor_year_month(f_name, f_year, f_month, s_name, s_year, s_month):
    """
    A function that that returns the name of the older tutor, given their
    names (as strings), years (as positive integers), and months (0 to 11).
    If they happen to be the same age return a string: 'Same Age'.

    You can reuse the function from the first question when needed.

    >>> older_tutor_year_month("Aaron", 22, 10, "James", 22, 5)
    'Aaron'
    >>> older_tutor_year_month("Elvy", 18, 11, "Yuxuan", 18, 11)
    'Same Age'
    >>> older_tutor_year_month("Simon", 10, 11, "Sean", 30, 3)
    'Sean'
    >>> older_tutor_year_month("Joe", 19, 4, "Ann", 19, 5)
    'Ann'
    >>> older_tutor_year_month("Dan", 19, 5, "Tim", 19, 2)
    'Dan'
    >>> older_tutor_year_month("Josh", 22, 0, "Kim", 22, 0)
    'Same Age'
    """
    if f_year > s_year:
        return f_name
    elif f_year < s_year:
        return s_name
    elif f_year == s_year:
        if f_month > s_month:
            return f_name
        elif f_month < s_month:
            return s_name
        else:
            return 'Same Age'

# Question 3
def message(name, dow, time):
    """
    A function that takes in (name, day of the week, time) and returns
    Sharmi's invitation to her discussion session. Check the doctest
    for the output string format.

    Note:
        <BLANKLINE> denotes a blank line in doctest.
        DO NOT append this token to the returned string.

    >>> print(message("Marina", "Friday", "4:00 PM"))
    Dear Marina,
    Please join our discussion on Friday at 4:00 PM.
    <BLANKLINE>
    Sharmi
    >>> print(message("Ann", "Tuesday", "4:15 PM"))
    Dear Ann,
    Please join our discussion on Tuesday at 4:15 PM.
    <BLANKLINE>
    Sharmi
    >>>
    print(message("Colin", "Friday", "3:50 PM"))
    Dear Colin,
    Please join our discussion on Friday at 3:50 PM.
    <BLANKLINE>
    Sharmi
    """
    return ('Dear' + ' ' + name + ',' + '\n' + 'Please join our discussion on '
            + dow + ' ' + 'at' + ' ' + time + '.' + '\n' + '\n' + 'Sharmi')

# Question 4
def larger_room(
        first_name,
        first_room_length,
        first_room_width,
        second_name,
        second_room_length,
        second_room_width,
):
    """
    A function that returns the name of the tutor living in a larger room,
    given their names (as strings), and their room dimensions (height and
    width as positive integers). If they happen to have the same room area,
    return a string: "Same Area".

    You may assume that their rooms are rectangular.

    >>> larger_room("Aaron", 22, 5, "James", 22, 10)
    'James'
    >>> larger_room("Elvy", 18, 11, "Yuxuan", 20, 3)
    'Elvy'
    >>> larger_room("Simon", 30, 3, "Sean", 2, 45)
    'Same Area'
    >>> larger_room("Colin", 12, 4, "Aaron", 22, 5)
    'Aaron'
    >>> larger_room("Sean", 2, 45, "Jack", 10, 9)
    'Same Area'
    >>> larger_room("Amy", 15, 7, "Yuxuan", 20, 3)
    'Amy'
    """
    first_room_size = first_room_length * first_room_width
    second_room_size = second_room_length * second_room_width

    if first_room_size > second_room_size:
        return first_name
    elif first_room_size < second_room_size:
        return second_name
    else:
        return 'Same Area'

# Question 5
def larger_multidim_room(
        first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room,
    given their names (as strings), and their room dimensions (as a list of
    positive integers). If they happen to have the same room volume,
    return a string: "Same Volume".

    You may assume two rooms have the same number of dimensions.

    >>> larger_multidim_room("Aaron", [22, 5, 7, 11], "James", [10, 11, 2, 9])
    'Aaron'
    >>> larger_multidim_room("Elvy", [11, 8, 1], "Yuxuan", [3, 5, 20])
    'Yuxuan'
    >>> larger_multidim_room("Simon", [20, 9], "Sean", [18, 10])
    'Same Volume'
    >>> larger_multidim_room("Yuxuan", [3, 5, 20], "Jack", [10, 8, 9])
    'Jack'
    >>> larger_multidim_room("Em", [4, 7, 10, 14, 2], "Lee", [2, 6, 8, 12, 2])
    'Em'
    >>> larger_multidim_room("Ann", [10, 9, 8], "Jack", [10, 8, 9])
    'Same Volume'
    """
    first_subspace = 1
    second_subspace = 1

    for first_dimension in first_room_dims:
        first_subspace = first_subspace * first_dimension
    for second_dimension in second_room_dims:
        second_subspace = second_subspace * second_dimension
    if first_subspace > second_subspace:
        return str(first_name)
    elif first_subspace < second_subspace:
        return str(second_name)
    else:
        return 'Same Volume'

# Question 6
def larger_room_subspace(
        ndim, first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room with
    larger subspace (calculated using only the first `ndim` dimensions), given
    their names (as strings), and their room dimensions (as a list of positive
    integers). If they happen to have the same room volume, return a string:
    "Same Volume".

    You may assume two rooms have the same number of dimensions, and `ndim`
    won't exceed the number of dimensions of both rooms.

    >>> larger_room_subspace(2, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'Same Volume'
    >>> larger_room_subspace(3, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'James'
    >>> larger_room_subspace(5, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'Aaron'
    >>> larger_room_subspace(2, "Jack", [10, 5, 3], "Tim", [5, 9, 12])
    'Jack'
    >>> larger_room_subspace(4, "Sean", [2, 4, 5, 2], "Ann", [2, 3, 2, 5])
    'Sean'
    >>> larger_room_subspace(3, "Jack", [10, 5, 3], "Tom", [5, 10, 3])
    'Same Volume'
    """
    first_list = first_room_dims[:ndim]
    second_list = second_room_dims[:ndim]

    return larger_multidim_room(first_name, first_list, second_name, second_list)

# Question 7
def larger_room_subspace_unbounded(
        ndim, first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room with
    larger subspace (calculated using only the first `ndim` dimensions), given
    their names (as strings), and their room dimensions (as a list of positive
    integers). If they happen to have the same room volume, return a string:
    "Same Volume".

    If the given dimensions `ndim` exceeds the number of dimensions of both
    rooms, you should apply the following procedure to each room:
        (1) Find the dimensions with maximum and minimum length
        (2) Take the square root of the product of the max and min found
        (3) Truncate this number to only keep the 3 digits after the decimal
        point
    Then, compare the truncated numbers of two rooms, and return the name of
    the tutor associated with a larger truncated number, or "Same Volume"
    if two numbers are equal.

    You may assume two rooms have the same number of dimensions.

    >>> larger_room_subspace_unbounded(10, "Yuxuan", [2, 8, 6, 8, 9],
    ...                                    "James", [4, 1, 18, 15, 6])
    'Same Volume'
    >>> larger_room_subspace_unbounded(10, "Aaron", [2, 4, 6, 7, 8],
    ...                                    "James", [4, 2, 8, 10, 3])
    'James'
    >>> larger_room_subspace_unbounded(10, "Jerry", [9, 7, 1, 2, 11],
    ...                                    "Colin", [8, 5, 8, 3, 12])
    'Jerry'
    >>> larger_room_subspace_unbounded(5, "Jerry", [9, 7, 1, 2, 11],
    ...                                   "Colin", [8, 5, 8, 3, 12])
    'Colin'
    >>> larger_room_subspace_unbounded(4, "Aaron", [2, 4, 6, 7, 8],
    ...                                   "James", [4, 2, 8, 10, 3])
    'James'
    >>> larger_room_subspace_unbounded(10, "Aaron", [2, 4, 6, 7, 8],
    ...                                    "Colin", [8, 5, 8, 3, 12])
    'Same Volume'
    """
    if ndim <= len(first_room_dims):
        return larger_room_subspace(
            ndim, first_name, first_room_dims, second_name, second_room_dims)
    elif ndim > len(first_room_dims):
        first_room_square_root_product = (max(first_room_dims) * min(first_room_dims)) ** .5
        second_room_square_root_product = (max(second_room_dims) * min(second_room_dims))**.5
        new_first_room_dims = round((first_room_square_root_product -
                                     int(first_room_square_root_product)), 3)
        new_second_room_dims = round((second_room_square_root_product -
                                      int(second_room_square_root_product)), 3)
        if new_first_room_dims > new_second_room_dims:
            return first_name
        elif new_first_room_dims < new_second_room_dims:
            return second_name
        else:
            return 'Same Volume'

# Question 8
def odd_even_list(names):
    """
    A function that returns a list, where each name in the names list is
    replaced with the string "Even" if the name has even length, or "Odd"
    otherwise. If the names list is empty, return a list with the string
    "Empty list was given" in it.

    >>> odd_even_list(["Marina", "Elvy", "James", "Sharmi"])
    ['Even', 'Even', 'Odd', 'Even']
    >>> odd_even_list(["Yuxuan", "Simon", "Sean"])
    ['Even', 'Odd', 'Even']
    >>> odd_even_list([])
    ['Empty list was given']
    >>> odd_even_list(["P", "Jack"])
    ['Odd', 'Even']
    >>> odd_even_list(["Lauv", "Mary", "Josh"])
    ['Even', 'Even', 'Even']
    >>> odd_even_list(["James"])
    ['Odd']
    """
    result = []
    if names == []:
        result.append('Empty list was given')
    else:
        for characters in names:
            if len(characters) % 2 != 0:
                result.append('Odd')
            else:
                result.append('Even')
    return result

# Question 9
def is_james_more_than_aaron(names):
    """
    A function that returns whether the name 'James' occurs more often than
    the name 'Aaron' in the input list of names. Return True if the above
    statement is true.

    >>> is_james_more_than_aaron(["James", "Aaron", "James"])
    True
    >>> is_james_more_than_aaron(["Aaron", "Aaron"])
    False
    >>> is_james_more_than_aaron(["Aaron", "Marina", "Yuxuan", "James"])
    False
    >>> is_james_more_than_aaron(["Aaron", "Aaron", "James", "James"])
    False
    >>> is_james_more_than_aaron(["James", "James"])
    True
    >>> is_james_more_than_aaron([2, 1, "James", "Aaron", "Aaron"])
    False
    """
    if names.count("James") > names.count("Aaron"):
        return True
    else:
        return False

# Question 10
def string_sum(lst):
    """
    A function that calculates the sum of all integers in the input list. All
    integers in the input list are given in string format, and the returned
    sum should also be a string.

    >>> string_sum(["1", "2", "3"])
    '6'
    >>> string_sum(["111", "205", "377"])
    '693'
    >>> string_sum(["777", "-999"])
    '-222'
    >>> string_sum(["100","-40", "-60"])
    '0'
    >>> string_sum([])
    '0'
    >>> string_sum(["0", "2", "9"])
    '11'
    """
    if lst == []:
        return '0'
    else:
        lst = [int(i) for i in lst]
        return str(sum(lst))
