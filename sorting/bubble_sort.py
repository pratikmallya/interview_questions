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
        bubble_sort(v)
        self.assertEqual(v, list(range(1,11)))


def bubble_sort(v):

    for i in reversed(range(len(v))):
        for j in range(i):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]


if __name__ == "__main__":
    unittest.main()
