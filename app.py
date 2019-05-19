import networkx as nx
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox as msgBox
import cnf_file
import mcSATan.parsers.DIMACS as parser


def cnf_sat_search(node_number, adjacency_list):
    colour_searching = True
    # Creating the CNF file and searching for minimal valid number of colours
    counter = 1
    result = []
    if node_number > 1:
        while colour_searching:
            cnf_file.create_cnf_file(node_number=node_number, adjacency_list=adjacency_list, colour_number=counter)
            solver = parser.parse_cnf(open("ColourGraph.cnf"))
            temp = solver.solve()
            print(temp)
            if temp is False:
                counter += 1
            else:
                result = temp
                colour_searching = False
    return [result, counter]


def create_colour_list(node_number, adjacency_list):
    [result, counter] = cnf_sat_search(node_number, adjacency_list)
    # creating colour list
    colour_list = []
    for x in range(0, node_number):
        temp = result[x * counter:((x + 1) * counter):]
        temp = [y.value for y in temp]
        # print(temp)
        colour_list.append(temp.index(True) + 1)
    # print(colour_list)

    # Returning a message box with result
    msgBox.showinfo("Colour search result", "You can colour this graph with " + str(counter) + " colours used")
    return  colour_list


def calculate_graph_form_textbox():
    if stringGraph.get() == "":
        msgBox.showerror("Empty input", "Please enter the adjacency lists for the graph.\n"
                                        "Use the following format: [x1,x2];[y1];[]")
        return
    # variables for CNF file
    node_number = stringGraph.get().count(';')+1
    adjacency_list = parse(stringGraph.get())

    draw_graph(node_number, adjacency_list)


def draw_graph(node_number, adjacency_list):

    colour_list = create_colour_list(node_number, adjacency_list)

    # draw graph
    graph_to_draw = nx.Graph()
    graph_to_draw.add_nodes_from(range(node_number))
    graph_to_draw.add_edges_from(adjacency_list)
    nx.draw_networkx(graph_to_draw, node_size=800, node_color=colour_list)
    plt.show()


def graph_import_file():
    file_import = open(stringFileName.get(), mode='r')
    string_lines = file_import.readlines()
    node_number = None
    edge_number = None
    edge_list = []
    if string_lines.__len__() < 2:
        msgBox.showerror("Empty input", "Please check the path for the graph file.")
        return
    for string_line in string_lines:
        if string_line[0] == "p":
            [_, _, node_number, _] = string_line.split(' ')
        elif string_line[0] == "e":
            [_, node1, node2] = string_line.split(" ")
            edge = (int(node1, 10), int(node2, 10))
            edge_list.append(edge)
        elif string_line[0] != "c":
            msgBox.showerror("Wrong file formatting", "Please check the graph file formatting.")
            return
    draw_graph(int(node_number, 10), adjacency_list=edge_list)


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
    WindowMain.geometry("500x150")
    WindowMain.resizable(0, 0)
    WindowMain.title("Draw Graph")

    # Variables used in the GUI
    stringGraph = tkinter.StringVar()
    stringGraphLabel = tkinter.StringVar()
    stringFileLabel = tkinter.StringVar()
    stringFileName = tkinter.StringVar()

    stringGraphLabel.set("Graph: ")
    stringFileLabel.set("File: ")

    # The GUI elements
    FrameBackground = tkinter.Frame(WindowMain)
    FrameBackground.pack_propagate(0)
    LabelGraphInput = tkinter.Label(FrameBackground, textvariable=stringGraphLabel)
    EntryGraphInput = tkinter.Entry(FrameBackground, width=100, textvariable=stringGraph)
    ButtonDrawGraph = tkinter.Button(FrameBackground, text="Draw Graph", command=lambda: calculate_graph_form_textbox())

    FrameFileImport = tkinter.Frame(WindowMain)
    FrameFileImport.pack_propagate(0)
    LabelFileName = tkinter.Label(FrameFileImport, textvariable=stringFileLabel)
    EntryFileName = tkinter.Entry(FrameFileImport, width=100, textvariable=stringFileName)
    ButtonFileImport = tkinter.Button(FrameFileImport, text="Import File", command=lambda: graph_import_file())

    # Packing the elements
    FrameBackground.pack(fill=tkinter.BOTH, expand=True)
    ButtonDrawGraph.pack(side=tkinter.BOTTOM)
    LabelGraphInput.pack(side=tkinter.LEFT)
    EntryGraphInput.pack(side=tkinter.RIGHT)

    FrameFileImport.pack(fill=tkinter.BOTH, expand=True)
    ButtonFileImport.pack(side=tkinter.BOTTOM)
    LabelFileName.pack(side=tkinter.LEFT)
    EntryFileName.pack(side=tkinter.RIGHT)

    # Setting everything in motion
    WindowMain.mainloop()


