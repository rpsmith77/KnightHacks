"""
This Project was created during the KnightHacks hackathon October 2020

The purpose is to visually show how different pathfinding algorithms work.

TODO:
    improve instruction screen
    add more search algos
        * depth first
        * breadth first

__author__ = Ryan Smith
"""

import pygame
import colors
from node import Node
from a_star_search import a_star_search
import instructions

# Window Settings
WIDTH = 500
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding")


def create_grid(rows, width):
    """
    Breaks the pygame window into a grid and assigns each square as node.
    Since the window is square, the rows and columns are the same

    :param rows: number of rows/columns
    :param width: how wide the pygame window is
    :return: grid: 2-D list of nodes that correspond to the squares in the
                   window
    """

    grid = []
    node_dimension = width // rows
    for row in range(rows):
        grid.append([])
        for column in range(rows):
            node = Node(row, column, node_dimension, rows)
            grid[row].append(node)

    return grid


def draw_grid_lines(window, rows, width):
    """
    Draw the visuals to show the division between nodes
    :param window: pygame window
    :param rows: number of rows
    :param width: width of pygame window
    :return:
        none
    """
    node_dimension = width // rows
    for row in range(rows):
        pygame.draw.line(window, colors.GRAY, (0, row * node_dimension),
                         (width, row * node_dimension))
        for column in range(rows):
            pygame.draw.line(window, colors.GRAY, (column * node_dimension, 0),
                             (column * node_dimension, width))


def draw(window, grid):
    """
    Draw pygame window
    :param window: pygame window
    :param grid: 2-D list of node objects
    :param rows: number of rows
    :param width: width of window
    :return:
        none
    """
    window.fill(colors.ORANGE_YELLOW)

    for row in grid:
        for node in row:
            node.draw(window)

    pygame.display.update()


def get_clicked_position(position, rows, width):
    """
    Figure out which node was clicked on
    :param position: mouse click position
    :param rows: number of rows
    :param width: width of pygame window
    :return:
        int: row and column of node clicked
    """
    node_dimension = width // rows
    y, x = position

    row = y // node_dimension
    column = x // node_dimension

    return row, column


def main(window, width):
    """
    Creates the pygame visuals, and runs the algorithm(s)
    :param window: pygame window
    :param width: window width
    :return:
        none
    """

    instructions.main()

    # number of rows and columns with nodes
    rows = 50
    grid = create_grid(rows, width)

    # starting and ending nodes
    start = None
    end = None

    run = True
    while run:
        draw(window, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # left mouse click
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, column = get_clicked_position(position, rows, width)
                node = grid[row][column]

                # if there is no starting node make left clicked node start
                if not start and node != end:
                    start = node
                    start.set_start()

                # if there is no end node make left clicked node end
                elif not end and node != start:
                    end = node
                    end.set_end()

                # all other left clicked nodes are walls
                elif node != end and node != start:
                    node.set_wall()

            # right click resets clicked nodes
            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, column = get_clicked_position(position, rows, width)
                node = grid[row][column]

                node.reset()

                # allows new start and end nodes
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                # begin search
                if event.key == pygame.K_SPACE and start and end:
                    a_star_search(lambda: draw(window, grid),
                                  grid, start, end)

                # reset all nodes
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = create_grid(rows, width)

    pygame.quit()


main(WINDOW, WIDTH)
