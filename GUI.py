import tkinter
import GraphAlgo
import DiGraph
class GUI:
    def __init__(self, graph: DiGraph = None):
        self.graph = DiGraph() if graph is None else graph
    r = tkinter.Tk()
    r.title('Counting Seconds')
    button = tkinter.Button(r, text='show graph', width=25, command=)
    button.pack()

    r.mainloop()