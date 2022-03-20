"""
DSC 20 Lab 06
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def recursive_odd_sum(upper):
    """
    Return the sum of odd integers from 1 to `upper` (inclusive) by
    only using recursion. You may assume that `upper` is an integer >= 1.

    >>> recursive_odd_sum(5)
    9
    >>> recursive_odd_sum(1)
    1
    >>> recursive_odd_sum(10)
    25
    """
    # base case
    if upper == 0:
        return 0
    if upper % 2 != 0:
        return upper + recursive_odd_sum(upper - 1) #add to upper to sum ?
    else:
        return recursive_odd_sum(upper - 1) #reducing problem

# Question 2
def remove_vowels_recursive(string):
    """
    Recursively remove uppercase and lowercase vowels (a, e, i, o, u)
    from the input `string`.

    >>> remove_vowels_recursive('input')
    'npt'
    >>> remove_vowels_recursive('HELLO HELLO')
    'HLL HLL'
    >>> remove_vowels_recursive('AeI oU')
    ' '
    """
    vowels = 'aeiouAEIOU'
    if len(string) == 0:
        return string
    # check if the first character is a vowel
    elif string[0] in vowels:
        return remove_vowels_recursive(string[1:])
    return string[0] + remove_vowels_recursive(string[1:])

# Question 3
def difference_of_counts(string, target0, target1):
    """
    Given a `string` and two target characters `target0` and `target1`,
    return the difference between the count of `target0` and the count of
    `target1` in the `string`.

    >>> difference_of_counts("ABCcccCBA", "A", "c")
    -1
    >>> difference_of_counts("ABCcccCBA", "A", "B")
    0
    >>> difference_of_counts("ABCcccCBA", "A", "a")
    2
    """
    if string == '':
        return 0
    if target0 == target1:
        return 0
    if target0 in string[0]:
        return 1 + difference_of_counts(string[1:], target0, target1)
    if target1 in string[0]:
        return difference_of_counts(string[1:], target0, target1) - 1
    else:
        return difference_of_counts(string[1:], target0, target1)

# Question 4
def parity_mismatch(lst):
    """
    Given a list of non-negative integers (`lst`), recursively check if
    all elements at even indices are odd integers and all elements at
    odd indices are even integers. Return True if `lst` satisfies this
    requirement or `lst` is empty, otherwise return False.

    >>> parity_mismatch([])
    True
    >>> parity_mismatch([1, 0, 3, 2, 5, 4])
    True
    >>> parity_mismatch([1, 0, 3, 2, 5, 5])
    False
    """
    # empty list case
    if len(lst) == 0:
        return True
    # length of 1 = even indice
    if len(lst) == 1:
        return lst[0] % 2 != 0
    else:
        return lst[0] % 2 != 0 and lst[1] % 2 == 0 and parity_mismatch(lst[2:])

# Question 5
def integer_with_comma(num):
    """
    A recursive function that takes an integer `num`, and return
    a string form of this integer, where a comma is added for every 3 digits.

    >>> integer_with_comma(100500)
    '100,500'
    >>> integer_with_comma(13544312)
    '13,544,312'
    >>> integer_with_comma(-9999)
    '-9,999'
    """
    # converting to string
    if not isinstance(num, str):
        num = str(num)
    # returns itself (no comma) if less than 3 digits
    if len(num) < 4:
        return num
    else:
        # all but last three digits + comma + last three digits
        return integer_with_comma(num[:-3]) + ',' + num[-3:]

# Question 6
def range_join(bound1, bound2, sep):
    """
    A recursive function that takes two integers `bound1` and `bound2`,
    and return a string with all integers between `bound1` and `bound2`
    (both inclusive) separated by a specified string separator `sep`.

    >>> range_join(10, 10, 'marina')
    '10'
    >>> range_join(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> range_join(8, 1, '->')
    '8->7->6->5->4->3->2->1'
    """
    if bound1 == bound2:
        return str(bound1)
    if bound1 < bound2:
        return str(bound1) + sep + range_join(bound1 + 1, bound2, sep)
    if bound1 > bound2:
        return str(bound1) + sep + range_join(bound1 - 1 , bound2, sep)
