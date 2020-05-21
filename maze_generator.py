import numpy as np
import random
from typing import Tuple
from PIL import Image

def generate_maze(size: int) -> np.array:
    """ Return a numpy array that represents a maze. The maze is generated 
    using 'Prim's Algorithm'. 

    <size> : An integer representing the size of the maze to be generated,
    i.e size = 3 means a 3x3 maze.
    """
    # create the maze array, full of walls (0)
    maze = np.zeros((size, size))

    rand_x = random.randint(0, len(maze) - 1)
    rand_y = random.randint(0, len(maze) - 1)
    # start at a random cell in the maze
    cell = maze[rand_y, rand_x]
    maze[rand_y, rand_x] = 1
    wall_list = get_cell_walls((rand_x, rand_y))

    while len(wall_list) > 0:
        # pick a random wall
        rand_wall = wall_list[random.randint(0, len(wall_list) - 1)]
        print(rand_wall) 
    return maze

def get_cell_walls(position: Tuple[int, int]):
    """Given a position, return the position of the four cells 
    surrounding that position, return the tuple as coordinates (x, y)"""
    adjacent_cells = [
    (position[0], position[1] - 1),
    (position[0], position[1] + 1),
    (position[0] - 1, position[1]),
    (position[0] + 1, position[1])
    ]
    for cell in adjacent_cells:
        if (cell[0] < 0) or (cell[1] < 0):
            adjacent_cells.remove(cell)
        elif (cell[0] > len(maze) - 1) or (cell[1] > len(maze) - 1):
            adjacent_cells.remove(cell)
    return adjacent_cells

if __name__ == '__main__':
    maze = generate_maze(10)
    print(maze)
    maze_image = Image.fromarray(maze, mode='L')
    maze_image.save('maze_100.png')
