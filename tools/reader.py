def read():
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            yield line.strip()
