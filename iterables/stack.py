"""
Implementation of a stack
"""

from linked_list import LinkedList
import unittest


class TestStack(unittest.TestCase):

    def test_1(self):
        N = 1000
        stack = Stack()
        for i in range(N):
            self.assertTrue(stack.push(i))
        for i in reversed(range(N)):
            self.assertEqual(i, stack.pop())
        for i in range(N):
            self.assertTrue(stack.push(i))
        for i in reversed(range(N)):
            self.assertEqual(i, stack.pop())


class Stack(LinkedList):
    """Implementation of a stack using linked list

        Note that in this implementation, the first element is a
        dummy element. This is apparantly required for this impplementation.
        Actually, you need a dummy element whenever you have an empty stack.
        Perhaps, this can be better designed

    """

    def __init__(self):
        super().__init__(None)

    def pop(self):
        """remove the last-added element"""
        first = self.next
        self.next = first.next
        return first.data

    push = LinkedList.linsert


if __name__ == "__main__":
    unittest.main()
