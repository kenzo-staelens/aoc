import re
with open("input.txt") as f:
    inp = f.read().strip().split("\n\n")

rules = [x for x in inp[0].split("\n")]
parts = [x for x in inp[1].split("\n")]

part2_sum=0

def parse_part(part):
    return re.findall(r"(\d+)",part)

def map_rules(rules):
    mapping = {}
    for rule in rules:
        k,r = rule.split("{")
        mapping[k]=r[:-1]
    return mapping

def run_rule(rule, x,m,a,s):
    split = rule.split(",")
    for r in split[:-1]:
        k,v=r.split(":")
        k = k.replace("x",x).replace("m",m).replace("a",a).replace("s",s)
        if eval(k): #eval is evil but fuck it, this shit works
            return v
    return split[-1]

def accept_parts(x,m,a,s,thisrange,var):
    global part2_sum
    xdiff = x[1]-x[0]+1
    mdiff = m[1]-m[0]+1
    adiff = a[1]-a[0]+1
    sdiff = s[1]-s[0]+1
    rangediff = thisrange[1]-thisrange[0]+1
    partialsum = xdiff*mdiff*adiff*sdiff*rangediff
    if var =="x":
        partialsum/=xdiff
    elif var =="m":
        partialsum/=mdiff
    elif var =="a":
        partialsum/=adiff
    elif var =="s":
        partialsum/=sdiff
    part2_sum+=partialsum

#ruleset = 1 entry in rules dict
def run_ranged_rule(ruleset, x,m,a,s,ruledict):#where xmas = as ranges (1,4000)
    split = ruleset.split(",")
    ranges = {"x":x,"m":m,"a":a,"s":s}
    for i,r in enumerate(split[:-1]):
        rule,dest = r.split(":")
        var = rule[0]
        _range = ranges[var] 
        op = rule[1] # < or >
        rulenum = int(rule[2:])
        this,_next = split_range(_range,op,rulenum)
        if dest=="A":
            accept_parts(ranges['x'],ranges['m'],ranges['a'],ranges['s'],this,var)
            ranges[var]=_next
        elif dest=="R": #part rejected
            ranges[var]=_next
        else:
            ranges[var]=_next
            nextrule = ruledict[dest]
            temp = {k:v for k,v in ranges.items()}
            temp[var] = this
            run_ranged_rule(nextrule, temp['x'],temp['m'],temp['a'],temp['s'],ruledict)
    #lastrule:
    if split[-1]=="A":
        accept_parts(ranges['x'],ranges['m'],ranges['a'],ranges['s'],(0,0),None)
    elif split[-1]=="R":
        pass
    else:
        run_ranged_rule(ruledict[split[-1]],ranges['x'],ranges['m'],ranges['a'],ranges['s'],ruledict)

def split_range(_range, op, num):
    if op=="<":
        return (_range[0],num-1),(num,_range[1])
    else:
        return (num+1,_range[1]),(_range[0],num)

A=0
rules = map_rules(rules)
for p in parts:
    pd = parse_part(p)
    rule = rules["in"]
    while True:
        o=run_rule(rule,*pd)
        if o=="A":
            A+=sum([int(x) for x in pd])
            break
        elif o!="R":
            rule=rules[o]
        else:
            break
print("part1:",A)

run_ranged_rule(rules["in"],(1,4000),(1,4000),(1,4000),(1,4000),rules)
print("part2:",int(part2_sum))