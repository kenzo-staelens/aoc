import numpy as np
import scipy
inp = np.array([list(x.strip()) for x in read(strip=True)])
inp[inp=='.']=0
inp[inp=='@']=1
inp = inp.astype(int)

def solve_arrays(a):
    b = np.array([[1,1,1],[1,0,1], [1,1,1]])

    c = scipy.signal.convolve2d(a,b,mode='same')
    d = np.logical_and(c < 4, a==1)
    res = sum(sum(d))
    return res, d.astype(int)

res = 0
last = 0
while last!=0 or res == 0:
    last, r = solve_arrays(inp)
    inp = inp - r
    res += last
print(res)
