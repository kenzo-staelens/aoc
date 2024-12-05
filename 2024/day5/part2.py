with open('input.txt', 'r') as f:
    sections =f.read().strip().split('\n\n')

rules_before = {}
rules_after = {}

rules = sections[0].strip().split("\n")
books = [[int(y) for y in x.split(',')] for x in sections[1].strip().split("\n")]

for rule in rules:
    before, after = (int(x) for x in rule.split("|"))
    if before not in rules_before:
        rules_before[before]={after}
    else:
        rules_before[before].add(after)

    if after not in rules_after:
        rules_after[after]={before}
    else:
        rules_after[after].add(before)


def process_line(line):
    for index, element in enumerate(line):
        before = line[:index]
        after = line[index+1:]
        for item in before:
            if element not in rules_before:
                break
            if item in rules_before[element]:
                return False
        for item in after:
            if element not in rules_after:
                break
            if item in rules_after[element]:
                return False
    return True

def order_line(line):
    # make a copy as a set
    working = set(line)
    res = []
    while len(working)>0:
        flag = True
        for item in working:
            other = working - {item}
            # if item not in rules_before or len(rules_before[item] - other)==0:
            if item not in rules_after or len(rules_after[item] & other)==0:
                res.append(item)
                working.remove(item)
                flag = False
                break
        if flag:
            working.remove(item)
            res.append(item)
    return res

wrong = [order_line(line)[len(line)//2] for line in books if not process_line(line)]
print(sum(wrong))
