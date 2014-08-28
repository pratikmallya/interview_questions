"""
Insertion Sort

Pick lowest element, push it to the front of the list
This will be an in-place sort. Why? Because that's a little
more complicated.

"""

import unittest
from random import sample
from copy import deepcopy

class TestAlg(unittest.TestCase):
    def test_case_1(self):
        v = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(v)
        self.assertEqual(v, list(range(1,11)))

        maxlen = 10000
        v1 = sample(range(maxlen), maxlen)
        v2 = deepcopy(v1)
        self.assertEqual(
            v1.sort(), insertion_sort(v2))


def insertion_sort(v):

    for i in range(1, len(v)):
        ind = find_ind(v[:i], v[i])
        insert_elem(v, i, ind)

def find_ind(v, elem):
    for i,item in enumerate(v):
        if elem < item:
            return i
    return i

def insert_elem(v, from_ind, to_ind):
    elem = v[from_ind]
    for i in reversed(range(to_ind+1, from_ind+1)):
        v[i] = v[i-1]
    v[to_ind] = elem


if __name__ == "__main__":
    unittest.main()
