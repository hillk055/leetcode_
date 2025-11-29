def number_paths():

    # How many different ways can we get from S to E, once a square has been traversed, we can no longer use it

    grid = [
        ["S", "0", "1", "0"],
        ["0", "0", "1", "0"],
        ["1", "0", "0", "0"],
        ["0", "1", "0", "E"]
    ]

    height = len(grid)
    width = len(grid[0])

    res = []

    def backtracking(h, w, path):

        print(h, w)
        # Check out of bounds
        if not (0 <= h < height and 0 <= w < width):
            return

        # Check wall or used path
        if grid[h][w] == '1' or grid[h][w] == 'V':
            return

        # Base case
        if grid[h][w] == 'E':
            res.append(path[:])

        # Temporarily mark cell visited

        temp = grid[h][w]
        grid[h][w] = 'V'

        # Go up
        path.append((h - 1, w))
        backtracking(h - 1, w, path)
        path.pop()

        # Go down
        path.append((h + 1, w))
        backtracking(h + 1, w, path)
        path.pop()

        # Go right
        path.append((h, w + 1))
        backtracking(h, w + 1, path)
        path.pop()

        # Go left
        path.append((h, w - 1))
        backtracking(h, w - 1, path)
        path.pop()

        grid[h][w] = temp

    backtracking(0, 0, [])
    print(res)
    print(len(res))
