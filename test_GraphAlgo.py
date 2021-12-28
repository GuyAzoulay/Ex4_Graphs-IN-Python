from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):
    graph_A0 =DiGraph()
    galgo_A0 = GraphAlgo(graph_A0)
    galgo_A1 = GraphAlgo(graph_A0)
    galgo_A2 = GraphAlgo(graph_A0)
    galgo_1000n = GraphAlgo(graph_A0)
    galgo_A5 = GraphAlgo(graph_A0)
    galgo_1000n.load_from_json("1000Nodes.json")
    galgo_A0.load_from_json("A0.json")
    galgo_A0.load_from_json("A1.json")
    galgo_A0.load_from_json("A2.json")
    galgo_A5.load_from_json("A5.json")


    def test_load_from_json_A0(self):
        self.assertTrue(self.galgo_A0.load_from_json("A0.json"))

    def test_save_to_json_A0(self):
        self.assertTrue(self.galgo_A0.save_to_json("testG.json"))

    def test_shortest_path_A0(self):
        self.assertEqual(self.galgo_A0.shortest_path(0,6),(6.670946327534079, [0, 10, 9, 8, 7, 6]))
        self.assertEqual(self.galgo_A0.shortest_path(0,8),(4.008297880877075, [0, 10, 9, 8]))

    def test_tsp_A0(self):
        self.assertEqual(self.galgo_A0.TSP([0,5,6]),([0, 10, 9, 8, 7, 6, 5], 8.188180635656211))

    def test_center_point_A0(self):
        self.assertEqual(self.galgo_A0.centerPoint(),(7, 6.806805834715163))


    def test_load_from_json_A1(self):
        self.galgo_A1.save_to_json("testing.json")
        self.assertTrue(self.galgo_A1.load_from_json("testing.json"))

    def test_save_to_json_A1(self):
        self.assertTrue(self.galgo_A1.save_to_json("testG_A2.json"))

    def test_shortest_path_A1(self):
        self.assertEqual(self.galgo_A1.shortest_path(0,6),(4.827508242889207, [0, 1, 2, 6]))
        self.assertEqual(self.galgo_A1.shortest_path(0,8),(3.5127618139337136, [0, 1, 26, 8]))

    def test_tsp_A1(self):
        self.assertEqual(self.galgo_A1.TSP([0,5,7]),([0, 1, 26, 8, 7, 6, 5], 8.910100578669805))

    def test_center_point_A1(self):
        self.assertEqual(self.galgo_A1.centerPoint(),(1, 7.699910325475899))

    def test_load_from_json_A2(self):
        self.assertTrue(self.galgo_A2.load_from_json("A2.json"))

    def test_save_to_json_A2(self):
        self.galgo_A2.save_to_json("A2_test")
        self.assertTrue(self.galgo_A1.load_from_json("A2_test.json"))

    def test_shortest_path_A2(self):
        self.assertEqual(self.galgo_A2.shortest_path(6, 7), (1.237565124536135, [6, 7]))
        self.assertEqual(self.galgo_A2.shortest_path(0, 20), (4.19127715881604, [0, 10, 11, 20]))


    def test_tsp_A2(self):
        self.assertEqual(self.galgo_A2.TSP([0,7,8,9,15]), ([0, 1, 26, 8, 7, 6, 5], 8.910100578669805))

    def test_center_point_A2(self):
        self.assertEqual(self.galgo_A2.centerPoint(), (1, 7.699910325475899))


    def test_load_from_json_A1(self):
        self.galgo_A1.save_to_json("testing.json")
        self.assertTrue(self.galgo_A1.load_from_json("testing.json"))

    def test_save_to_json_A1(self):
        self.assertTrue(self.galgo_A1.save_to_json("testG_A2.json"))

    def test_shortest_path_A1(self):
        self.assertEqual(self.galgo_A1.shortest_path(0,6),(4.827508242889207, [0, 1, 2, 6]))
        self.assertEqual(self.galgo_A1.shortest_path(0,8),(3.5127618139337136, [0, 1, 26, 8]))

    def test_tsp_A1(self):
        self.assertEqual(self.galgo_A1.TSP([0,5,7]),([0, 1, 26, 8, 7, 6, 5], 8.910100578669805))

    def test_center_point_A1(self):
        self.assertEqual(self.galgo_A1.centerPoint(),(1, 7.699910325475899))


    def test_shortest_path_A1000(self):
       self.assertEqual(self.galgo_1000n.shortest_path(0,57),(1283.1952774536992, [0, 10, 9, 100, 114, 57]))
       self.assertEqual(self.galgo_1000n.TSP([1,3,99]),([1, 2, 3, 2, 79, 99], 5.181854933001607))

    def test_A5_center(self):
        tr = self.galgo_A5.centerPoint()
        self.assertEqual(tr,(40, 9.291743173960954))
