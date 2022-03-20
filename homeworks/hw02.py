"""
DSC 20 Homework 02
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def convert_to_tuples(courses, instructors):
    """
    This function takes a list of courses and corresponding instructors and
    returns it as a list of tuples. If there are more courses than instructors
    ,the instructor for those courses will be a "staff". An empty list will be
    returned if not provided a course.

    Assumptions:
        len(courses) >= len(instructors).

    >>> convert_to_tuples(['DSC10', 'DSC20', 'DSC30', 'DSC40B',
    ... 'DSC80', 'DSC180A'], ['Justin Eldridge', 'Marina Langlois',
    ... 'Marina Langlois', 'Justin Eldridge', 'Marina Langlois',
    ... 'Aaron Fraenkel'])
    [('DSC10', 'Justin Eldridge'), ('DSC20', 'Marina Langlois'), \
('DSC30', 'Marina Langlois'), ('DSC40B', 'Justin Eldridge'), \
('DSC80', 'Marina Langlois'), ('DSC180A', 'Aaron Fraenkel')]
    >>> convert_to_tuples(['DSC102', 'DSC106', 'DSC100'],
    ... ['Arun Kumar', 'Thomas Powell'])
    [('DSC102', 'Arun Kumar'), ('DSC106', 'Thomas Powell'), \
('DSC100', 'STAFF')]
    >>> convert_to_tuples(['DSC90', 'DSC190'], [])
    [('DSC90', 'STAFF'), ('DSC190', 'STAFF')]
    >>> convert_to_tuples(['DSC10', 'DSC20'], ['Thomas Powell'])
    [('DSC10', 'Thomas Powell'), ('DSC20', 'STAFF')]
    >>> convert_to_tuples(['DSC10','DSC20', 'DSC30'], ['Justin Eldridge',
    ... 'Marina Langlois', 'Marina Langlois'])
    [('DSC10', 'Justin Eldridge'), ('DSC20', 'Marina Langlois'), \
('DSC30', 'Marina Langlois')]
    >>> convert_to_tuples([],[])
    []
    """
    # Case 1: pair elements from courses and instructors when the number of
    # elements are equal, so checking for equal lengths
    if len(courses) == len(instructors):
        return list(zip(courses, instructors))
    # Case 2: if more courses than instructors, assign 'STAFF' to those courses
    elif len(courses) > len(instructors):
        difference = len(courses) - len(instructors)
        for num in range(difference):
            instructors = instructors + ['STAFF']
        return list(zip(courses, instructors))

# Question 2
def convert_to_dict(tuples):
    """
    This function takes a list of tuples of coures and corresponding
    instructors and returns it as a dictionary, where instructor names are the
    keys and coures are values. If an instructor is in multiple tuples,
    meaning they teach more than one course, those courses will be added to
    the values corresponding to that instructor. The order in which instructors
    appear in the tuple list shall remain the same.

    Assumptions:
        there aren't duplicate instructor names or course codes.

    >>> convert_to_dict([('DSC10', 'Justin Eldridge'),
    ... ('DSC20', 'Marina Langlois'), ('DSC30', 'Marina Langlois'),
    ... ('DSC40B', 'Justin Eldridge'), ('DSC80', 'Marina Langlois'),
    ... ('DSC180A', 'Aaron Fraenkel')])
    {'Justin Eldridge': ['DSC10', 'DSC40B'], \
'Marina Langlois': ['DSC20', 'DSC30', 'DSC80'], 'Aaron Fraenkel': ['DSC180A']}
    >>> convert_to_dict([('DSC102', 'Arun Kumar'),
    ... ('DSC106', 'Thomas Powell'), ('DSC100', 'STAFF')])
    {'Arun Kumar': ['DSC102'], 'Thomas Powell': ['DSC106'], \
'STAFF': ['DSC100']}
    >>> convert_to_dict([('DSC90', 'STAFF'), ('DSC190', 'STAFF')])
    {'STAFF': ['DSC90', 'DSC190']}
    >>> convert_to_dict([('DSC10', 'Justin Eldridge'), \
('DSC40B', 'Justin Eldridge')])
    {'Justin Eldridge': ['DSC10', 'DSC40B']}
    >>> convert_to_dict([('DSC10', 'Justin Eldridge'),('DSC180A', 'STAFF')])
    {'Justin Eldridge': ['DSC10'], 'STAFF': ['DSC180A']}
    >>> convert_to_dict([('DSC10', 'STAFF'), ('DSC20', 'Marina Langlois')])
    {'STAFF': ['DSC10'], 'Marina Langlois': ['DSC20']}
    """
    dictionary = {}
    for value, key in tuples:
        #Case 1: if instructor name is already in the dictionary, append other
        # courses corresponding to their names
        if key in dictionary:
            dictionary[key].append(value)
        #Case 2: otherwise, instructor name and the corresponding course will
        # be added to the dictionary as is
        else:
            dictionary[key] = [value]
    return dictionary

# Question 3
def even_old_ops(string):
    """
    Depending on the indices (odd or even), this function will perform
    different operations on the characters and return it as a string. If at
    even indices, the characters will be reversed. If at odd indices, the
    function will change an uppercase letter to lowercase and vice versa.
    Otherwise, if at an odd index and the character is not a letter, it will
    be replaced with a dot, (“.”).  An empty string will be returned if the
    input is empty.

    >>> even_old_ops("Rand0mStr1NG")
    'NArDSM0Tn.Rg'
    >>> even_old_ops("d_s_c__20")
    '0._.c.s.d'
    >>> even_old_ops("0U1U2l3l4?5?6")
    '6u5u4L3L2.1.0'
    >>> even_old_ops('<3frufts<3')
    '<.tRuFfS<.'
    >>> even_old_ops('3m pl3h')
    'hMlP .3'
    >>> (even_old_ops('__w__  '))
    ' ._.w._'
    """
    new_string = ''
    divisor = 2
    # skips a character in a string and reveres it:
    reversing = string[::2][::-1]
    # checking for odd or even positions in our string
    for index, character in enumerate(string):
        # Case 1: if in an even position, reverse them by the index // divisor
        # because divisor = 2, so we're reversing the character at even indices
        if index % 2 == 0:
            new_string = new_string + reversing[index//divisor]
        # Case 2: if a character is at an odd indice:
        # we change uppercase to lowercase and vice versa
        # every non-letter will be replaced with a "."
        elif index % 2 != 0: # odd --> lower & upper
            if character.isupper() is True:
                new_string = new_string + character.lower()
            elif character.islower() is True:
                new_string = new_string + character.upper()
            else:
                new_string = new_string + character.replace(character, '.')
    return new_string

# Question 4
def context_words(document, target_word, window_size):
    """
    This function checks for a target word in a given document(string). If the
    target word is found in the string, the context(surrounding) words ahead
    and behind it will be returned. The amount of context words returned is
    based off of the window size. A list of tuples containing the target word
    and context words will be returned.

    Assumptions:
        `document` is always a string where words are seperated by spaces.
        `document` string will only have uppercase or lowercase letters,
            hyphens (only in compound words), and spaces.
        `target_word` will always exist in the `document`.

    >>> test_doc = "fifty-two UNITS from lower-division courses " + \
    "AND sixty UNITS from upper-division courses"
    >>> context_words(test_doc, "lower-division", 2)
    [('lower-division', 'units'), ('lower-division', 'from'), \
('lower-division', 'courses'), ('lower-division', 'and')]
    >>> context_words(test_doc, "upper-division", 2)
    [('upper-division', 'units'), ('upper-division', 'from'), \
('upper-division', 'courses')]
    >>> context_words(test_doc, "units", 1)
    [('units', 'fifty-two'), ('units', 'from'), ('units', 'sixty'), \
('units', 'from')]
    >>> own_test_doc = "there is no such thing as TOO MUCH cheese in mac " + \
    "AND CHEESE"
    >>> context_words(own_test_doc, "as", 3)
    [('as', 'no'), ('as', 'such'), ('as', 'thing'), ('as', 'too'), \
('as', 'much'), ('as', 'cheese')]
    >>> context_words(own_test_doc, "is", 2)
    [('is', 'there'), ('is', 'no'), ('is', 'such')]
    >>> context_words(own_test_doc, 'cheese', 2)
    [('cheese', 'too'), ('cheese', 'much'), ('cheese', 'in'), \
('cheese', 'mac'), ('cheese', 'mac'), ('cheese', 'and')]
    """
    new_list = []
    # split entire string & change all words to lowercase
    lowercase_split_document = document.lower().split()
    # convert target word to lower
    target_word = target_word.lower()
    # iterate over the numbers up to the length of doc
    for index in range(len(lowercase_split_document)):
        # Looping through the list to check for the target word
        if lowercase_split_document[index] == target_word:
            upper_bound = index + window_size
            lower_bound = index - window_size
            if lower_bound < 0:
                lower_bound = 0
            elif upper_bound > len(lowercase_split_document):
                upper_bound = len(lowercase_split_document)
            # loop through the list(document) check if target word is found
            for word in lowercase_split_document[lower_bound:upper_bound +1]:
                # append created tuple to empty list
                if word != target_word:
                    new_list.append((target_word, word))
    return new_list

# Question 5
def flip_matrix(matrix_path):
    """
    This function takes in a matrix written in a file and flips in both
    horizontally and vertically. The flipped matrix will be written to a new
    file.

    Assumptions:
        The matrix will be represented as lines of space-seperated integers.
        The matrix will be N x M, where N and M >= 1.

    >>> flip_matrix("testfiles/matrix1.txt")
    >>> with open("testfiles/matrix1_flipped.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    1 0 1 0 0
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
    0 0 1 0 1
    >>> flip_matrix("testfiles/matrix2.txt")
    >>> with open("testfiles/matrix2_flipped.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    7 6 5 4 3
    6 5 4 3 2
    5 4 3 2 1
    >>> flip_matrix("testfiles/matrix3.txt")
    >>> with open("testfiles/matrix3_flipped.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    81 10051 99
    17 31 42
    1 770 90
    2 1 88
    96 51 52
    90 12 105
    >>> flip_matrix("testfiles/matrix4.txt")
    >>> with open("testfiles/matrix4_flipped.txt", "r") as outfile4:
    ...     print(outfile4.read().strip())
    1 3 2
    3 2 1
    2 1 2
    >>> flip_matrix("testfiles/matrix5.txt")
    >>> with open("testfiles/matrix5_flipped.txt", "r") as outfile5:
    ...     print(outfile5.read().strip())
    5 1 7 8
    7 1 9 0
    2 1 1 0
    >>> flip_matrix("testfiles/matrix6.txt")
    >>> with open("testfiles/matrix6_flipped.txt", "r") as outfile6:
    ...     print(outfile6.read().strip())
    0 96 66 65
    20 24 54 55
    """
    # read file by lines
    with open(matrix_path) as file:
        lines_in_file = file.readlines()
        # looping through each line
        for num in range(len(lines_in_file)):
            # remove trailing "\n"
            lines_in_file[num] = lines_in_file[num].rstrip("\n")
            # split by space
            line_list = lines_in_file[num].split(" ")
            # flip numbers in the matrix
            line_list.reverse()
            # Join the list of strings into a string based on a space & add \n
            # reverse again
            lines_in_file[num] = " ".join(line_list)
            lines_in_file[num] = lines_in_file[num] + "\n"
        lines_in_file.reverse()
    # assigning to a new file and path name
    new_file_name = matrix_path.lstrip("testfiles/").rstrip(".txt")
    new_path = "testfiles/" + new_file_name + "_flipped.txt"
    outfile = open(new_path, "w")
    outfile.writelines(lines_in_file)
    outfile.close()
    return None

# Question 6.1
def parse_timelog(timelog_path):
    """
    Taking in an input of time logs of worked minutes by tutors as a text
    file, this function ultimately returns a dictionary of these entries.
    After splitting the entries by line, the names of the tutors will be the
    keys in the dictionary and a tuple of dates and minutes will be the values.

    Assumptions:
        The log will be sorted in chronological order.
        Each line of the time log will have name (str), date (str,
            MM-DD-YYYY), and minutes seperated by comma (",").
            For example: "Marina,09-30-2020,300".
        Each person will have only one entry per day.

    >>> parse_timelog("testfiles/timelog1.txt")
    {'Marina': [('09-30-2020', 300), ('10-01-2020', 300)], \
'Elvy': [('09-30-2020', 120), ('10-01-2020', 215)], \
'Yuxuan': [('09-30-2020', 185), ('10-01-2020', 90)]}
    >>> parse_timelog("testfiles/timelog2.txt")
    {'Colin': [('10-08-2020', 120), ('10-09-2020', 10), ('10-10-2020', 90), \
('10-11-2020', 30)], 'James': [('10-08-2020', 100), ('10-09-2020', 85)], \
'Simon': [('10-09-2020', 115)], 'Jerry': [('10-09-2020', 120)], \
'Sean': [('10-10-2020', 150)]}
    >>> parse_timelog("testfiles/timelog3.txt")
    {'Elvy': [('10-02-2020', 120), ('10-03-2020', 60)], \
'Sean': [('10-03-2020', 60), ('10-08-2020', 120)]}
    >>> parse_timelog("testfiles/timelog4.txt")
    {'Jack': [('09-20-2020', 100)], 'Elvy': [('09-20-2020', 200)], \
'Marina': [('10-3-2020', 200), ('10-4-2020', 200)]}
    >>> parse_timelog("testfiles/timelog5.txt")
    {'Sean': [('10-14-2020', 125), ('9-30-2020', 130), ('10-2', 2020), \
('10-16-2020', 100)]}
    """
    third_element_index = 2
    dictionary = {}
    # split by lines
    with open(timelog_path) as file:
        splitted_string = file.read().splitlines()
    # split the lines by comma
    for line in splitted_string:
        current_line = line.split(",")
        # assigning elements in the line split by commas by name, date, & mins
        name = current_line[0]
        date = current_line[1]
        minutes = current_line[third_element_index]
        # need date and minutes to be dictionary value later
        tuples = (date, int(minutes))
        # check if name already exists,
        # if it does not: value of dictionary is tuples, otherwise append
        # values associated with the same name(key)
        if name not in dictionary:
            dictionary[name] = [tuples]
        else:
            dictionary[name].append(tuples)
    return dictionary

# Question 6.2
def extract_extreme_time(data, is_max):
    """
    This function takes the dictionary called by the parse_timelog function as
    the parameter, "data", and a boolean parameter, is_max. The entry with
    the most or least minutes worked for each name(key), depending on whether
    is_max is True or False, respectedly will be returned as a dictionary. If
    a name has multiple values(time logs) that are equivalent to one another,
    the entry with the earliest date will be returned.

    Assumptions:
        When any comparison results a tie, keep the entry with earlier date.

    >>> data1 = parse_timelog("testfiles/timelog1.txt")
    >>> extract_extreme_time(data1, True)
    {'Marina': ('09-30-2020', 300), 'Elvy': ('10-01-2020', 215), \
'Yuxuan': ('09-30-2020', 185)}
    >>> extract_extreme_time(data1, False)
    {'Marina': ('09-30-2020', 300), 'Elvy': ('09-30-2020', 120), \
'Yuxuan': ('10-01-2020', 90)}
    >>> data2 = parse_timelog("testfiles/timelog2.txt")
    >>> extract_extreme_time(data2, True)
    {'Colin': ('10-08-2020', 120), 'James': ('10-08-2020', 100), \
'Simon': ('10-09-2020', 115), 'Jerry': ('10-09-2020', 120), \
'Sean': ('10-10-2020', 150)}
    >>> extract_extreme_time(data2, False)
    {'Colin': ('10-09-2020', 10), 'James': ('10-09-2020', 85), \
'Simon': ('10-09-2020', 115), 'Jerry': ('10-09-2020', 120), \
'Sean': ('10-10-2020', 150)}
    >>> data3 = parse_timelog("testfiles/timelog3.txt")
    >>> extract_extreme_time(data3, True)
    {'Elvy': ('10-02-2020', 120), 'Sean': ('10-08-2020', 120)}
    >>> extract_extreme_time(data3, False)
    {'Elvy': ('10-03-2020', 60), 'Sean': ('10-03-2020', 60)}
    >>> data4 = parse_timelog("testfiles/timelog4.txt")
    >>> extract_extreme_time(data4, True)
    {'Jack': ('09-20-2020', 100), 'Elvy': ('09-20-2020', 200), \
'Marina': ('10-3-2020', 200)}
    >>> extract_extreme_time(data4, False)
    {'Jack': ('09-20-2020', 100), 'Elvy': ('09-20-2020', 200), \
'Marina': ('10-3-2020', 200)}
    """
    dictionary = {}
    # if is_max == True, find the max minutes worked
    if is_max is True:
        for name in data:
            # initializing max as zero
            max_minutes = 0
            max_date = 0
            # loop checking for extreme values from parse_timelog dictionary
            for values in data[name]:
                # checking for maximum (extreme)
                if values[1] > max_minutes:
                    max_minutes = values[1]
                    max_date = values[0]
                elif values[1] == max_minutes: 
                    max_date = min(max_date, values[0])
                else:
                    pass
            dictionary[name] = (max_date, max_minutes)
    # if is_max == False, find minimum minutes worked
    elif is_max is False:
        for name in data:
            #initializing minimum as a large number
            min_minutes = (float('inf'))
            min_date = 0
            # Loop to check for minimum value of minutes
            for values in data[name]:
                if values[1] < min_minutes:
                    min_minutes = values[1]
                    min_date = values[0]
                # Case when the entries of minutes are the same for a given key(name)
                elif values[1] == min_minutes:
                    min_date = min(min_date, values[0])
                else:
                    pass
            dictionary[name] = (min_date, min_minutes)
    return dictionary
