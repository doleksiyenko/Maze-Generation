import numpy as np
from stack import Stack
import random
from typing import Tuple
from PIL import Image

def generate_maze(size: int) -> np.array
    """ Return a numpy array that represents a maze. The maze is generated 
    using 'Prim's Algorithm'. 

    <size> : An integer representing the size of the maze to be generated,
    i.e size = 3 means a 3x3 maze.
    """
    # create the maze array
    maze = np.zeros((size, size))
    visited = {}

    # start at a random cell in the maze
    cell = maze[random.randint(0, len(maze) - 1,
                random.randint(0, len(maze) - 1)]
    visited[cell] = 1
    
    # select a random neightbouring cell that has not been visited
    


if __name__ == '__main__':
    maze = generate_maze(10)
    maze_image = Image.fromarray(maze, mode='L')
    maze_image.save('maze_100.png')
