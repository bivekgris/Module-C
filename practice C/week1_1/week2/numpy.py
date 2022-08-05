import numpy as np

# Addition

a1 = np.arange(9).reshape(3,3)
a2 = np.arange(3)
print('a1=\n', a1)
print('a2=\n', a2)

print('Addition a1 + 5 =\n', a1+5)
print ('np.add a1 + 5 =\n', np.add(a1,5))

# Addition two arrays 
print ('np.add a1 + a2 =\n', np.add(a1,a2))
