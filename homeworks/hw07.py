"""
DSC 20 Homework 07
Name: Tonia Le
PID:  A15662706
"""

def doctests_go_here():
    """
    >>> available_time1 = [[1, 3, 21], [4, 6, 30], [9, 12, 8]]
    >>> ps1 = PersonalSchedule("Sun", "Curly", available_time1)
    >>> print(ps1)
    Curly Sun is available at [[1, 3, 21], [4, 6, 30], [9, 12, 8]].

    >>> available_time2 = [[1, 7, 20], [9, 10, 5], [11, 16, 8]]
    >>> ps2 = PersonalSchedule("Ran", "Sean", available_time2)
    >>> print(ps2)
    Sean Ran is available at [[1, 7, 20], [9, 10, 5], [11, 16, 8]].

    >>> available_time3 = [[2, 8, 25], [3, 12, 20], [1, 11, 20]]
    >>> ps3 = PersonalSchedule('Marz', 'Mirz', available_time3)
    >>> print(ps3)
    Mirz Marz is available at [[2, 8, 25], [3, 12, 20], [1, 11, 20]].

    >>> available_time4 = [[1, 12, 35], [2, 10, 20]]
    >>> ps4 = PersonalSchedule('Rice', 'Eric', available_time4)
    >>> print(ps4)
    Eric Rice is available at [[1, 12, 35], [2, 10, 20]].

    >>> available_time5 = [[7, 10, 10], [1, 3, 5], [1, 2, 15]]
    >>> ps5 = PersonalSchedule('Yabs', 'Gabs', available_time5)
    >>> print(ps5)
    Gabs Yabs is available at [[7, 10, 10], [1, 3, 5], [1, 2, 15]].

    >>> t1 = Task(2, 5, 20, 1000, "Chopping potatoes")
    >>> t2 = Task(4, 5, 32, 2000, "Coding")
    >>> t3 = Task(11, 12, 8, 4000, "Playing League")
    >>> t4 = Task(1, 2, 21, 1200, "Gardening")
    >>> t5 = Task(11, 16, 6, 500, "Jogging")
    >>> t6 = Task(4, 6, 20, 1200, "Chopping potatoes")
    >>> t7 = Task(6, 9, 20, 1000, "Chopping potatoes")
    >>> t8 = Task(3, 5, 12, 2500, "Typing")
    >>> t9 = Task(1, 8, 24, 1000, "Plumbing")
    >>> t10 = Task(2, 3, 1, 5, "Crying")
    >>> t11 = Task(1, 12, 32, 3000, "Coding")

    >>> print(t1)
    Task Chopping potatoes starts at 2, ends at 5, requires 20 focus level, \
and gives 1000 profit.

    >>> print(t2)
    Task Coding starts at 4, ends at 5, requires 32 focus level, and gives \
2000 profit.

    >>> print(t3)
    Task Playing League starts at 11, ends at 12, requires 8 focus level, \
and gives 4000 profit.

    >>> print(t8)
    Task Typing starts at 3, ends at 5, requires 12 focus level, \
and gives 2500 profit.

    >>> print(t9)
    Task Plumbing starts at 1, ends at 8, requires 24 focus level, \
and gives 1000 profit.

    >>> print(t10)
    Task Crying starts at 2, ends at 3, requires 1 focus level, \
and gives 5 profit.

    >>> ps1.can_handle(t1)
    False
    >>> ps1.can_handle(t2)
    False
    >>> ps1.can_handle(t3)
    True
    >>> ps2.can_handle(t4)
    False
    >>> ps2.can_handle(t5)
    True
    >>> ps3.can_handle(t8)
    True
    >>> ps3.can_handle(t9)
    False
    >>> ps4.can_handle(t10)
    True

    >>> ps1.can_handle_task_sequence([t1, t2, t3])
    False
    >>> ps1.can_handle_task_sequence([t3, t4])
    True
    >>> ps2.can_handle_task_sequence([t3, t4])
    False
    >>> ps2.can_handle_task_sequence([t3, t5])
    True
    >>> ps3.can_handle_task_sequence([t8, t9])
    False
    >>> ps3.can_handle_task_sequence([t9, t10])
    False
    >>> ps4.can_handle_task_sequence([t1,t10])
    True
    >>> ps5.can_handle_task_sequence([t2, t4])
    False

    >>> t1.can_merge_task(t6)
    True
    >>> t1.can_merge_task(t7)
    False
    >>> t1.can_merge_task(t10)
    False
    >>> t4.can_merge_task(t10)
    False
    >>> t6.can_merge_task(t7)
    True

    >>> merged_task1 = t1.merge_two_tasks(t6)
    >>> print(merged_task1)
    Task Chopping potatoes starts at 2, ends at 6, requires 20 focus level, \
and gives 2200 profit.
    >>> merged_task2 = t1.merge_two_tasks(t7)
    >>> print(merged_task2)
    None
    >>> merged_task3 = t6.merge_two_tasks(t7)
    >>> print(merged_task3)
    Task Chopping potatoes starts at 4, ends at 9, requires 20 focus level, \
and gives 2200 profit.
    >>> merged_task4 = t4.merge_two_tasks(t10)
    >>> print(merged_task4)
    None
    >>> merged_task5 = t2.merge_two_tasks(t11)
    >>> print(merged_task5)
    Task Coding starts at 1, ends at 12, requires 32 focus level, \
and gives 5000 profit.


    >>> task_sequences = [[t1, t2, t3], [t3, t4], [t3, t6]]
    >>> result1 = ps1.most_profitable_task_sequence(task_sequences)
    >>> result2 = ps1.most_profitable_task_sequence_recursion(task_sequences)
    >>> result1 == [[t3, t4], [t3, t6]]
    True
    >>> result1 == result2
    True
    >>> result3 = ps2.most_profitable_task_sequence_recursion([[t3], [t5]])
    >>> result3 == [[t3]]
    True

    >>> task_sequences = [[t3, t5], [t1, t10]]
    >>> result4 = ps2.most_profitable_task_sequence(task_sequences)
    >>> result4 == [[t3, t5]]
    True
    >>> res4_recu = ps2.most_profitable_task_sequence_recursion(task_sequences)
    >>> res4_recu == [[t3, t5]]
    True

    >>> task_sequences = [[t1, t10]]
    >>> result5 = ps3.most_profitable_task_sequence(task_sequences)
    >>> result5 == [[t1, t10]]
    True
    >>> res5_recu = ps3.most_profitable_task_sequence_recursion(task_sequences)
    >>> res5_recu == result5
    True

    >>> task_sequences = [[t1, t10], [t1, t9]]
    >>> result6 = ps3.most_profitable_task_sequence(task_sequences)
    >>> result6 == [[t1, t10]]
    True
    >>> res6_recu = ps3.most_profitable_task_sequence_recursion(task_sequences)
    >>> result6 == res6_recu
    True

    >>> ps2.handle_two_tasks(t1, t6)
    True
    >>> ps2.handle_two_tasks(t1, t7)
    False
    >>> ps2.handle_two_tasks(t6, t7)
    False
    >>> ps3.handle_two_tasks(t3, t11)
    False
    >>> ps4.handle_two_tasks(t4, t10)
    False
    >>> ps4.handle_two_tasks(t1, t3)
    False
    >>> ps5.handle_two_tasks(t10, t11)
    False
    """
    return


class Task:
    """
    Implementation of a task.
    """

    def __init__(self, start_time, end_time, focus_level_required, \
                profit, task_description):
        """
        Constructor of Task.

        Requirement:
        Input validation

        Parameters:
        start_time (int): Start time of this task should be a non-negative
                          integer.
        end_time (int): End time of this task should also be a non-negative
                        integer.
                        Start time should be strictly less than end time.
        focus_level_required (int): Focus level required for one person to
                                    handle this task.
                                    It should be a positive integer.
        profit (int): A positive integer that represents how much value would
                      be made if the task is successfully handled.
        task_description (str): Description of this task.
        """

        assert isinstance(start_time, int)
        assert isinstance(end_time, int)
        assert isinstance(focus_level_required, int)
        assert isinstance(profit, int)
        assert isinstance(task_description, str)


        self.start_time = int(start_time)
        self.end_time = int(end_time)
        self.focus_level_required = int(focus_level_required)
        self.profit = int(profit)
        self.task_description = task_description


    def get_start_time(self):
        """Getter for start_time attribute"""
        return self.start_time


    def get_end_time(self):
        """Getter for end_time attribute"""
        return self.end_time


    def get_focus_level_required(self):
        """Getter for focus_level_required attribute"""
        return self.focus_level_required


    def __str__(self):
        """
        String representation of Task.
        """
        return ("Task {} starts at {}, ends at {}, requires {} focus level, "
                + \
                "and gives {} profit.").format(self.task_description, \
                self.get_start_time(), self.get_end_time(), \
                self.get_focus_level_required(), self.profit)


    def can_merge_task(self, other_task):
        """
        Give another Task called other_task, this function determines whether
        we are able to merge the current task and other_task.

        Requirement:
        Input validation

        Parameters
        other_task (Task): The other task to be merged with this task.

        Returns:
        True if we are able to merge those two tasks, False otherwise.
        """
        #min(self.start_time, other_task.start_time)
        if ((self.focus_level_required == other_task.focus_level_required)
                and (self.task_description == other_task.task_description)
                and (max(self.start_time, other_task.start_time)
                     <= min(self.end_time, other_task.end_time))):
            return True
        else:
            return False

    def merge_two_tasks(self, other_task):
        """
        Merge two tasks if the merge is possible.

        Requirement:
        Input validation

        Parameters:
        other_task (Task): The other task to be merged with this task.

        Returns:
        The Task object after merging two tasks, where the new profit is
        the sum of two tasks' profit; otherwise, None is returned.
        """
        if self.can_merge_task(other_task):
            merged = Task(min(self.start_time, other_task.start_time),
                          max(self.end_time, other_task.end_time),
                          self.focus_level_required,
                          self.profit + other_task.profit,
                          self.task_description)
            return merged
        else:
            return None

class PersonalSchedule:
    """
    Implementation of a personal schedule.
    """

    def __init__(self, last_name, first_name, available_time):
        """
        Constructor of PersonalSchedule.

        Requirement:
        Input validation

        Parameters:
        last_name (str): Last name of this person. This string must have at
                        least 2 characters.
        first_name (str): First name of this person. This string must have at
                        least 2 characters.
        available_time (list[list]): A list of available intervals.
                        Each interval has three elements: [start_time,
                        end_time, focus_level]. You may assume that given
                        intervals don't have overlaps with one another.
        """
        assert isinstance(last_name, str)
        assert isinstance(first_name, str)
        assert isinstance(available_time, list)
        assert (all(isinstance(inner_list, list))
                for inner_list in available_time)


        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.available_time = available_time


    def get_last_name(self):
        """Getter for last_name attribute"""
        return self.last_name

    def get_first_name(self):
        """Getter for first_name attribute"""
        return self.first_name


    def get_available_time(self):
        """Getter for available_time attribute"""
        return self.available_time


    def __str__(self):
        """
        String representation of PersonalSchedule.
        """
        return "{} {} is available at {}.".format(self.get_first_name(), \
                self.get_last_name(), self.get_available_time())


    def can_handle(self, task):
        """
        This function determines whether this person can handle the given task.

        Requirement:
        Input validation

        Parameters:
        task (Task): A task that this person needs to handle.

        Returns:
        True if there exists a time interval in the schedule that can properly
        handle the task with the required focus level, False otherwise.
        """
        for lists in self.available_time:
            available_start = lists[0]
            available_end = lists[1]
            available_focus_lvl = lists[2]
            if (((available_start <= task.start_time) and
                 (available_end >= task.end_time)) and
                    (available_focus_lvl >= task.focus_level_required)):
                return True
        return False

    def can_handle_task_sequence(self, task_sequence):
        """
        Given a list of tasks, this function determines whether this person
        can handle this task sequence.

        Requirement:
        Input validation

        Parameters:
        task_sequence (list[Task]): A list of tasks this person needs to
        handle.

        Returns:
        True if all tasks can be properly handled, False otherwise. To simplify
        the question, we assume that multitasking is possible, i.e., a person
        can handle multiple tasks in a single time interval.
        """
        # loop through elements of a list of task
        bool_list = []
        for tasks in task_sequence:
            if self.can_handle(tasks):
                bool_list.append(True)
            else:
                bool_list.append(False)
        # check if all tasks in the sequene can be handled
        if all(elements is True for elements in bool_list):
            return True
        else:
            return False

    def most_profitable_task_sequence(self, task_sequences):
        """
        Given a list of task sequences, find all task sequences that give
        you the maximum profit.

        Requirement:
        Input validation

        Parameters:
        task_sequences (list[list]): A list of task sequences.

        Return:
        Sequence(s) of tasks (that a person can handle) that gives you the
         most profit.
        """
        # list of tasks
        max_profit = -1
        output = []
        for sequence in task_sequences:
            if self.can_handle_task_sequence(sequence):
                # tasks inside the sequence
                total_profit = 0
                for tasks in sequence:
                    # add up the profit of each task in the sequence
                    total_profit += tasks.profit
            else:
                total_profit = 0
            # overwrite
            if total_profit > max_profit:
                max_profit = total_profit
                # fresh list without non-max profits
                output = []
                output.append(sequence)
                # append sequence
            elif total_profit == max_profit:
                output.append(sequence)
        return output

    def most_profitable_task_sequence_recursion(self, task_sequences):
        """
        Given a list of task sequences, find all task sequences that give you
        the maximum profit.
        You MUST USE RECURSION in your solution.

        Requirement:
        Input validation

        Parameters:
        task_sequences (list[list]): A list of task sequences.

        Return:
        Sequence(s) of tasks (that a person can handle) that gives you the
        most profit.

        """
        # check if can handle task sequence or not
        if not all(list(map(self.can_handle_task_sequence, task_sequences))):
            return list(filter(self.can_handle_task_sequence, task_sequences))

        def get_profit(tsk_seq):
            """
            This function returns the sum of the task profits of a task
            sequence.
            """
            profit = 0
            for tsk in tsk_seq:
                profit += tsk.profit
            return profit

        # base cases
        if len(task_sequences) == 0:
            return []
        if len(task_sequences) == 1:
            return task_sequences

        # define elements to compare
        rest_of_seq = (
            self.most_profitable_task_sequence_recursion(task_sequences[1:]))
        max_profit = 0
        first_task_seq_profit = get_profit(task_sequences[0])

        if len(rest_of_seq) == 0:
            max_profit = 0
        else:
            max_profit = get_profit(rest_of_seq[0])
        # compare the max_profit with first task seq's profit
        if first_task_seq_profit > max_profit:
            return [task_sequences[0]]
        elif first_task_seq_profit == max_profit:
            return [task_sequences[0]] + rest_of_seq
        return rest_of_seq

    def handle_two_tasks(self, task1, task2):
        """
        Given two tasks, the function determines whether this personal can
        handle them together.

        Requirement:
        Input validation

        Parameters:
        task1 (Task): The first task.
        task2 (Task): The second task.

        Returns:
        True if and only if two tasks can be merged and handled by this
        PersonalSchedule, False otherwise.
        """
        single_merged_task = task1.merge_two_tasks(task2)
        if single_merged_task is None:
            return False
        else:
            return self.can_handle(single_merged_task)

# END OF FILE #
