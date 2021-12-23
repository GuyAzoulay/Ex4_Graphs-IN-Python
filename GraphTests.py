import unittest
from DiGraph import DiGraph

class TestGraph(unittest.TestCase):
    def addNode(self):
        g = DiGraph()
        for i in range(5):
            g.add_node(i, None)
        print(g.nodes)
        #self.assertEqual(g.nodes[0], 0)





