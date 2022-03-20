"""
DSC 20 Lab 10
Name: Tonia Le
PID:  A15662706
"""


# Question 1.1
class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """

        self.items = []
        self.num_items = 0

    def size(self):
        """ Get the number of items stored. """

        return self.num_items

    def is_empty(self):
        """ Check whether the collection is empty. """
        if self.num_items == 0:
            return True
        return False

    def clear(self):
        """ Remove all items in the collection. """

        self.items.clear()
        self.num_items = 0


# Question 1.2
class Stack(Collection):
    """
    Stack class.

    >>> stk = Stack()
    >>> stk.size()
    0
    >>> stk.is_empty()
    True
    >>> str(stk)
    '(bottom) (top)'
    >>> stk.push(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> stk.push('LAB 10')
    >>> stk.size()
    1
    >>> stk.is_empty()
    False
    >>> stk.push('DSC')
    >>> stk.push(20)
    >>> stk.size()
    3
    >>> str(stk)
    '(bottom) LAB 10 -- DSC -- 20 (top)'
    >>> stk.pop()
    20
    >>> stk.pop()
    'DSC'
    >>> stk.peek()
    'LAB 10'
    >>> stk.size()
    1
    >>> stk.clear()
    >>> stk.pop()
    >>> stk.peek()
    """

    def push(self, item):
        """ Push `item` to the stack. """
        if item is None:
            raise ValueError("item cannot be None")
        else:
            self.items.append(item)
            self.num_items += 1

    def pop(self):
        """ Pop the top item from the stack. """
        if self.items == []:
            return None
        else:
            removed = self.items.pop(-1)
            self.num_items -= 1
            return removed

    def peek(self):
        """ Peek the top item. """
        if self.items == []:
            return None
        else:
            return self.items[-1]

    def __str__(self):
        """ Return the string representation of the stack. """
        result = ""
        if self.num_items == 0:
            result = "(bottom) (top)"
        elif self.num_items == 1:
            result = "(bottom) " + str(self.items[0]) + " (top)"
        elif self.num_items > 1:
            result = "(bottom) " + (' -- '.join([str(elements) for elements \
                                    in self.items]))+ " (top)"
        return result

# Question 1.3
class Queue(Collection):
    """
    Queue class.

    >>> que = Queue()
    >>> que.size()
    0
    >>> que.is_empty()
    True
    >>> str(que)
    '(front) (rear)'
    >>> que.enqueue(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> que.enqueue('LAB 10')
    >>> que.size()
    1
    >>> que.is_empty()
    False
    >>> que.enqueue('DSC')
    >>> que.enqueue(20)
    >>> que.size()
    3
    >>> str(que)
    '(front) LAB 10 -- DSC -- 20 (rear)'
    >>> que.dequeue()
    'LAB 10'
    >>> que.dequeue()
    'DSC'
    >>> que.peek()
    20
    >>> que.size()
    1
    >>> que.clear()
    >>> que.dequeue()
    >>> que.peek()
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        if item is None:
            raise ValueError('item cannot be None')
        self.items.append(item)
        self.num_items += 1

    def dequeue(self):
        """ Dequeue the front item from the queue. """
        if self.items == []:
            return None
        else:
            removed_item = self.items.pop(0)
            self.num_items -= 1
            return removed_item

    def peek(self):
        """ Peek the front item. """
        if self.items == []:
            return None
        else:
            return self.items[0]

    def __str__(self):
        """ Return the string representation of the queue. """
        result = ""
        if self.num_items == 0:
            result = "(front) (rear)"
        elif self.num_items == 1:
            result = "(front) " + str(self.items[0]) + " (rear)"
        elif self.num_items > 1:
            result = "(front) " + (' -- '.join([str(elements) for elements \
                                   in self.items]))+ " (rear)"
        return result


# Question 2
def parentheses_checker(expression):
    """
    A function that checks whether all parentheses `{}, [], ()`
    are balanced in the given `expression`.

    >>> parentheses_checker("(((]})")
    False
    >>> parentheses_checker("(")
    False
    >>> parentheses_checker("(){}[]]")
    False
    >>> parentheses_checker("(   x   )")
    True
    >>> parentheses_checker("a()b{}c[]d")
    True
    >>> parentheses_checker("")
    True
    """
     # The checker will look for three kinds of parentheses: `{}`, `[]` and `()`, and ignore all other characters. This function will take a string expression, and return True if all parentheses pairs are balanced.

    # open = ["{", "[", "("]
    # closed = ["}", "]", ")"]
    # stk = Stack()
    # for char in expression:
    #     if char in open:
    #         stk.push()
    #
    # for char in expression:
    #     last_element = stk.peek(char)
    #     if last_element in closed:
    #         continue
    #         next_element = stk.peek(last_element)
    #         if next_element not in




# Question 3
def inf_skip_increasing(iterable):
    """
    A generator that takes in an `iterable` object and infinitely yields its
    items. This generator skips items by an increasing amount after each
    yield. If this generator reached the end of the `iterable`, proceed from
    the front.

    >>> gen = inf_skip_increasing(range(10))
    >>> next(gen)
    0
    >>> next(gen)
    1
    >>> [next(gen) for _ in range(10)]
    [3, 6, 0, 5, 1, 8, 6, 5, 5, 6]
    """
    # YOUR CODE GOES HERE #
    return ...
