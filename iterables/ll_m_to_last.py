"""
This is the awesome problem where you have to find the m-th to last
element in the linked list. The solution is simple: use 2 pointers
separated by m steps

"""

from linked_list import LinkedList
import unittest


class TestAlg(unittest.TestCase):

    def test_1(self):

        N = 10
        ll = LinkedList(range(N))

        for i in range(N):
            self.assertEqual(find_mth_last(ll, i), N-1-i)



def find_mth_last(ll, m):
    """return m-th to last element"""
    head = ll
    for i in range(m):
        try:
            head = head.next
        except AttributeError:
            return None

    mhead = ll
    while head.next:
        head = head.next
        mhead = mhead.next

    return mhead.data


if __name__ == "__main__":
    unittest.main()