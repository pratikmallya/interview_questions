"""
Insertion Sort

Pick lowest element, push it to the front of the list
This will be an in-place sort. Why? Because that's a little
more complicated.

"""

import unittest


class TestAlg(unittest.TestCase):
    def test_case_1(self):
        v = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(v)
        self.assertEqual(v, list(range(1,11)))


def insertion_sort(v):

    for i in range(len(v)):
        min_elem = min(v[i:])
        min_ind = v.index(min_elem)
        v[i], v[min_ind] = v[min_ind], v[i]


if __name__ == "__main__":
    unittest.main()
