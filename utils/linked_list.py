import math


class ListNode:
    """
    A class that implements a node in linked lists
    """

    def __init__(self, value=0, next_node=None):
        """
        Method to initialize a linked-list node
        :param value: value of the linked-list node
        :param next_node: next linked-list node
        """
        self.value = value
        self.next_node = next_node

    def get_data(self):
        """
        Method to get value of node
        :return: value of node
        """
        return self.value

    def set_data(self, val):
        """
        Method to set value of node
        :param val: value of node
        :return: nothing
        """
        self.value = val

    def get_next_node(self):
        """
        Method to get value of next node
        :return: value of next node
        """
        return self.next_node

    def set_next_node(self, val):
        """
        Method to set value of next node
        :param val: value of next node
        :return: nothing
        """
        self.next_node = val


class LinkedList:
    """
    A class that implements singly-linked list
    """
    def __init__(self, head=None):
        """
        Method to initialize linked list class
        :param head: value of the current linked list node
        """
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        new_node = ListNode(data, self.head)
        self.head = new_node
        self.size += 1

    def print_node(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.get_next_node()
        print()


if __name__ == '__main__':
    # Define value to be stored in the linked list
    storing_value = 243
    # Get length of the number
    digits = len(str(storing_value))
    # Initialize object of linked list
    linked_list = LinkedList()
    # Store each digit of the number
    for y in range(digits - 1, -1, -1):
        divisor = int(math.pow(10, y))
        linked_list.add_node(storing_value // divisor)
        storing_value %= divisor
    # Print the linked list
    linked_list.print_node()
