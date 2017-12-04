import sys

N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
turnleft = {S: E, E: N, N: W, W: S}

def spiral(width, height):
    numsum = 0
    x, y = width // 2, height // 2
    dx, dy = S
    matrix =[[None] * width for _ in range(height)]
    while True:

        try:
            if (x+1) >=0 and (y) >= 0:
                a = int(matrix[y][x+1] or 0)
            else:
                a = 0
        except IndexError:
            a = 0

        try: 
            if (x+1) >= 0 and (y+1) >= 0:
                b = int(matrix[y+1][x+1] or 0)
            else:
                b = 0
        except IndexError:
            b = 0
            
        try: 
            if (x+1) >= 0 and (y-1) >= 0:
                c = int(matrix[y-1][x+1] or 0)
            else:
                c = 0
        except IndexError:
            c = 0
            
        try: 
            if (x) >= 0 and (y+1) >= 0:
                d = int(matrix[y+1][x] or 0)
            else:
                d = 0
        except IndexError:
            d = 0

        try: 
            if (x) >= 0 and (y-1) >= 0:
                e = int(matrix[y-1][x] or 0)
            else:
                e = 0
        except IndexError:
            e = 0

        try: 
            if (x-1) >= 0 and (y) >= 0:
                f = int(matrix[y][x-1] or 0)
            else:
                f = 0
        except IndexError:
            f = 0

        try: 
            if (x-1) >= 0 and (y+1) >= 0:
                g = int(matrix[y+1][x-1] or 0)
            else:
                g = 0
        except IndexError:
            g = 0

        try:
            if (x-1) >= 0 and (y-1) >= 0:
                h = int(matrix[y-1][x-1] or 0)
            else:
                h = 0
        except IndexError:
            h = 0

        count = a + b + c + d + e + f + g + h
        if count == 0:
            count = 1
        matrix[y][x] = count 
        if count > 368078:
            print(count)
            sys.exit()
        ndx, ndy = turnleft[dx, dy]
        nx, ny = x + ndx, y + ndy
        if (0 <= nx < width and 0 <= ny < height and matrix[ny][nx] is None):
            x, y = nx, ny
            dx, dy = ndx, ndy
        else:
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix

print(spiral(1000, 1000))