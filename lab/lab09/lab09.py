"""
DSC 20 Lab 09
Name: Tonia Le
PID:  A15662706
"""


# Question 1
def polynomial_doctests():
    """
    >>> p1 = Polynomial({0: 8, 1: 2, 3: 4})
    >>> p2 = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})
    >>> p3 = Polynomial({0: 8, 1: 2, 3: 4, 2: 0})
    >>> print(p1)
    8 + 2 x + 4 x^(3)
    >>> p2
    {0: 8, 1: 2, 2: 8, 4: 4}
    >>> print(p2)
    8 + 2 x + 8 x^(2) + 4 x^(4)
    >>> print(p3)
    8 + 2 x + 4 x^(3)
    >>> print(p1 + p2)
    16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)
    >>> print(p1 * p2)
    64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)
    >>> p1 == p1
    True
    >>> p1 == p2
    False
    >>> p1 == p3
    True
    """
    return


class Polynomial:
    """
    A class that abstracts polynomial expressions.
    """


    def __init__(self, dictionary):
        """
        Constructor of Polynomial.

        Parameters:
            dictionary (dict): key(non-negative integer powers),
            values(integer coefficient)represents the terms of
            polynomial

        """
        self.dictionary = dict(sorted(dictionary.items()))
    # repr for actual input
    def __repr__(self):
        # str(dict(sorted(self.dictionary.items())))
        # }
        return str(self.dictionary)

    # str for things that need to be printed(mathematical form)
    def __str__(self):
        term = 'x'
        # empty string/ list
        result = ""
        # for loop to go one by one in dictionary
        for power in self.dictionary:
        # look at key value pairs (self.dictionary[power] == coefficient)
            if self.dictionary[power] == 0:
                continue
            elif power == 0:
                result += str(self.dictionary[power])
            elif power == 1:
                result += str(self.dictionary[power]) + ' ' + term
            elif power > 1:
                result += str(self.dictionary[power]) + ' ' + term + '^' + \
                '(' + str(power) + ')'
            result += ' + '
        return result[:-3]

    def __eq__(self, other_poly):


        for key1, val1 in self.dictionary.items():
            if key1 in other_poly.dictionary and val1 != other_poly.dictionary[key1]:
                return False
            if key1 not in other_poly.dictionary and val1 != 0:
                return False

        for key2, val2 in other_poly.dictionary.items():
            if key2 in self.dictionary and val2 != self.dictionary[key2]:
                return False
            if key2 not in self.dictionary and val2 != 0:
                return False
        return True

    def __add__(self, other_poly): # other is another polynoimal object
        sum_dict = {}
        for key1, val1 in self.dictionary.items():
            # see if key is present in sum_dict, if its not : set the value of that key to self.dictionary[key],, otherwise add the value to that key
            if key1 in sum_dict:
                sum_dict[key1] += val1
            else:
                sum_dict[key1] = val1

        for key2, val2 in other_poly.dictionary.items():
            if key2 in sum_dict:
                sum_dict[key2] += val2
            else:
                sum_dict[key2] = val2

        return Polynomial(sum_dict)

    def __mul__(self, other_poly):
        mult_dict = {}
        for key1, val1 in self.dictionary.items():
            for key2, val2 in other_poly.dictionary.items():
                if (key1 + key2) in mult_dict:
                    mult_dict[key1 + key2] += val1 * val2
                else:
                    mult_dict[key1 + key2] = val1 * val2

        return Polynomial(mult_dict)


# Question 2.1
def fix_1(lst1, lst2):
    """
    Divide all of the elements in `lst1` by each element in `lst2`
    and return the values in a list.

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div)
            except:
                pass
    return out


# Question 2.2
def fix_2(*filepaths):
    """
    Open all of the files in `filepaths` and PRINT a string for each file
    that indicates if this file can be opened or not.

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found

    >>> fix_2('docs.txt')
    docs.txt not found
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r")
            print ('{} opened'.format(filepath))
            cur_file.close()
        except:
            print ('{} not found'.format(filepath))


# Question 2.3
def fix_3(lst):
    """
    For each element in `lst`, add it with its following element
    in the list. Returns all of the summed values in a list.

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []

    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]

    >>> fix_3([])
    []
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1])  # add try-except block
        except IndexError as err:
            print(type(err))
        except TypeError as err:
            print(type(err))

    return sum_of_pairs
