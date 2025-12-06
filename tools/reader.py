def read(strip=False):
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if strip and line.strip() == '':
                continue
            if strip:
                yield line.strip()
            else:
                yield line
