import networkx as nx
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox as msgBox


def drawgraph():
    G = nx.Graph()

    G.add_edges_from([(1, 2),
                      (2, 3),
                      (3, 4),
                      (4, 1),
                      (4, 5),
                      (5, 6),
                      (6, 2)])
    colors = [1, 2, 1, 1, 1, 1]
    nx.draw(G, node_color=colors, node_size=800)
    plt.show()


if __name__ == "__main__":

    ## Hello dear frens! To learn more about the magic below please visit this link:
    ## https://www.tutorialspoint.com/python/python_gui_programming.htm

    ## Main window
    WindowMain = tkinter.Tk("DrawGraph")
    WindowMain.geometry("500x100")
    WindowMain.resizable(0, 0)


    ## Variables used in the GUI
    stringGraph = tkinter.StringVar()
    stringGraphLabel = tkinter.StringVar()
    stringGraphLabel.set("Graph: ")

    ## The GUI elements
    FrameBackground = tkinter.Frame(WindowMain)
    FrameBackground.pack_propagate(0)
    LabelGraphInput = tkinter.Label(FrameBackground, textvariable=stringGraphLabel, )
    EntryGraphInput = tkinter.Entry(FrameBackground, width=100, textvariable=stringGraph)
    ButtonDrawGraph = tkinter.Button(FrameBackground, text="Draw Graph", command=lambda: drawgraph())

    ## Packing the elements
    FrameBackground.pack(fill=tkinter.BOTH, expand=True)
    ButtonDrawGraph.pack(side=tkinter.BOTTOM)
    LabelGraphInput.pack(side=tkinter.LEFT)
    EntryGraphInput.pack(side=tkinter.RIGHT)


    ## Setting everything in motion
    WindowMain.mainloop()


