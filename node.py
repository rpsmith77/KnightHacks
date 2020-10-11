import colors
import pygame


class Node:
    """
    Node object which acts like a node in a Eulerian Graph. Each node is
    connected to neighboring nodes with an edge of weight of 1.
    """

    def __init__(self, row, column, width, total_rows):
        """

        :param row: the row this node is in
        :param column: the column this node is in
        :param width: width of pygame window
        :param total_rows: total number of rows and columns since window is
                           square
        """
        self.row = row
        self.column = column
        self.total_rows = total_rows
        self.width = width
        self.x_coord = row * width
        self.y_coord = column * width
        # default color
        self.color = colors.ORANGE_YELLOW
        self.touching_nodes = []

    def get_position(self):
        """
        returns what row and column this node is in
        :return:
            int: row and column where this node is located
        """
        return self.row, self.column

    def is_checked(self):
        """
        check if node has already been checked
        :return:
            bool if color is correct
        """
        return self.color == colors.BURNT_SIENNA

    def is_checking(self):
        """
        check if node is currently being checked
        :return:
            bool if color is correct
        """
        return self.color == colors.SANDY_BROWN

    def is_wall(self):
        """
        check if node is a wall/barrier
        :return:
            bool if color is correct
        """
        return self.color == colors.GUNMETAL_BLUE

    def is_start_node(self):
        """
        check if node is starting node
        :return:
            bool if color is correct
        """
        return self.color == colors.PERSIAN_GREEN

    def is_end_node(self):
        """
        check if node is end node
        :return:
            bool if color is correct
        """
        return self.color == colors.ASPARAGUS

    def set_checked(self):
        """
        set node to checked
        :return:
            none
        """
        self.color = colors.BURNT_SIENNA

    def set_checking(self):
        """
        set node to being checked
        :return:
            none
        """
        self.color = colors.SANDY_BROWN

    def set_wall(self):
        """
        set node to wall/barrier
        :return:
            none
        """
        self.color = colors.GUNMETAL_BLUE

    def set_start(self):
        """
        set node to starting node
        :return:
            none
        """
        self.color = colors.PERSIAN_GREEN

    def set_end(self):
        """
        set node to ending node
        :return:
            none
        """
        self.color = colors.ASPARAGUS

    def set_path(self):
        """
        set node to path
        :return:
            none
        """
        self.color = colors.SKOBELOFF

    def reset(self):
        """
        reset node to default
        :return:
            none
        """
        self.color = colors.ORANGE_YELLOW

    def draw(self, window):
        """
        Draw node
        :param window: pygame display window
        :return:
            none
        """
        pygame.draw.rect(window, self.color,
                         (self.x_coord, self.y_coord, self.width, self.width))

    def update_touching_nodes(self, grid):
        """
        ensure the nodes that the current node can look at next are not valid
        :param grid: 2-D list of nodes
        :return:
            none
        """
        self.touching_nodes = []

        # check node above
        if self.row > 0 and not grid[self.row - 1][self.column].is_wall():
            self.touching_nodes.append(grid[self.row - 1][self.column])

        # check node below
        if self.row < self.total_rows - 1 and \
                not grid[self.row + 1][self.column].is_wall():
            self.touching_nodes.append(grid[self.row + 1][self.column])

        # check node to the left
        if self.column < self.total_rows - 1 and \
                not grid[self.row][self.column + 1].is_wall():
            self.touching_nodes.append(grid[self.row][self.column + 1])

        # check node to the right
        if self.column > 0 and \
                not grid[self.row][self.column - 1].is_wall():
            self.touching_nodes.append(grid[self.row][self.column - 1])
