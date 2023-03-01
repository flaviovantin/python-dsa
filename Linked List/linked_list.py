
class Node:

    def __init__(self, value):
        """ {'value': value, 'next': None} """
        self.value = value
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
        if self.head is not None:
            print('Head--> ' + str(self.head.value))
        else:
            print('Head--> None')
        while n is not None:
            print(n.value)
            n = n.next
        if self.tail is not None:
            print('Tail--> ' + str(self.tail.value))
        else:
            print('Tail--> None')
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
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            n = self.head
            temp = None
            while n is not None:
                if n.next is not None:
                    self.tail = n
                temp = n.value
                n = n.next
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        """ O(1) """
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop_first(self):
        """ O(1) """
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head.value
            self.head.next = None
            self.head = self.tail
            self.length -= 1
            return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            count = 0
            n = self.head
            while n is not None:
                if count == index:
                    return n.value
                count += 1
                n = n.next

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
        # TODO implement the index correctly
        if index == 0:
            self.prepend(value)
        elif index == self.length-1:
            self.append(value)
        else:
            # TODO implement it
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

print('>> Removed: ' + str(my_linked_list.pop()))
my_linked_list.print_list()

#  Head           Tail
#   |              |
#   V              V
#  (22)--> (4)--> (23)--> null
my_linked_list.append(4)
my_linked_list.print_list()

my_linked_list.append(23)
my_linked_list.print_list()

my_linked_list.prepend(22)
my_linked_list.print_list()

my_linked_list.prepend(11)
my_linked_list.print_list()

my_linked_list.insert(0, 15)  # TODO o que deveria ser o index? 0 ou 1
my_linked_list.print_list()

# my_linked_list.insert(6, 16)
# my_linked_list.print_list()

print('>> Removed: ' + str(my_linked_list.pop()))
my_linked_list.print_list()

print('>> Removed: ' + str(my_linked_list.pop()))
my_linked_list.print_list()

print('>> Removed: ' + str(my_linked_list.pop()))
my_linked_list.print_list()

print('>> Removed: ' + str(my_linked_list.pop()))
my_linked_list.print_list()

print('>> Removed: ' + str(my_linked_list.pop()))
my_linked_list.print_list()

my_linked_list.append(9)
my_linked_list.append(21)
my_linked_list.print_list()
