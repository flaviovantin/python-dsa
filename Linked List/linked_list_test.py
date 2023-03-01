import unittest
from linked_list import LinkedList


class MyTestCase(unittest.TestCase):

    def test_append(self):
        my_linked_list = LinkedList()
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        my_linked_list.append(4)
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 4)
        self.assertEqual(my_linked_list.tail.value, 4)
        my_linked_list.append(9)
        self.assertEqual(my_linked_list.length, 2)
        self.assertEqual(my_linked_list.head.value, 4)
        self.assertEqual(my_linked_list.tail.value, 9)

    def test_prepend(self):
        my_linked_list = LinkedList()
        my_linked_list.prepend(3)
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 3)
        self.assertEqual(my_linked_list.tail.value, 3)
        my_linked_list = LinkedList(5)
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 5)
        self.assertEqual(my_linked_list.tail.value, 5)
        my_linked_list.prepend(6)
        self.assertEqual(my_linked_list.length, 2)
        self.assertEqual(my_linked_list.head.value, 6)
        self.assertEqual(my_linked_list.tail.value, 5)

    def test_pop(self):
        my_linked_list = LinkedList()
        number = my_linked_list.pop()
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertIsNone(number)
        my_linked_list.append(20)
        my_linked_list.append(30)
        self.assertEqual(my_linked_list.length, 2)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(my_linked_list.tail.value, 30)
        number = my_linked_list.pop()
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(number, 30)
        number = my_linked_list.pop()
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertEqual(number, 20)


if __name__ == '__main__':
    unittest.main()
