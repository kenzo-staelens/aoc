import numpy as np
import scipy
a = np.array([list(x.strip()) for x in read(strip=True)])
a[a=='.']=0
a[a=='@']=1
a = a.astype(int)
b = np.array([[1,1,1],[1,0,1], [1,1,1]])

c = scipy.signal.convolve2d(a,b,mode='same')
res = sum(sum(np.logical_and(c < 4, a==1)))
print(res)
