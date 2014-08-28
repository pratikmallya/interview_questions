"""
The infamous binary search algorithm. This is my go at it.
"""
import unittest
from random import sample


class TestAlg(unittest.TestCase):
    def test_case_1(self):
        arr = list(range(100))
        for i, item in enumerate(arr):
            self.assertEqual(
                binsearch(arr, item), i
                )

    def test_case_2(self):
        maxrange = 100000
        arr = sample(range(maxrange), int(maxrange/10))
        arr.sort()
        for i, item in enumerate(arr):
            self.assertEqual(
                binsearch(arr, item), i
            )


def binsearch(array, item, imin=None, imax=None):
    if not imin:
        imin = 0

    if not imax:
        imax = len(array)

    if imin > imax:
        return -1
    else:
        mid = int((imin + imax)/2)
        if item > array[mid]:
            return binsearch(array, item, imin=mid, imax=imax)
        elif item < array[mid]:
            return binsearch(array, item, imin=imin, imax=mid)
        else:
            return mid

if __name__ == "__main__":
    unittest.main()
