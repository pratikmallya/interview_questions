"""
Merge Sort
Invented by John Von Neumann:
http://en.wikipedia.org/wiki/Merge_sort

"""
import unittest
from random import sample


class TestMergeSort(unittest.TestCase):

    def test_1(self):
        N = 1000
        v = list(reversed(range(N)))
        self.assertEqual(mergesort(v), list(range(N)))
        v = sample(range(10000000), N)
        vsort = v
        vsort.sort()
        self.assertEqual(vsort, mergesort(v))
        self.assertEqual([], mergesort([]))
        self.assertEqual([10], mergesort([10]))


def mergesort(A):
    """sort elements of list using merge sort"""

    if len(A) <= 1:
        return A
    else:
        mid = int(len(A)/2)
        return merge(mergesort(A[:mid]), mergesort(A[mid:]))


def merge(a, b):
    """merge 2 sorted lists a and b"""
    res = []
    while a and b:
        if a[0] < b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    while a:
        res.append(a.pop(0))
    while b:
        res.append(b.pop(0))

    return res


if __name__ == "__main__":
    unittest.main()
