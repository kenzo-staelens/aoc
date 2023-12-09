with open("input.txt","r") as f:
    input = f.read().strip()

sequences = [[int(item) for item in sequence.strip().split(" ")]
    for sequence in input.split("\n")]

def generate_triangle(sequence):
    returns = []
    nextsequence = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
    returns.append(sequence)
    if not all(i==0 for i in nextsequence):
        for item in generate_triangle(nextsequence):
            returns.append(item)
    return returns

def process_triangle(triangle):
    len_last = len(triangle[-1])
    for i in range(len(triangle)-2,-1,-1):
        triangle[i].append(triangle[i+1][-1]+triangle[i][-1])
        triangle[i].insert(0,triangle[i][0]-triangle[i+1][0])
    return triangle[0][-1], triangle[0][0]

sum = 0
sum2 = 0
for i in sequences:
    t = generate_triangle(i)
    a,b=process_triangle(t)
    sum += a
    sum2+=b
    # sum2+=process_triangleL(t)
print(sum,sum2)

