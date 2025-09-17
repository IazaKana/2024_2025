def step_function(x):
	y = x > 0
	return y.astype(int)

import numpy as np
x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)
y = y.astype(int)
print(y)
