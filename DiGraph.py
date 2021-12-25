import json
from GraphInterface import *


# this class represent the node class, in it we have a unique id
# and the node position in the space as a tuple which will contain
# three values of x,y,z, in addition we jad a tag variable
# which will help us later in the algo part
# class Node:
#
#     def __init__(self, id: int, pos: tuple):
#         self.id = id
#         self.pos = pos
#         self.tag = 0
#
#     def __repr__(self):
#         return f"id = {self.id} pos = {self.pos}"
#

# this class represent an edge in the graph, in it we have
# three types of variables, one represent what is the node's id
# we started in, what is the node id destination, and the "weight"
# of this edge
# class Edge:
#
#     def __init__(self, src: Node, dest: Node, w: float):
#         self.src = src
#         self.dest = dest
#         self.w = w
#
#     def __repr__(self):
#         return f"src = {self.src} dest = {self.dest} weight = {self.w}"


# this class represent a Directed weighted graph,
# in this class the variables are dictionary of nodes, dict
# of edges, and two other dictionary which will held the edges that
# go into a specific node, and out from the specific node
class DiGraph(GraphInterface):

    def __init__(self, nodes=[], edges=[]):
        # for every node's id we held his position using is id
        # in this wat it might help us later when we will draw our graph
        self.nodes = {}
        for node in nodes:
            self.nodes[node['id']] = tuple((float(n) for n in node['pos'].split(',')))
        # in aim to help our self, every edge is represented as a tuple, when in the
        # '0' place is the src, and in the '1' place is dest, and for every tuple
        # we update the weight
        self.edges = {}
        for edge in edges:
            self.edges[(edge['src'], edge['dest'])] = edge['w']
        self.mc = 0

    # return the number of nodes
    def v_size(self) -> int:
        return len(self.nodes)

    # return the number of edges
    def e_size(self) -> int:
        return len(self.edges)

    # return a dict with all the nodes inside
    def get_all_v(self) -> dict:
        return self.nodes

    # return a dict of all the edges into a specific node
    #
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._all_out(id1, 1)

    # return a dict of all the edges which go out from a node
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._all_out(id1, 0)
    # this function will help us to fill our dict of in edges and out edges
    # here we use the id in the tuple which represented a edge ( '0' place in the tuple
    # is out of a node aand '1' place is in to node
    def _all_out(self, id, loc):
        return {p: self.edges[p] for p in self.edges.keys() if p[loc] is id}

    # a variable which help us to know how much action we did in the graph
    def get_mc(self) -> int:
        return self.mc

    ################################################################
    # adding a new edge to the graph
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        edge_ids = (id1, id2)
        if edge_ids in self.edges.keys():
            self.edges[edge_ids]=weight
            return True
        else:
            self.edges[edge_ids] = weight
            self.mc += 1
            return True

    # adding a new node to the graph
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            self.nodes[node_id] = pos
            self.mc += 1
            return True

    # removing a node from the graph ( when we remove node we need to remove
    # all the edges which came out of it and into it)
    def remove_node(self, node_id: int) -> bool:
        tempEdge = self.edges.copy()
        if node_id not in self.nodes:
            return False
        else:
            del self.nodes[node_id]
        for key in tempEdge.keys():
            if key[0] == node_id:
                self.edges.pop(key)
            elif key[1] == node_id:
                self.edges.pop(key)
        self.mc += 1
        return True

    # removing a edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        edge_key = (node_id1, node_id2)
        if edge_key not in self.edges.keys():
            return False
        else:
            del self.edges[edge_key]
            self.mc += 1
            return True

    def there_is_edge(self, id1:int, id2:int)->bool:
        edge_to_check = (id1,id2)
        if self.edges.keys().__contains__(edge_to_check):
            return True
        return False

    def __repr__(self):
        return f"nodes: {self.nodes}\nedges: {self.edges.__repr__()}"


if __name__ == '__main__':
    import json
    f_name = "A0.json"
    with open(f_name) as f:
        a = json.load(f)
    grp = DiGraph(nodes=a['Nodes'], edges=a['Edges'])
    print (grp.there_is_edge(0,5))
    print(grp.all_out_edges_of_node(0))

    # grp.all_in_edges_of_node(0)
    # grp.all_out_edges_of_node(0)
