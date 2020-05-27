from PIL import Image
from typing import Tuple, Dict, List
import numpy as np
import sys
import time
from prim_maze_generator import get_cell_walls

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
                self.start = (column, 0)
        for column in range(row - 1, -1, -1):
            if self.maze[-1, column] == 255:
                self.end = (column, len(self.maze) - 1)
        print("Maze loaded.")
        print("Start: {}, End: {}".format(self.start, self.end))

    def _get_node_neighbours(self, position: Tuple[int, int],
            visited: Dict[Tuple[int, int], int]) -> List[Tuple[int, int]]:
        neighbours = []
        neighbours.extend(get_cell_walls(position, maze=self.maze, 
            distance=1, state=1))
        # now check whether the neighbours in neighbours are visited
        for neighbour in neighbours:
            if neighbour in visited:
                neighbours.remove(neighbour) 
        return neighbours

    def DFS(self) -> List[Tuple[int,int]]:
        """ Apply DFS to the maze """ 
        # start timing the algorithm
        print("Applying DFS on maze size: {}".format(
            self.maze.shape))
        time_a = time.time()

        # use the DFS algorithm
        stack = [self.start]
        # use a dictionary to check which nodes have already been visited
        visited = {}
        # each node points to the previous node from which it came
        previous_node = [None] * self.maze.shape[0] * self.maze.shape[1]

        while len(stack) > 0:
            vertex = stack.pop(-1) 

            if vertex == self.end:
                break

            visited[vertex] = 1

            for neighbour in self._get_node_neighbours(vertex, visited):
                stack.append(neighbour)
                previous_node[neighbour[1] * self.maze.shape[0] + neighbour[0]] = vertex
        
        # figure out the path
        path = []
        vertex = self.end

        while vertex is not None:
            path.append(vertex)
            vertex = previous_node[vertex[1] * self.maze.shape[0] + vertex[0]]

        # print out time taken
        time_b = time.time()
        print("Finished DFS. Took: {} seconds".format(time_b - time_a))   
        return path

    def BFS(self):
        """ Apply BFS to the maze """
        pass

    def path_image(self, path: List[Tuple[int, int]], file_name: str) -> None:
        path_array = np.zeros(self.maze.shape)
        for pos in path:
            path_array[pos[1], pos[0]] = 128

        maze_path = self.maze - path_array
        image = Image.fromarray(maze_path)
        image.save(file_name)
        print("Path generated to file: {}".format(file_name))

if __name__ == '__main__':
    file_name = sys.argv[-1]
    maze_image = Image.open(file_name).convert('L')

    solver = Solver(maze_image)
    dfs = solver.DFS()
    solver.path_image(dfs, 'maze_path.gif')
