"""
Base class for singly linked-list
"""
from collections import Iterable
import unittest


class TestLinkedList(unittest.TestCase):

    def test_1(self):
        N = 1000
        ll = LinkedList(N)
        self.assertEqual(ll.data, N)
        ll = LinkedList(range(N))
        for index in range(N):
            self.assertEqual(ll.data, index)
            ll = ll.next


class LinkedList(object):
    """A singly-linked linked-list

    Attributes:
        data: data stored in the node
    """

    def __init__(self, data):
        if isinstance(data, Iterable):
            self = self.__build_list(data)
        else:
            self.data = data
            self.next = None

    def __build_list(self, data):
        head = first = LinkedList(None)
        for node in data:
            head.next = LinkedList(node)
            head = head.next
        return first.next


if __name__ == "__main__":
    unittest.main()
