import unittest

from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = DiGraph()
        graph.add_node(0, (0, 1, 0))
        graph.add_node(1, (2, 1, 0))
        graph.add_node(2, (1.2, 1.6, 0))
        graph.add_node(3, (1, 1.9, 0))
        graph.add_node(4, (0.5, 1.4, 0))
        graph.add_node(5, (0.8, 1.2, 0))
        graph.add_node(6, (2, 0.5, 0))
        graph.add_edge(0, 1, 0.5525)
        graph.add_edge(0, 2, 1.025)
        graph.add_edge(0, 3, 4.825)
        graph.add_edge(2, 6, 2.725)
        graph.add_edge(4, 3, 1.005)

        nodes = graph.get_all_v()
        t = True
        for x in graph.nodes.keys():
            if nodes[x] != graph.nodes[x]:
                t = False
        self.assertTrue(t)

        edgesout = graph.all_out_edges_of_node(0)
        self.assertEqual(graph.edges[(0,1)],edgesout[(0,1)])
        self.assertEqual(graph.all_out_edges_of_node(0).items(),edgesout.items())
        #test all out edges

        edgesin = graph.all_in_edges_of_node(3)
        self.assertEqual(graph.edges[(0,3)],edgesin[(0,3)])
        self.assertEqual(graph.all_in_edges_of_node(3).items(),edgesin.items())
        #test all in edges

        self.assertEqual(graph.v_size(),7) # test nodes size
        self.assertEqual(graph.e_size(),5) # test edges size

        te = graph.remove_edge(0,1)
        self.assertTrue(te)
        te = graph.remove_node(3)
        self.assertTrue(te)



if __name__ == '__main__':
    unittest.main()
