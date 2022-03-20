"""
DSC 20 Homework 09
Name: Tonia Le
PID:  A15662706
"""


# Question 1
def check_inputs(input1, input2):
    """
    A function that checks if the parameters meet the following requirements:
        1) input1 is a list of numeric values
        2) input2 is a numeric value and contained in input1
    If all are met, the inputs are validated.

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'

    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type

    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric

    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type

    >>> check_inputs([0, 'first', 'second'], 5)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 1 is not numeric

    >>> check_inputs(('tup', 'le'), 'same')
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type

    >>> check_inputs([1, 4, 9, 3], 3)
    'Input validated'

    >>> check_inputs([1,2,3], True)
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    """
    # input1 is a list
    if not type(input1) is list:
        raise TypeError('input1 is not the correct type')
    # input1 needs numeric values
    for index, element in enumerate(input1):
        if not isinstance(element, (int, float)):
            raise TypeError('The element at index {} is not numeric' \
            .format(index))
    # input2 is numeric
    if ((type(input2) == int) or (type(input2) == float)) is False:
        raise TypeError('input2 is not the correct type')
    # input2 contained in input1
    if not input2 in input1:
        raise TypeError('input2 not in input1')
    return 'Input validated'

# Question 2
def load_file(filename):
    """
    A function that checks if the parameters meet the following requirements:
        1) filepath is a string type
        2) filepath should be a valid filepath (i.e. we can open the file)
        3) The file at filepath should not be empty
        If all are met, the number of words in the file is returned.


    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    >>> load_file('files/ten_words.txt')
    10

    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty

    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist

    >>> load_file('files/twelve.txt')
    12

    >>> load_file((tuple))
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    >>> load_file('files/hideandseek.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/hideandseek.txt does not exist

    >>> load_file(['i', 'am', 'a', 'JOKE'])
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    """
    if not type(filename) is str:
        raise TypeError('filename is not a string')
    try:
        file = open(filename, 'r')
        num_words = 0
        for line in file:
            words = line.split()
            num_words += len(words)
            return num_words
    except:
        raise FileNotFoundError('{} does not exist'.format(filename))
    else:
        if not file.readlines():
            raise ValueError('File is empty')
        file.close()

# Question 3
def q3_doctests():
    """
    Q3 doctests go here.

    >>> h = Nonmetal("H")
    >>> h
    Nonmetal("H")
    >>> print(h)
    Nonmetal name: H, atomic number: 8, period: 2, group: 2
    >>> h.get_mass()
    66

    >>> f = Metal("F")
    >>> f
    Metal("F")
    >>> print(f)
    Metal name: F, atomic number: 6, period: 1, group: 6
    >>> f.get_mass()
    78

    >>> f == h
    False
    >>> f != h
    True
    >>> f > h
    True
    >>> f < h
    False

    >>> water = Compound("H2O1")
    >>> water
    Compound("H2O1")
    >>> print(water)
    H2O1
    >>> water.elements
    {'H': 2, 'O': 1}
    >>> water.get_compound_mass()
    255

    >>> yummy_metal = Compound("U1")
    >>> dsc2 = Compound("D2S2C2")
    >>> dsc3 = Compound("D3S3C3")
    >>> cse = Compound("C7S8E9")
    >>> lava = Compound("H3O4")
    >>> obsidian = Compound("H5O5")
    >>> smelly_gas = Compound("H2")

    >>> water == yummy_metal
    True
    >>> water <= yummy_metal
    True
    >>> water > dsc2
    False

    >>> dsc2 + dsc3
    Compound("C5D5S5")
    >>> water - smelly_gas
    Compound("O1")
    >>> dsc2 + cse
    Traceback (most recent call last):
    ...
    ValueError
    >>> water - lava
    Traceback (most recent call last):
    ...
    ValueError
    >>> water + lava == obsidian
    True

    # MY DOCTESTS
    >>> t = Nonmetal("T")
    >>> t
    Nonmetal("T")
    >>> print(t)
    Nonmetal name: T, atomic number: 20, period: 4, group: 2
    >>> t.get_mass()
    164

    >>> r = Metal("R")
    >>> r
    Metal("R")
    >>> print(r)
    Metal name: R, atomic number: 18, period: 3, group: 6
    >>> r.get_mass()
    222

    >>> whoah = Metal("WH")
    Traceback (most recent call last):
    ...
    ValueError: invalid argument

    >>> s = Metal("S")
    >>> s
    Metal("S")
    >>> print(s)
    Metal name: S, atomic number: 19, period: 4, group: 1
    >>> s.get_mass()
    229


    >>> r == t
    False
    >>> r != t
    True
    >>> r > t
    True
    >>> r < t
    False

    >>> methane = Compound("C1H4")
    >>> methane
    Compound("C1H4")
    >>> print(methane)
    C1H4
    >>> methane.elements
    {'C': 1, 'H': 4}
    >>> methane.get_compound_mass()
    289

    >>> amphetamine = Compound("C9H13N1")
    Traceback (most recent call last):
    ...
    ValueError: invalid argument

    >>> nope = Compound("N1O1")
    >>> print(nope)
    N1O1

    >>> hydro_pero = Compound("H2O2")
    >>> hydro_pero
    Compound("H2O2")
    >>> print(hydro_pero)
    H2O2
    >>> hydro_pero.elements
    {'H': 2, 'O': 2}
    >>> hydro_pero.get_compound_mass()
    378

    >>> ammonia = Compound("N1H3")
    >>> iodate = Compound("I1O3")

    >>> iodate == nope
    False

    >>> iodate > nope
    True

    >>> iodate < ammonia
    False

    >>> iodate + nope
    Compound("I1N1O4")
    >>> hydro_pero - nope
    Traceback (most recent call last):
    ...
    ValueError
    >>> nope == water
    False
    >>> ammonia + hydro_pero
    Compound("H5N1O2")

    """
    return


LIST_METAL = "FKLPQRUVWXZ"


class Element:
    """
    A class that abstracts a chemical element
    """

    def __init__(self, name):
        """
        Constructor of Element

        Input validation is required

        Parameter:
        name (str): a single uppercase character from 'A' to 'Z' that
                    represents the name of the element
        # """
        # raise errors for incrrect input types
        if not isinstance(name, str):
            raise ValueError('invalid argument')
        if len(name) != 1 or name.islower():
            raise ValueError('invalid argument')
        # use ascii
        ord_ind = 64
        div_6 = 6
        six_dig = 6
        self.name = name
        self.atomic_num = ord(name) - ord_ind
        self.period = (self.atomic_num - 1) // six_dig + 1
        group = self.atomic_num % div_6
        if group == 0:
            group = six_dig
        self.group = group

    def get_mass(self):
        """
        Returns atomic mass of this element

        This method is a placeholder to avoid style check errors in some
        editors or tools. You will overwrite this method in the subclasses.
        """
        # DO NOT MODIFY #
        raise NotImplementedError("must be implemented in the subclasses")

    def __eq__(self, other_elem):
        """
        Returns True when two Elements are equal.
        Equality is determined by their atomic mass
        """
        if self.get_mass() == other_elem.get_mass():
            return True
        else:
            return False
    def __ne__(self, other_elem):
        """ Returns True when two Elements are not equal """
        if self.get_mass() != other_elem.get_mass():
            return True
        else:
            return False

    def __gt__(self, other_elem):
        """ Returns True when this Element is greater than the other """
        if self.get_mass() > other_elem.get_mass():
            return True
        else:
            return False

    def __ge__(self, other_elem):
        """
        Returns True when this Element is greater than or
        equal to the other
        """
        if self.get_mass() >= other_elem.get_mass():
            return True
        else:
            return False

    def __lt__(self, other_elem):
        """ Returns True when this Element is less than the other """
        if self.get_mass() < other_elem.get_mass():
            return True
        else:
            return False

    def __le__(self, other_elem):
        """
        Returns True when this Element is less than or
        equal to the other
        """
        if self.get_mass() <= other_elem.get_mass():
            return True
        else:
            return False

    def __repr__(self):
        """ Returns object representation of this Element """
        # uncomment the following code
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form

class Nonmetal(Element):
    """
    A class that abstracts nonmetal elements
    """

    def get_mass(self):
        """ Returns atomic mass of this Nonmetal element """
        #Nonmetal: atomic mass = 8 * atomic number + period number
        multiplier = 8
        return multiplier * self.atomic_num + self.period

    def __str__(self):
        """ Returns string representation of this Nonmetal element """
        # uncomment the following code
        str_form = (
            "Nonmetal name: {}, atomic number: {}, period: {}, group: {}")
        return str_form.format(self.name, self.atomic_num, self.period, \
                               self.group)

class Metal(Element):
    """
    A class that abstracts metal elements
    """

    def get_mass(self):
        """ Returns atomic mass of this Metal element """
        # atomic mass = 12 * atomic number + group number
        multiplier = 12
        return multiplier * self.atomic_num + self.group

    def __str__(self):
        """ Returns string representation of this Metal element """
        # uncomment the following code
        str_form = "Metal name: {}, atomic number: {}, period: {}, group: {}"
        return str_form.format(self.name, self.atomic_num, self.period, \
                               self.group)

class Compound:
    """
    A class that abstracts a compound element(contains one or more elements)
    """

    def __init__(self, name):
        """
        Constructor of Compound

        Input validation is required

        Parameter:
        name (str): a string that represents the name of the compound
        """
        pair = 2
        skip_two = 2
        # raise errors for invalid arguments
        if not isinstance(name, str):
            raise ValueError('invalid argument')
        if len(name) % 2 != 0:
            raise ValueError('invalid argument')
        self.name = name
        # create dictionary where element names are keys and number of
        # max_atoms are values
        self.elements = {}
        for ind in range(0, len(name), skip_two):
            pair = name[ind: ind + skip_two]
            ele = pair[::skip_two]
            num_atoms = int(pair[1::skip_two])
            max_atoms = 9
            min_atoms = 1
            if not min_atoms <= num_atoms <= max_atoms:
                raise ValueError('invalid argument')
            else:
                self.elements[ele] = num_atoms
        # get compound mass depending on the type of element
        self.compound_mass = 0
        for element, num_atoms in self.elements.items():
            ele = Element(element)
            if ele.name in LIST_METAL:
                self.compound_mass += Metal.get_mass(ele) * num_atoms
            else:
                self.compound_mass += Nonmetal.get_mass(ele) * num_atoms

    def get_compound_mass(self):
        """ A simple getter of compound_mass """
        return self.compound_mass

    def __eq__(self, other_comp):
        """
        Returns True when two Compounds are equal.
        Equality is determined by their compound mass
        """
        if self.get_compound_mass() == other_comp.get_compound_mass():
            return True
        else:
            return False

    def __ne__(self, other_comp):
        """ Returns True when two Compounds are not equal """
        if self.get_compound_mass() != other_comp.get_compound_mass():
            return True
        else:
            return False

    def __gt__(self, other_comp):
        """ Returns True when this Compound is greater than the other """
        if self.get_compound_mass() > other_comp.get_compound_mass():
            return True
        else:
            return False

    def __ge__(self, other_comp):
        """
        Returns True when this Compound is greater than or
        equal to the other
        """
        if self.get_compound_mass() >= other_comp.get_compound_mass():
            return True
        else:
            return False

    def __lt__(self, other_comp):
        """ Returns True when this Compound is less than the other """
        if self.get_compound_mass() < other_comp.get_compound_mass():
            return True
        else:
            return False

    def __le__(self, other_comp):
        """
        Returns True when this Compound is less than or
        equal to the other
        """
        if self.get_compound_mass() <= other_comp.get_compound_mass():
            return True
        else:
            return False

    def __add__(self, other_comp):
        """
        Synthesize a new Compound by adding this Compound with another

        Exception:
        ValueError will be raised if the product is invalid
        """
        max_num_atom = 9
        new_compound = {}
        # add number of atoms together if the key exists in new compound
        # dictionary, otherwise the number of atoms is just itself
        for self_elem, self_elem_num_atom in self.elements.items():
            if self_elem in new_compound:
                new_compound[self_elem] += self_elem_num_atom
            elif self_elem not in new_compound:
                new_compound[self_elem] = self_elem_num_atom
            # raise error if the product is > 9 and or negative
            if new_compound[self_elem] > max_num_atom:
                raise ValueError()
            if new_compound[self_elem] < 0:
                raise ValueError()
        # same but checking the cases if other_comp has elements not shared
        # with self
        for other_elem, other_elem_num_atom in other_comp.elements.items():
            if other_elem in new_compound:
                new_compound[other_elem] += other_elem_num_atom
            elif other_elem not in new_compound:
                new_compound[other_elem] = other_elem_num_atom
            # product cannot exceed 9 nor can it be negative
            if new_compound[other_elem] > max_num_atom:
                raise ValueError()
            if new_compound[other_elem] < 0:
                raise ValueError()

        # remove element if number of atoms is zero
        no_zeros = {elem: num_atoms for elem, num_atoms \
                    in new_compound.items() if num_atoms != 0}
        new_compound = no_zeros

        #sort dictionary items and then create the string to be printed
        sorted_dict = sorted(new_compound.items())
        new_str = ""
        for key, val in sorted_dict:
            new_str += key + str(val)
        return Compound(new_str)


    def __sub__(self, other_comp):
        """
        Decompose this Compound by subtracting another from it. A new product
        is returned after decomposition

        Exception:
        ValueError will be raised if the product is invalid
        """
        max_num_atom = 9
        sub_dict = {}
        # loops based off of self's keys
        for other_element in other_comp.elements.keys():
            for self_element in self.elements.keys():
                # returns self's atom number if not a shared key
                if self_element not in other_comp.elements.keys():
                    sub_dict[self_element] = self.elements[self_element]
                # subtract other's num from self
                elif other_element in self.elements.keys():
                    sub_dict[other_element] = (
                        self.elements[other_element] - \
                                            other_comp.elements[other_element])
                # other_element has to be in self's keys
                elif other_element not in self.elements.keys():
                    raise ValueError()
                # raise errors for negative total num of atoms and if > 9
                if sub_dict[self_element] < 0:
                    raise ValueError()
                if sub_dict[self_element] > max_num_atom:
                    raise ValueError()
                    
        # remove atom number of zero
        no_zeros = {elem: num_atoms for elem, num_atoms in sub_dict.items() \
                    if num_atoms != 0}
        sub_dict = no_zeros

        # string form
        new_str = ""
        for elements, num_atoms in sub_dict.items():
            new_str += elements + str(num_atoms)
        return Compound(new_str)

    def __str__(self):
        """ Returns string representation of this Compound """
        return '{}'.format(self.name)

    def __repr__(self):
        """ Returns object representation of this Compound """
        # uncomment the following code
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form
