import math

# For further reading on Type 1, 2 and 3 clauses check this PDF
# https://airccj.org/CSCP/vol3/csit3213.pdf?fbclid=IwAR2LNBg_ZN6C-74MC-jGQ8Y0sZzGWTvxMQwlTl2giClylAjPKN1K0RypmXI


def create_cnf_file(node_number, adjacency_list, colour_number):
    # create variables for the cnf_file
    cnf_variable_number = node_number*colour_number
    cnf_clause_number = (adjacency_list.__len__()*colour_number) \
        + node_number + get_num_of_type3(node_number, colour_number)
    variable_list = create_variable_list(node_number=node_number, colour_number=colour_number)

    # create the string for the cnf_file
    string_cnf = "c Graph colouring\n"
    string_cnf += "c\n"
    string_cnf += "p cnf " + str(cnf_variable_number) + " " + str(cnf_clause_number) + "\n"
    string_cnf += get_string_type1(adjacency_list, variable_list)
    string_cnf += get_string_type2(variable_list)
    string_cnf += get_string_type3(variable_list)

    # open the file
    cnf_input = open("ColourGraph.cnf", mode='w')
    cnf_input.write(string_cnf)
    cnf_input.close()


def get_num_of_type3(node_number, colour_number):
    # gets number of the type3 clauses
    if colour_number == 1:
        return 0
    return int(math.factorial(colour_number) / (math.factorial(2)*math.factorial(colour_number-2)))*node_number


def create_variable_list(node_number, colour_number):
    # creates variable list for the CNF file
    counter = 1
    variable_list = []
    for x in range(node_number):
        temp = []
        for c in range(colour_number):
            temp.append(counter)
            counter += 1
        variable_list.append(temp)
    # print(variable_list)
    return variable_list


def get_string_type1(adjacency_list, variable_list):
    # creates the type1 clauses
    string_type1 = ""
    for edge in adjacency_list:
        counter = 0
        for node_variable in variable_list[edge[0]]:
            string_type1 += str(-node_variable) + " " + str(-variable_list[edge[1]][counter]) + " 0\n"
            counter += 1
    return string_type1


def get_string_type2(variable_list):
    # creates type 2 clauses
    string_type2 = ""
    for node in variable_list:
        for node_variable in node:
            string_type2 += str(node_variable) + " "
        string_type2 += "0\n"
    return string_type2


def get_string_type3(variable_list):
    # creates type 3 clauses
    string_type3 = ""
    for node in variable_list:
        start_index = 0
        end_index = node.__len__()-1
        for node_var in node:
            start_index += 1
            start_index_counter = start_index
            while start_index_counter <= end_index:
                string_type3 += str(-node_var) + " " + str(-node[start_index_counter]) + " 0\n"
                start_index_counter += 1
    return string_type3
