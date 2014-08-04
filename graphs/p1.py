# find the lowest common ancestor given two nodes in a tree

# notice that they must have an ancestor, due to the nature of trees
# The easiest way to do this would be to simultaneously walk up both
# trees, one step at a time. This rapidly reduces the need to search.
# All you really have to do is to walk up and compare at every step;
# when you find that you are on the same node in both cases, you have
# the common ancestor
# Since its a tree we're talking about, it will simply take O(logn)
# time to get to its root, so the complexity is O(logn)

# There is a problem with the above approach, though. You are
# assuming that both the nodes are at the same level. What if one is
# the ancestor of the other? Or in general, at any different level?

# I think the best way here is to simply walk up the tree till the
# root node and diff the list of ancestors. The walks will take O(logn)
# steps and the diff, done on a list of size O(logn) will also be
# O(logn) (Note: `n` here is the no. of nodes in the tree)

import unittest
import functools


class Node(object):
    """Represents a node in a tree.
    """
    def __init__(self, uid, parent, data=None):
        """Initializes node.

        Args:
            parent: parent node
            data: data to be stored in the node

        Returns:
            A new node object
        """
        self.uid = uid
        self.parent = parent
        if parent is not None:
            parent.children.append(self)
        self.data = data
        self.children = []

    def get_children(self):
        """Returns an iterator over the children list."""
        for node in self.children:
            yield node


def get_common_ancestor(nodes):
    """find the common ancestor of nodes.

    Args:
        nodes: nodes whose ancestor has to be found

    Returns:
        common ancestor

    """
    nodesp = [get_all_ancestors(node) for node in nodes]
    common_line = functools.reduce(get_common_ancestor_two, nodesp)
    return common_line[0]


def get_common_ancestor_two(nodep1, nodep2):
    """find the common ancestor of only two nodes, given a list of
    their ancestors."""

    if len(nodep2) > len(nodep1):
        nodep1, nodep2 = nodep2, nodep1
    nodep1 = nodep1[-len(nodep2):]

    for i in range(len(nodep1)):
        if nodep1[i] == nodep2[i]:
            return nodep1[i:]


def get_all_ancestors(node):

    if node.parent is not None:
        return [node.parent] + get_all_ancestors(node.parent)
    else:
        return []


class TestLCA(unittest.TestCase):

    def setUp(self):
        """Construct a tree.

                      1
                    /    \
                   2      3
                  /|\     /\
                 4 5  6  7  8
                /\    /\
               9  10 11 12
        """
        self.data = {
            "Jedi": ["Obi Wan Kenobi", "Mace Windoo"],
            "Sith": ["Count Dooku", "Chancellor Palpatine"]
            }
        self.node1 = Node('1', None, self.data)
        self.node2 = Node('2', self.node1)
        self.node3 = Node('3', self.node1)
        self.node4 = Node('4', self.node2)
        self.node5 = Node('5', self.node2)
        self.node6 = Node('6', self.node2)
        self.node7 = Node('7', self.node3)
        self.node8 = Node('8', self.node3)
        self.node9 = Node('9', self.node4)
        self.node10 = Node('10', self.node4)
        self.node11 = Node('11', self.node6)
        self.node12 = Node('12', self.node6)

    def test_node_object_init(self):
        """See if Node objects can be initialized with data."""
        self.assertEqual(self.node1.data, self.data)
        self.assertEqual(self.node7.children, [])
        self.assertEqual(
            self.node2.children,
            [self.node4, self.node5, self.node6])

    def test_node_get(self):
        """Test the get method of node."""

        node3_children = self.node3.get_children()
        self.assertEqual(next(node3_children), self.node7)
        self.assertEqual(next(node3_children), self.node8)

    def test_common_ancestor(self):
        """Test the common ancestor algorithm."""
        anc_node = get_common_ancestor([self.node9, self.node10, self.node11])
        self.assertEqual(anc_node, self.node2)
        anc_node = get_common_ancestor([self.node9, self.node10, self.node8])
        self.assertEqual(anc_node, self.node1)
        anc_node = get_common_ancestor([self.node9, self.node10, self.node5])
        self.assertEqual(anc_node, self.node2)
        anc_node = get_common_ancestor([self.node9, self.node9])
        self.assertEqual(anc_node, self.node4)


if __name__ == '__main__':
    unittest.main()
