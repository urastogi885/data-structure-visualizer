import cv2
import os
import numpy as np


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

    def animate_list(self):
        """
        Method to create gif of linked list
        :return: nothing
        """
        img_size = 100, self.size * 100, 3
        img = np.zeros(img_size, dtype=np.uint8)
        img.fill(255)
        current_node = self.head
        initial_pos = 35, 60
        if not os.path.exists('gifs/'):
            os.mkdir('gifs/')
        video_format = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        video_output = cv2.VideoWriter('gifs/video_animation.avi', video_format, 2, (img_size[1], img_size[0]))
        for i in range(self.size):
            cv2.putText(img, str(current_node.get_data()), (initial_pos[0] + i * img_size[0], initial_pos[1]),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            for _ in range(2):
                video_output.write(img)
            if i != self.size - 1:
                cv2.arrowedLine(img, (initial_pos[0] + i * img_size[0] + 30, initial_pos[1] - 10),
                                (initial_pos[0] + (i + 1) * img_size[0] - 20, initial_pos[1] - 10), (0, 0, 0))
                for _ in range(2):
                    video_output.write(img)
            print(current_node.get_data(), end=' ')
            current_node = current_node.get_next_node()
        video_output.release()
        os.system('ffmpeg -y -i gifs/video_animation.avi -vf "fps=5" -loop 0 gifs/linked_list.gif')
        os.system('rm -rf gifs/video_animation.avi')
        print()
