# DSC 20 Lab 00
# Name: Tonia Le
# PID:  A15662706

def name_sum(firstName, lastName):
    """
    Write a Python program to sum up the lengths of two given names.
    However, if the sum is strictly greater than 15, return only the
    length of the firstName. If the sum is less than 10, return my
    name as a string: "Marina".

    >>> name_sum("Marina", "Langlois")
    14
    >>> name_sum("Elvy", "Chen")
    'Marina'
    >>> name_sum("Kiefer", "Sutherland")
    6
    """
    if len(firstName) + len(lastName) > 15:
        return len(firstName)
    if  len(firstName) + len(lastName) < 10:
        return ('Marina')
    else:
        return len(firstName) + len(lastName)
    return
