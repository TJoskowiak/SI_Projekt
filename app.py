import networkx as nx
import matplotlib.pyplot as plt
import tkinter


def draw_graph():
    adjacency_list = parse(stringGraph.get())

    graph_to_draw = nx.Graph()

    graph_to_draw.add_edges_from(adjacency_list)
    nx.draw_networkx(graph_to_draw, node_size=800)
    plt.show()


def parse(string_to_parse):
    # Parse the entry string to list of edges for the graph
    # print(string_to_parse)
    # Parse the string into list of adjacency lists
    edge_list = string_to_parse.split(';')
    edge_list = [x.replace('[', '').replace(']', '').split(',') for x in edge_list]
    edge_list = [[int(x, 10) for x in row if x != ''] for row in edge_list]
    # print(edge_list)

    # Create one big list of edges
    edge_list_final = []
    counter = 0
    for row in edge_list:
        edge_list_final.extend([(counter, x) for x in row])
        counter += 1
    # print(edge_list_final)
    return edge_list_final


if __name__ == "__main__":

    # Hello dear frens! To learn more about the magic below please visit this link:
    # https://www.tutorialspoint.com/python/python_gui_programming.htm

    # Main window
    WindowMain = tkinter.Tk("DrawGraph")
    WindowMain.geometry("500x100")
    WindowMain.resizable(0, 0)
    WindowMain.title("Draw Graph")

    # Variables used in the GUI
    stringGraph = tkinter.StringVar()
    stringGraphLabel = tkinter.StringVar()
    stringGraphLabel.set("Graph: ")

    # The GUI elements
    FrameBackground = tkinter.Frame(WindowMain)
    FrameBackground.pack_propagate(0)
    LabelGraphInput = tkinter.Label(FrameBackground, textvariable=stringGraphLabel, )
    EntryGraphInput = tkinter.Entry(FrameBackground, width=100, textvariable=stringGraph)
    ButtonDrawGraph = tkinter.Button(FrameBackground, text="Draw Graph", command=lambda: draw_graph())

    # Packing the elements
    FrameBackground.pack(fill=tkinter.BOTH, expand=True)
    ButtonDrawGraph.pack(side=tkinter.BOTTOM)
    LabelGraphInput.pack(side=tkinter.LEFT)
    EntryGraphInput.pack(side=tkinter.RIGHT)

    # Setting everything in motion
    WindowMain.mainloop()


