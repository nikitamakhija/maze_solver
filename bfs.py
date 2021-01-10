from collections import deque

class BFS:

    def solve(maze, start, end):
        rows = len(maze)
        cols = len(maze[0])

        q = deque()
        q.appendleft(start)
        parent = {}
        vis = {}
        vis[BFS.get_key(start[0], start[1])] = 1
        parent[BFS.get_key(start[0], start[1])] = None

        while q:
            current = q.pop()
            if current == end:
                break
            
            directions =[[0,1], [0,-1], [1,0], [-1,0]]

            for direction in directions:
                x = direction[0] + current[0]
                y = direction[1] + current[1]
                if BFS.is_valid_position(x, y, rows, cols):
                    key = BFS.get_key(x, y)
                    if key not in vis and maze[x][y] == 1:
                        vis[key] = 1
                        q.appendleft([x,y])
                        parent[key] = current

        path = []
        current = end
        while(current != None):
            path.append(current)
            current = parent[BFS.get_key(current[0], current[1])]
        
        return reversed(path)

    def get_key(x, y):
        return str(x)+"."+str(y)
    
    def is_valid_position(x, y, rows, cols):
        return x>=0 and y>=0 and x<rows and y <cols




        