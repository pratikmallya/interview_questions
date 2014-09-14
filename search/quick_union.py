"""
An implementation of quick find data structure to find the connected
components in a forest
"""

import unittest


class QuickUnion:
    """A QuickUnion data structure.

    Attributes:
        union: union the input objects
        connected: find if the input objects are connected
    """

    def __init__(self, N):
        """Initialize QF data structure"""
        self.data = list(range(N))
        self.weights = [1]*N

    def union(self, x, y):
        """union the sets to which x and y belong.


        Args:
            x, y: objects to be union-ed

        Returns:
            A data structure that has x, y belong to the same set

        """
        rootx = self.__find_root(x)
        rooty = self.__find_root(y)

        if self.weights[rootx] >= self.weights[rooty]:
            self.data[rooty] = rootx
            self.weights[rootx] += self.weights[rooty]
        else:
            self.data[rootx] = rooty
            self.weights[rooty] += self.weights[rooty]

    def connected(self, x, y):
        """Returns true iff x and y beling to the same connected component"""

        return self.__find_root(x) == self.__find_root(y)

    def __find_root(self, x):
        """Returns the root of the tree """
        index = x
        while self.data[index] != index:
            self.data[index] = self.data[self.data[index]]
            index = self.data[index]

        return index


class TestAlg(unittest.TestCase):

    def test_1(self):
        N = 10
        qu = QuickUnion(N)
        qu.union(0, 5)
        self.assertTrue(qu.connected(0, 5))
        self.assertFalse(qu.connected(0, 1))
        qu.union(5, 6)
        self.assertTrue(qu.connected(0, 6))
        self.assertTrue(qu.connected(5, 6))


if __name__ == "__main__":
    unittest.main()
