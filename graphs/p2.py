# implement BFS and DFS on a random graph

# DFS: visit neighbor of neighbor, then visit other neighbors
# BFS: visit all neighbors, then visit their neighbors

# note that we are implementing these strategies on graphs and not
# trees (although all trees are graphs). Which means that you might reach
# the same node twice, so you need to handle that


import unittest

class Graph(object):
    """"Global class that reprents entire graph."""

    def __init__(self, adjacency_list):
        """Initializes the graph.

        Attributes:
            adjacency_list: dictionary with adjacency list used
                            to create Graph
        """
        self._graph = self._construct_graph(adjacency_list)

    def _construct_graph(self, adjacency_list):
        """Constructs the graph.

            Attributes:
                adjacency_list: adjacency list used to create Graph

            Returns:
                graph object
        """
        _adjacency_list = {}
        for idn, listn in adjacency_list.items():
            _adjacency_list[idn] = {'neighbors': listn, 'visited': False}

        return _adjacency_list

    def get_node(self, node_id):
        """"returns the object for node_id."""
        return self._graph[node_id]

    def get_ids(self):
        """return an iterator over all the ids"""
        return self._graph.keys()

    def add_nodes(self, nodes):
        """"add the nodes"""
        for idn, listn in nodes.items():
            self._graph[idn] = {'neighbors': listn, 'visited': False}





class TestGraphAlgos(unittest.TestCase):

    def setUp(self):
        """construct a graph

                       1
                    /      \
                   2        3-----
                  /| \     / \    \
                 4 -5  6- 7 - 8----13
                /\    /\
               9  10 11 12
        """
        self._adjacency_list = {
        '1': ['2', '3'],
        '2': ['1', '4', '5', '6'],
        '3': ['1', '7', '8'],
        '4': ['2', '5', '9', '10'],
        '5': ['2', '4'],
        '6': ['2', '7', '11', '12'],
        '7': ['3', '6', '8'],
        '8': ['3', '7'],
        '9': ['4'],
        '10': ['4'],
        '11': ['6'],
        '12': ['6']
        } 
        self.graph = Graph(self._adjacency_list)

    def test_graphNode(self):
        """test GraphNode methods"""
        # test if Graph has been correctly constructed
        for key in self.graph.get_ids():
            node = self.graph.get_node(key)
            self.assertFalse(node['visited'])
            self.assertEqual(node['neighbors'], self._adjacency_list[key])

        # test if node can be added correctly
        node = {'13': ['3', '8']}
        self.graph.add_nodes(node)
        node13 = self.graph.get_node('13')
        self.assertFalse(node13['visited'])
        self.assertEqual(node13['neighbors'], node['13'])



if __name__=='__main__':
    unittest.main()