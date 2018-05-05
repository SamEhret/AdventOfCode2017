N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
turnleft ={S: E, E: N, N: W, W: S}

def spiral(width, height):
    x, y = width // 2, height // 2
    dx, dy = S
    matrix =[[None] * width for _ in range(height)]
    count = 0
    while True:
        count = count + 1
        matrix[y][x] = count
        if count == 368078:
            print abs((width/2 - x)) + abs((height/2 - y))
        ndx, ndy = turnleft[dx, dy]
        nx, ny = x + ndx, y + ndy
        if (0 <= nx < width and 0 <= ny < height and matrix[ny][nx] is None):
            x, y = nx, ny
            dx, dy = ndx, ndy
        else:
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix

spiral(1000, 1000)