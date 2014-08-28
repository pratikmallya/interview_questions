"""
The infamous binary search algorithm.
I cheated and took a look at the wikipedia page here:
http://en.wikipedia.org/wiki/Binary_search_algorithm

"""
import unittest
from random import sample


class TestAlg(unittest.TestCase):
    def test_case_1(self):
        maxrange = 10000
        arr = list(range(maxrange))
        for i, item in enumerate(arr):
            self.assertEqual(
                binsearch(arr, item), i
                )
        maxrange = 5000
        arr = list(range(maxrange))
        self.assertEqual(
            binsearch(arr, maxrange+10), -1
            )

    def test_case_2(self):
        maxrange = 100000
        arr = sample(range(maxrange), int(maxrange/10))
        arr.sort()
        for i, item in enumerate(arr):
            self.assertEqual(
                binsearch(arr, item), i
            )

    def test_corner_cases(self):
        self.assertEqual(binsearch([], 20), -1)
        self.assertEqual(binsearch([10], 20), -1)
        self.assertEqual(binsearch([10], 10), 0)
        self.assertEqual(binsearch([10, 20], 10), 0)
        self.assertEqual(binsearch([10, 20], 20), 1)


def binsearch(array, item, imin=None, imax=None):
    if imin is None:
        imin = 0

    if imax is None:
        imax = len(array)-1

    if imin > imax:
        return -1
    else:
        mid = int((imin + imax)/2)
        if item > array[mid]:
            return binsearch(array, item, imin=mid+1, imax=imax)
        elif item < array[mid]:
            return binsearch(array, item, imin=imin, imax=mid-1)
        else:
            return mid


if __name__ == "__main__":
    unittest.main()
