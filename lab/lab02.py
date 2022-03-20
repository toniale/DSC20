"""
DSC 20 Lab 02
Name: Tonia Le
PID:  A15662706
"""

# Question 1
def check_Blackjack(player1, player2):
    """
    Returns a list of results of the Blackjack game between player1 and
    player 2. For the i-th round, the i-th index of player1 list represents
    the sum of all cards of player1, and the i-th index of player2 list
    represents player2's card sum. The i-th index of the returned list should
    be the winner's card sum. If the card sum is closer to 21 but not going
    over it, that player wins. If both players' card sum go over 21 in a
    round, we put 0 for that round instead.

    Parameters:
        player1 (List[int]): card sums for player 1
        player2 (List[int]): card sums for player 2

    Returns:
        (List[int]): game results judged with the rule above

    Assumptions:
        player1 and player2 will always have the same length

    >>> check_Blackjack([19, 21, 22], [21, 19, 3])
    [21, 21, 3]
    >>> check_Blackjack([17, 21, 22, 29], [15, 19, 3, 4])
    [17, 21, 3, 4]
    >>> check_Blackjack([], [])
    []
    """
    new_list = []
    for i in range(len(player1)):
        cardsum1 = player1[i]
        cardsum2 = player2[i]
        if cardsum1 <= 21 and cardsum2 <= 21:
            new_list.append(max(cardsum1, cardsum2))
        elif cardsum1 > 21 and cardsum2 > 21:
            new_list.append(0)
        else:
            new_list.append(min(cardsum1, cardsum2))
    return new_list

# Question 2
def majority_element(nums):
    """
    Returns the majority element in the `nums` list. The majority element
    is the element that appears more than ⌊ n/2 ⌋ times, where n is the length
    of `nums` list.

    Parameters:
        nums (List[int]): the list of integers to apply this function

    Returns:
        (int) the majority element found

    Assumptions:
        `nums` list is non-empty
        A majority element always exists in `nums` list

    >>> majority_element([3,2,3])
    3
    >>> majority_element([2,2,1,1,1,2,2])
    2
    >>> majority_element([1,1,2,2,2])
    2
    """
    for element in nums:
        occurrences = nums.count(element)
        if occurrences > ((len(nums))/2):
            return element

# Question 3
def remove_vowels(string):
    """
    Removes vowels (a, e, i, o, u) from `string` and returns the resulted
    string. Capitalized vowel letters should also be removed.

    Parameters:
        string (str): the string to apply this function

    Returns:
        (str): the string with vowel letters removed

    >>> remove_vowels('Hello')
    'Hll'
    >>> remove_vowels('')
    ''
    >>> remove_vowels('Hi how are...you?')
    'H hw r...y?'
    """
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for characters in string:
        if characters in vowels:
            string = string.replace(characters, '')
    return string

# Question 4
def pig_latin(string):
    """
    Returns `string` translated into Pig Latin. Please read the write-up
    for specific rules of translating a string into Pig Latin.

    However, for whatever reason we are afraid of 8 letter words. If we
    encounter a 8 letter word, we will immediately stop translating and
    return what we have translated so far.

    Parameters:
        string (str): the string to translate

    Returns:
        (str): the translated string

    Assumptions:
        there will be no punctuation in `string`.
        all words will only be separated by one space.
        all words will have at least one vowel.

    >>> pig_latin('Hi how are you')
    'iHay owhay areyay ouyay'
    >>> pig_latin('Absolute')
    ''
    >>> pig_latin('When words begin with consonant clusters')
    'enWhay ordsway eginbay ithway onsonantcay'
    """
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    new_list = []
    list = string.split()
    for word in list:
        if len(word) == 8:
            break
        if word[0] in vowels:
             new_list.append(word + 'yay')
        else:
            first_vowel = -1
            for index, char in enumerate(word):
                if char in vowels:
                    first_vowel = index
                    break
            new_word = word[first_vowel:] + word[:first_vowel] + 'ay'
            new_list.append(new_word)
    return (' '.join(new_list))
