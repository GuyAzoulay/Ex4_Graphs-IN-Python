import math
import _tkinter
from _tkinter import *
from typing import List

from IPython.utils.timing import clock
from future.moves import tkinter
from future.moves.tkinter import simpledialog,messagebox
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
import json
from queue import PriorityQueue
import pygame
from pygame import Color, display, gfxdraw, font
from pygame.constants import RESIZABLE

WIDTH, HEIGHT = 1080, 720
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20, bold=True)

def scale(data, min_screen, max_screen, min_data, max_data):
    return int(((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen)
def draw_arrow(color, start, end):
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    pygame.draw.polygon(screen, color, (
        (end[0] + 10 * math.sin(math.radians(rotation)), end[1] + 10 * math.cos(math.radians(rotation))),
        (end[0] + 10 * math.sin(math.radians(rotation - 120)), end[1] + 10 * math.cos(math.radians(rotation - 120))),
        (end[0] + 10 * math.sin(math.radians(rotation + 120)), end[1] + 10 * math.cos(math.radians(rotation + 120)))))

# in this class we implement known algorithms  using the graph
# structure we built earlier
class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.graph = DiGraph() if graph is None else graph

    # get graph is function which return us the graph we work on
    def get_graph(self) -> GraphInterface:
        return self.graph

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
            for key in self.graph.edges.keys():
                temp_Edge_Dict = {'src': key[0], 'w': self.graph.edges[key], 'dest': key[1]}
                ans["Edges"].append(temp_Edge_Dict)
            json.dump(ans, fp=f, indent=2)
            return True
        # Here we are saving the graph in json file format, we going through all the nodes and it
        # variables, and Edges and it variables and save it in a new file format

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
    # we doing it using the Dijksta algorithm and priority queue,
    # at first we update all the nodes "weight" to infinity except the first one,
    # than we ran on all the other nodes and mark every node if we visit in or not,
    # also we update the previous node we walk from, in ain to return the path we walk in

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        currect_paths = []
        if len(node_lst) == 0:
            return ([], -1)
        all_Paths = [[]]
        weight_list = []
        for i in node_lst:
            for j in node_lst:
                if i == j:
                    continue
                all_Paths.append(self.shortest_path(i, j)[1])
        for list1 in all_Paths:
            if len(list1) == 0: continue
            res = list1.__contains__(node_lst)
            if res:
                currect_paths.append(list1)
            else:
                for list2 in all_Paths:
                    if len(list2) == 0: continue
                    if list1[-1] == list2[0] and list1[0] != list2[-1]:
                        currect_paths.append(list1[0:len(list1) - 1] + list2)

        for currect in currect_paths:
            weight_list.append((currect, self.weight_calc(currect)))

        return min(weight_list, key=lambda lst: lst[1])
        # the known problem; TSP, Travel SalesMan Problem, here we are given a list of city and we
        # need to find the shortest path which go through all this cities and the weight of this
        # path, we doing it thanks to the Dijkstra algorithm, we ran on every node in the city
        # list and put the shortest path between every two in a temp list.
        # than we are checking if there is a path that contain all the cities that is given to us
        # and put that list in a list that contain all the paths that contain the cities inside
        # if we didnt find one like this we merge between two lists that the last value in one list is the first
        # of the other list and the first one of the same list is not equal to the last one of the second list,
        # we are doing it in aim to not create a circle path, that we are returning the path with the min weight
        # using a help function that calculate the total path.

    def weight_calc(self, list):
        weight = 0
        for i in list:
            e = (i, i + 1)
            if e in self.graph.edges.keys():
                weight += self.graph.edges[e]
            else:
                continue
        return weight

    # a function that help me to calculate the weight of each list

    def centerPoint(self) -> (int, float):
        if not self.isConnected(self.graph):
            return (-1,float('inf'))
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

    # the center function return us the node that is the center of the graph,
    # we doing it like this: for every node we are measuring the shortest path from the whole
    # other nodes and take the max from it, after we did it to the whole other nodes we
    # return the min between all the max.
    # of course that in the beginning we check that the graph is strongly connected

    def plot_graph(self) -> None:
        min_x = min(self.graph.nodes.values(), key=lambda pos_x: pos_x[0])[0]
        min_y = min(self.graph.nodes.values(), key=lambda pos_y: pos_y[1])[1]
        max_x = max(self.graph.nodes.values(), key=lambda pos_x: pos_x[0])[0]
        max_y = max(self.graph.nodes.values(), key=lambda pos_y: pos_y[1])[1]
        running = True
        isCenter = []
        tsp = []
        while running:
            click = False
            screen.fill(Color(100, 100, 100))
            # Drawing the nodes
            scaled_x = {}
            scaled_y = {}
            for id, n in self.graph.nodes.items():
                x = scale(n[0], 50, screen.get_width() - 50, min_x, max_x)
                y = scale(n[1], 50, screen.get_height() - 50, min_y, max_y)
                scaled_x[id] = x
                scaled_y[id] = y
                gfxdraw.filled_circle(screen, x, y, 10, Color(120, 69, 42))
                gfxdraw.aacircle(screen, x, y, 10, Color(255, 255, 255))
                if isCenter == id:
                    gfxdraw.filled_circle(screen, x, y, 10, Color(0, 0, 0))
                if len(tsp) != 0 and id in tsp:
                    gfxdraw.filled_circle(screen, x, y, 10, Color(0, 255, 0))
                id_srf = FONT.render(str(id), True, pygame.Color(255, 255, 255))
                rect = id_srf.get_rect(center=(x, y))
                screen.blit(id_srf, rect)

            # Drawing the edges
            for e in self.graph.edges.keys():
                src_x = scale(self.graph.nodes[e[0]][0], 50, screen.get_width() - 50, min_x, max_x)
                src_y = scale(self.graph.nodes[e[0]][1], 50, screen.get_height() - 50, min_y, max_y)
                dest_x = scale(self.graph.nodes[e[1]][0], 50, screen.get_width() - 50, min_x, max_x)
                dest_y = scale(self.graph.nodes[e[1]][1], 50, screen.get_height() - 50, min_y, max_y)
                pygame.draw.line(screen, Color(61, 72, 126),
                                 (src_x, src_y), (dest_x, dest_y), width=2)
                draw_arrow("black", [src_x, src_y], [(src_x + dest_x) / 2, (src_y + dest_y) / 2])

            # Drawing the shortest path(tsp or shortestPath)
            for i in range(len(tsp) - 1):
                src_x = scale(self.graph.nodes[tsp[i]][0], 50, screen.get_width() - 50, min_x, max_x)
                src_y = scale(self.graph.nodes[tsp[i]][1], 50, screen.get_height() - 50, min_y, max_y)
                dest_x = scale(self.graph.nodes[tsp[i + 1]][0], 50, screen.get_width() - 50, min_x, max_x)
                dest_y = scale(self.graph.nodes[tsp[i + 1]][1], 50, screen.get_height() - 50, min_y, max_y)
                pygame.draw.line(screen, Color(0, 255, 0),
                                 (src_x, src_y), (dest_x, dest_y), width=2)
                draw_arrow("white", [src_x, src_y], [(src_x + dest_x) / 2, (src_y + dest_y) / 2])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    click = True
                    print(pygame.mouse.get_pos())
                    for i in range(len(scaled_y)):
                        if (scaled_y[i] + 10 > pygame.mouse.get_pos()[1] > scaled_y[i] - 10) and \
                                (scaled_x[i] + 10 > pygame.mouse.get_pos()[0] > scaled_x[i] - 10):
                            print()

            button1 = pygame.Rect(0, 0, 60, 45)
            pygame.draw.rect(screen, (52, 235, 177), button1, border_radius=10)
            font1 = pygame.font.SysFont("Grobold", 20)
            screen.blit((font1.render('Center', True, (255, 255, 255))), (10, 15))
            button2 = pygame.Rect(65, 0, 60, 45)
            pygame.draw.rect(screen, (52, 235, 177), button2, border_radius=10)
            screen.blit((font1.render('TSP', True, (255, 255, 255))), (75, 15))
            button3 = pygame.Rect(130, 0, 60, 45)
            pygame.draw.rect(screen, (52, 235, 177), button3, border_radius=10)
            screen.blit((font1.render('Shortest Path', True, (255, 255, 255))), (140, 15))
            button4 = pygame.Rect(195, 0, 60, 45)
            pygame.draw.rect(screen, (52, 235, 177), button4, border_radius=10)
            screen.blit((font1.render('Refresh', True, (255, 255, 255))), (205, 15))

            if click:
                pos = pygame.mouse.get_pos()
                if button1.collidepoint(pos):
                    center = self.centerPoint()
                    isCenter = center[0]
                elif button2.collidepoint(pos):
                    ROOT = tkinter.Tk()
                    ROOT.withdraw()
                    cities = simpledialog.askstring(title="TSP",
                                                    prompt="Enter city Id's and space between each city")
                    cities = cities.split()
                    for i in range(len(cities)):
                        cities[i] = int(cities[i])
                    tsp = self.TSP(cities)
                    tkinter.messagebox.showinfo("Length Of Path", tsp[1])
                    tsp = tsp[0]
                elif button3.collidepoint(pos):
                    ROOT = tkinter.Tk()
                    ROOT.withdraw()
                    src = simpledialog.askstring(title="Shortest Path",
                                                 prompt="Source")
                    dest = simpledialog.askstring(title="Shortest Path",
                                                  prompt=["Destination"])
                    tsp = self.shortest_path(int(src), int(dest))
                    print(tsp)
                    tkinter.messagebox.showinfo("Length Of Path", tsp[0])
                    tsp = tsp[1]
                elif button4.collidepoint(pos):
                    isCenter = []
                    tsp = []
            display.update()
            clock.tick(60)



    def isConnected(self, g):

        for nodeid in self.graph.get_all_v().keys():
            visit = [False] * self.graph.v_size()
            self.DFS(g, nodeid, visit)
            for x in visit:
                if not x:
                    return False
        return True

    # checking if a graph is strongly connected for the center function, we doing it
    # using the DFS algorithm

    def DFS(self, graph, nodeid, visit):
        visit[nodeid] = True

        for e in self.graph.all_out_edges_of_node(nodeid):
            if not visit[e[1]]:
                self.DFS(graph, e[1], visit)


if __name__ == '__main__':
    galgo = GraphAlgo()
    galgo.load_from_json("A0.json")
    # galgo.save_to_json("new.json")
    # for x in a:
    #     print(x)
    # print(galgo.shortest_path(0, 1))
    # print(galgo.isConnected(g))
    # print((galgo.centerPoint()))
    # print(galgo.graph.get_all_v())
    g = galgo.graph
    #print(galgo.graph)
    galgo.plot_graph()
    #print(galgo.TSP([0,1,6]))
# print(galgo.centerPoint())
#  e = g.edges
# galgo.plot_graph()
