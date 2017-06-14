"""
Findings on maximum independent subset from a graph
author: Christina Chaniotaki
"""
import argparse
import matplotlib.pyplot as plt
import networkx as nx


def maximum_independent_set(set_graph, sorted_nodes, graph):
    """
    Find the maximum independent set for the list
    :param set_graph: The set from the graph
    :param sorted_nodes: The sorted nodes from the graph
    :param graph: The graph from the file
    :return: The sorted set with maximum independent
    """
    for i in sorted_nodes:
        counter = 0  #
        for j in set_graph:
            if i != j and j in graph.neighbors(i):
                counter += 1
        if counter == 0 and i not in set_graph:
            set_graph.add(i)
    return sorted(set_graph)


def check_max(max_or_not, sorted_nodes, graph):
    """
    Check if it is the maximum independently sets for j nodes
    :param max_or_not: dictionary with the subset
    :param sorted_nodes: The sorted nodes from the graph
    :param graph: The graph from the file
    :return: True or False(if is maximum independently sets for j nodes or not)
    """
    new_graph = nx.Graph()  # We need new graph with the first j nodes
    for i in sorted_nodes:
        new_graph.add_node(i)
        neighbords = graph.neighbors(i)
        for j in neighbords:
            if j in sorted_nodes:
                new_graph.add_edge(i, j)
    for i in sorted(new_graph.nodes()):
        counter = 0
        for j in max_or_not:
            if i != j and i in graph.neighbors(j):
                counter = counter + 1
        if counter == 0 and i not in max_or_not:
            return False
    return True


def find_all_maximum(sorted_nodes, graph):
    """
    Find all the maximum independent sets of graph
    :param sorted_nodes: The sorted nodes from the graph
    :param graph: The graph from the file
    :return: All the maximun independently sets
    """
    all_the_maximum_intependent = []
    sorted_graph = [sorted(maximum_independent_set(set([sorted_nodes[0]]),
                                                   sorted_nodes, graph))]
    while sorted_graph:
        min_set = min(sorted_graph)
        all_the_maximum_intependent.append(min_set)
        sorted_graph.remove(min_set)
        new_graph = []
        for j in sorted_nodes:
            for i in min_set:
                new_graph.append([j, i])
        for pair in new_graph:
            if pair[0] in graph.neighbors(pair[1]) and pair[1] < pair[0]:
                for k in range(0, len(sorted_nodes)):
                    if sorted_nodes[k] == pair[0]:
                        first_j_nodes = sorted_nodes[:k + 1]
                        break
                sorted_j = set(min_set).intersection(set(first_j_nodes))
                small_or_max_int = sorted_j.difference(set(
                    graph.neighbors(pair[0])))
                if check_max(small_or_max_int.union(set([pair[0]])),
                             first_j_nodes, graph):
                    set_t = maximum_independent_set(small_or_max_int.union(
                        set([pair[0]])), sorted_nodes, graph)
                    if sorted(set_t) not in sorted_graph and set_t != \
                            min_set:
                        sorted_graph.append(sorted(set_t))
    return all_the_maximum_intependent


def show_images(graph, pos, all_the_maximum_intep):
    """
    Show the images by using networkx
    :param graph: The graph from the file
    :param pos: The possitions from nodes
    :param all_the_maximum_intep: All the maximun independently sets
    """
    nx.draw_networkx_nodes(graph, pos, node_color='w')
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    plt.axis('off')
    plt.show()  # Show the graph
    for i in all_the_maximum_intep:  # Show all the maximum intependent set
        nx.draw_networkx_nodes(graph, pos, nodelist=i)
        nx.draw_networkx_nodes(graph, pos,
                               nodelist=(set(graph.nodes()) - set(i)),
                               node_color='w')
        nx.draw_networkx_edges(graph, pos)
        nx.draw_networkx_labels(graph, pos)
        plt.axis('off')
        plt.show()


def save_image(name, figure, graph, pos, all_the_maximum_intep):
    """
    Save the images by using networkx
    :param name: The name of the image files (name_0, name_1 etc)
    :param figure: The type of the image file.
    :param graph: The graph from the file
    :param pos: The possitions from nodes
    :param all_the_maximum_intep: All the maximun independently sets
    """
    for i in range(0, len(all_the_maximum_intep)):
        nx.draw_networkx_nodes(graph, pos, nodelist=all_the_maximum_intep[i])
        nx.draw_networkx_nodes(graph, pos, nodelist=(set(graph.nodes()) - set(
            all_the_maximum_intep[i])), node_color='w')
        nx.draw_networkx_edges(graph, pos)
        nx.draw_networkx_labels(graph, pos)
        plt.axis('off')
        plt.savefig(name + "_" + str(i) + "." + figure)


def main():
    """ The beginning of the program that calls the functions."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", action="store_true",
                        help="Displays on the computer screen the graphical "
                             "representation of the graph and each set of "
                             "graphic.")
    parser.add_argument("-n", "--name", type=str,
                        help="The name of the file to store the images.")
    parser.add_argument("-f", "--figure", type=str,
                        help="The type of the image file.")
    parser.add_argument("input", help="The name of input file")
    args = parser.parse_args()
    # Open the file
    graph = nx.read_adjlist(args.input, delimiter=";", nodetype=str)
    sorted_nodes = sorted(graph.nodes())
    all_the_maximum_intep = find_all_maximum(sorted_nodes, graph)
    for i in all_the_maximum_intep:
        print(i)
    pos = nx.spring_layout(graph)
    if args.display:
        # Show images
        show_images(graph, pos, all_the_maximum_intep)
    if args.name and args.figure:
        # Save the image. A unique photo for each maximum intependent set
        save_image(args.name, args.figure, graph, pos, all_the_maximum_intep)


if __name__ == '__main__':
    main()
