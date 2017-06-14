import argparse
import matplotlib.pyplot as plt
import networkx as nx


def maximum_independent_set(set, sorted_nodes, G):
    """Find the maximum independent set for the list"""
    for i in sorted_nodes:
        counter = 0  #
        for j in set:
            if i != j and j in G.neighbors(i):
                counter += 1
        if counter == 0 and i not in set:
            set.add(i)
    return sorted(set)


def check_max(max_or_not, sorted_nodes, G):
    """Check if it is the maximum independently sets for j nodes"""
    new_graph = nx.Graph()  # We need new graph with the first j nodes
    for i in sorted_nodes:
        new_graph.add_node(i)
        neighbords = G.neighbors(i)
        for j in neighbords:
            if j in sorted_nodes:
                new_graph.add_edge(i, j)
    for i in sorted(new_graph.nodes()):
        counter = 0
        for j in max_or_not:
            if i != j and i in G.neighbors(j):
                counter = counter + 1
        if counter == 0 and i not in max_or_not:
            return False
    return True


def find_all_maximum(sorted_nodes, G):
    """Find all the maximum independent sets of graph"""
    all_the_maximum_intependent = []
    Q = [sorted(maximum_independent_set(set([sorted_nodes[0]]), sorted_nodes, G))]
    while Q:
        S = min(Q)
        all_the_maximum_intependent.append(S)
        Q.remove(S)
        for j in sorted_nodes:
            for i in S:
                if j in G.neighbors(i) and i < j:
                    for k in range(len(sorted_nodes)):
                        if sorted_nodes[k] == j:
                            first_j_nodes = sorted_nodes[:k + 1]
                            break
                    Sj = set(S).intersection(set(first_j_nodes))
                    small_or_max_int = Sj.difference(set(G.neighbors(j)))
                    if check_max(small_or_max_int.union(set([j])), first_j_nodes, G):
                        T = maximum_independent_set(small_or_max_int.union(set([j])), sorted_nodes, G)
                        if sorted(T) not in Q and T != S:
                            Q.append(sorted(T))
    return all_the_maximum_intependent


def show_images(G, pos, all_the_maximum_intep):
    nx.draw_networkx_nodes(G, pos, node_color='w')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.axis('off')
    plt.show()  # Show the graph
    for i in all_the_maximum_intep:  # Show all the maximum intependent set
        nx.draw_networkx_nodes(G, pos, nodelist=i)  # Thelo na vro kai ta upoloipa. pos tha ta vro?
        nx.draw_networkx_nodes(G, pos, nodelist=(set(G.nodes()) - set(i)), node_color='w')
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        plt.axis('off')
        plt.show()


def save_image(name, figure, G, pos, all_the_maximum_intep):
    for i in range(len(all_the_maximum_intep)):
        nx.draw_networkx_nodes(G, pos, nodelist=all_the_maximum_intep[i])
        nx.draw_networkx_nodes(G, pos, nodelist=(set(G.nodes()) - set(all_the_maximum_intep[i])), node_color='w')
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
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

    G = nx.read_adjlist(args.input, delimiter=";", nodetype=str)  # Open the file

    sorted_nodes = sorted(G.nodes())

    all_the_maximum_intep = find_all_maximum(sorted_nodes, G)
    for i in all_the_maximum_intep:
        print(i)
    pos = nx.spring_layout(G)
    if args.display:  # Show images
        show_images(G, pos, all_the_maximum_intep)
    if args.name and args.figure:  # Save the image. A unique photo for each maximum intependent set
        save_image(args.name, args.figure, G, pos, all_the_maximum_intep)


if __name__ == '__main__':
    main()
