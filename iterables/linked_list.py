"""
Base class for singly linked-list
"""
from collections import Iterable
import unittest


class TestLinkedList(unittest.TestCase):

    def test_1(self):

        N = 10

        ll = LinkedList(range(N))

        for index, item in enumerate(ll):
            self.assertEqual(item, index)

        self.assertFalse(ll.find(-15))

        self.assertTrue(ll.insert(-15))
        self.assertTrue(ll.find(-15))

        self.assertTrue(ll.delete(-15))
        self.assertFalse(ll.find(-15))

        self.assertTrue(ll.delete(1))
        self.assertFalse(ll.find(1))


class LinkedList(object):
    """A singly-linked linked-list

    Attributes:
        data: data stored in the node
    """

    def __init__(self, data):
        """Initializes a Linked List

        My implementation of a linked list uses a dummy first element
        Arguments:
            data: either a single object or iterable
        """
        self.data = None
        self.next = None

        if isinstance(data, Iterable):
            ll = self.__build_list(data)
            self.data = ll.data
            self.next = ll.next
        else:
            self.data = data

    def __iter__(self):
        """yield data values stored in linked list"""
        node = self

        while node:
            yield node.data
            node = node.next

    def __build_list(self, datas):
        """build the list from the iterable

        Returns:
            reference to the head of created list
        """
        head = node = LinkedList(None)
        for data in datas:
            node.next = LinkedList(data)
            node = node.next
        return head.next

    def rinsert(self, data):
        """insert element data in the linked list to the right
        """
        node = self
        while node.next:
            node = node.next
        node.next = LinkedList(data)
        return True

    def linsert(self, data):
        """insert element data in the linked list to the left
        """
        node = LinkedList(data)
        node.next = self.next
        self.next = node
        return True

    insert = linsert

    def delete(self, data):
        """delete element from linked list"""
        prev = self
        node = self.next
        while node:
            if node.data == data:
                prev.next = node.next
                del node
                return True
            prev = node
            node = node.next
        return False

    def find(self, data):
        """check if element exists in linked list"""
        node = self.next

        while node:
            if node.data == data:
                return True
            node = node.next

        return False




if __name__ == "__main__":
    unittest.main()
