"""
DSC 20 Homework 05
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function.
    Do not add new doctests for this function.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # 1: Constant
    # 2: Linear < Quadratic
    # 3: n**2 > n, so compare using n**2
    # 4: sqrt(n) == n**.5 < n
    # 5: 2n < n log n, so compare using n log n
    # 6: 2**n > n log n, so compare using 2**n
    # 7: fraction: n**7/n**4 = n**3 --> n**4 > n**3
    # 8: 2**n < 3**n; False
    # 9: arithmetic = O(n^2) from lecture
    # 10: geometric = exponential; exponential > linear
    ans = [False, False, True, False, True, False, False, False, False, False]
    return ans

# Question 2
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function.
    Do not add new doctests for this function.

    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 7 for ans in answers])
    True
    """
    #1: Linear, O(n), bcus 2n iteration / 2 step size --> O(n)
    #2: Quadratic, O(n^2), bcus nested for loop, for a list of n items,
    # we will have to perform n operations for every item in the list!
    # This means in total, we will perform n times n assignments, or n².
    #3: Constant, bcus looping through (0, 200)
    #4: Logarithmic O(logn), bcus start is doubled?
    #5: Polynomial, O(n^3), bcus 1st loop is 2n, then n^3, then constant?
    #6: Constant, just printing...?
    #7: Linear, because the for loop iterates n times
    #8: Linearithmic, O(n log n) bcus loop through n and then i // 3 (log n)
    #9: Quadratic, O(n^2), 1st for loop: n, 2nd: constant, 3rd: n
    #10: Linear, O(n)
    return [3, 5, 1, 2, 6, 6, 7, 4, 5, 5]

# Question 3
def advanced_search(data, min_elem, max_elem, min_total, max_total):
    """
    This function takes in five parameters: a data dictionary, and four
    numeric value, later used as requirement bounds.
    It will return the keys of the data dictionary as a list of strings if the
    following requirements are satisfied:
        1. All numeric values in the list is greater or equal to min_elem.
        2. All numeric values in the list is smaller of equal to max_elem.
        3. The sum of the list is between min_total and max_total (inclusive).
    Otherwise, if all three of the requirements are not met, an empty list
    will be returned.
    >>> data = {"Marina": [10, 9.2, 11.4, 17.5, 13.8], \
        "Elvy": [3.2, 8.6, 9.1, 1.0, 2.3, 6.6], \
        "Yuxuan": [14.41, 12.21, 10.01, 13, 11.1], \
        "Simon": [84.82, 91.96, 31.32], \
        "Sean": [66.0112, 88.8888, 45.6789], \
        "Colin": [44.1214, 55.5663, 77], \
        "Jerry": [10, 20, 30, 80]}
    >>> advanced_search(data, 10, 20, 0, 300)
    ['Yuxuan']
    >>> advanced_search(data, 40, 100, 150.5, 279.9)
    ['Sean', 'Colin']
    >>> advanced_search(data, 10, 80, 130, 150)
    ['Jerry']
    >>> data2 = {'Joe': [9, 45, 55, 90, 100], \
        'Bayes': [62.9, 90, 88.5, 10], \
        'Jack': [99.9, 90.3, 98.2, 97.5]}
    >>> advanced_search(data2, 10, 100, 200, 500)
    ['Bayes', 'Jack']
    >>> advanced_search(data2, 5, 100, 100, 290)
    ['Bayes']
    >>> advanced_search(data2, 200, 300, 400, 900)
    []
    """
    # lambda function checks if the values to the corresponding keys satisfy
    # the requirements
    # then filter according to conditions
    return list(filter(lambda key: min(data.get(key)) >= min_elem and \
                       max(data.get(key)) <= max_elem and \
                       sum(data.get(key)) >= min_total and \
                       sum(data.get(key)) <= max_total, data))

# Question 4
def best_curve_function(scores, funcs):
    """
    This function checks if a curve function(in list of functions, funcs)
    meets the requirements to be qualified, which are:
        1. Must be a function
        2. The function must not decrease any numeric values in scores list
        3. The function must also not add greater than five points to a score
    If the function is qualified(all requirements are met), the best curve
    function will be returned, which is the one that improves the scores the
    most.
    >>> best1 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 4.55, lambda score: score * 1.05, 105.0])
    >>> best1(100.0)
    104.55
    >>> best2 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 100, lambda score: score * 0.95, 103.5])
    >>> best2(95.5)
    95.5
    >>> best3 = best_curve_function([80.0, 90.0, 100.0], \
        [100.0, 103.5, False])
    >>> best3(91.0)
    91.0
    >>> best4 = best_curve_function([10.0, 60.7, 77.7], \
        [lambda score: score + 10.0])
    >>> best4(96.0)
    96.0
    >>> best5 = best_curve_function([45, 98, 90, 88.8], \
    [lambda score: score * .5 + 12])
    Traceback (most recent call last):
    AssertionError
    >>> best6 = best_curve_function([60.9, 88.9, 45.1], \
    [lambda score: score + 2.5, lambda score: score * 2.5])
    >>> best6(80.6)
    83.1
    """
    lower_bound = 0
    upper_bound = 100
    # check if scores is a list
    assert isinstance(scores, list)
    # check that none of the list of scores are empty
    assert len(scores) > 0
    # check if the elements of scores are floats
    assert all(isinstance(score, float) for score in scores)
    # check if the elements are between 0 and 100
    assert ((lower_bound <= score <= upper_bound) for score in scores)

    def check_scores(func):
        """
        A function that takes in a function, func, and checks if it passes
        the checks to be a qualified curve function.
        """
        five_pts = 5
        decrease_check = all(map(lambda score: func(score) - score >= 0,
                                 scores))
        five_pt_check = all(map(lambda score: func(score) - score <=
                                five_pts, scores))
        return bool(decrease_check and five_pt_check)

    # functions that satisfy requirements & are functions(callable)
    is_function = list(filter(lambda x: callable(x), funcs))
    qualified_list = list(filter(check_scores, is_function))

    # the argument itself is returned if all curve function are disqualified
    if not qualified_list:
        return lambda x: x

    # find the function with the greatest sum out of all of the qualified
    # functions after inputting the raw scores to them
    total_improv_list = []
    for func in qualified_list:
        curved_scores = list(map(func, scores))
        total_improv = (sum(curved_scores))
        total_improv_list.append(total_improv)
    greatest_improv = max(total_improv_list)
    greatest_index = total_improv_list.index(greatest_improv)
    best_func = qualified_list[greatest_index]
    return best_func

# Question 5 (Extra Credit)
def unique_data_generator(path):
    """
    This function takes in a text file, path, where each line contains items
    separated by values. It will process the lines to a tuple, where the first
    item is the "key" and the others are values, wrapped in their own tuple.

    >>> gen1 = unique_data_generator("infiles/data1.txt")
    >>> [next(gen1, None) for _ in range(3)]
    [('key1', ('val1', 'val2', 'val3')), ('key2', ('val1', 'val2')), \
('key3', ('val1', 'val2', 'val3', 'val4'))]
    >>> [next(gen1, None) for _ in range(5)]
    [('key4', ('val4', 'val5', 'val6')), \
('key5', ('val3', 'val4', 'val5', 'val6', 'val7')), None, None, None]
    >>> gen2 = unique_data_generator("infiles/data2.txt")
    >>> [next(gen2, None) for _ in range(5)]
    [('Colin', ('10-08-2020', '120')), ('James', ('10-08-2020', '100')), \
('Simon', ('10-09-2020', '115')), ('Jerry', ('10-09-2020', '120')), \
('Sean', ('10-10-2020', '150'))]
    """
    key_set = set()
    with open(path, 'r') as file:
        splitted = [tuple(line.split(',')) for line in file.readlines()]
        for tuple in splitted:
            key = tuple[0]
            values = tuple[1:]
            if key not in key_set:
                key_set.add(key)
                yield (key, values)
