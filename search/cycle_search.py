"""
Find all cycles in the given input digraph
* one node points at 1 or less other node
* N not large enough to overflow set(range(N))

"""

import sys


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
    main()
