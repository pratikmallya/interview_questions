"""
An implementation of quick find data structure to find the connected
components in a forest
"""

import unittest


class QuickFind:

    def __init__(self, N):
        """Initialize QF data structure"""
        self.data = list(range(N))

    def union(self, x, y):
        """union the sets to which x and y belong.

        Finds all elements in the data array and set it to the value in
        data[y]. Note that always setting the value of data[x] to data[y]
        allows us to maintain consistency and without this, the algorithm
        would not work

        Args:
            x, y: objects to be union-ed

        Returns:
            A data structure that has x,y belong to the same set

        """
        for index, elem in enumerate(self.data):
            if elem == self.data[x]:
                self.data[index] = self.data[y]

    def connected(self, x, y):
        """Returns true iff x and y beling to the same connected component"""
        if self.data[x] == self.data[y]:
            return True
        else:
            return False


class TestAlg(unittest.TestCase):

    def test_1(self):
        N = 10
        uf = QuickFind(N)
        uf.union(0, 5)
        self.assertTrue(uf.connected(0, 5))
        self.assertFalse(uf.connected(0, 1))
        uf.union(5,6)
        self.assertTrue(uf.connected(0, 6))
        self.assertTrue(uf.connected(5, 6))




if __name__ == "__main__":
    unittest.main()
