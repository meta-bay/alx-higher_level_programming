#!/usr/bin/python3
"""Class for singly listed link"""


class Node:
    """defines a node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.
        Args:
            data: The data of the Node
            next_node: The next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly-linked list."""

    def __init__(self):
        """Initalizes a new singly inked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the singly listed link
        in a sorted way
        Args:
            value (Node): The new Node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """defines print for the list"""
        temp = self.__head
        values = []
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
