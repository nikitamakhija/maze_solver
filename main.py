from PIL import Image
from maze import Maze
from solver import Solver
from drawer import Drawer

def solve(img_name, method):
    img = Image.open(img_name)
    
    maze = Maze.generateMaze(img)
    start = [0,1]
    end = [14,13]
    path = Solver.solve(maze, method, start, end)
    img = Drawer.draw(img, list(path))


def main():
    # Add whatever is required
    solve("images/small.png", "BFS")


if __name__ == "__main__":
    main()
