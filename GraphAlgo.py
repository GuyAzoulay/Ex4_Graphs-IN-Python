from DiGraph import DiGraph
from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
import json
from queue import PriorityQueue
import matplotlib.pyplot as plt
import matplotlib.widgets as wgt
from matplotlib.widgets import Button
import numpy as np
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.graph = DiGraph() if graph is None else graph


    def get_graph(self) -> GraphInterface:
        return self.graph
    #getting the graph information

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as f:
                graph_Loaded = json.load(f)
            if 'pos' in graph_Loaded['Nodes'][0]:
                for node in graph_Loaded['Nodes']:
                    self.graph.nodes[node['id']] = tuple((float(n) for n in node["pos"].split(',')))
            else:
                for node in graph_Loaded['Nodes']:
                    self.graph.nodes[node['id']] = None
            for edge in graph_Loaded['Edges']:
                self.graph.edges[(edge['src'], edge['dest'])] = edge['w']
            return True
        except IOError as e:
            print(e)
            return False
        # here we load a graph from a json file, because that in the given graphs there are
        # nodes with position that equal to None, we had to fix that problem too


    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, "w") as f:
            tempdict = {}
            ans = {"Edges": [], "Nodes": []}
            for pos in self.graph.nodes.values():
                if pos is not None:
                    for key in self.graph.nodes.keys():
                        tempdict = {
                            'pos': f"{self.graph.nodes[key][0]},{self.graph.nodes[key][1]},{self.graph.nodes[key][2]}",
                            'id': key}
                        ans["Nodes"].append(tempdict)
                # else:
                #   tempdict={'pos':None,'id':self.graph.nodes.values().-}
            for key in self.graph.edges.keys():
                temp_Edge_Dict = {'src': key[0], 'w': self.graph.edges[key], 'dest': key[1]}
                ans["Edges"].append(temp_Edge_Dict)
            json.dump(ans, fp=f, indent=2)
            return True
        # Here we are saving the graph in json file format




    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dict = {node: float('inf') for node in range(self.graph.v_size())}
        visit = []
        prevNode = {}
        shortestPath = []
        dict[id1] = 0
        pq = PriorityQueue()
        pq.put((0, id1))
        thereIsPath = False

        while not pq.empty():
            (distance, index) = pq.get()
            if (index == id2):
                thereIsPath = True
                break
            visit.append((index))
            for nodeN in self.graph.all_out_edges_of_node(index):
                weight = self.graph.edges[nodeN]
                if nodeN[1] not in visit:
                    cost = dict[nodeN[1]]
                    newCost = dict[index] + weight
                    if newCost < cost:
                        pq.put((newCost, nodeN[1]))
                        dict[nodeN[1]] = newCost
                        prevNode[nodeN[1]] = index
        if thereIsPath:
            temp = id2
            shortestPath.append(temp)
            while True:
                prev = prevNode.get(temp)
                if prev is None:
                    break
                shortestPath.append(prev)
                temp = prev
            shortestPath.reverse()
        return (dict.get(id2), shortestPath)

    # in this function we measure the shortest path between 2 nodes id
    # we doing it using the Dijksta algorithm and priority queue

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        currect_paths = []
        if len(node_lst) == 0:
            return ([], -1)
        all_Paths = [[]]
        weight_list = [()]
        for i in node_lst:
            for j in node_lst:
                if i == j:
                    continue
                all_Paths[i] = self.shortest_path(i, j)[1]
        for list1 in all_Paths:
            res = list1.__contains__(node_lst)
            if res:
                currect_paths.append(list1)
            else:
                for list2 in all_Paths:
                    if list1[-1] == list2[0] and list1[0] != list2[-1]:
                        currect_paths.append(list1[0:-2] + list2)
        for currect in currect_paths:
            weight_list.append(currect, self.weight_calc(currect))

        return min(weight_list[1])

    def weight_calc(self, list):
        weight = 0
        for i in list:
            e = (i, i + 1)
            weight += self.graph.edges[e]
        return weight

    def centerPoint(self) -> (int, float):
        if not self.isConnected(self.graph):
            return None
        dict = {}
        for node1 in self.graph.nodes.keys():
            temp_dict = {}
            for node2 in self.graph.nodes.keys():
                if (node1 != node2):
                    weight = self.shortest_path(node1, node2)[0]
                    temp_dict[(node1, node2)] = weight
            dict[node1] = max(temp_dict.values())
        i = min(dict.values())
        key_list = list(dict.keys())
        value_list = list(dict.values())
        t = value_list.index(i)
        return t, i

    def plot_graph(self) -> None:

        nodes = self.graph.nodes
        edges = self.graph.edges
        ids, x, y = [], [], []
        # z=[]
        for k, v in nodes.items():
            ids.append(k)
            if v != None:
                x.append(v[0])
                y.append(v[1])
            else:
                if k <= 2:
                    x.append(5 * k)
                    y.append(4 * k)
                else:
                    b = random.random()
                    c = random.random()
                    x.append(k * k * b)
                    y.append(k * k * c)

        fig = plt.figure()
        ax = fig.subplots()
        plt.subplots_adjust(bottom=0.4)
        p, = ax.plot(x, y, color="black", marker="o")
        fig.set_size_inches(17.5, 7.5, forward=True)
        ax.scatter(x, y, c='red')

        for i, txt in enumerate(ids):
            ax.annotate(txt, (x[i], y[i]), color='red')

        for src, dest in edges.keys():
            if nodes[src] != None and nodes[dest] != None:
                _x, _y, _ = nodes[src]
                _dx, _dy, _ = np.array(nodes[dest]) - np.array(nodes[src])
                r = 0.2
                x, y = _x + r * _dx, _y + r * _dy
                dx, dy = (1 - r) * _dx, (1 - r) * _dy
                plt.arrow(x, y, dx, dy, width=5e-5, length_includes_head=True)
            else:
                plt.arrow(x[src], y[src], x[dest], y[dest], width=5e-5, length_includes_head=True)

        def add_edge(id1, id2):
            if nodes.keys().__contains__(id1) and nodes.keys().__contains__(id2):
                x, y, _ = nodes[id1]
                dx, dy, _ = nodes[id2]
                ax.plot(x, y, color="blue")

        # axes =plt.axes([0.06, 0.05, 0.15, 0.075])
        # edge_button= Button(axes,'ADD EDGE',color= "blue")
        # edge_button.on_clicked(add_edge(1,10))

        plt.show()

    def isConnected(self, g):
        for nodeid in self.graph.get_all_v().keys():
            visit = [False] * self.graph.v_size()
            self.DFS(g, nodeid, visit)
            for x in visit:
                if not x:
                    return False
        return True

    def DFS(self, graph, nodeid, visit):
        visit[nodeid] = True
        for e in self.graph.all_out_edges_of_node(nodeid):
            if not visit[e[1]]:
                self.DFS(graph, e[1], visit)


if __name__ == '__main__':
    galgo = GraphAlgo()
    a = {1: 2, 3: 4}
    galgo.load_from_json("A0.json")
    # galgo.save_to_json("new.json")
    # for x in a:
    #     print(x)
    # print(galgo.shortest_path(0, 1))
    # print(galgo.isConnected(g))
    # print((galgo.centerPoint()))
    # print(galgo.graph.get_all_v())
    g = galgo.graph
    print(g)
    e = g.edges
    galgo.plot_graph()
