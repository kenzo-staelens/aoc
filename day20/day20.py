from math import lcm

with open ("input.txt","r") as f:
    inp = f.read().strip().split("\n")

queue=[]

class flipflop():
    def __init__(self,name,ts):
        self.name=name
        self.state=0
        self.targets=ts.split(", ")
    def write(self,_,pulse):
        if pulse==0:
            self.state=(self.state+1)%2
            for target in self.targets:
                queue.append((self.name,target,self.state))
    def __repr__(self):
        return f"{self.name} {self.state} {self.targets}"
    def reset(self):
        self.state=0

class conjunction():
    def __init__(self,name,ts):
        self.name=name
        self.state={}
        self.targets=ts.split(", ")
    
    def add_input(self,name):
        self.state[name]=0
    
    def write(self,src,pulse):
        self.state[src]=pulse
        s = sum(x for x in self.state.values())
        if s==len(self.state):
            newstate = 0
        else:
            newstate=1
        for target in self.targets:
            queue.append((self.name,target,newstate))
    def __repr__(self):
        return f"{self.name} {self.state} {self.targets}"
    def reset(self):
        self.state={k:0 for k in self.state.keys()}

class broadcast:
    def __init__(self,_,ts):
        self.state=0
        self.name="broadcaster"
        self.targets = ts.split(", ")
    def write(self,_=None,__=None):
        for t in self.targets:
            queue.append(("broadcaster",t,0))
    def __repr__(self):
        return f"broadcaster {self.targets}"
    def reset(self):
        pass

modules={}
for item in inp:
    s,ts= item.split(" -> ")
    s=s[1:]
    if item[0]=="%":
        m = flipflop(s,ts)
        modules[s]=m
    elif item[0]=="&":
        modules[s]=conjunction(s,ts)
    elif item[0:9]=="broadcast":
        modules[f"b{s}"]=broadcast(None,ts)

#set all conj sources
for item in inp:
    s,ts = item.split(" -> ")
    s=s[1:]
    ts = ts.split(",")
    for t in ts:
        try:
            modules[t].add_input(s)
        except Exception as e:
            pass


#print(modules)
#print(queue)

def build_statedict():
    return {k:modules[k].state for k in modules.keys()}

def run_button_press(key=None):
    state0=0
    state1=0
    while len(queue)!=0:
        name,target,state=queue.pop(0)
        if state==0:
            state0+=1
        else:
            state1+=1
        #print(name,target,state)
        if target==key and state==0:
            return 0,0,True
        if target not in modules:
            continue
        modules[target].write(name,state)
    return state0,state1,False

def part2(keys):
    comps=[]
    for key in keys:
        comps.append(solve(key))
    return comps,lcm(*comps)

def solve(key=None):
    ls=0
    hs=0
    i=0
    for mod in modules.values():
        mod.reset()
    while True:
        queue.append((None,"broadcaster",0))
        l,h,rx=run_button_press(key)
        ls+=l
        hs+=h
        #print(l,h)
        if rx:
            return i+1
        if i==999 and key==None:
            return ls*hs
        i+=1

target = None #item before rx
keys_to_target = []
for key in modules.keys():
    if "rx" in modules[key].targets:
        target=key
for key in modules.keys():
    if target in modules[key].targets:
        keys_to_target.append(key)
print(keys_to_target)
print("part1:",solve())
print("part2:",part2(keys_to_target)[1])#[0]=test

