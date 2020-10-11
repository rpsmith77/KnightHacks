"""
This holds the A* searching algorithm, further explained here:
    https://brilliant.org/wiki/a-star-search/
It uses concepts from Eulerian graph theory. The basics of this algorithms :
                f(n)=g(n)+h(n)
where
f(n) = total estimated cost of path through node nn
g(n) = cost so far to reach node nn
h(n) = estimated cost from nn to goal. This is the heuristic part of the
       cost function, so it is like a guess.

h(n) can be calculated differnt ways, but these are the main 2
    Manhattan Distance Heuristic
        abs(x_start - x_end) + abs(y_start - y_end)
    Euclidean Distance Heuristic
        sqrt((x_start - x_end)^2 + (y_start - y_end)^2)

Manhattan Distance Heureistic is quicker to calculate, but the Euclidean
Distance Heuristic created more realistic paths, so I went with the latter

Tech with Tim's youtube channel helped me figure out how to take this
algorithm and make code out of it
"""
import math
from queue import PriorityQueue
import pygame


def h_score(point1, point2):
    """
    Heuristic score / approximate distance
    :param point1: where the node is located
    :param point2: where the ending node is located
    :return:
        distance from current node to end node ignoring walls
    """
    # x is column, y is row
    x1, y1 = point1
    x2, y2 = point2
    # return abs(x1 - x2) + abs(y1 - y2)
    return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def create_path(last_node, current, draw):
    """
    use the f(n) values to figure out the shortest path
    :param last_node: node that was used to get to current node
    :param current: the node we are currently at
    :param draw: lambda draw function from main.py
    :return:
        none
    """
    while current in last_node:
        current = last_node[current]
        current.set_path()
        draw()


def a_star_search(draw, grid, start, end):
    """
    performs the A* search.
    :param draw: lambda function to draw in pygame from main.py
    :param grid: 2-D list of nodes
    :param start: starting node
    :param end: ending node
    :return:
        bool if end is or no path open
    """

    # valid touching nodes
    for row in grid:
        for node in row:
            node.update_touching_nodes(grid)

    # count is for tiebreakers between nodes
    count = 0

    # list of nodes and their nodes that is sorted by PriorityQueue
    open_set = PriorityQueue()
    # ensure starting node is 0
    open_set.put((0, count, start))
    # store the immediate nodes used to reach current node
    last_node = {}
    # default all node scores to infinity
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    # set starts f score to distance from end position
    f_score[start] = h_score(start.get_position(), end.get_position())

    # open_set_hash is used to keep track if a node is in the queue
    open_set_hash = {start}

    # if the open set is empty, that means every possible node has been
    # considered. If path isn't found, it doesn't exist
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # PriorityQueue get sorts the list and .get() dequeues the value.
        # index 2 is the node
        current = open_set.get()[2]
        # keep track if what nodes are in the queue
        open_set_hash.remove(current)

        if current == end:
            create_path(last_node, end, draw)
            end.set_end()
            return True

        # look at all the nodes touching the current nodes
        for node in current.touching_nodes:
            # temp variable since nodes can be accessed from many sides,
            # and we only care about the most optimal route
            possible_g_score = g_score[current] + 1
            # g_score is defaulted to infinity so as long as the node has 1
            # other node touching it, the g_score will change
            if possible_g_score < g_score[node]:
                last_node[node] = current
                g_score[node] = possible_g_score
                f_score[node] = possible_g_score + h_score(node.get_position(),
                                                           end.get_position())
                # add node to open_set if its not in there
                if node not in open_set_hash:
                    count += 1
                    open_set.put((f_score[node], count, node))
                    open_set_hash.add(node)
                    node.set_checking()

        # update pygame
        draw()

        if current != start:
            current.set_checked()

    return False
