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
        """
        Method to get size of linked list
        :return: size of linked list
        """
        return self.size

    def add_node(self, data):
        """
        Method to add node to linked list
        :param data: value of new node
        :return: nothing
        """
        new_node = ListNode(data, self.head)
        self.head = new_node
        self.size += 1

    def print_list(self):
        """
        Method to print the entire linked list
        :return: nothing
        """
        current_node = self.head
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.get_next_node()
        print()

    def reverse_list(self):
        """
        Method to reverse the linked list
        :return: nothing
        """
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.get_next_node()
            current_node.set_next_node(prev_node)
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
