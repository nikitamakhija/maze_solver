from bfs import *
from dfs import *

class Solver:
    
    def solve(maze, method, start, end):
            if(method == "BFS"):
                return BFS.solve(maze, start, end)
            elif (method == "DFS"):
                return DFS.solve(maze)