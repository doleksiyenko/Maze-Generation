import numpy as np
import random
from typing import Tuple, List
from PIL import Image


def generate_maze(size: int) -> np.array:
    """ Return a numpy array that represents a maze. The maze is generated
    using 'Prim's Algorithm'.

    <size> : An integer representing the size of the maze to be generated,
    i.e size = 3 means a 3x3 maze.
    """
    # create the maze array, full of walls (0)
    maze = np.zeros((size, size))

    # start at a random cell in the maze
    rand_x = random.randint(0, len(maze) - 1)
    rand_y = random.randint(0, len(maze) - 1)
    print("Cell {}".format((rand_x, rand_y)))
    # mark this random cell as a passage
    maze[rand_y, rand_x] = 1
    # create the wall_list, and add the 'frontier' cells to it.
    wall_list = get_cell_walls((rand_x, rand_y), maze, 2, 0)
    print("Wall List: {}".format(wall_list))
    # print(maze)
    while len(wall_list) > 0:
        frontier_cell = wall_list[random.randint(0, len(wall_list) - 1)]
        frontier_neighbours = get_cell_walls(frontier_cell, maze, distance=2,
                                             state=1)
        # to prevent too many loops (can be set to 2 to prevent any loops)
        if len(frontier_neighbours) < 2:
            rand_frontier_neighbour = frontier_neighbours[
                random.randint(0, len(frontier_neighbours) - 1)]
            x = (rand_frontier_neighbour[0] + frontier_cell[0]) // 2
            y = (rand_frontier_neighbour[1] + frontier_cell[1]) // 2
            # set the cell between frontier cell and neighbour cell to passage
            maze[y, x] = 1
            maze[frontier_cell[1], frontier_cell[0]] = 1
            # find the frontier cells of the frontier cell and add
            # them to the wall list
            wall_list.extend(get_cell_walls(frontier_cell, maze=maze,
                                            distance=2,
                                            state=0))
        wall_list.remove(frontier_cell)
        print(len(wall_list))

    return maze


def get_cell_walls(position: Tuple[int, int], maze: np.array, distance: int,
                   state: int) -> List:
    """Given a position, return the position of the four cells
    surrounding that position with a <distance> of <position>, and only cells
    with <state>, 0 representing blocked cells and 1 representing unblocked
    cells. Return the tuple as coordinates (x, y)"""
    adjacent_cells = [
        (position[0], position[1] - distance),
        (position[0], position[1] + distance),
        (position[0] - distance, position[1]),
        (position[0] + distance, position[1])
    ]
    # check if the cells are within the maze
    to_pop = []
    for cell in adjacent_cells:
        if (cell[0] < 0) or (cell[1] < 0):
            to_pop.append(cell)
        elif (cell[0] > len(maze) - 1) or (cell[1] > len(maze) - 1):
            to_pop.append(cell)
    for _pop in to_pop:
        if _pop in adjacent_cells: adjacent_cells.remove(_pop)

    to_pop = []
    # check the state of the remaining cells
    for cell in adjacent_cells:
        if state == 0:
            if maze[cell[1], cell[0]] == 1:
                to_pop.append(cell)
        elif state == 1:
            if maze[cell[1], cell[0]] == 0:
                to_pop.append(cell)
    for _pop in to_pop:
        if _pop in adjacent_cells: adjacent_cells.remove(_pop)

    return adjacent_cells


if __name__ == '__main__':
    maze = generate_maze(50)
    maze *= 255
    print(maze)
    maze_image = Image.fromarray(maze)
    maze_image.save('maze_100.gif')
