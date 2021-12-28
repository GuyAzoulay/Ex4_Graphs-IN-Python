from unittest import TestCase
from DiGraph import DiGraph


class TestDiGraph(TestCase):
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
    def test_v_size(self):
        self.assertEqual(self.graph.v_size(), 7)

    def test_e_size(self):
        self.assertEqual(self.graph.e_size(),5)

    def test_get_all_v(self):
        nodes = self.graph.get_all_v()
        t = True
        for x in self.graph.nodes.keys():
            if nodes[x] != self.graph.nodes[x]:
                t = False
        self.assertTrue(t)

    def test_all_in_edges_of_node(self):
        edgesout = self.graph.all_out_edges_of_node(0)
        self.assertEqual(self.graph.edges[(0, 1)], edgesout[(0, 1)])
        self.assertEqual(self.graph.all_out_edges_of_node(0).items(), edgesout.items())

    def test_all_out_edges_of_node(self):
        edgesin = self.graph.all_out_edges_of_node(0)
        self.assertEqual(self.graph.edges[(0, 1)], edgesin[(0, 1)])
        self.assertEqual(self.graph.all_out_edges_of_node(0).items(), edgesin.items())


    def test_add_edge(self):
        t0 = self.graph.add_edge(0,5,4)
        t1 = self.graph.add_edge(0,6,2.22)
        t2 = self.graph.add_edge(1,3,3.22)
        t3 = self.graph.add_edge(2,6,4.22)
        t4 = self.graph.add_edge(6,4,5.22)
        self.assertTrue(t0)
        self.assertTrue(t1)
        self.assertTrue(t2)
        self.assertTrue(t3)
        self.assertTrue(t4)

    def test_add_node(self):
        t0 = self.graph.add_node(7,None)
        t1 = self.graph.add_node(8,None)
        t2 = self.graph.add_node(9,None)
        t3 = self.graph.add_node(10,None)
        t4 = self.graph.add_node(11,None)
        t5 = self.graph.add_node(12,None)
        self.assertTrue(t0)
        self.assertTrue(t1)
        self.assertTrue(t2)
        self.assertTrue(t3)
        self.assertTrue(t4)
        self.assertTrue(t5)

    def test_remove_node(self):
        t0 = self.graph.remove_node(0)
        self.assertTrue(t0)
        t1 = self.graph.remove_node(0)
        self.assertFalse(t1)
        t2 = self.graph.remove_node(22) # id that is not exist
        self.assertFalse(t2)

    def test_remove_edge(self):
        t0 = self.graph.remove_edge(0,1)
        self.assertTrue(t0)
        t1 = self.graph.remove_edge(6,2)
        self.assertFalse(t1)


