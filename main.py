from sys import argv
from utils.linked_list import SinglyLinkedList


script, number = argv


if __name__ == '__main__':
    # Define value to be stored in the linked list
    storing_value = int(number)
    # Get length of the number
    digits = len(str(storing_value))
    # Initialize object of linked list
    linked_list = SinglyLinkedList()
    # Store each digit of the number
    for y in range(digits - 1, -1, -1):
        divisor = 10 ** y
        linked_list.add_node(storing_value // divisor)
        storing_value %= divisor
    # Reverse linked list
    linked_list.reverse_list()
    print(linked_list)
    linked_list.animate_list()
