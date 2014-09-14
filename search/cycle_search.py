"""
Find all cycles in the given input digraph
* one node points at 1 or less other node
* N not large enough to overflow set(range(N))

"""

import sys
import unittest


class TestNumCycles(unittest.TestCase):

    def test_sanity(self):
        N = 7
        nodes = [2, 3, 4, 5, 6, -1, 0]
        graph = {}
        for i, item in enumerate(nodes):
            graph[i] = item
        self.assertEqual(num_cycles(graph, N), 1)

    def test_simple_large_graphs(self):
        N = 3000

        graph = {}
        for i in range(N):
            graph[i] = i
        self.assertEqual(num_cycles(graph, N), N)

        for i in range(N-1):
            graph[i] = i+1
        graph[N-1] = 0

        self.assertEqual(num_cycles(graph, N), 1)

        graph[int(N/3)] = 0
        graph[2*int(N/3)] = int(N/3) + 1
        graph[N-1] = 2*int(N/3) + 1

        self.assertEqual(num_cycles(graph, N), 3)

    def test_border_cases(self):
        self.assertRaises(KeyError, num_cycles, {}, 100)


def main():
    with open(sys.argv[1], 'r') as o:

        while True:

            N = o.readline()
            if N == '':
                # reached EOF
                break

            graph = {}

            for i in range(int(N)):
                graph[i] = int(o.readline())

            sys.stdout.write("{}\n".format(num_cycles(graph, int(N))))


def num_cycles(graph, N):
    """Return the number of cycles in the graph"""

    nodes = set(range(N))
    num_cycles = 0

    while nodes:
        start = nodes.pop()
        node = start

        while True:
            next = graph[node]
            nodes.discard(next)

            if next == -1:
                break
            elif next == start:
                num_cycles += 1
                break
            else:
                node = next

    return num_cycles

if __name__ == "__main__":
    unittest.main()
