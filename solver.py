from PIL import Image
from typing import Tuple
import numpy as np
import sys
import time

class Solver:
    """A maze solver that solves mazes using different graph traversal
    algorithms. """

    def __init__(self, image: Image) -> None:
        """Load <image> into memory, find the starting position on the 
        top row and ending position on the bottom row.""" 

        self.maze = np.array(image)
        self.start = None 
        self.end = None
        
        # assumption is made that the entrance and exit to the maze is on
        # the top and the bottom of the image
        row = len(self.maze[0])
        for column in range(row):
            if self.maze[0, column] == 255:
                self.start = column
        for column in range(row - 1, -1, -1):
            if self.maze[-1, column] == 255:
                self.end = column
        print("Maze loaded.")

    def DFS(self):
        """ Apply DFS to the maze """ 
        print("Applying DFS on maze size: {}".format(
            self.maze.shape))
        time_a = time.time()

        # use the DFS algorithm
        visited = {}
        
        

        # print out time taken
        time_b = time.time()
        print("Finished DFS. Took: {} seconds".format(time_b - time_a))
        
        
    def BFS(self):
        """ Apply BFS to the maze """
        pass

if __name__ == '__main__':
    file_name = sys.argv[-1]
    maze_image = Image.open(file_name).convert('L')
    solver = Solver(maze_image)
    solver.DFS()
