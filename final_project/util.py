"""
DSC 20 Final Project Utility File

Please copy and paste your Stack and Queue implementation from Lab 10.
"""


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


class Stack(Collection):
    """
    Stack class.
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

class Queue(Collection):
    """
    Queue class.
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
