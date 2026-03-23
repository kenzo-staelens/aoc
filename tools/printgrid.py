def print_grid(grid, y, x, spacing):
    print(' ' * spacing, end='')
    for i in range(len(grid[0])):
        print(str(i).rjust(spacing, ' '), end='')
    print()
    for i, line in enumerate(grid):
        print(str(i).rjust(spacing, ' '), end='')
        for j, item in enumerate(line):
            if i == y and j == x:
                print('[' + str(item).rjust(spacing - 2, ' ') + ']', end='')
            else:
                print(str(item).rjust(spacing, ' '), end='')
        print()
    print()
