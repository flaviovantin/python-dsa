
class Node:

    def __init__(self, value):
        """ {'value': value, 'next': None} """
        self.value = None if value is None else value
        self.next = None


class LinkedList:

    def __init__(self, value=None):
        if value is None:
            node = None
            self.length = 0
        else:
            node = Node(value)
            self.length = 1
        self.head = node
        self.tail = node

    def print_list(self):
        """ O(n) """
        n = self.head
        print('Head--> ' + str(self.head.value) if self.head is not None else 'Head--> None')
        while n is not None:
            print(n.value)
            n = n.next
        print('Tail--> ' + str(self.tail.value) if self.tail is not None else 'Tail--> None')
        print('Length: ' + str(self.length) + '\n')

    def append(self, value):
        """ O(1) """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def pop(self):
        """ O(n) """
        pass

    def prepend(self, value):
        """ O(1) """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def remove(self, index, value):
        """
        at the beginning: O(1)
        in the middle or at the end (pop): O(n)
        """
        pass

    def insert(self, index, value):
        """
        at the beginning (prepend) or at the end (append): O(1)
        in the middle: O(n)
        """
        if index == 0:
            self.prepend(value)
        elif index == self.length-1:
            self.append(value)
        else:
            node = Node(value)


    def lookup(self, value):
        """ O(n) """
        pass


#  Head/Tail
#    |  |
#    V  V
#    None
my_linked_list = LinkedList()
my_linked_list.print_list()
#
# my_linked_list.prepend(22)
# my_linked_list.print_list()

#  Head           Tail
#   |              |
#   V              V
#  (4)--> (23)--> (7)--> null
# my_linked_list = LinkedList(4)
# my_linked_list.print_list()

my_linked_list.append(23)
my_linked_list.print_list()

my_linked_list.append(7)
my_linked_list.print_list()

my_linked_list.prepend(11)
my_linked_list.print_list()
