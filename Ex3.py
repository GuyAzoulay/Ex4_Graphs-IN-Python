from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

if __name__ == '__main__':
    file = input()
    g = DiGraph()
    galgo = GraphAlgo(g)
    galgo.load_from_json(file)
    galgo.plot_graph()