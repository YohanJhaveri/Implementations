import numpy as np
import argparse
import random
import math

from collections import defaultdict

def pageRank(input, output):
    input = list(open(input, "r"))

    # storing the edges of the graph
    edges = [line.split() for line in input[1:-1]]

    # initializing sets
    vertices = set()
    outward = set()
    inward = set()

    for edge in edges:

        # keeping track of which vertices have edges pointing inward and outward
        outward.add(edge[0])
        inward.add(edge[2])

        # adding all vertices encountered
        vertices = vertices.union(set(edge))

    # removing the '->' string from the set of vertices
    vertices.remove('->')

    # finding vertices that are dead ends (these vertices have only inward edges and no outward edges)
    dead_ends = inward - outward

    # removing dead end vertices from the list of vertices as it skews page rank
    vertices = sorted(list(vertices - dead_ends))

    n = len(vertices)

    # initializing adjacency matrix
    adjacency_matrix = np.zeros((n, n))

    # updating the adjacency matrix
    for edge in edges:
        if edge[2] not in dead_ends:
            x = vertices.index(edge[0])
            y = vertices.index(edge[2])
            adjacency_matrix[x][y] = 1

    # initializing page rank for each vertex as 1/n
    page_rank = [(1/n) for vertex in vertices]

    # normalizing the adjacency matrix my number of outward edges
    row_sums = adjacency_matrix.sum(axis=1)
    normalized_adjacency_matrix = (adjacency_matrix / row_sums[:, np.newaxis]).T

    # damping the normalized adjacency matrix to deal with spider traps
    N = normalized_adjacency_matrix.shape[1]
    DAMPING_FACTOR = 0.85
    dampened_normalized_adjacency_matrix = DAMPING_FACTOR * normalized_adjacency_matrix + (1 - DAMPING_FACTOR) / N

    # matrix multiplication of dampened and normalized adjacency matrix to update page rank values for each vertex
    while True:
        old_page_rank = page_rank
        page_rank = dampened_normalized_adjacency_matrix.dot(page_rank)

        # threshold for considering two values the same is 10^-10
        if round(sum(np.absolute(old_page_rank - page_rank)), 10) == 0:
            break

    output = open(output, "w+")

    output.write('vertex,pagerank \n')

    # storing vertex-page rank pairs in a tuple for easier sorting and writing to output
    page_rank_tuples = [(vertices[i], round(page_rank[i], 10)) for i in range(n)]

    # sorting in non-decreasing order of pagerank and settling lexicographically
    page_rank_tuples.sort(key=lambda x: (-x[1], x[0]))

    # writing the sorted output into the output file with vertex and page rank seperated by a comma
    for x in page_rank_tuples:
        output.write(x[0] + ',' + str(x[1]) + '\n')



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input",
                        nargs='?',
                        default="graph2.txt")
    parser.add_argument("output",
                        nargs='?',
                        default="pagerank2.csv")

    args = parser.parse_args()

    pageRank(args.input, args.output)


if __name__ == "__main__":
    main()
