class Maze:

    def generateMaze(img):
        rows, cols = img.size
        print(rows, cols)
        pixels = list(img.getdata())
        maze = []
        cnt = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(pixels[cnt])
                cnt += 1
            maze.append(row)
        return maze

    