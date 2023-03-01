import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

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
        self.assertEqual(my_linked_list.tail.value, 20)
        self.assertEqual(number, 30)
        number = my_linked_list.pop()
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertEqual(number, 20)

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

    def test_pop_first(self):
        my_linked_list = LinkedList()
        number = my_linked_list.pop_first()
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertIsNone(number)
        my_linked_list.append(20)
        my_linked_list.append(30)
        self.assertEqual(my_linked_list.length, 2)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(my_linked_list.tail.value, 30)
        number = my_linked_list.pop_first()
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 30)
        self.assertEqual(my_linked_list.tail.value, 30)
        self.assertEqual(number, 20)
        number = my_linked_list.pop_first()
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertEqual(number, 30)

    def test_get(self):
        my_linked_list = LinkedList()
        node = my_linked_list.get(0)
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertIsNone(node)
        node = my_linked_list.get(3)
        self.assertIsNone(node)
        my_linked_list.append(10)
        node = my_linked_list.get(1)
        self.assertIsNone(node)
        my_linked_list.append(20)
        my_linked_list.append(30)
        node = my_linked_list.get(-1)
        self.assertIsNone(node)
        node = my_linked_list.get(1)
        self.assertEqual(node.value, 20)
        node = my_linked_list.get(0)
        self.assertEqual(node.value, 10)
        node = my_linked_list.get(2)
        self.assertEqual(node.value, 30)
        self.assertEqual(my_linked_list.length, 3)
        self.assertEqual(my_linked_list.head.value, 10)
        self.assertEqual(my_linked_list.tail.value, 30)

    def test_set(self):
        my_linked_list = LinkedList()
        my_linked_list.set(1, 30)
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        my_linked_list.set(0, 100)
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        my_linked_list.append(10)
        my_linked_list.append(20)
        my_linked_list.append(30)
        my_linked_list.append(40)
        self.assertEqual(my_linked_list.length, 4)
        self.assertEqual(my_linked_list.head.value, 10)
        self.assertEqual(my_linked_list.tail.value, 40)
        my_linked_list.set(2, 333)
        self.assertEqual(my_linked_list.length, 4)
        self.assertEqual(my_linked_list.head.value, 10)
        self.assertEqual(my_linked_list.tail.value, 40)
        node = my_linked_list.get(2)
        self.assertEqual(node.value, 333)
        my_linked_list.set(0, 111)
        self.assertEqual(my_linked_list.length, 4)
        self.assertEqual(my_linked_list.head.value, 111)
        self.assertEqual(my_linked_list.tail.value, 40)
        my_linked_list.set(3, 444)
        self.assertEqual(my_linked_list.tail.value, 444)

    def test_insert(self):
        my_linked_list = LinkedList()
        succeeded = my_linked_list.insert(3, 100)
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertFalse(succeeded)
        succeeded = my_linked_list.insert(0, 20)
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(my_linked_list.tail.value, 20)
        self.assertTrue(succeeded)
        my_linked_list.insert(1, 21)
        my_linked_list.insert(2, 22)
        succeeded = my_linked_list.insert(3, 23)
        self.assertEqual(my_linked_list.length, 4)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(my_linked_list.tail.value, 23)
        self.assertTrue(succeeded)
        my_linked_list.insert(0, 30)
        self.assertEqual(my_linked_list.length, 5)
        self.assertEqual(my_linked_list.head.value, 30)
        my_linked_list.insert(5, 55)
        self.assertEqual(my_linked_list.length, 6)
        self.assertEqual(my_linked_list.head.value, 30)
        self.assertEqual(my_linked_list.tail.value, 55)

    def test_remove(self):
        my_linked_list = LinkedList()
        number = my_linked_list.remove(0)
        self.assertEqual(my_linked_list.length, 0)
        self.assertIsNone(my_linked_list.head)
        self.assertIsNone(my_linked_list.tail)
        self.assertIsNone(number)
        number = my_linked_list.remove(10)
        self.assertIsNone(number)
        my_linked_list.append(20)
        my_linked_list.append(21)
        my_linked_list.append(22)
        self.assertEqual(my_linked_list.length, 3)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(my_linked_list.tail.value, 22)
        number = my_linked_list.remove(1)
        self.assertEqual(my_linked_list.length, 2)
        self.assertEqual(my_linked_list.head.value, 20)
        self.assertEqual(my_linked_list.tail.value, 22)
        self.assertEqual(number, 21)
        number = my_linked_list.remove(0)
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 22)
        self.assertEqual(my_linked_list.tail.value, 22)
        self.assertEqual(number, 20)
        number = my_linked_list.remove(0)
        self.assertEqual(my_linked_list.length, 0)
        self.assertEqual(number, 22)

    def test_all(self):
        my_linked_list = LinkedList()
        my_linked_list.append(33)
        my_linked_list.pop()
        my_linked_list.append(12)
        my_linked_list.prepend(5)
        node = my_linked_list.get(1)
        self.assertEqual(node.value, 12)
        my_linked_list.pop()
        my_linked_list.append(77)
        number = my_linked_list.pop_first()
        self.assertEqual(my_linked_list.length, 1)
        self.assertEqual(my_linked_list.head.value, 77)
        self.assertEqual(my_linked_list.tail.value, 77)
        self.assertEqual(number, 5)
        my_linked_list.set(0, 1977)
        self.assertEqual(my_linked_list.head.value, 1977)


if __name__ == '__main__':
    unittest.main()