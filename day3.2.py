N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
turnleft = {S: E, E: N, N: W, W: S}

def spiral(width, height):
    numsum = 0
    x, y = width // 2, height // 2
    dx, dy = S
    matrix =[[None] * width for _ in range(height)]
    while True:

        try:
            a = matrix[y][x+1]
        except IndexError:
            a = None
        try: 
            b = matrix[y+1][x+1]
        except IndexError:
            b = None
        try: 
            c = matrix[y-1][x+1]
        except IndexError:
            c = None
        try: 
            d = matrix[y+1][x]
        except IndexError:
            d = None
        try: 
            e = matrix[y-1][x]
        except IndexError:
            e = None
        try: 
            f = matrix[y][x-1]
        except IndexError:
            f = None
        try: 
            g = matrix[y+1][x-1]
        except IndexError:
            g = None
        try:
            h = matrix[y-1][x-1]
        except IndexError:
            h = None

        print(a, b, c, d, e, f, g, h)
        print(x, y)
        count = int(a or 0) + int(b or 0) + int(c or 0) + int(d or 0) + int(e or 0) + int(f or 0) + int(g or 0) + int(h or 0)
        if count == 0:
            count = 1
        matrix[y][x] = count
        print('Count = %d' % count)   
        ndx, ndy = turnleft[dx, dy]
        nx, ny = x + ndx, y + ndy
        if (0 <= nx < width and 0 <= ny < height and matrix[ny][nx] is None):
            x, y = nx, ny
            dx, dy = ndx, ndy
        else:
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix

print(spiral(3, 3))