

class Node:

    def __init__(self, value):
        self.value = value
        self.next: None


class LinkedList:

    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        # create a new node
        node = Node(value)
        # add the node to end
        pass

    def pop(self):
        pass

    def prepend(self, value):
        # create a new node
        node = Node(value)
        # add the node to beginning
        pass

    def remove(self, index, value):
        pass

    def insert(self, index, value):
        # create a new node
        node = Node(value)
        # insert the node at the desire position
        pass

    def lookup(self, value):
        pass


my_linked_list = LinkedList(3)

